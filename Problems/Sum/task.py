# read sums.txt
text_file = open('sums.txt', 'r')
for line in text_file:
    x, y = line.split()
    print(int(x) + int(y))
text_file.close()
