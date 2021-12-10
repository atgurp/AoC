lst = [] 

with open('day3text.txt') as file:
    for line in file:
        desc = line.rstrip()
        lst.append(desc)
        

print(lst)
zeronum1 = 0
onenum1 = 0 
gamma_rate_lst = []
for i in range(len(lst)):
    num = (lst[i])

    p = sum(5 for l in lst[i])
    
    print(p)

