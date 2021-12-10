import goody


res = 0
lst = []
with open('day1text.txt') as file:
    for line in file:
        desc = line.rstrip()
        lst.append(int(desc))

for i in range(1, len(lst)):
	if lst[i] > lst[i-1]:
		res += 1
        
print(res)
