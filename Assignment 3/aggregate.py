# Assignment 03, Task 01
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:30 hrs
def my_min(p: float, q: float, r: float) -> float :
    if p<q and p<r:
        return p
    elif q<p and q<r:
        return q
    elif r<p and r<q:
        return r

def my_mean(p: float, q: float, r: float) -> float:
    return (p+q+r)/3


def my_med(p: float, q: float, r: float) -> float:
    if q<p<r:
        return p
    elif q<r<p:
        return r
    elif r<p<q:
        return p
    elif r<q<p:
        return q
    elif p<q<r:
        return q
    elif p<r<q:
        return r
