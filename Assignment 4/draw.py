# Assignment 04, Task 03
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 01:30 hrs
def triangle(k: int) -> None: #k line, 2k-1charactor in each line
    for i in range(1,k+1):
        star = "*" * ((2*i)-1)
        square = "#" * (k-i)
        print (square+star+square)

def diamond(k: int) -> None:
    for i in range(1,k+1): #top
        star = "*" * ((2*i)-1)
        square = "#" * ((k+1)-i)
        print (square+star+square)
    for i in range(1,k+1): #bottom
        star = "*" * ((2*(k-i))+1)
        square = "#" * (i)
        print (square+star+square)



