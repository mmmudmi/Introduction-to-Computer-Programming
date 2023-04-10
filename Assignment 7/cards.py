# Assignment 07, Task 02
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 04:30 hrs
Hand = set[tuple[str, str]]

def sort_rank(a):
    if '2' in a:
        ranks = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2','A']
    else:
        ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    with_index = [(i,j) for j in range(len(ranks)) for i in a if i == ranks[j]]
    index = [y for x,y in with_index]
    index.sort()
    new = [ranks[j] for j in index]
    return new

def is_straight_flush(h: Hand) -> bool: #("Diamond", "3")
    lst = list(h)
    dif_suit  = 0
    for i in range(len(lst)-1):
        if lst[i][0] != lst[i+1][0]:
            dif_suit += 1
    if dif_suit != 0:
        return False
    else:
        rank = [i[1] for i in lst]
        rank = sort_rank(rank)
        r = ''
        for i in rank:
            r+=i
        if r in 'AKQJ1098765432A':
            return True
        else:
            return False

def is_four_of_a_kind(h: Hand) -> bool:
    diamonds = 0
    hearts = 0
    spades = 0
    clubs = 0
    lst = list(h)
    for i in lst:
        if i[0] == 'Diamond':
            diamonds += 1
        elif i[0] == 'Heart':
            hearts += 1
        elif i[0] == 'Spade':
            spades += 1
        elif i[0] == 'Club':
            clubs += 1
    return diamonds!=0 and hearts!=0 and spades!=0 and clubs!=0

def is_full_house(h: Hand) -> bool:
    rank = dict()
    lst = list(h)
    for x,y in lst:
        if y in rank:
            rank[y] += 1
        else:
            rank[y] = 1
    if len(rank.items()) != 2:
        return False
    else:
        for i in rank.values():
            if i == 2 or i == 3:
                return True
            else:
                return False

def is_two_pair(h: Hand) -> bool:
    rank = dict()
    lst = list(h)
    for x,y in lst:
        if y in rank:
            rank[y] += 1
        else:
            rank[y] = 1
    return set(rank.values()) == {2,2,1}

def all_hands() -> list[Hand]:
    ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ["Club", "Diamond", "Heart", "Spade"]
    decks = [(s, str(i)) for i in ranks for s in suits]
    def combine(d, n):
        if n == 0:
            return [[]]
        else:
            l = [set([decks[i]]+list(j)) for i in range(len(decks)) for j in combine(decks[:i]+decks[i+1:],n-1)]
        return l
    return combine(decks, 5)

def all_straight_flush() -> list[Hand]:
    return [i for i in all_hands() if is_straight_flush(i)]

def all_four_of_a_kind() -> list[Hand]:
    return [i for i in all_hands() if is_four_of_a_kind(i)]

def all_full_house() -> list[Hand]:
    return [i for i in all_hands() if is_full_house(i)]

def all_two_pair() -> list[Hand]:
    return [i for i in all_hands() if is_two_pair(i)]