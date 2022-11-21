"""Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""

def fun():
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in List:
      if x%2==0:
        print(x)
    
fun()