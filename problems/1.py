"""
Fibonacci DP implementation
"""


def fib(n):
    if n <= 2:
        return n - 1
    array = [0] * n
    array[1] = 1

    for i in range(2, n):
        array[i] = array[i-1] + array[i-2]

    return array[-1]


if __name__ == '__main__':
    assert fib(1) == 0
    assert fib(3) == 1
    assert fib(10) == 34

    print('Done')