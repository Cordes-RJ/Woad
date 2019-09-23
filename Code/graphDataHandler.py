# -*- coding: utf-8 -*-

"""
graphDataHandler pulls in data and gets it ready for graphing
"""

import pandas as pd
import pullData as pull
import utility as util
from scipy import stats
import numpy as np

class MrGraphDataManager:
    def __init__(self,db,snapshots,itemID):
        self.db = db
        self.itemID = itemID
        self.snapshots = snapshots
        self.df = pd.DataFrame(columns = ["snapshot","price","bid|buyout","stacksize","count","totalquantity","timeleft"])
    def populateAndReturnDFwithinZscore(self,withinZscore):
        self.populate()
        #remove outliers
        df = pd.DataFrame(self.df['price'])
        self.df['zscore'] = (df - df.mean())/df.std()
        self.df= self.df[self.df['zscore'] < withinZscore]
        return self.df
    def populateAndReturnDFwithinprice(self,above,below):
        self.populate()
        #remove outliers
        self.df= self.df[self.df['price'] < below]
        self.df= self.df[self.df['price'] > above]
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
        Item["snapshot"] = str(util.intToDateTime(auctionTuple[1]))
        Item["count"] = int(auctionTuple[4])
        Item["stacksize"] = int(auctionTuple[5])
        Item["timeleft"] = int(auctionTuple[8])
        Item["totalquantity"] = int(auctionTuple[5]*auctionTuple[4])
        ObjectTuple = [{},{}]
        bid,buyout = False, False
        if auctionTuple[6] > 0:
            buyout = True
            x = util.makeDeepCopyofDict(Item)
            x['bid|buyout'] = "buyout"
            x['price'] = float(auctionTuple[6])
            ObjectTuple[0]=x
        if auctionTuple[7] > 0:
            bid = True
            y = util.makeDeepCopyofDict(Item)
            y['bid|buyout'] = "bid"
            y['price'] = float(auctionTuple[7])
            ObjectTuple[1]=y
        return bid,buyout,ObjectTuple
        