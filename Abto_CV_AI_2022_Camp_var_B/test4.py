from typing import List
import random as r


def task4(x: List[List[int]]) -> int:
    ###
    """Write your code here"""
    ###
    row = len(x)
    max_circle = 0
    i = 0
    while i < row:
        for j in range(i, row):
            if x[i][j] != 1:
                if i == j - 1:
                  max_circle += 1
                  j += 1
                i = j - 1
                break
            if j == row - 1 and x[i-1][j] == 0:
                max_circle += 1
            if j == row - 1:
                i += 1

    return max_circle
      #a b c d
x = [[1,1,0],   #a
     [1,1,1],   #b
     [0,1,1]]   #d

expected_result = 1
result = task4(x)
print(result)
#assert expected_result == result