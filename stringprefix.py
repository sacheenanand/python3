'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
print(longestcommonprefix(["sacheen", "sachith","sachin"]))
print(longestcommonprefix(["te", "tq","tn"]))

'''

def longestcommonprefix(strs):
    prefix = strs[0]
    for i in range(len(prefix)):
        for word in strs:
            if i == len(word) or prefix[i]!= word[i]:
                return prefix[:i]
    return prefix
print(longestcommonprefix(["sacheen", "sachith","sachin"]))
print(longestcommonprefix(["te", "tq","tn"]))








