'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105


'''


# [1, 0,1,1] k =1

def duplicatestwo(nums, k):
    d = {}

    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k:
            print(d[nums[i]])
            return True
        d[nums[i]] = i
    return False
print(duplicatestwo([1,0,1,1], 1))
print(duplicatestwo([1,2,3,1], 3))
print(duplicatestwo([1,2,3,1,2,3], 1))
