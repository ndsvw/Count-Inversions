# This is a divide and conquer solution that runs
# in O(n log n).
# run it with: python3 divide_and_conquer.py 10000

import random
import sys


def modifiedMerge(l1, l2):
    # normal merge code with a few changes
    m1, m2 = len(l1), len(l2)
    newList = []
    i, j = 0, 0
    count = 0  # new
    while i < m1 and j < m2:
        if l1[i] < l2[j]:
            newList.append(l1[i])
            i += 1
        else:
            newList.append(l2[j])
            count += len(l1) - i  # new
            j += 1
    return newList + l1[i:] + l2[j:], count  # new


def inversionen(p):
    # divide and conquer
    m = len(p)
    if m < 2:
        return (p, 0)

    x1 = p[:m//2]
    x2 = p[len(x1):]

    l1, invs1 = inversionen(x1)
    l2, invs2 = inversionen(x2)

    merged, inversionsOverBothLists = modifiedMerge(l1, l2)
    return merged, invs1 + invs2 + inversionsOverBothLists


if __name__ == "__main__":
    # print(inversionen([6, 5, 4, 3, 2, 1, 0])[1])
    # print(inversionen([0, 1, 2, 3, 4, 5, 6])[1])
    # print(inversionen([0, 1, 2, 3, 4, 6, 5])[1])
    size = int(sys.argv[1])
    arr = [random.randrange(-10000, 10000, 1) for _ in range(size)]
    print(inversionen(arr)[1])
