# Merged strings alternately 
'''
ou are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

'''


def mergedstring(word1, word2):
    i=j=0
    merged = ""

    a1 = len(word1)
    a2 = len(word2)

    while i < a1 and j < a2:
        merged += word1[i] + word2[j]
        i+=1
        j+=1
    if i <  a1:
        merged += word1[i:]
    else:
        merged += word2[j:]

    return merged
print(mergedstring("pq", "estuvwxy"))



