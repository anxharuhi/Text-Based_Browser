import os
import sys
from collections import deque
import re
import requests
from bs4 import BeautifulSoup
from colorama import init, Style, Fore
init()

class Browser:
    url_regex = {'protocol': r'^(https?://)', 'url': r'([A-Z0-9-]+\.)', 'domain': r'([A-Z0-9]){2,6}$'}

    def __init__(self, folder=None):
        """
        A simple text-based browser written in python. Supports caching and
        going back in history.
        :param folder: Program's cache folder
        """
        self.history = deque()
        if folder is None:
            self.cache_folder = None
        else:
            self.cache_folder = os.path.join(os.getcwd() + '/' + folder + '/')

    def is_valid_url(self, url):
        """
        Checks for a valid url. Valid url is at least composed of a
        :param url:
        """
        regex = re.compile(
            self.url_regex['protocol'] + '?'
            + self.url_regex['url'] + '+'
            + self.url_regex['domain'], re.IGNORECASE)
        return re.match(regex, url) is not None

    def cache_name(self, url):
        url = url.lstrip('http://').lstrip('https://')
        for position, letter in reversed(list(enumerate(url))):
            if letter == '.':
                return url[0:position]

    def is_cached(self, url):
        if self.cache_folder is not None:
            return os.path.exists(os.path.join(self.cache_folder + url + '.txt'))
        return False

    def cache_store(self, cached_name, web_page):
        if not os.path.exists(self.cache_folder):
            os.mkdir(self.cache_folder)
        with open((os.path.join(self.cache_folder + cached_name + '.txt')), 'wt', encoding='utf-8') as file:
            file.write(web_page)

    def cache_load(self, cached_name):
        with open((os.path.join(self.cache_folder + cached_name + '.txt')), 'rt', encoding='utf-8') as file:
            return file.read()

    def request(self, url):
        print(url)
        r = requests.get(url.strip('\n'))
        return r.text

    def navigate_to_webpage(self, url):
        if url == 'back':
            if len(self.history) <= 1:
                return ''
            elif len(self.history) > 1:
                self.history.pop()
                return self.cache_load(self.history[-1])
        elif self.is_cached(url):
            self.history.append(url)
            return self.cache_load(url)
        else:
            if self.is_valid_url(url):
                regex = re.compile(self.url_regex['protocol'], re.IGNORECASE)
                if re.match(regex, url) is None:
                    webpage = self.request('https://' + url)
                else:
                    webpage = self.request(url)
                soup = BeautifulSoup(webpage, 'html.parser')
                for tag in soup.find_all(name='script'):
                    tag.decompose()
                for tag in soup.find_all(name='p'):
                    tag.string = Fore.BLUE + tag.get_text() + Style.RESET_ALL
                if self.cache_folder is not None:
                    self.cache_store(self.cache_name(url), soup.get_text())
                self.history.append(self.cache_name(url))
                return soup.text
            else:
                return 'Error: Incorrect URL'


input_url = input()
if len(sys.argv) > 1:
    browser = Browser(sys.argv[1])
else:
    browser = Browser()

while input_url != 'exit':
    print(browser.navigate_to_webpage(input_url))
    input_url = input()
