# is_vowel = lambda value : value in ['a','e','i','o','u']
# print(is_vowel('e'))


# a=[1,2,3,4,5,6,7,8,9]
#
# result= list(filter(lambda x:x%2==0,a))
# print(result)


c=['a','b','c','d','e']

result= list(map(lambda x:x.upper(),c))
print(result)

# from functools import reduce
#
# a=[1,2,3,4,5,6]
# result= reduce(lambda x,y:x+y ,a)
# print(result)