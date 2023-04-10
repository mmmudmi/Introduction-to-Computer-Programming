# Assignment 04, Task 06
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 02:00 hrs
def sumOfDigitsSquared(n: int) -> int:
    n = str(n)
    i = 0
    total = 0
    while i < len(n):
        total += (int(n[i])**2)
        i += 1
    return total

def isHappy(n: int) -> bool:
    while True:
        n = sumOfDigitsSquared(n)
        if n == 4:
            return False
        elif n == 1:
            return True

def kThHappy(k: int) -> int:
    s = []
    i = 1
    while len(s)<k:
        if isHappy(i) == False:
            i += 1
            continue
        s.append(i)
        i+=1
    return s[k-1]

#print(kThHappy(1))

