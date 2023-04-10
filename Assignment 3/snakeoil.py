# Assignment 03, Task 02
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:25 hrs
def  price(vol: int) -> float:
    a = vol*18
    shipping = 0
    discount = 0
    if 0<vol<20:
        shipping = 250
        return float(a+shipping-discount)
    elif 20<=vol<=100:
        shipping = vol * 10
        return float(a+shipping-discount)
    elif vol>100:
        discount = a/100
        return float(a+shipping-discount)
    else:
        return float(a+shipping-discount)

