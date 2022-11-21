"""Write a python program to create a function to check whether a string is a pangram
or not."""

def pangram():
  str=input("enete a pangram string ")
  print(str)
  alph="qwertyuioplkjhgfdsazxcvbnm"
  for char in str:
    if char in alph:
      print("pangram string")
    else:
      print("not pangram string")  

pangram()      