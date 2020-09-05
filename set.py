#set
a={1,2,3,4,5}
print(a)
for i in a:
	print(i)

a={10,20,30,40}
if 10 in a:
	print('yes')

a.add(50)
print(a)
a.remove(40)
print(a)
a.discard(20)
print(a)
b=a.pop()
print(a)
print(b)

a={12,24,36,48}
b={13,26,39,52}
print(a.union(b))
print(a.difference(b))
print(a.intersection(b))
print(a.issubset(b))
print(a.isdisjoint(b))
print(a.issuperset(b))







