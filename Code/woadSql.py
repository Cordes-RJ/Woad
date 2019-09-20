# -*- coding: utf-8 -*-



#mysql-connector-python==8.0.17
import dbcredentials as cdb
import mysql.connector as db

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
            action = ("INSERT INTO auctionTest2 "
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
            action = ("INSERT INTO auctionTest2 "
                          "(hashID,timeStamp,itemID,seller,count,stackSize,buyPrice,bidPrice,timeLeft) "
                          "VALUES (%(hashID)s,%(timeStamp)s,%(itemID)s,%(seller)s,%(count)s,%(stackSize)s,%(buyPrice)s,%(bidPrice)s,%(timeLeft)s)")
            cursor = self.db.cursor()
            cursor.executemany(action,auctionList)
            self.db.commit()
            cursor.close()
        
            

     