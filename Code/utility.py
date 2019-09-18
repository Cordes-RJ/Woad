# -*- coding: utf-8 -*-

"""
For general utility functions used across more than one file.
from utility import *, or import utilityWoad as u
"""
import pandas as pd

# read-in file as list
def Readin_lines(path):
    f = open(path, "r",encoding = "utf8")
    rawFile = f.readlines()
    f.close()
    return rawFile

# read-in file as string
def Readin_bloc(path):
    f = open(path, "r",encoding = "utf8")
    rawFile = f.read()
    f.close()
    return rawFile

# take raw CSV path and return Pandas dataframe
# assumes header
def Readin_CSVtoDF(path):
    return pd.read_csv(path)

def Readin_CSVtoMap(path):
    return DFtoMap(Readin_CSVtoDF(path))

# takes a two column dataframe and converts it to a map
def DFtoMap(df):
    buffer1 = []
    for col in df.columns:
        buffer1.append(df[col].tolist())
    # format data for map input
    buffer2 = []
    for i in range(len(buffer1[0])):
        buffer2.append([buffer1[0][i],buffer1[1][i]])
    return map(buffer2)
    
# wanted something similar to an empty interface obj in go
def EmptyInterface():
    return type('', (), {})()
    
# class map is a utility class, a decorator for dictionaries
# requires a list of 2dVectors
class map:
    def __init__(self, KVpairs):
        self.m = dict()
        for i in KVpairs:
            self.m[i[0]] = i[1]
    # Check checks for existence of key
    def Check(self,key):
        if key in self.m.keys():
            return True
        else:
            return False
    # Set sets or adds a key value pair
    def Set(self, key, value):
        self.m[key] = value
    # Del removes a key from the map
    def Del(self,key):
        if key in self.m.keys():
            self.m.pop(key)
    # Get gets a key from the map
    def Get(self,key):
        if key in self.m.keys():
            return self.m[key]
        else:
            print(key+" not found in map")
    # List returns a list of keys in the map
    def List(self):
        return self.m.keys()