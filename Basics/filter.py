a=[1,2,3,4,5,6,7,8,9]


def is_even(value):
    return value%2==0

result= list(filter(is_even,a))
print(result)


c=['a','b','c','e']
def is_vowel(values):
    b = ['a', 'e', 'i', 'o', 'u']
    return values in b

result= list(filter(is_vowel,c))
print(result)