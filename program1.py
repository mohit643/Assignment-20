"""Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements."""




def list():
 FirstList=[eval(a) for a in input("enter  list").split(',')]
 SecondList=[]
 for element in FirstList:
  if element not in SecondList:
    SecondList.append(element)
 return SecondList   


print(list()) 
