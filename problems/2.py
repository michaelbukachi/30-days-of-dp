"""
Maximum sum of subarray implementation
"""


def max_sum(array):
    cur_sum = global_sum = array[0]
    for i in array[1:]:
        cur_sum = max(i, cur_sum + i)
        global_sum = max(cur_sum, global_sum)

    return global_sum


if __name__ == '__main__':
    assert max_sum([2, -9, 5, 1, -4, 6, 0, -7, 8]) == 9
    assert max_sum([1, 5, -1, 0, 10]) == 15
    assert max_sum([0, -1, -5, 0, -4]) == 0
    assert max_sum([-4, -3, -1, -9, -10]) == -1
