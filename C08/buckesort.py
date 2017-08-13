from random import random


def insertSort(nums):
    n = len(nums)
    if n <= 1:
        pass
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while key < nums[j] and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


def sort(nums):
    n = len(nums)
    s = [[] for i in range(n)]
    print len(s)
    for i in nums:
        s[int(i * n)].append(i)
    print s
    for i in s:
        insertSort(i)
    return [i for j in s for i in j]


a = [random() for i in xrange(10000)]
print sort(a)
