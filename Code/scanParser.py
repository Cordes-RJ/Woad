# -*- coding: utf-8 -*-

"""
parser is used to scan the auction data file for auction entries
"""
import parameters as p
    
class Parser:
    def __init__(self, Parameters):
        #
        Parameters = p.Parameters()
        #
        self.p = Parameters
        self.rawList = []
    #find where entries begin
    def Parse(self, content):
        self.parseRawTxt(content)
        self.cleanList()
    def parseRawTxt(self,content):
        #Find Start
        content = str(content[content.find("return {") + 9:len(content)])
        cont = True
        while cont:
            content, cont = self.findNext(content)
    def findNext(self, content):
        nextStart = content.find("Hitem:") #+ 6 
        if nextStart == -1:
            return "", False
        nextStart+=6
        nextDelimit = content.find(",}", nextStart, len(content))
        self.rawList.append(str(content[nextStart:nextDelimit]))
        return str(content[nextDelimit:len(content)]), True
    def checkWL(self,item):
        if self.p.Check(int(str(item[0:item.find(":")]))):
            return True
        else:
            return False
    def cleanList(self):
        i = 0
        while i < len(self.rawList):
            if self.checkWL(self.rawList[i]):
                i+=1
            else:
                self.rawList.pop(i)