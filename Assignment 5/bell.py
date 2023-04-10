# Assignment 05, Task 01
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 01:50 hrs
def loveTri(n: int) -> list[list[int]]:
    new = []
    i = 0
    j = 0
    while i < n: #3
        new_in = []
        if i == 0:#start with [1]
            new_in.append(1)
            new.append(new_in)
            i+=1
            continue
        else:
            while j < i:
                new_in.append(new[j][-1]) #last elem of the previous row
                h = 0
                while h < j+1:
                    x = new_in[h]+new[j][h]
                    new_in.append(x)
                    h += 1
                j += 1
        new.append(new_in)
        i += 1
    return new



