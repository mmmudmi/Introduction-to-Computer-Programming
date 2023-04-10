# Assignment 06, Task 06
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 06:30 hrs

def isGameOver(board: list[list[str]]) -> bool:
    count = 0
    for i in range(len(board)):
        count_in = 0
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                count_in += 1
        count += count_in
    if count != 0:
        return False
    else:
        another_count = 0 #when there is no ' ', but numbers still can add up
        for i in range(len(board)):
            j = 0
            while j < len(board[i])-1:
                if board[i][j] == board[i][j+1]:
                    another_count += 1
                    j += 2
                else:
                    j+=1
        for i in range(len(board[0])):
            j = 0
            while j < len(board)-1:
                if board[j][i] == board[j+1][i]:
                    another_count += 1
                    j += 2
                else:
                    j += 1
        return another_count == 0

def doKeyUp(board: list[list[str]]) -> tuple[bool, list[list[str]]]:
    def elements(d):  # should combine everything here
        columns = []  # list of each columns
        for i in range(len(d[0])):
            column = []
            for j in range(len(d)):
                if d[j][i] != ' ':
                    column.append(d[j][i])
            if len(column) == 0:
                column.append(' ')
            columns.append(column)
        step2 = columns  # combine same numbers
        for i in range(len(step2)):
            for j in range(1, len(step2[i])):
                if step2[i][-j] == step2[i][-(j + 1)]:
                    f, s = int(step2[i][-j]), int(step2[i][-(j + 1)])
                    step2[i][-j], step2[i][-(j + 1)] = str(f + s), ' '
        for i in step2:
            if ' ' in i:
                i.remove(' ')
        return step2
    def go_left(b):
        blank = []  # column*row
        for i in b[0]:
            blank_in = []
            for j in b:
                blank_in.append(' ')
            blank.append(blank_in)
        result = blank[:]
        e = elements(b)
        for i in range(len(e)):
            for j in range(len(e[i])):
                result[i][j] = e[i][j]
        return result
    new_board = []  # [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    for i in board:
        blank_in = []
        for j in board[0]:
            blank_in.append(' ')
        new_board.append(blank_in)
    last_step = go_left(board)
    for i in range(len(new_board[0])):
        for j in range(len(new_board)):
            new_board[j][i] = last_step[i][j]
    return new_board != board ,new_board

def doKeyDown(board: list[list[str]]) -> tuple[bool, list[list[str]]]:
    def elements(d):  # should combine everything here
        columns = []  # list of each columns
        for i in range(len(d[0])):
            column = []
            for j in range(len(d)):
                if d[j][i] != ' ':
                    column.append(d[j][i])
            if len(column) == 0:
                column.append(' ')
            columns.append(column)
        step2 = columns  # combine same numbers
        for i in range(len(step2)):
            for j in range(len(step2[i]) - 1):
                if step2[i][j] == step2[i][j + 1]:
                    f, s = int(step2[i][j]), int(step2[i][j + 1])
                    step2[i][j], step2[i][j + 1] = str(f + s), ' '
        for i in step2:
            if ' ' in i:
                i.remove(' ')

        return step2  # [['4', '2', '4'], ['4', '2'], ['4', '2'], [], ['4', '2'], ['4', '16']]
    def go_right(b):
        blank = []  # [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
        for i in b[0]:
            blank_in = []
            for j in b:
                blank_in.append(' ')
            blank.append(blank_in)
        result = blank[:]
        e = elements(b)
        for i in range(len(e)):
            for j in range(1, len(e[i]) + 1):
                result[i][-j] = e[i][-j]
        return result
    new_board = []  # [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    for i in board:
        blank_in = []
        for j in board[0]:
            blank_in.append(' ')
        new_board.append(blank_in)
    last_step = go_right(board)
    for i in range(len(new_board[0])):
        for j in range(len(new_board)):
            new_board[j][i] = last_step[i][j]
    return new_board != board ,new_board

def doKeyLeft(board: list[list[str]]) -> tuple[bool, list[list[str]]]:
    def elements(d):  # should combine everything here
        rows = []  # list of each columns
        for i in range(len(d)):
            row = []
            for j in range(len(d[i])):
                if d[i][j] != ' ':
                    row.append(d[i][j])
            if row == []:
                rows.append([])
            else:
                rows.append(row)  # [['2', '4', '4', '4'], ['2', '8'], ['2', '2', '2'], ['2', '2', '2', '8'], []]
        step2 = rows[:]
        for i in range(len(step2)):
            for j in range(1,len(step2[i])):
                if step2[i][-j] == step2[i][-(j + 1)] and step2[i][-j] != ' ':
                    f, s = int(step2[i][-j]), int(step2[i][-(j + 1)])
                    step2[i][-j], step2[i][-(j + 1)] = str(f + s), ' '
        for i in step2:
            for j in i:
                if ' ' in j:
                    i.remove(' ')
        return step2
    blank = []  # row*column
    for i in board:
        blank_in = []
        for j in i:
            blank_in.append(' ')
        blank.append(blank_in)
    new_board = blank[:]
    e = elements(board)
    for i in range(len(new_board)):
        for j in range(len(e[i])):
            new_board[i][j] = e[i][j]
    return new_board != board ,new_board

def doKeyRight(board: list[list[str]]) -> tuple[bool, list[list[str]]]:
    def elements(d):  # should combine everything here
        rows = []  # list of each columns
        for i in range(len(d)):
            row = []
            for j in range(len(d[i])):
                if d[i][j] != ' ':
                    row.append(d[i][j])
            if row == []:
                rows.append([])
            else:
                rows.append(row)  # [['2', '4', '4', '4'], ['2', '8'], ['2', '2', '2'], ['2', '2', '2', '8'], []]
        step2 = rows[:]
        for i in range(len(step2)):
            for j in range(len(step2[i]) - 1):
                if step2[i][j] == step2[i][j + 1] and step2[i][j] != ' ':
                    f, s = int(step2[i][j]), int(step2[i][j + 1])
                    step2[i][j], step2[i][j + 1] = str(f + s), ' '
        for i in step2:
            for j in i:
                if ' ' in j:
                    i.remove(' ')
        return step2
    blank = []  # row*column
    for i in board:
        blank_in = []
        for j in i:
            blank_in.append(' ')
        blank.append(blank_in)
    new_board = blank[:]
    e = elements(board)
    for i in range(len(new_board)):
        for j in range(1,len(e[i])+1):
            new_board[i][-j] = e[i][-j]
    return new_board != board ,new_board

def emptyPos(board: list[list[str]]) -> list[tuple[int, int]]:
    row_col = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                row_col.append((i,j))
    return row_col #input[[' ', '2'],['4', ' ']] #return [(0,0), (1,1)]








