# read animals.txt
# and write animals_new.txt
old_file = open('animals.txt', 'rt')
new_file = open('animals_new.txt', 'wt')

for animal in old_file:
    new_file.write(animal.rstrip('\n') + ' ')

old_file.close()
new_file.close()