# -*- coding: utf-8 -*-

"""
AuctionObj contains the auction classes
"""
import hashlib as hash

#auctioninput requires a delimited rope and a date
#it's used as the basis for input into the DB
class AuctionInput:
    def __init__(self, delimitedRope, timestamp):
        self.timeStamp = timestamp
        self.itemID = delimitedRope[0] # item id
        self.size = delimitedRope[10] # stack size
        self.bid = int(int(delimitedRope[17])/int(self.size))# current bid, divided by the stacksize, rounded
        self.buy = int(int(delimitedRope[16])/int(self.size)) # current buyout price, divided by the stacksize, rounded
        self.timeLeftMin,self.timeLeftMax = self.makeTimeLeft(delimitedRope[6]) # time left
        self.seller = self.cleanSeller(delimitedRope[19])
        self.ID = self.makeID()
    # returns the class in list form
    def toList(self):
        return [self.ID,self.timeStamp,self.itemID,self.seller,self.size,self.buy,self.bid,self.timeLeftMin,self.timeLeftMax]
    def makeID(self):
        s = ""
        attributes = [self.timeStamp,self.itemID,self.seller,self.size,self.buy,self.bid,self.timeLeftMin,self.timeLeftMax]
        for i in attributes:
            s+= str(i) + ","
        return hash.sha224(s.encode('utf-8')).hexdigest()[0:16]
    def makeTimeLeft(self, ropeValue):
        t = int(ropeValue) # time left
        cipher= [[0,1],[1,4],[4,16],[16,48]] #in halfhour blocs, 1 == 30m
        for i in [1,2,3,4]:
            if t == i:
                return cipher[i-1][0], cipher[i-1][1]
    def cleanSeller(self,ropeValue):
        return str(ropeValue[2:len(ropeValue)-2])