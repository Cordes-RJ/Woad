# -*- coding: utf-8 -*-

"""
graphDataHandler pulls in data and gets it ready for graphing
"""

import pandas as pd
import pullData as pull
import utility as util

class MrGraphManager:
    def __init__(self,db,snapshots,itemID):
        self.db = db
        self.itemID = itemID
        self.snapshots = snapshots
        self.df = pd.DataFrame(columns = ["snapshot","price","bid|buyout","stacksize","count","totalquantity","timeleft"])
    def populateAndReturnDF(self):
        self.populate()
        return self.df
    def populate(self):
        for i in self.snapshots:
            self.grabData(i)
    def grabData(self,snapshot):
        print(util.intToDateTime(snapshot))
        auctions = pull.getAuctionsAtSnapshot(self.db, snapshot, self.itemID)
        for i in range(len(auctions)):
            bid,buyout,obj = self.rawTupletoAuction(auctions[i])
            if buyout:
                self.df = self.df.append(obj[0], ignore_index=True)
            if bid:
                self.df = self.df.append(obj[1],ignore_index=True)
    def rawTupletoAuction(self,auctionTuple):
        """
        0 | hashID    | char(16)
        1 | timeStamp | int(11)
        2 | itemID    | smallint(6)
        3 | seller    | char(16)    
        4 | count     | smallint(6)
        5 | stackSize | tinyint(4) 
        6 | buyPrice  | int(11)   
        7 | bidPrice  | int(11)   
        8 | timeLeft  | tinyint(4)  
        TO
        snapshot |x
        price    |x
        bid|bo   |x
        stacksize|x
        count    |x
        totalquan|x
        timeLeft |x
        """
        Item = {}
        Item["snapshot"] = util.intToDateTime(auctionTuple[1])
        Item["count"] = auctionTuple[4]
        Item["stacksize"] = auctionTuple[5]
        Item["timeleft"] = auctionTuple[8]
        Item["totalquantity"] = auctionTuple[5]*auctionTuple[4]
        ObjectTuple = [{},{}]
        bid,buyout = False, False
        if auctionTuple[6] > 0:
            buyout = True
            x = util.makeDeepCopyofDict(Item)
            x['bid|buyout'] = "buyout"
            x['price'] = auctionTuple[6]
            ObjectTuple[0]=x
        if auctionTuple[7] > 0:
            bid = True
            y = util.makeDeepCopyofDict(Item)
            y['bid|buyout'] = "bid"
            y['price'] = auctionTuple[7]
            ObjectTuple[1]=y
        return bid,buyout,ObjectTuple
        