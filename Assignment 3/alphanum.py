# Assignment 03, Task 05
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:35 hrs

def phoneWord2Num(word: str) -> int:
    word = word.lower()

    def findnum(length: int) -> int:
        if word[length] in "abc":
            return 2
        elif word[length] in "def":
            return 3
        elif word[length] in "ghi":
            return 4
        elif word[length] in "jkl":
            return 5
        elif word[length] in "mno":
            return 6
        elif word[length] in "pqrs":
            return 7
        elif word[length] in "tuv":
            return 8
        elif word[length] in "wxyz":
            return 9

    return findnum(0)*1000000+findnum(1)*100000+findnum(2)*10000+findnum(3)*1000+findnum(4)*100+findnum(5)*10+findnum(6)
