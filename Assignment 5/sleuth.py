# Assignment 05, Task 05
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 04:30 hrs

def read_left_to_right(grid,w):
    count, row, word = 0,0,''
    while row < len(grid):
        for i in grid[row]:
            word += i
        if w in word:
            count += 1
            row += 1
        else:
            row += 1
            word = ''
    return count != 0

def contains_word(grid: list[list[str]], w: str) -> bool:
    if read_left_to_right(grid,w):
        return True
    else:
        column = 0
        new = []
        i = 0
        while i < len(grid):
            new_in = []
            j = 0
            while j < len(grid[i]):
                new_in.append(grid[j][i])
                j += 1
            new.append(new_in)
            i += 1
        if read_left_to_right(new,w)==True:
            return True
        else:
            i, new = 0, []
            while i < len(grid):  # first half, included the diagonal
                new_in = ''
                j = 0
                while j < len(grid[i]) - i:
                    new_in += grid[i + j][j]
                    j += 1
                new.append(new_in)
                i += 1
            i = 0
            while i < len(grid) - 1:  # second half
                new_in = ''
                j = 0
                while j < len(grid[i]) - (i + 1):
                    new_in += grid[j][i + j + 1]
                    j += 1
                new.append(new_in)
                i += 1
            count = 0
            for c in new:
                if w in c:
                    count += 1
            if count != 0:
                return True
            else:
                i, new = 0, []
                while i < len(grid):
                    j = 0
                    new_in = ''
                    while i - j >= 0:
                        new_in += grid[i - j][j]
                        j += 1
                    new.append(new_in)
                    i += 1
                i = 0
                while i < len(grid) - 1:
                    new_in = ''
                    j = 1
                    while i + j + 1 < len(grid[i]) + 1:
                        new_in += grid[len(grid[i]) - (j)][i + j]
                        j += 1
                    new.append(new_in)
                    i += 1
                count = 0
                for c in new:
                    if w in c:
                        count += 1
                if count != 0:
                    return True
                else:
                    return False

def make_unique(lst: list[str]) -> list[str]:
    return list(set(lst))

def word_sleuth(grid: list[list[str]], words: list[str])->list[str]:
    words = make_unique(words)
    result = []
    for i in words:
        if contains_word(grid,i):
            result.append(i)
    return result





