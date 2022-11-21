# Write a python program to create a function to find the Min of three numbers.


def compare():
  a,b,c=int(input("enter three no ")),int(input()),int(input())
  print(a,b,c)
  if a>b and a>c:
    print(a)
  elif b>a and b>c:
    print(b)
  else:
    print(c)    



compare()