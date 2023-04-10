# Assignment 03, Task 03
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 02:00 hrs

def kthDigit(x: int, b: int, k: int) -> int:
    first = int(x / 100)
    second = int((x - (first * 100)) / 10)
    third = int((x - (first * 100) - (second * 10)))

    if b == 10:
        radix = (first * (b ** (2))) + (second * (b ** (1))) + (third * (b ** (0)))
        f = int(radix / 100)
        s = int((radix - (f * 100)) / 10)
        t = int((radix - (f * 100) - (s * 10)))
        if k == 0:
            return t
        elif k == 1:
            return s
        elif k == 2:
            return f
        else:
            return 0
    else:
        first_step = x // b
        second_step = first_step / b
        third_step = second_step - int(second_step)  # int(second_step) is k=2
        forth_step = third_step * b  # result for k=1
        if k == 0:
            return int(x%b)
        elif k == 1:
            return int(forth_step)
        elif k == 2:
            return first_step//b
        else:
            return 0

