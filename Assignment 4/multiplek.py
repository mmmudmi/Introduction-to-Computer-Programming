# Assignment 04, Task 05
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:06 hrs
def allMultiplesOfK(k: int, lst: list[int]) -> bool:
    i = 0
    a = 0
    while i<len(lst):
        if lst[i] % k == 0:
            a += 1
            i += 1
            continue
        i += 1
    if a == len(lst):
        return True
    else:
        return False

#print(allMultiplesOfK(1, []))