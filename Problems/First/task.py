# read test_file.txt
text_file = open('test_file.txt', 'rt', encoding='utf-16')
print(text_file.readline())
text_file.close()