# Assignment 03, Task 07
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:9 hrs

def got_table(you: int, date: int) -> str:
    if you<=2 or date<=2:
        return "no"
    elif you>=8 or date>=8:
        return "yes"
    else:
        return "maybe"
