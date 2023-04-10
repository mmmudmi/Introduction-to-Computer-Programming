# Assignment 06, Task 04
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:30 hrs
def eto(lst: list[int]) -> list[int]:
    if len(lst) == 0:
        return []
    else:
        new = []
        head = (lst[0])
        tail = lst[1:]
        if head % 2 == 0:
            new = new + [head] + eto(tail)
        else:
            new = new + eto(tail) + [head]
        return new
