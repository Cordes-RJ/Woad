# -*- coding: utf-8 -*-

"""
parser is used to scan the auction data file for auction entries
"""
import auctionObj as ao
import time
class Parser:
    def __init__(self, Parameters):
        self.p = Parameters
        self.rawList = []
        self.tStamp = int(time.time())
    #find where entries begin
    def Parse(self, content):
        self.parseRawTxt(content)
        self.cleanList()
        self.delimitList()
        return self.ReturnRawAuctionList()
    def parseRawTxt(self,content):
        #Find Start
        content = str(content[content.find("return {") + 9:len(content)])
        cont = True
        while cont:
            content, cont = self.findNextRope(content)
    def findNextRope(self, content):
        nextStart = content.find("Hitem:") #+ 6 
        if nextStart == -1:
            return "", False
        nextStart+=6
        nextDelimit = content.find(",}", nextStart, len(content))
        self.rawList.append(str(content[nextStart:nextDelimit]))
        return str(content[nextDelimit:len(content)]), True
    def checkWL(self,item):
        ID = int(item[0:item.find(":")])
        return self.p.CheckWL(ID)
    def cleanList(self):
        i = 0
        while i < len(self.rawList):
            if self.checkWL(self.rawList[i]):
                i+=1
            else:
                self.rawList.pop(i)
    def delimitList(self):
        for i in range(len(self.rawList)):
            if type(self.rawList[i]) == str:
                s = self.rawList[i]
                d = self.delimitItem(s)
                for i2 in range(i,len(self.rawList),1):
                    if self.rawList[i] == s:
                        self.rawList[i] = d
    def delimitItem(self,item):
        attList = []
        x0 = item.find(":")
        attList.append(int(item[0:x0]))
        pos = item.find(",")+1 # find first comma
        cont = True
        while cont:
            att,pos,cont = self.findNextObj(item,pos)
            attList.append(att)
        return attList
    def findNextObj(self, item, pos):
        nextDelim = item.find(",", pos, len(item))
        if nextDelim == -1:
            return str(item[pos:len(item)]), -1, False
        return str(item[pos:nextDelim]),nextDelim+1,True
    def ReturnRawAuctionList(self):
        auctionList = []
        for i in self.rawList:
            auctionList.append(ao.AuctionRawInput(i,self.tStamp))
        return auctionList