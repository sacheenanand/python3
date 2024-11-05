'''
move all the 1's on the end
'''


def moveones(nums):
    a = 0

    for i in range(len(nums)):
        if nums[i]!=1:
            nums[a], nums[i] = nums[i],nums[a]
            a+=1
    return nums
print(moveones([1,2,3,1,9,7,6,5,1,2,4]))
print(moveones([1,1,1,2,7,6,5,1,2,4]))