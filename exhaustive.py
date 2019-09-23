# This is an exhaustive search solution that runs
# in O(n^2).
# run it with: python3 exhaustive.py 10000

import random
import sys


def inversionen(p):
    # for each element in the array:
    # is there an element after is that is smaller?
    # then => count it
    m = len(p)
    count = 0
    for i in range(m):
        for j in range(i, m):
            if p[j] < p[i]:
                count += 1
    return count


if __name__ == "__main__":
    # print(inversionen([6, 5, 4, 3, 2, 1, 0]))
    # print(inversionen([0, 1, 2, 3, 4, 5, 6]))
    # print(inversionen([0, 1, 2, 3, 4, 6, 5]))
    size = int(sys.argv[1])
    arr = [random.randrange(-10000, 10000, 1) for _ in range(size)]
    print(inversionen(arr))
