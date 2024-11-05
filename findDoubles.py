'''
find doubles in 

Find all elements of the list for which there exists exactly one element of the list which is twice that number. The integers range 
from 0 to 1000. The list has no more than 100,000 elements. Your code should find the appropriate values and print them to STDOUT in
 sorted order. Examples: 1 2 3 4 5 6 7 8 9 0 8 -> 0 1 2 3 (8 is 4*2, but 8 is present twice; O is its own double, so it's part 
 of the result) 7 17 11 1 23 -> (nothing is exactly twice another element) 1 1 2 -> 1 1 (1 and 1 both have their double 2 present, 
 and 2 is present in the list only once) write in python code
'''


def doubles(list):
    from collections import Counter

    frequency = Counter(list)
    result = []
    for num in list:
        if num*2 in frequency:
            if frequency[num*2]==1:
                result.append(num)

    print(sorted(result))

    
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8]
list1 = [1, 1,2]

doubles(list)
doubles(list1)




