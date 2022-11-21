"""Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters."""



def str():
  str=input("enter a string ")
  num=0
  num2=0
  for x in str:
    if x.isupper():
      num+=1
    else:
      num2+=1
  print("uperr str is ",num ,"lower str is ",num2)

str()


