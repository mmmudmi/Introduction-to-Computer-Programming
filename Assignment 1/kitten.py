# Assignment 02, Task 06
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:10 hrs

minute: float= minute/100
time: float = hour+minute

in_trouble: bool = (time<6.30 or time>21.00) and meowing
print(in_trouble)