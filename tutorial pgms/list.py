mylist =["banana","cherry","apple"]

print(mylist[-1])

for i in mylist:
	print (i)

if "banana" in mylist:
	print("true")
else: print("false")

print(mylist)

mylist.append("lemon")
mylist.insert(1,"blueberry")
print(len(mylist))
print("---------------------")
item=mylist.pop()
print(item)
print(mylist)
item2=mylist.remove("cherry")
print(mylist)
item3=mylist.reverse()
print(mylist)
item3=mylist.sort()
print(mylist)
mylist.clear()
print(mylist)
