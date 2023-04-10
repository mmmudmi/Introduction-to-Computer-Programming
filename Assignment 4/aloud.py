# Assignment 04, Task 04
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 01:50 hrs

def readAloud(lst: list[int]) -> list[int]:
    i = 0
    s = 1
    a = []
    while i<len(lst):
        if i+1<len(lst):
            if lst[i] == lst[i + 1]:
                s += 1
                i += 1
                continue
            elif lst[i - 1] == lst[i] and lst[i] != lst[i + 1] and i > 0:
                a.append(s)
                a.append(lst[i])
                s -= (s-1) #reset s
                i += 1
                continue
            else:
                a.append(s)
                a.append(lst[i])
                i += 1
        else:
            a.append(s)
            a.append(lst[i])
            i += 1
    return a

print(readAloud([-1,-1,-1]))
