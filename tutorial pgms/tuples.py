#way1
mytuple=("Max",28,"Boston")
print(mytuple)

#way2
mytuple="Max",28,"Boston"
print(mytuple)

#defining single element in tuple
mytuple="Max",
print(mytuple)

#list vs tuple
A=["Max",28,"Boston"]
print(type(A)) #list

#way3
mytuple=tuple(["Max",28,"Boston"])
print(mytuple)


print("-----------------------")
#ways to access tuples elements
for i in mytuple:
    print(i)
print("-----------------------")
for i in range(len(mytuple)):
    print(mytuple[i])
print("-----------------------")

#behaves like list
print(mytuple[-1])#Boston
print(mytuple[-2])#28
print(mytuple[1:2])#28,
print(mytuple[0:2])#Max,28,
print(mytuple[::])#whole tuple
print(mytuple[::1])#whole tuple
print(mytuple[::2])#Max,Boston

#how to change tuple elements
#mytuple[0]="tim" is not valid method since tuple is immutable


my_tuple=('a','b','c','d','a','b','c','c')
unique=[]
for i in range(len(my_tuple)):
    if  my_tuple[i] not in (unique):
        print(my_tuple[i]," exists in tuple ",my_tuple.count(my_tuple[i])," times")
        unique.append(my_tuple[i])
print(unique)

print(type(my_tuple))
print(type(unique))

#conversion of tuple to list
my_list=list(my_tuple)
print(my_list)
my_list=tuple(my_list)
print(my_list)

print(my_list[1:5])#('b', 'c', 'd', 'a')

#unpacking values of tuple
#specifying same number of elements in mytuple
a,b,c=mytuple
print(a,b,c)
#not specifying same number of elements in mytuple

a,*b,c=my_tuple
print(a)#a
print(*b)#b c d a b c  --- all variable elements
print(c)#c

#tuple is more efficient in large data
#Tuple: ordered, immutable,allows duplicate elements

import sys
my_list=[0,1,2,"hello",True]
my_tuple=(0,1,2,"hello",True)
print(sys.getsizeof(my_list),"bytes")#104 bytes
print(sys.getsizeof(my_tuple),"bytes")#88 bytes

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000)) #66ms
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000)) #15ms