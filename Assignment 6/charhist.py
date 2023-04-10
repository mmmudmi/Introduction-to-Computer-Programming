# Assignment 06, Task 01
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 04:30 hrs

def charHistogram(filename: str) -> None:
    reader = open(filename, 'r')
    info = ''
    for i in reader.read():
        info += i
    info = info.lower()
    letter = dict()
    for i in info:
        if i.isalpha():
            if i in letter:
                letter[i] += 1
            else:
                letter[i] = 1
    s_to_l = sorted(letter.values())
    l_to_s = []
    for i in range(1, len(s_to_l) + 1):
        l_to_s.append(s_to_l[-i])
    new = []
    while len(new) <= len(letter):
        #after sorted will return list so convert list to dict
        letter2 = sorted(letter.items())
        letter = dict()
        for x, y in letter2:
            letter[x] = y

        for l in l_to_s:
            for i, j in letter.items():
                if j == l:
                    new.append([i, j])
                    break
            del letter[i]
    for i, j in new:
        print(i,'+' * j)
    reader.close()


