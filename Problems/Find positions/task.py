# put your python code here
number_list = input().split()
number = input()
positions = []

for i, value in enumerate(number_list):
    if value == number:
        positions.append(str(i))

if not positions:
    print('not found')
else:
    print(' '.join(positions))
