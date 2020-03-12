from random import randint
#-----Cycle "FOR"---------
l = [randint(1,9) for i in range(randint(10,30))]
x=0
x += int(l[i] for i in range(len(l)))
ss = int()
print(str(l) + '\n' + str(ss))
s = 0
for i in range(len(l)):
    s += l[i]
print(str(l) + '\n' + str(s))