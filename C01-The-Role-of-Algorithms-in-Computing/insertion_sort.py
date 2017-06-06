def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

print insertion_sort([5, 4, 4, 6, 1, 3])
'''
Running time:
1. depends on input sorted
2. input size
'''