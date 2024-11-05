'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''

def combinationsum(list, target):
    list.sort()
    result = []

    def comb(curr, start, target):
        if target == 0:
            result.append(curr)
            return
        for i in range(start, len(list)):
            if i > start and list[i] == list[i-1]:
                continue
            if list[i]> target:
                break
            comb(curr + [list[i]], i+1, target- list[i])
            return
        comb([], 0, target)
        return result
    


    

    

        
        








