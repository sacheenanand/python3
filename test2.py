

'''def checking(str, k):
    vowels = {'a','e','i','o','u'}
    for i in range(k):
        print(str[i])
print("sacheen", 3)
'''


def testn19(str):
    i=0
    j=0
    result = 0
    sacheen = {}

    for j in range(len(str)):

        if str[j] in sacheen:
            i = max(sacheen[str[j]], i)

        sacheen[str[j]] = j+1
        result = max(result, j-i+1)
    return result
print(testn19(("abcabcbb")))
print(testn19(("abcdefaswertyuio")))
print(testn19(("Hello World!")))







