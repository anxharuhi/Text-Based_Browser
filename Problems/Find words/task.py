sentence = input().split()
words = []
for word in sentence:
    if word[-1] == 's':
        words.append(word)
print('_'.join(words))