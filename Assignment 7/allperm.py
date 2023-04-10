# Assignment 07, Task 01
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 04:30 hrs

def all_perm(n: int) -> set[tuple[int, ...]]:
    if n == 1:
        return {(1,)}
    else:
      n_1 = list(all_perm(n-1))
      for i in range(len(n_1)):
        n_1[i] = list(n_1[i])
      new = []
      for i in range(len(n_1)):
          for j in range(len(n_1[i]) + 1):
              new_in = []
              for h in [x for x in n_1][i]:
                  new_in.append(h)
              new_in.insert(j, n)
              new.append(tuple(new_in))
      return set(new)

