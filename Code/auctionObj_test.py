# -*- coding: utf-8 -*-
"""
all files tested in console in the interest of efficiency
"""
import utility as util
import parameters as p
import scanParser as sps
import auctionObj as ao
import time
import woadSql as wSql

from datetime import datetime
Parameters = p.Parameters()
parser = sps.Parser(Parameters)
x = parser.Parse(util.Readin_bloc("TestData/Auc-ScanData_2.lua"))
print(datetime.fromtimestamp(x[0].timeStamp))
y = ao.AuctionInputHandler(x).GetList()
MrManager = wSql.MrSqlManager("localhost","woad001")
MrManager.Connect()
MrManager.InsertAuctionList(y)
MrManager.Disconnect()
#%%
