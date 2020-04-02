#dictionary: key-value pairs,unordered,Mutable
#ways of defining

#way1 Key:value pair
mydict={"Name":"Anand","Age":29,"Company":"Ross"}
print(mydict)

#way2
mydict2=dict(Name="Kanchana",Age=26,Company="Ford")
print(mydict2)

#accessing values
value=mydict["Name"]
print(value)
value2=mydict2["Age"]
print(value2)


#value=mydict["namasdasde"]

#adding new key value pair to dictionary after its define
mydict["Email"]="abcd@abcd.com"
mydict2["Email"]="abcd@abcd.com"

print(mydict)
print(mydict2)

#assigning a dictionary to another
mydict3=mydict

#delete items wil remove items in all assigned dictionaries
#way1
del mydict3["Name"]
print(mydict3)

#way2
mydict3.pop("Age")
print(mydict3)

#way3: removing arbitrary pair:last inserted item
mydict3.popitem()
print(mydict3)

print("---------------------------")
print(mydict)


#check keys in dictionaries

if "Name" in mydict2:
    print(True)
else: print(False)

#or
if "Name" in mydict2:
    print(mydict2["Name"])
if "Age" in mydict2:
    print(mydict2["Age"])
if "Company" in mydict2:
    print(mydict2["Company"])


#try catch
try:
    print(mydict("Name"))
except:
    print("Error:Key doesn't exist")

print("--------------------------------------------------")
#output all keys in dictionary
#way1
for key in mydict:
    print(key)
print("--------------------------------------------------")
for key in mydict2:
    print(key)

print("--------------------------------------------------")
#way2

for key in mydict2.keys():
    print(key)
print("--------------------------------------------------")
#output all values in dictionary
for val in mydict2.values():
    print(val)

print("--------------------------------------------------")
#output all key,value pairs in dictionary

for key,val in mydict2.items():
    print(key,":",val)

print("--------------------------------------------------")
#merging dictionary
#example 2
mydict={"Name":"Anand","Age":29,"Company":"Ross"}
mydict2=dict(Name="Kanchana",Age=26,City="Boston")

mydict.update(mydict2)  # only update values for corresponding keys and then add extra key value pairs if any
print(mydict)
print(mydict2)
print("--------------------------------------------------")
#example 2
A={1:11,2:12,3:13,4:14,5:15}
B={1:21,3:45,4:55,7:88,9:101}

A.update(B)
print(A)

print("--------------------------------------------------")
#accessing all elements
for key in A:
    print(A[key])

print("--------------------------------------------------")
#creating dictionary out of two lists
#way1
A=[1,2,3,4,5,6,7,8,9,0]
B=["a","b","c","d","e","f","g","h","i","j"]
mydict={}
for key in A:
    for val in B:
        mydict[key]=val
        B.remove(val)
        break

print(mydict)
print("--------------------------------------------------")
#way2
A=[1,2,3,4,5,6,7,8,9,0]
B=["a","b","c","d","e","f","g","h","i","j"]
mydict_way2=dict(zip(A,B))
print(mydict_way2)
print("--------------------------------------------------")

#using tuples in dictionary
mytuple=(8,7)
mydict={mytuple:15}
print(mydict)
print("--------------------------------------------------")

#can't use list in dictionary
mylist=[8,7]
#mydict={mylist:15}#TypeError: unhashable type: 'list'