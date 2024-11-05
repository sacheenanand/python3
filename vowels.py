def rev_vowels(s):
    vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    st = []
    new_s = ''
    for v in s:
        if v in vow:
            st.append(v)
    for v in s:
        if v in vow:
            new_s = new_s + st.pop()
        else:
            new_s = new_s + v
    return new_s
s = "Eunonia"
print(rev_vowels(s))
s = "Finxter"
print(rev_vowels(s))
s = "hellOO"
print(rev_vowels(s))



