# Assignment 05, Task 06
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 01:30 hrs
def index_of_largest_gap(data: list[int]):
    index = dict()
    i = 0
    while i < len(data)-1:
        index[i] = abs(data[i]-data[i+1])
        i += 1
    for x,y in index.items():
        if y == max(index.values()):
            largest = x
    return largest

def separate(data: list[int], k: int) -> list[list[int]]:
    if len(data) == 0:
        return []
    data.sort()
    new = data[:]
    result = []
    i = 1
    while i < k:
        x = index_of_largest_gap(new)
        result.insert(0,new[x+1:])
        new = new[:x+1]
        i += 1
    result.insert(0,new)
    return result

print(separate([],1))




