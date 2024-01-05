'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''

nums = [20,100,10,12,5,13]
is_triplet = False
first = second = float('Inf')
for x in nums:
    if x <= first:
        first = x
    elif x <= second:
        second = x
    else:
        is_triplet = True

    '''if(i+2)<len(nums):
        if nums[i] < nums[i+1] < nums[i+2]:
            is_triplet = True
            break'''

print(is_triplet)

