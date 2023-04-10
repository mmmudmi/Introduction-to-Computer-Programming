# Assignment 05, Task 04
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 03:00 hrs

def parse_time(line: str) -> int:
    new = line[:]
    time = ''
    minute = ''
    i = 0
    while i < len(new):
        if new[i] == ';':
            new = new[i+6:]
            break
        else:
            i+=1
    j = 0
    while j < len(new):
        if new[j] not in '0123456789':
            new = new[j:]
            break
        else:
            time+=new[j]
            j += 1
    h = 0
    while h < len(new):
        if new[h] == ';':
            minute += '0'
            break
        else:
            if new[h+1] not in '0123456789':
                break
            else:
                minute += new[h+1]
                h += 1
                continue
    time, minute = int(time), int(minute)

    result = (time*60)+minute
    return result

def parse_dist(line: str) -> float:
    number = ''
    n = line[:]
    i = 0
    while i < len(n):
        if n[i:i+9] == 'distance:':
            number += n[i+9:]
            i += 1
            continue
        else:
            i += 1
    result = float(number)
    if result - int(result) == 0:
        result = int(result)
    return result

def jogging_average(activities: list[str]) -> float:
    new_lst = []
    j = 0
    while j < len(activities):
        if activities[j][:8] == 'jogging;':
            new_lst.append(activities[j])
            j += 1
        else:
            j += 1
    distance = 0
    time = 0
    for i in new_lst:
        distance += parse_dist(i)
        time += parse_time(i)
    distance = distance*1000
    avg = distance/time
    return avg







