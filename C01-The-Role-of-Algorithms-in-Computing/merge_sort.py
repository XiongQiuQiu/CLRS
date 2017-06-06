'''\
    1. if input [1] done
    2. recursive sort nums[1:len/2] and nums[len/2+1:n]
    3. merge 2 sorted lists'''
from collections import deque

def merge_sort(lst):
    '''
    1. if input [1] done
    2. recursive sort nums[1:len/2] and nums[len/2+1:n]
    3. merge 2 sorted lists
    '''
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] >= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

print merge_sort([5,4,4,6,1,3])