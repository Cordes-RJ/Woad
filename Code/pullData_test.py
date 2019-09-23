# -*- coding: utf-8 -*-

import pullData
import woadSql as wSql

MrManager = wSql.MrSqlManager("localhost",'woad003')
MrManager.Connect()
auctions = MrManager.GetSnapshotList()
MrManager.Disconnect()
#%%
#essence of fire
auctions = pullData.pull("woad003",1569097981,7078)


#%%
import utility as util

print(util.intToDateTime(1569097981))
#%%
x = pullData.getListofSnapshots("woad003")