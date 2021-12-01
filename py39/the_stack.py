#! /bin/python3

#Explination on how to implement the stack in python.


list=[]
list.append(1) # append 1
print("push:",list)
list.append(2) # append 2
print("push:",list)
list.append(3) # append 3
print("push:",list)
list.pop() # pop 3
print("pop:",list)
print("peek:",list[-1]) # get top most element
list.pop() # pop 2
print("pop:",list)
print("peek:",list[-1]) # get top most element
