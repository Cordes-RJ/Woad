# -*- coding: utf-8 -*-

import utility as util

"""
Parameters:
ScanDataPath
WhiteListPath
"""

class Parameters:
    def __init__(self):
        self.p = util.Readin_CSVtoMap("parameters.csv")
        self.WL = util.Map([])
        self.CreateWhiteList()
    def CreateWhiteList(self):
        df = util.Readin_CSVtoDF(self.Get("WhiteListPath"))
        for i in range(len(df["ID"])):
            if df["Include"][i]:
                self.WL.Set(df["ID"][i], util.EmptyInterface())
    def Check(self,key):
        return self.p.Check(key)
    # Set sets or adds a key value pair from parameters
    def Set(self, key, value):
        self.p.Set(key,value)
    # Del removes a key from parameters
    def Del(self,key):
        self.p.Del(key)
    # Get gets a key from parameters
    def Get(self,key):
        return self.p.Get(key)
    # List returns a list of keys within the parameter map
    def List(self):
        return self.p.List()
    # CheckWL checks the whiteList for an entry
    def CheckWL(self,key):
        return self.WL.Check(key)
    
