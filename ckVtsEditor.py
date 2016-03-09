# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 13:48:41 2016

@author: shokimc
"""

import os, sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from os.path import dirname, isdir, isfile, join
import ckCtrlEditor as ctrl



class Programa(QWidget): #Antes tenia QDialog. Esto es para que aparezca el minimizado, etc
    def __init__(self):
        super(Programa, self).__init__()
        
        self.setWindowTitle(self.tr("Editor de archivos"))
        self.setMinimumSize(700,500)
        
       
        #Widget
        self.label = QLabel("")
        self.label.hide()
        self.carpeta=QLabel("Carpeta")
        self.line=QLineEdit("")
        self.boton = QPushButton("Seleccionar")
        self.archivos=QLabel("Archivos")
        self.Editor=QTextEdit("")

        self.lista = QListWidget()

         
        
        self.salvar=QPushButton("Salvar")
        self.salvarComo=QPushButton("Salvar como")

        grilla=QGridLayout(self)
        grilla.addWidget(self.carpeta, 1, 1, 1, 1) 
        grilla.addWidget(self.line, 1, 2, 1, 24)
        grilla.addWidget(self.boton, 1, 26, 1, 4)
        grilla.addWidget(self.archivos, 3, 1, 1, 4)
        grilla.addWidget(self.Editor, 5, 7, 8, 20)
        grilla.addWidget(self.lista,5, 1, 8, 6)
        grilla.addWidget(self.salvar, 17, 1, 2, 3)
        grilla.addWidget(self.salvarComo, 17, 4, 2, 5 )



            
        self.boton.clicked.connect(self.elegir)
        self.lista.itemDoubleClicked.connect(self.editar)
        self.salvarComo.clicked.connect(self.saveLike)
        self.salvar.clicked.connect(self.save)



    
    def elegir(self):
        global url
        url = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.line.setText(url) #Que la etiqueta combo tenga lo del combo
        files = [f for f in os.listdir(str(url)) if os.path.isfile(os.path.join(str(url),f))]
        self.lista.clear ()

        for item in files:
            
            self.lista.addItem(item)
            
       
                
    def editar(self):
        row = self.lista.currentRow()
        item = self.lista.item(row)
        print item.text()
        fileName=item.text()
        dirName=self.line.text()
        #print dirName,fileName,type(dirName),type(fileName)
        self_path = os.path.join(str(dirName),str(fileName))
        print self_path
        text=ctrl.readEvent(self_path)
        #f = open(self_path, 'r')
        #filedata = f.read()
        self.Editor.setText(text)
        #f.close()
                
    def saveLike(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save File')
        print fileName
        #f = open(filename, 'w')
        text = self.Editor.toPlainText()
        #f.write(filedata)
        #f.close()
        ctrl.saveAsEvent(fileName,text)
        
    def save(self):
        row = self.lista.currentRow()
        item = self.lista.item(row)
        fileName=item.text()
        dirName=self.line.text()
        fileNameAbs = os.path.join(str(dirName), str(fileName))
        #print item.text()
        #f = open(self_path, 'w')
        text = self.Editor.toPlainText()
        #f.write(filedata)
        #f.close()
        ctrl.saveAsEvent(fileNameAbs,text)


if __name__=='__main__':

    app=QApplication([])
    w=Programa()
    w.show()
    
    sys.exit(app.exec_())
