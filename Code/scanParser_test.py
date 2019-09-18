# -*- coding: utf-8 -*-

"""
all files tested in console in the interest of efficiency
"""

#import utility as util
#import parameters as p
import scanParser as sps

#Parameters = p.Parameters()
parser = sps.Parser()
parser.Parse("TestData/Auc-ScanData_short")
x = parser.rawList

#%%
