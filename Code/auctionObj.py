# -*- coding: utf-8 -*-

"""
AuctionObj contains the auction classes
"""
import hashlib as hash
import utility as util

#auctioninput requires a delimited rope and a date
#it's used to prep for input into the DB
class AuctionRawInput:
    def __init__(self, delimitedRope, timestamp):
        self.timeStamp = timestamp
        self.itemID = delimitedRope[0] # item id
        self.size = delimitedRope[10] # stack size
        self.bid = int(int(delimitedRope[5])/int(self.size))# current bid, divided by the stacksize, rounded
        self.buy = int(int(delimitedRope[16])/int(self.size)) # current buyout price, divided by the stacksize, rounded
        self.timeLeft = int(delimitedRope[6]) # time left
        self.seller = self.cleanSeller(delimitedRope[19])
        self.ID = self.makeID()
    # returns the class in list form
    def toList(self):
        return [self.ID,self.timeStamp,self.itemID,self.seller,self.size,self.buy,self.bid,self.timeLeft]
    def makeID(self):
        s = ""
        attributes = [self.timeStamp,self.itemID,self.seller,self.size,self.buy,self.bid,self.timeLeft]
        for i in attributes:
            s+= str(i) + ","
        return hash.sha224(s.encode('utf-8')).hexdigest()[0:16]
    # likely an unneeded function
    def makeTimeLeft(self, ropeValue):
        t = int(ropeValue) # time left
        cipher= [[0,1],[1,4],[4,16],[16,48]] #in halfhour blocs, 1 == 30m
        for i in [1,2,3,4]:
            if t == i:
                return cipher[i-1][0], cipher[i-1][1]
    def cleanSeller(self,ropeValue):
        s = str(ropeValue[2:len(ropeValue)-2])
        if s == "":
            return "_UNNAMED"
        else:
            return s
  
class AuctionInputHandler:
    def __init__(self, rawInputList):
        self.AuctionList = util.Map([]) # map, itemID: dictionary{}
        self.RawtoAuctionList(rawInputList)
    def GetList(self):
        List = []
        for i in self.AuctionList.List():
            List.append(self.AuctionList.Get(i))
        return List
    def RawtoAuctionList(self,rawInputList):
        for item in rawInputList:
            self.InsertItemIntoMap(item)
    def InsertItemIntoMap(self,item):
        if self.AuctionList.Check(item.ID):
            (self.AuctionList.m[item.ID])['count'] += 1
        else:
            self.AuctionList.m[item.ID] = {
                    'hashID':item.ID,
                    'timeStamp':item.timeStamp,
                    'itemID':item.itemID,
                    'seller':item.seller,
                    'count':1,
                    'stackSize':item.size,
                    'buyPrice':item.buy,
                    'bidPrice':item.bid,
                    'timeLeft':item.timeLeft
                    }