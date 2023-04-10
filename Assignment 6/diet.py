# Assignment 06, Task 05
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 04:30 hrs
def count(lst,word):
    c = 0
    for i in lst:
        if word == i :
            c+=1
    return c

def seperate_db(string):
    new = []
    i = 0
    while i < len(string):
        if string[i] == ':':
            new.append(string[:i])
            string = string[i+1:]
            break
        i+=1
    c,p,f = string.split(',')
    c,p,f = float(c)*4, float(p)*4, float(f)*9
    new.append(c+p+f)
    return new

def seperate_recipes(string):
    re = []
    i = 0
    while i < len(string):
        if string[i] == ':':
            re.append(string[:i])
            string = string[i + 1:]
            break
        i += 1
    x = []
    for j in string.split(','):
        n,q = j.split('*')
        y = []
        y.append(int(q))
        y.append(n)
        x.append(y)
    return re+x


def mealCal(meal: list[str], recipes: list[str], db: list[str]) -> float:
    cals = dict()
    for i in db:
        new = seperate_db(i)
        cals[new[0]] = new[1]
    recipe = dict()
    for j in recipes:
        re = seperate_recipes(j)
        recipe[re[0]] = re[1:]
    second = 0
    third = []
    for a in recipe.items():
        for b in range(len(a[1])):
            x = cals[a[1][b][1]] * a[1][b][0]
            second += x
            third.append([a[0],second])
        second = 0
    menu = dict()
    for i,j in third:
        menu[i] = j
    final = []
    for r in meal:
        if r not in str(final):
            final.append([count(meal,r),r])
    total = 0
    for l in final:
        total += menu[l[1]]*l[0]
    return total

"""
print(mealCal(["T-Bone", "T-Bone", "Green Salad1"], [
              "Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
              "Green Salad1:Cabbage*10,Carrot*2,Pineapple*5",
              "T-Bone:Carrot*2,Steak Meat*1"],
              ["Cabbage:4,2,0", "Carrot:9,1,5", "Fatty Pork:431,1,5",
               "Pineapple:7,1,0", "Steak Meat:5,20,10", "Rabbit Meat:7,2,20"]))
"""

