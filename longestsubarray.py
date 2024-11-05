'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.



[0,1,1,1,0,1,1,0,1]
'''

def longestsubarray(array):
    res = 0
    zercount = 0
    left = 0


    for right in range(len(array)):
        if array[right]==0:
            zercount+=1
        while zercount>1:
            if array[left]==0:
                zercount -= 1
            left+=1
        print(right-left, "tracingvalue")
        res = max(res, right-left)
        print(res, "loop")
    return res

#print(longestsubarray([0,1,1,1,0,1,1,0,1]))
#print(longestsubarray([1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1]))
#print(longestsubarray([1,1,0,1]))
print(longestsubarray([1,1,1]))




            








