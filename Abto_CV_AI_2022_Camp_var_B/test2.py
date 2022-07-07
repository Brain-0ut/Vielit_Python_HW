from typing import List
import random as r


def task1(x: List[int]) -> bool:
    ###
    """Write your code here"""
    ###
    lenght = len(x)
    if lenght < 2:
        return False
    elif lenght == 2:
        if x[0] == x[1]:
            return True
        else:
            return False
    x.sort()
    print(x)
    average = sum(x) / lenght
    start = 0
    end = lenght - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if x[mid] <= average < x[mid + 1]:
            print(mid)
            break
        elif average < x[mid]:
            end = mid - 1
        else:
            start = mid + 1
    mid += 1
    first = x[:mid]
    second = x[mid:]
    print(first, '|', second)

    sum1 = first[0] + first[-1] + second[0] + second[-1]
    mas1 = [first.pop(0), first.pop(-1), second.pop(0), second.pop(-1)]
    sum2 = (sum(x) - sum1)
    mas2 = first + second
    aver1 = sum1 / 4
    aver2 = sum2 / (lenght - 4)
    print(mas1, " ", mas2)
    print(sum1, " ", sum2)
    print(aver1, " ", aver2)
    print(average)
    if aver1 == aver2:
        return True
    return False


x = [r.randrange(0, 10000) for x in range(r.randrange(1, 30))]
#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(x)
expected_result = True
result = task1(x)
print(result)
#assert result == expected_result
