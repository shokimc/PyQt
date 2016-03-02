# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 18:50:50 2016

@author: shokimc
"""

import sys
from PyQt4 import QtGui, QtCore
 
class Main(QtGui.QMainWindow):
 

    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
         
        newAction = QtGui.QAction('Nuevo  Ctrl+N', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newFile)
         
        saveAction = QtGui.QAction('Guarda como   Ctrl+S', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)
        
        saveAction2 = QtGui.QAction('Guarda   Ctrl+D', self)
        saveAction2.setShortcut('Ctrl+D')
        saveAction2.triggered.connect(self.save)
         
        openAction = QtGui.QAction('Abrir   Ctrl+O', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)
         

        closeAction = QtGui.QAction('Cerrar  Ctrl+Q', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Cerrar editor')
        closeAction.triggered.connect(self.close)
 
        fontChoice = QtGui.QAction('Fuente', self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar("Font")
        
        #color = QtGui.QColor(0, 0, 0)

        fontColor = QtGui.QAction('Color', self)
        fontColor.triggered.connect(self.color_picker)  

        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Archivo')
        fileMenu.addAction(newAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAction2)
        fileMenu.addAction(openAction)
        fileMenu.addAction(closeAction)

        fileMenu2 = menubar.addMenu('Ver')
        fileMenu2.addAction(fontColor)
        fileMenu2.addAction(fontChoice)


 
        self.txt = QtGui.QTextEdit(self)
        self.setCentralWidget(self.txt)
         
#---------Window settings --------------------------------
         
        self.setGeometry(350,350,350,350)
        self.setWindowTitle("Editor de texto")
        self.show()
 
#---------Slots-------------------------------------------
 
    def newFile(self):
        self.txt.clear()
         
    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar archivo como')
        f = open(filename, 'w')
        filedata = self.txt.toPlainText()
        f.write(filedata)
        f.close()
        
       
    def save(self):
            self.txt.toPlainText()

         
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo')
        f = open(filename, 'r')
        filedata = f.read()
        self.txt.setText(filedata)
        f.close()
        
    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())
        
    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
         
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
