#!/usr/bin/python
#Ref Generators implementations & usage: https://www.programiz.com/python-programming/generator

#This steps were executed in Jupyter Notebook. To understand the generatr go through the reference link & then execute below sample code.
#Comment '#-----------------------------------' is the breakpoint for execution.

#----------------------------------- 
myList = [1,4,5,6,88,3,3,4,5,46,6,7,4,7]
print(myList)

#-----------------------------------

#for x in myList:
#    print(x)

print(str([x*2 for x in myList]))
#myIter = iter(myList)
#print(myIter)
#print(next(myIter))
myDict = {'A':1,'B':2,'C':3}
print(myDict)
print('A' in myDict)
print('X' in myDict)

#-----------------------------------

print(myIter.__next__())
print(next(myIter))

#-----------------------------------

my_list=[1,2,3,4,4,5]
def my_gen():
    for i in my_list:
        yield i

a = my_gen()    
print(next(a))
print(next(a))

#-----------------------------------

my_list=[1,2,3,4,4,5]
print(type([x*2 for x in my_list]))
print([x*2 for x in my_list])
print(type((x*2 for x in my_list)))
a = (x*2 for x in my_list)
print(next(a))
print(next(a))

print('using for loop')

b = (x*2 for x in my_list)
#This is an infinite stream call for even numbers
#for x in b:
    #print (x)
    
#-----------------------------------

myList = [0,9,8,7,6,5,4,3,2,1,23,43,4,54,5,5,66,5,6,66,7]
print('sum on list '+ str(sum(myList)))
evenNum = (x for x in myList if x%2==0)
for num in evenNum:
    print (num)

oddNum = (x for x in myList if x%2!=0)    
print('sum methos on generator '+str(sum(oddNum)))

#-----------------------------------

