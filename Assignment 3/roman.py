# Assignment 03, Task 08
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:9 hrs

def toRoman(n: int) -> str:
    one = "I"
    five = "V"
    ten = "X"
    fifty = "L"
    hundred = "C"
    five_hundred = "D"
    thoundsand = "M"
    length = len(str(n))
    def last(n: int):
        if int(n[length-1]) in (1,2,3):
            return I*(int(n[length-1]))
        elif int(n[length-1]) in (6,7,8):
            return I*(int(n[length-1])-5)
        elif int(n[length-1])==5:
            return V
    def second_last(n:int):
        if int(n[length-2])==10:
            return




    if n < 10:
        if n[0] in (1,2,3):
            return I*n
    elif 10 <= n <= 99:

    elif 100 <= n <= 999:

    elif n >= 1000:
