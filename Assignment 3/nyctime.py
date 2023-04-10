# Assignment 03, Task 06
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 01:20 hrs
def nycHour(bkkHour: int) -> str:

    def bkk(bkkHour: int):
        if bkkHour == 0:
            return 12
        elif 1<=bkkHour<=12:
            return bkkHour
        else:
            return bkkHour-12

    nyc = str(abs(bkk(bkkHour)+1))

    if 1<=bkkHour<=10 or bkkHour==23:
        return nyc+"pm"
    elif bkkHour == 0:
        return "1"+"pm"
    elif 11<=bkkHour<=22:
        return nyc+"am"






