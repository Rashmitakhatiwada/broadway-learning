s1 = {1,2,3}
s1.add(4)
print("using add" ,s1)
s1.update([4,5,6])
print("using update" ,s1)
s1.remove(2)
print("using remove" ,s1) #if value doesnt exits it displays an error
s1.discard(7)
print("using discard" ,s1) #if value doesnt exist it doesnt display an error
s1.pop()
print("using pop" ,s1)
s1.clear()
print("using clear" ,s1)
a= {1,2,3,4}
b= {3,4,5,6}
c=a.intersection(b)
print("intersection" ,c)
d= a.union(b)
print("union" ,d)
e= a.difference(b)
print("difference" ,e)
f=a.symmetric_difference(b) #intersection ko complement
print("symmetric difference" ,f)

