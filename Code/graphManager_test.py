# -*- coding: utf-8 -*-

import graphDataHandler as gdh
import graphManager as gm

snapshots = [1569097981, 1569106184, 1569242546, 1569247080]
MrManager = gdh.MrGraphDataManager('woad003', snapshots,2318)
df = MrManager.populateAndReturnDFwithinprice(0,150)

#%%
MrGraphManager = gm.MrGraphManager(df)
MrGraphManager.GraphSimple("test")

#%%