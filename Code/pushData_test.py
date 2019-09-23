# -*- coding: utf-8 -*-

"""
all files tested in console in the interest of efficiency
"""

import pushData

pushData.scan()
#%%
import parameters as p
params = p.Parameters()
os.remove(params.Get('ScanDataBackupPath'))
#%%
os.rename(params.Get('ScanDataPath'),params.Get('ScanDataBackupPath'))
#%%
import utility as util
import parameters as p
import scanParser as sps
import woadSql as wSql
import auctionObj as ao
import os

MrManager = wSql.MrSqlManager("localhost","woad003")
MrManager.Connect()
MrManager.CheckforSeller("5131e6a9a52310a3")
MrManager.Disconnect()

#%%
params = p.Parameters()
AuctionList = ao.AuctionInputHandler(sps.Parser(params).Parse()).GetList()


