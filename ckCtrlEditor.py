# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 13:48:41 2016

@author: shokimc
"""

import ckModAppEditor as modAp


def saveEvent(fileName,text):
    modAp.saveText(fileName,text)
    

def saveAsEvent(fileName,text):
    modAp.saveText(fileName,text)

def readEvent(fileName):
    text=modAp.readText(fileName)
    return text
    
