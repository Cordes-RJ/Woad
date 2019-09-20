# -*- coding: utf-8 -*-
"""
pullData gets the data from auc-scan
"""


import utility as util
import parameters as p
import scanParser as sps
import woadSql as wSql
import auctionObj as ao

def scan():
    AuctionList = ao.AuctionInputHandler(sps.Parser(p.Parameters()).Parse()).GetList()
    print(len(AuctionList))
    MrManager = wSql.MrSqlManager("localhost","woad001")
    MrManager.Connect()
    MrManager.InsertAuctionList(AuctionList)
    MrManager.Disconnect()
    