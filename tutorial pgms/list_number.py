A=[1,2,3,4,5,4,5,10,8,3,2,1]

A.sort()
print("list A is ",A)
A.reverse()
print("list A reverse is ",A)

new_A=sorted(A)
print(new_A)
new_list =[0]*5
print(new_list)
n_l =A+new_A
print(n_l)

a=[]
for i in range(5):
    a.append(i+1)

print(a)

#slicing
sample=[1,2,3,4,5,6,7,8,9]
a=sample[1:5]
print(a)
#step index
print(sample[1::2])
print(sample[::1])
print(sample[1:5:2])
print(sample[1:10:2])

print(sample[::-1])  #reversing list

#list assignment
A=[1,3,4,6]
a=A  #this will assign whole list and any future operations on original list
b=A[:] #this will assign whole list and not  any future operations on original list
print(A)
print(a)
A.append(5)
print(A)
print(a)
print(b)


A=[1,2,3,4,5]
B=[i*i for i in A]
print(B)