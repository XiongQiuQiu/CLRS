import random
def partition(nums, p, q):
    x = nums[p]
    i = p
    for j in range(p+1, q+1):
        if nums[j] < x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[p], nums[i] = nums[i], nums[p]
    return i

def random_partition(nums, p, q):
    i1 = random.choice(range(p, q+1))
    nums[p], nums[i1] = nums[i1], nums[p]
    return partition(nums, p, q)

def random_quicksort(nums, p, q):
    if p < q:
        k = random_partition(nums, p, q)
        random_quicksort(nums, p, k-1)
        random_quicksort(nums, k+1, q)
    return nums

if __name__ == '__main__':
    nums = [6,10,13,5,8,3,2,11]
    p = 0
    q = len(nums) -1
    print random_quicksort(nums, p, q)
