# merge two lists and remove duplicates

list1 = [2,4,5,6,7,8,9,]
list2=[25,2,12,13,14,15,8]

sum = set(list1 + list2)
print(sum)


nums = range(1, 1000)

primes = filter(is_prime, nums)

