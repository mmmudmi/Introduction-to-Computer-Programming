# Assignment 02, Task 01
# Name: Pearploy Chaicharoensin
# Collaborators: Jet Khampitukgula
# Time Spent: 00:35 hrs

s = s.lower()
t = t.upper()
s = s.replace("s","m").replace("l","m").replace("a","m")
t = t.replace("P","T").replace("O","T").replace("I","T").replace("N","T")
first_s = s[:1]
remain_s = s[1:]
first_t = t[:1]
remain_t = t[1:]
s = first_t+remain_s
t = first_s+remain_t
last_s: int = int(len(s)/3)
the_rest_s = s[:last_s*2]
middle_t:int = int(len(s)/3)
middle_t:str= t[middle_t : (middle_t*2)]
s = the_rest_s+middle_t
z = s+t
print(z)