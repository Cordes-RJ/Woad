# -*- coding: utf-8 -*-

"""
all files tested in console in the interest of efficiency
"""
#%%
from utility import *

#%%
from utility import *
x = Readin_bloc("TestData/utility_testFile.txt")
#%%
from utility import *
x = Readin_lines("TestData/utility_testFile.txt")
#%%
from utility import *
x = Readin_CSVtoDF("TestData/utility_testParams.csv")
#%%
from utility import *
x = DFtoMap(Readin_CSVtoDF("TestData/utility_testParams.csv"))
#%%
from utility import *
print(EmptyInterface())
#%%
from utility import *
x = Readin_CSVtoMap("TestData/utility_testParams.csv")
x.Get("key4")
#%%
