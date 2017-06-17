def bin_s(nums, x):
    '''binary search'''
    low = 0
    high = len(nums)
    while low < high:
        mid = (high + low) / 2
        if nums[mid] < x:
            low = mid
        elif nums[mid] > x:
            high = mid
        else:
            return nums[mid], mid
    return -1


print bin_s([1, 2,3], 3)

def bin_s_recur(nums, x):
    mid = len(nums) /2
    if nums[mid] == x:
        return nums[mid]
    elif nums[mid] > x:
        return bin_s_recur(nums[0:mid], x)
    else:
        return bin_s_recur(nums[mid:], x)

print bin_s_recur([1, 2,3],3)