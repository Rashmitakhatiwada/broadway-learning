#using iterations examples in
names=['john','jane']
name = iter(names)
print(next(name))
print(next(name))
print(next(name))

#using iterations examples in string
language ="java"
lang= iter(language)
print(next(lang))
print(next(lang))
print(next(lang))
print(next(lang))


#loop using iteration
names=['john','jane']
name_iter= iter(names)

while True:
    try:
        name=next(name_iter)
        print(name)
    except StopIteration:
        break