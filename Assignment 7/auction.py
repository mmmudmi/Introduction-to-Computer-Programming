# Assignment 07, Task 04
# Name: Pearploy Chaicharoensin
# Collaborators: -
# Time Spent: 07:00 hrs
class Bid:
    def __init__(self,bid_id, bidder_id, auction):
        self.bid_id = bid_id
        self.bidder_id = bidder_id
        self.auction = auction
    def __str__(self):
        return f'The bid id: {self.bid_id}, The bidder id: {self.bidder_id}, The auction id: {self.auction}'
    def __repr__(self):
        return f'bid_id: {self.bid_id}: bidder_id: {self.bidder_id}: auction_id: {self.auction}'
    def __lt__(self, other):
        return self.bid_id < other.bid_id

class Auction:
    def __init__(self,auction):
        self.auction = auction
        self.price = 1.0
        try:
            self.winner = self.bidder_id
        except:
            self.winner = None

    def placeBid(self, bidder_id):
        self.bidder_id, self.winner = bidder_id, bidder_id
        self.price += 1.5

    def __repr__(self):
        return f'Auction(price: {self.price}, winner: {self.winner})'
    def __str__(self):
        return f'Auction(\'price\': {self.price}, \'winner\': {self.winner})'

def CSV2List(csvFilename: str) -> list[Bid]:
    reader,new = open(csvFilename, 'r'), []
    for line in reader.readlines():
        new_in = ''
        for i in line:
            if i not in '\r\n\t ':
                new_in += i
        new.append(new_in)
    order, head = [], new[0].split(',')
    for i in range(len(head)):
        if head[i] == 'bid_id':
            order.append(('bid_id',i))
        elif head[i] == 'bidder_id':
            order.append(('bidder_id',i))
        elif head[i] == 'auction':
            order.append(('auction',i))
    lst = []
    for line in range(1,len(new)):
        lst_in,s = [], new[line].split(',')
        for x,y in order:
            if x == 'bid_id':
                lst_in.insert(0,s[y])
            elif x == 'bidder_id':
                lst_in.insert(1,s[y])
            elif x == 'auction':
                lst_in.insert(2,s[y])
        lst.append(lst_in)
    lst.sort()
    final = []
    for i in lst:
        final.append(Bid(i[0],i[1],i[2]))
    reader.close()
    return final

def mostPopularAuction(bidList: list[Bid]) -> set[Auction]:
    auc = dict()
    for i in bidList:
        if i.auction not in auc:
            auc[i.auction] = [i.bidder_id]
        elif i.auction in auc and i.bidder_id not in auc[i.auction]:
            auc[i.auction].append(i.bidder_id)
    for i in auc:
        auc[i] = len(auc[i])
    return {x for x,y in auc.items() if y == max(auc.values())}

def auctionWinners(bidList: list[Bid]) -> dict[str, Auction]:
    auc_dict = dict()
    for j in bidList:
        if j.auction not in auc_dict:
            auc_dict[j.auction] = Auction(j.auction)
    order = dict()
    for h in bidList:
        if h.auction not in order:
            order[h.auction] = [(int(h.bid_id),h)]
        else:
            order[h.auction].append((int(h.bid_id),h))
            order[h.auction].sort()
    for i in auc_dict:
        for x,y in order[i]:
            auc_dict[i].placeBid(y.bidder_id)
    return auc_dict

ll = CSV2List('sample_bids.csv')
hh = CSV2List('t.txt')
#print(ll)
#print(mostPopularAuction(ll))
print(auctionWinners(ll))

