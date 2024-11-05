'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.


'''

def palindrome(self, s, left, right):
    count = 0
    if left >=0 and right <= len(s) and s[left] == s[right]:
        count+=1
        left-=1
        right+=1
    return count




def palindromesubstrings(self, s):
    counts = 0
    for i in range(len(s)):
        counts += self.palindrome(s,i, i)
        counts += self.palindrome(s, i, i+1)
    return counts





