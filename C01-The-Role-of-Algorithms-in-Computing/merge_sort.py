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
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] >= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


print merge_sort([5, 4, 4, 6, 1, 3])

'''
def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists)/2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result+= left[l:]
    return result
print MergeSort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45])
'''
