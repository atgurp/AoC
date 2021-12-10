lst = []
horizontal_pos = 0
depth = 0 
aim = 0

with open('day2text.txt') as file:
    for line in file:
        desc = line.rstrip()
        lst.append(desc)


for i in lst:
    if 'forward' in i:
        horizontal_pos += int(i[-1])
        depth += aim * int(i[-1])
    elif 'down' in i:
        #depth += int(i[-1])
        aim += int(i[-1])
    elif 'up' in i:
        #depth -= int(i[-1])
        aim -= int(i[-1])
    print('hor_pos - {}'.format(horizontal_pos))
    print('depth - {}'.format(depth))
    print('aim - {}'.format(aim))
    print('----------------')

#print(horizontal_pos)
#print(depth)
#print(aim)