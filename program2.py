"""Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not."""

a=int(input('Enter a no '))

def paremeter(a):
  step=0
  for num in range(1,a+1):
      if a%num==0:
        step =step+1
  if step==2:
    print('perime no')
  else:
    print('not prime no')            

paremeter(a)  