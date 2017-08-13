def counting_sort(nums):
    k = max(nums)
    ans = [0 for i in range(len(nums))]
    new_array = [0 for i in range(k + 1)]
    for j in range(len(nums)):
        new_array[nums[j]] = new_array[nums[j]] + 1
    for i in range(1, k + 1):
        new_array[i] = new_array[i] + new_array[i - 1]
    for i in range(len(nums) - 1, -1, -1):
        ans[new_array[nums[i]] - 1] = nums[i]
        new_array[nums[i]] -= 1
    return ans


def radix_sort(nums):
    pass


print radix_sort([2, 5, 3, 0, 2, 3, 0, 3])
