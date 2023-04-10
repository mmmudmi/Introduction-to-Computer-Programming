# Assignment 06, Task 02
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 01:30 hrs
def passwordOK(password: str) -> bool:
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = '0123456789'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spe = '$#@%!'
    count_lower = 0
    count_number = 0
    count_upper = 0
    count_spe = 0
    for i in password:
        if i in lower:
            count_lower += 1
        elif i in number:
            count_number += 1
        elif i in upper:
            count_upper += 1
        elif i in spe:
            count_spe += 1
    if len(password) > 12 or len(password) < 6:
        return False
    else:
        for j in range(len(password)-1):
            if password[j] == password[j+1] and password[j] == password[j+2]:
                return False
        if count_lower>0 and count_spe>0 and count_upper>0 and count_number>0:
            return True
        else:
            return False




