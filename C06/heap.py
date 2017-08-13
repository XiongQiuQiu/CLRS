heap_size = 0
LEFT = lambda i: 2*i + 1
RIGHT = lambda i: 2*i + 2
PARENT = lambda i: (i-1)/2

def max_heapify(nums,i):
    global heap_size
    l = LEFT(i)
    r = RIGHT(i)
    largest = l if l < heap_size and nums[l] > nums[i] else i
    largest = r if r < heap_size and nums[r] > nums[i] else largest
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums, largest)

def heap_maximun(nums):
    return nums[0]

def heap_extract_max(nums):
    global heap_size
    if heap_size < 0:
        raise 'heap underflow'
    max = nums[0]
    nums[0] = nums[heap_size]
    heap_size -= 1
    max_heapify(nums, 0)
    return max

def heap_increase_key(nums, i, key):
    if key < nums[i]:
        raise 'new key is smaller than current key'
    nums[i] = key
    while i > 0 and nums[PARENT(i)] < nums[i]:
        nums[i], nums[PARENT(i)] = nums[PARENT(i)], nums[i]
        i = PARENT(i)

def max_heap_insert(nums, key):
    global heap_size
    heap_size += 1
    nums[heap_size] = float('-inf')
    heap_increase_key(nums, heap_size, key)

