'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

def movezeroes(nums):
    insert = 0

    for i in range(len(nums)):
    

        if nums[i]!=0:
            nums[insert], nums[i] = nums[i], nums[insert]
            insert+=1
            
    return nums
    
print(movezeroes([1,2,3,0,9,7,6,5,0,2,4]))
print(movezeroes([0,1,0,2,7,6,5,0,2,4]))

