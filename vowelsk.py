'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

'''
def vowelsk(str, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_vowels = 0
    max_vowels = 0

    for i in range(k):
        if str[i] in vowels:
            current_vowels += 1
    #        print(current_vowels)
    max_vowels = current_vowels
    print(max_vowels)

    for i in range(k, len(str)):
        if str[i-k] in vowels:
            current_vowels -= 1
            #print(current_vowels)
        if str[i] in vowels:
            current_vowels +=1
        max_vowels = max(max_vowels, current_vowels)
    #    print(max_vowels)

    return max_vowels
print(vowelsk("abciiidef", 3))
#print(vowelsk("maxum", 3))
#print(vowelsk("zxcvb", 3))





