# coding: utf-8
#---------------Start fourth---------------
#'''
x = int(input('Введите сумму, которую желаете получить: '))
nominal = [1000,500,200,100,50,20,10,5,2,1]
out = [x//nominal for nominal in nominal while x>0:x -= x//nominal*nominal]
i = 0
while x>0:
    n=x//nominal[i]
    print(f'Номиналом {nominal[i]} Вы получите {n} купюр')
    x -= n*nominal[i]
    i +=1
#'''