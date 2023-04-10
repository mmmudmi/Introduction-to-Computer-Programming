# Assignment 02, Task 03
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 01:20 hrs

length: int= len(st)
slice: int= int(k % length)
shift: str= st[length-slice:]
rest = st[:length-slice]
shifted_st = shift+rest
print (shifted_st)
