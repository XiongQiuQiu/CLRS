def partition(nums, p, q):
    x = nums[p]
    i = p
    for j in range(p+1, q+1):
        if nums[j] < x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[p], nums[i] = nums[i], nums[p]
    return i


def quicksort(nums, p, q):
    '''
    divide and conquer
    sorts in place
    very parctical
    '''
    if p < q:
        k = partition(nums, p, q)
        quicksort(nums, p, k-1)
        quicksort(nums, k+1, q)
    return nums

if __name__ == '__main__':
    nums = [6,10,13,5,8,3,2,11]
    p = 0
    q = len(nums) -1
    print quicksort(nums, p, q)
