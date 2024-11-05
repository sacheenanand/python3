# to check when you reverse the strings are the same

def reversestrings(str1, str2):
    for i in range(len(str1)):
        i2 = len(str2)-i-1
        print(i2)
        if str1[i]!=str2[i2]:
            return False
        return True
print(reversestrings("abc", "cba"))
print(reversestrings("cat","aaa"))

    