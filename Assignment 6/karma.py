# Assignment 06, Task 03
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 02:30 hrs
def list_to_str(l):
    s = ''
    for i in l:
        s+=i
    return s

def transfer(n): #"John->Jeff"
    n = list(n)
    first = []
    m = []
    i = 0
    while i < len(n): #"John->Jeff"
        if n[i] == '-':
            n = n[i+2:]
            break
        else:
            first.append(n[i])
            i+=1
    second = n
    f = ''
    for i in first:
        f += i
    s = ''
    for i in second:
        s += i
    return [f,s] #['John', 'Jeff']


def keepTabs(actions: list[str]) -> dict[str, int]:
    karma = dict()
    for i in actions:
        if '--' in i:
            i = list(i)[:-2]
            i = list_to_str(i)
            if i in karma:
                karma[i] -= 1
            else:
                karma[i] = -1
        elif '++' in i:
            i = list(i)[:-2]
            i = list_to_str(i)
            if i in karma:
                karma[i] += 1
            else:
                karma[i] = 1
        elif '->' in i:
            x,y = transfer(i)
            if x in karma:
                if y in karma:
                    karma[y] += karma[x]
                    karma[x] = 0
                else:
                    karma[y] = karma[x]
                    karma[x] = 0
        will_delete = []
        for i,j in karma.items():
            if j == 0:
                will_delete.append(i)
        for d in will_delete:
            del karma[d]
    return karma
