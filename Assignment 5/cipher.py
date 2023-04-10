# Assignment 05, Task 03
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 02:30 hrs
def break_down(a):
    s = []
    for i in a:
        s+=i
    return s

def enc(msg: str, key: int) -> str:
    table = [] #1
    m = break_down(msg)
    while len(m)!=0:
        table_in = []
        j = 0
        while j < key:
            if len(m)>=key:
                table_in.append(m[j])
                j += 1
                continue
            elif j < len(m):
                table_in.append(m[j])
                j += 1
                continue
            else:
                table_in.append('!NONE!')
                j += 1
        m = m[j:]
        table.append(table_in)

    i = 0
    result = ''
    while i < key:
        h = 0
        while h < len(table):
            if table[h][i] != '!NONE!':
                result+=table[h][i]
                h += 1
                continue
            else:
                h += 1
        i += 1
    return result




