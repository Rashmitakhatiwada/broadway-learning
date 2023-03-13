
t=(1,2,3,2,3,4,5,1,2,3,6,4,4,4,4)

val=t.count(4)
print(val)

index= t.index(2)
print(index)

index = t.index(2,3)
print(index)

s=sum(t)
print("sum is",s)

max=max(t)
print("maximum in the tupple", max)

min=min(t)
print("minimum in the tupple", min)

s=sorted(t)
print("sorted in tupple", sorted)

#Dictionary
student ={
    "name": "aaa",
    "age": 24,
    "address":"bhaktapur"
}
s= {"name":"john" , "age":24, "address":"kalanki"}
print(s.get("ager")) #nabhako value search garda result none auxa
s.get("hsjdgh", 4)  #if searched value not found it return 4

s["college"] ="asdfghjkl" #naya value add gareko
s["college"] ="kec" #value edit garne

len(s) #length of dictionary/list


print("all ", all(s)) #and operation jaster
print("all for empty", all({}))
print("any", any(s)) #or operation jastei
print("all in dictionary", all({1,2,3}))
print("all for dictionary",all({ "":2,'x':3}))
print("any for dictionary",any({ "":2,'x':3}))
print("length of s", len(s))
print("sorted value of s", sorted(s))
print("sorted and reversed", (sorted(s, reverse= True)))

print("keys matra call garna", s.keys())
print("values matra call garna", s.values())
print("items call garna", s.items())

t=s.copy()
print("copy garna",t)

a={"number": 9845678209}
s.update(a)
print("to add and check the updated values",s)

s.setdefault('name',"not found") #if value found changes are not made but if not found returns as the changed value/new value
print(s)
