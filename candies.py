'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the i<sup>th</sup> kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the i<sup>th</sup> kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:

COPY

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Explanation
You are given a group of kids, and each kid has a certain number of candies represented by an array called candies. Additionally, you have some extra candies. The goal is to find out, for each kid, if giving them all the extra candies would make them have the greatest number of candies among all the kids.

In other words, you want to determine if adding the extra candies to a particular kid’s current candies count would result in them having the most candies compared to all the other kids. It’s not about making just one kid have the most candies; multiple kids can have the greatest number of candies if they receive the extra candies.

The problem asks you to return a boolean array result, where each element result[i] will be True if giving the ith kid all the extra candies would make them have the greatest number of candies among all the kids, or False otherwise.

To summarize, you are checking if each kid can potentially have the most candies by adding the extra candies to their current count, and you will return a boolean array indicating which kids meet this condition.


'''

def find(candies, extraCandies):
    maxcandies = max(candies)

    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxcandies:
            candies[i] = True
        else:
            candies[i]= False
    return candies
print(find([2,3,5,1,3], 3))
print(find([4,2,1,1,2], 1))
print(find([12,1,12], 10))