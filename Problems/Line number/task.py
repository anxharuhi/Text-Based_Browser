# read sample.txt and print the number of lines
text_file = open('sample.txt', 'rt')
print(len(text_file.readlines()))
text_file.close()
