right = lambda i: i * 2 + 2
left = lambda i: i * 2 + 1
heap_size = 0


def max_heapify(nums, i):
    l = left(i)
    r = right(i)
    largest = l if l < heap_size and nums[l] > nums[i] else i
    largest = r if r < heap_size and nums[r] > nums[largest] else largest
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums, i)


def build_max_heap(nums):
    global heap_size
    heap_size = len(nums)
    for i in range(len(nums) / 2, -1, -1):
        max_heapify(nums, i)


def head_sort(nums):
    global heap_size
    build_max_heap(nums)
    for i in range(len(nums) - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heap_size -= 1
        max_heapify(nums, 0)


if __name__ == '__main__':
    nums = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    head_sort(nums)
    print nums
