# Assignment 07, Task 03
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 1.30 hrs

class DataFrame:
    def __init__(self):
        self.items = []
    def add(self, x):
        if isinstance(x,list) or isinstance(x,tuple):
            for i in x:
                self.items.append(i)
        else:
            self.items.append(x)
    def mean(self):
        sum = 0
        for i in self.items:
            sum+=i
        return sum/len(self.items)
    def percentile(self, r):
        new = sorted(self.items)
        percent = (r/100)*len(new)
        return new[int(percent)]
    def mode(self):
        count = dict()
        for i in self.items:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return [x for x,y in count.items() if y == max(count.values())][0]
    def sd(self):
        n = len(self.items)
        mean = self.mean()
        ans = 0
        for i in self.items:
            ans += (i-mean)**2
        return (ans/n)**0.5
