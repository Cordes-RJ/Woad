# -*- coding: utf-8 -*-

"""
PullData offers a handler to pull data from the DB
"""

import woadSql as wSql


def getAuctionsAtSnapshot(db, snapshot, itemID):
    MrManager = wSql.MrSqlManager("localhost",db)
    MrManager.Connect()
    auctions = MrManager.GetAuctions(1569097981,7078)
    MrManager.Disconnect()
    return auctions

def getListofSnapshots(db):
    MrManager = wSql.MrSqlManager("localhost",db)
    MrManager.Connect()
    auctions = MrManager.GetSnapshotList()
    MrManager.Disconnect()
    return auctions