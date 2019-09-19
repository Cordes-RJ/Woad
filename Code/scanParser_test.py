# -*- coding: utf-8 -*-

"""
all files tested in console in the interest of efficiency
"""

import utility as util
import parameters as p
import scanParser as sps

Parameters = p.Parameters()
parser = sps.Parser(Parameters)
parser.Parse(util.Readin_bloc("TestData/Auc-ScanData_short.txt"))
x = parser.rawList

#%%
