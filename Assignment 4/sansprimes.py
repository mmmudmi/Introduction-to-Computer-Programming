# Assignment 04, Task 07
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 03:40 hrs
def is_prime(n:int) -> bool:
    a = 0
    i = 1
    while i<=n:
        if (n % i) == 0:
            a += 1
            i += 1
            continue
        i += 1
    if n <= 1 :
        return False
    elif a>2:
        return False
    else:
        return True

def sans_primes(numbers: list[int])-> list[int]:
    b = []
    i = 0
    while i < len(numbers):
        if is_prime(numbers[i]) == True and i+1 < len(numbers):
            if is_prime(numbers[i+1]) == False:
                i += 2
                continue
            elif is_prime(numbers[i+1]) == True:
                i += 1
                continue
        elif is_prime(numbers[i]) == False:
            b.append(numbers[i])
            i+=1
            continue
        elif is_prime(numbers[len(numbers)-1]) == True:
            i += 1

    return b

