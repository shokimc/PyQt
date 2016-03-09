# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 13:48:41 2016

@author: shokimc
"""

import os, sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from os.path import dirname, isdir, isfile, join
from ckVtsEditor import Programa


app=QApplication([])
w=Programa()
w.show()
    
sys.exit(app.exec_())
