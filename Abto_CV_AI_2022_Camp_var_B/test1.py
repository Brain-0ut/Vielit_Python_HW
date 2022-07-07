
def task2(x: int) -> int:
    if x < 2:
        return x
    i = x >> 1
    if (x & 1) == 1:
        n = task2(i)
        print(n, (n << 2), (i << 2), "+1")
        return (n << 2) + (i << 2) + 1
    else:
        n = task2(i)
        print(n, n << 2)
        return n << 2


def main():
    x = 49
    y = 122 & 1#
    #y += 45<<4
    #y += 45
    print(y)
    print(49<<5, 49<<4, 49<<3)
    expected_result = 36
    result = task2(x)

    #assert result == expected_result
    print(result)

if __name__ == "__main__":
    main()