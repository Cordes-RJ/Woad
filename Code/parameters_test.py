# -*- coding: utf-8 -*-
"""
all files tested in console in the interest of efficiency
"""
#%%
from parameters import *
p = Parameters()
p.CreateWhiteList()
print(p.CheckWL(2318))
print(p.CheckWL(2592))
print(p.CheckWL(4306))