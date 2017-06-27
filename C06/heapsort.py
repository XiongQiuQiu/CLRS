right = lambda i: i*2 + 1
left = lambda i: i*2
heap_size = 0

def max_heapify(nums, i):
    l = left(nums)
    r = right(nums)
    largest = l if l < heap_size and nums[l] > nums[i] else i
    largest = r if r < heap_size and nums[r] > nums[largest] else largest
    if largest != 1:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums, i)

def build_max_heap(nums):
    heap_size = len(nums)
    for i in range(len(nums)/2-1, -1, -1):
        max_heapify(nums, i)

def head_sort(nums):
    build_max_heap(nums)
    for i in range(len(nums), 1, -1):
        nums[1], nums[i] = nums[i], nums[1]
        heap_size = heap_size - 1
        max_heapify(nums, 1)

