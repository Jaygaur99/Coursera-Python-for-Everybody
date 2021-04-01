import re
hand = open('ACTUAL DATA.txt')
lst = list()
for line in hand:
    line = line.rstrip()
    word = line.split()
    stuff = re.findall('([0-9]+)',line)
    if len(stuff)<1:continue
    elif len(stuff) == 1:
        num = int(stuff[0])
    elif len(stuff) == 2:
        num = int(stuff[0])+int(stuff[1])
    elif len(stuff) == 3:
        num = int(stuff[0])+int(stuff[1])+int(stuff[2])
    if num == 0:continue
    lst.append(num)
print(lst)
sum = 0
for n in lst:
    sum = sum + n
print(sum)
