# -*- coding: utf-8 -*-

import graphDataHandler as gdh

snapshots = [1569097981, 1569106184, 1569242546, 1569247080]
MrManager = gdh.MrGraphManager('woad003', snapshots,2318)
auctions2 = MrManager.populateAndReturnDF()
#%%

import pandas as pd

tPD = pd.DataFrame(columns = ["test1","test2"])

tPD.append({'test1':1,'test2':2}, ignore_index=True)