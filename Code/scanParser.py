# -*- coding: utf-8 -*-

"""
parser is used to scan the auction data file for auction entries
"""

    
class Parser:
    def __init__(self):
        self.rawList = []
    #find where entries begin
    def Parse(self, content):
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