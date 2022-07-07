from typing import List
import random as r


def task3(x: List[List[int]]) -> int:
    ###
    """Write your code here"""
    ###
    row = len(x)
    column = len(x[0])
    maxArea = 0
    for i in range(row):
        for j in range(column):
            hight = 0
            width = column
            cur_i = i
            cur_j = j

            while cur_i < row and x[cur_i][cur_j] == 1:
                tmp = 0
                hight += 1
                while cur_j < column and cur_i < row and x[cur_i][cur_j] == 1:
                    cur_j += 1
                    tmp += 1
                if tmp < width and hight > 1:
                    hight -= 1
                elif tmp < width:
                    width = tmp
                cur_i += 1
                cur_j = j

            area = width * hight

            if maxArea < area:
                maxArea = area

    return maxArea


x = [
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0]
]

expected_result = 6
result = task3(x)
print(result)
#assert result == expected_result