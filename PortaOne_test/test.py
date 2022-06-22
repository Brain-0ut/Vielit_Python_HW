#from numba import jit
import numpy as np
import sys

# print('Number of arguments:', len(sys.argv))
#@jit(nopython=True)
def main():
    if len(sys.argv) != 2:
        print('Use python test.py <datafile.txt>')
        exit(1)
    fileName = sys.argv[1]

    x = np.loadtxt(fileName, dtype=int)
    arrLen = len(x)
    upLen = 1
    upIdx = 0
    upCount = 1
    downLen = 1
    downIdx = 0
    downCount = 1
    for i in range(1, arrLen):
        if x[i] >= x[i-1]:
            upCount += 1
            if upCount > upLen:
                upLen = upCount
                upIdx = i
        else:
            upCount = 1

        if x[i] <= x[i-1]:
            downCount += 1
            if downCount > downLen:
                downLen = downCount
                downIdx = i
        else:
            downCount = 1

    print('Up LEN:', upLen)
    for i in range(upIdx-upLen+1, upIdx+1):
        print(x[i])

    print('\nDown LEN:', downLen)
    for i in range(downIdx-downLen+1, downIdx+1):
        print(x[i])

    print('\nArithmetic mean:', np.mean(x))
    x.sort()
    if arrLen & 1:
        med = x[round(arrLen/2)+1]
    else:
        med = (0.5*(x[round(arrLen/2)]+x[round(arrLen/2)+1]))
    print('Minimum:', x[0])
    print('Maximum:', x[arrLen-1])
    print('Mediana:', med)
    input('Press any key to exit.')

if __name__ == "__main__":
    main()