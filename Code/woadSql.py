# -*- coding: utf-8 -*-



#mysql-connector-python==8.0.17
import dbcredentials as cdb
import mysql.connector as db
import hashlib as hash
import utility as util

class dbinfo:
    def __init__(self,host,DB):
        self.host, self.DB, self.user, self.password = host,DB,cdb.cred.user,cdb.cred.password
        
class MrSqlManager:
    def __init__(self, host,DB):
        self.open = False
        self.DBinfo = dbinfo(host,DB)
        self.init = False
    def Connect(self):
        if self.open: 
            return
        else:
            self.db = db.connect(host=self.DBinfo.host, user=self.DBinfo.user, password=self.DBinfo.password, db=self.DBinfo.DB)
            #self.cursor = self.db.cursor()
            self.open = True
            self.init = True
    def Disconnect(self):
        if self.open and self.init:
            self.db.disconnect()
            self.open= False
    def InsertAuction(self,auction):
        if self.open:
            action = ("INSERT INTO auctions "
                      "(hashID,timeStamp,itemID,seller,count,stackSize,buyPrice,bidPrice,timeLeft) "
                      "VALUES (%(hashID)s,%(timeStamp)s,%(itemID)s,%(seller)s,%(count)s,%(stackSize)s,%(buyPrice)s,%(bidPrice)s,%(timeLeft)s)")
            self.cursor = self.db.cursor()
            self.cursor.execute(action,auction)
            self.db.commit()
            self.cursor.close()
    def InsertAuctionList1(self,auctionList):
        for auction in auctionList:
            self.InsertAuction(auction)
    def InsertAuctionList(self,auctionList):
        if self.open:
            auctionList = self.convertSellerstoIDs(auctionList)
            action = ("INSERT INTO auctions "
                          "(hashID,timeStamp,itemID,seller,count,stackSize,buyPrice,bidPrice,timeLeft) "
                          "VALUES (%(hashID)s,%(timeStamp)s,%(itemID)s,%(seller)s,%(count)s,%(stackSize)s,%(buyPrice)s,%(bidPrice)s,%(timeLeft)s)")
            cursor = self.db.cursor()
            cursor.executemany(action,auctionList)
            self.db.commit()
            cursor.close()
    def convertSellerstoIDs(self,auctionList):
        if self.open:
            # get all names
            nameList = {}
            #put all names into dictionary, and replace auctionList sellernames with hashIDs
            for i in range(len(auctionList)):
                sellerName = auctionList[i]['seller']
                sellerID = ((lambda seller: hash.sha224(seller.encode('utf-8')).hexdigest()[0:16])(sellerName))
                nameList[sellerID] = {
                        'hashID':sellerID,
                        'name':sellerName
                        } # add potential insertion entry to dictionary
                auctionList[i]['seller'] = sellerID # replace name with hashid in list
            keys = nameList.keys()
            nameListDeepCopy = util.makeDeepCopyofDict(nameList)
            for key in keys:
                if self.CheckforSeller(key):
                    nameListDeepCopy.pop(key) # if found in DB, remove the key from the list
            # now insert the List of keys that were not found in the DB
            keys = nameListDeepCopy.keys() # reset Key list
            # if no keys are unknown, return and skip the rest
            if len(keys)==0:
                return auctionList
            insertionList = []
            for key in keys:
                insertionList.append(nameList[key])
            cursor = self.db.cursor()
            action = ("INSERT INTO sellers "
                              "(hashID,name) "
                              "VALUES (%(hashID)s,%(name)s)")
            cursor.executemany(action,insertionList)
            self.db.commit()
            cursor.close()
            return auctionList
    def CheckforSeller(self, item):
        cursor = self.db.cursor()
        cursor.execute(
        "SELECT hashID, COUNT(*) FROM sellers WHERE hashID = %s",
        (item,)
    )
        x = cursor.fetchone()
        cursor.close()
        if x[1]:
            return True
        else:
            return False
    def GetAuctions(self, snapshot,itemID):
        if self.open:
            action = "SELECT * FROM auctions WHERE timeStamp = %s AND itemID = %s"
            cursor = self.db.cursor(buffered=True)
            cursor.execute(action,(snapshot,itemID,))
            record = cursor.fetchall()
            cursor.close()
            return record
        return []
    def GetSnapshotList(self):
        if self.open:
            cursor = self.db.cursor()
            cursor.execute("SELECT DISTINCT timeStamp FROM auctions")
            records = cursor.fetchall()
            cursor.close()
            List = []
            for i in records:
                List.append(i[0])
            List.sort()
            for i in range(len(List)):
                List[i] = [List[i],util.intToDateTime(List[i])]
            return List
        return []
        
            

     