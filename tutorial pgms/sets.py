#Sets : unordered,mutable, no duplicate

#ways of defining
#way1
myset={1,2,3,4,5,6,7,8,9,0}
print(type(myset))
print(myset)#prints sets in ascending order for numbers but arbitrary for strings

myset2={1,1,0}
print(myset2)  #display only 0,1 as it doesn't allow duplicate elements although no error message

print("----------------------------------")
#way2
myset3=set([1,2,3,4,4,5,6])
print(myset3)

myset4=set("Hello")
print(myset4)  #display in arbitrary order for strings

#defining empty set
# myset={}    ----> this is dictionary not a set
myset=set()
print(type(myset))

