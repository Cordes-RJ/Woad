# -*- coding: utf-8 -*-
"""
pullData gets the data from auc-scan
"""


import utility as util
import parameters as p
import scanParser as sps
import woadSql as wSql
import auctionObj as ao
import os

def scan():
    params = p.Parameters()
    AuctionList = ao.AuctionInputHandler(sps.Parser(params).Parse()).GetList()
    MrManager = wSql.MrSqlManager("localhost","woad003")
    MrManager.Connect()
    MrManager.InsertAuctionList(AuctionList)
    MrManager.Disconnect()
    os.remove(params.Get('ScanDataBackupPath')) # remove BACKUP file
    # set current scan data as new backup file
    os.rename(params.Get('ScanDataPath'),params.Get('ScanDataBackupPath'))

    