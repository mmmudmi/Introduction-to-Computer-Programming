# Assignment 04, Task 01
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:25 hrs
def altSum(lst: list[int]) -> int:
    if len(lst) == 0:
        return 0
    else:
        total = lst[0]
        for i in range(1, len(lst)):
            if (i % 2) != 0:  # odd index
                total = total + lst[i]
            else:  # even index
                total = total - lst[i]
        return total
#print (altSum([]))
