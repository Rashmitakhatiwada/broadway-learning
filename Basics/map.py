c=['a','b','c','d','e']

def capitalize(value):
    return value.upper()

result= list(map(capitalize,c))
print(result)