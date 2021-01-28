max_num = 10
max_read = max_num
line = 0
i = 0
while i < max_read:
    i += 1
    j = 0
    while j < i:
        j += 1
        max_read -= 1
 
    line += 1
 
 
n = 1
i = 0
while i < max_num:
    i += 1
    line -= 1
    for s in range(line):
        print(" ", end='')
 
    for j in range(i):
        print(n, end=' ')
        n += 1
        max_num -= 1
 
    print("")