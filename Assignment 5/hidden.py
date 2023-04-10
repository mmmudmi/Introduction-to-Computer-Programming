# Assignment 05, Task 02
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 00:30 hrs

def is_hidden(s:str,t:str)->bool:
    ss = s.lower()
    tt = t.lower()
    count = 0
    for i in tt:
        j = 0
        while j<len(ss):
            if ss[j] == i:
                count+=1
                ss = ss[j+1:]
                j+=1
                break
            else:
                j+=1
    return count == len(tt)






