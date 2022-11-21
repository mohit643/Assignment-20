# Write a python program to access a function inside a function.


def fun(a,b):
  return a+b


def sum(a,b,c):
  
  add=fun(a,b)
  return fun(c,add)
  

print(sum(2,3,1))  