from OpenGL import GL, GLU, GLUT

from PyQt5 import QtCore, QtWidgets, uic

import qdarkstyle

import traceback, sys, os, shutil, math

import numpy as np

import GLwidget

class mainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):

        super(mainWindow, self).__init__()
        uic.loadUi('MatrixUI.ui', self)
        self.threadpool = QtCore.QThreadPool()

        #Tabs
        self.Tabs = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.Tabs.setCurrentIndex(0)

        #Display matrix
        self.Displaymatrixbox00 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00')
        self.Displaymatrixbox01 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01')
        self.Displaymatrixbox02 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02')
        self.Displaymatrixbox10 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10')
        self.Displaymatrixbox11 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11')
        self.Displaymatrixbox12 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12')
        self.Displaymatrixbox20 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20')
        self.Displaymatrixbox21 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21')
        self.Displaymatrixbox22 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22')

        self.Vectorxdisplaybox0 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxdisplaybox0')
        self.Vectorxdisplaybox1 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxdisplaybox1')
        self.Vectorxdisplaybox2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxdisplaybox2')

        self.Displaymatrixbutton = self.findChild(QtWidgets.QPushButton, 'Displaymatrixbutton')
        self.Displaymatrixbutton.clicked.connect(self.Displaymatrixbuttonclicked)

    def setupUI(self):
        print("\033[1;101m SETUP UI \033[0m")

        self.openGLWidget = GLwidget.openGLDisplay(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, 1200, 950))
        self.openGLWidget.setObjectName("openGLWidget1")

        self.windowsHeight = self.openGLWidget.height()
        self.windowsWidth = self.openGLWidget.width()
        self.openGLWidget.resizeGL(self.windowsWidth, self.windowsHeight)

        self.openGLWidget.setFocus()

        self.matrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.vector = np.array([[0.0],[0.0],[0.0]])
        self.Displaymatrix_0()
        self.openGLWidget.matrix = self.matrix
        self.openGLWidget.displayflag = 1
        self.openGLWidget.updateflag = 1

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateopenGLWidget)
        self.timer.start(17)

    def updateopenGLWidget(self):
        if(self.openGLWidget.updateflag):
            self.openGLWidget.updateflag = 0
            self.openGLWidget.update()

    def Displaymatrix_0(self):
        self.Displaymatrixbox00.setValue(self.matrix[0, 0])
        self.Displaymatrixbox01.setValue(self.matrix[0, 1])
        self.Displaymatrixbox02.setValue(self.matrix[0, 2])
        self.Displaymatrixbox10.setValue(self.matrix[1, 0])
        self.Displaymatrixbox11.setValue(self.matrix[1, 1])
        self.Displaymatrixbox12.setValue(self.matrix[1, 2])
        self.Displaymatrixbox20.setValue(self.matrix[2, 0])
        self.Displaymatrixbox21.setValue(self.matrix[2, 1])
        self.Displaymatrixbox22.setValue(self.matrix[2, 2])

        self.Vectorxdisplaybox0.setValue(self.vector[0, 0])
        self.Vectorxdisplaybox1.setValue(self.vector[1, 0])
        self.Vectorxdisplaybox2.setValue(self.vector[2, 0])

    def Displaymatrixbuttonclicked(self):
        self.matrix[0, 0] = self.Displaymatrixbox00.value()
        self.matrix[0, 1] = self.Displaymatrixbox01.value()
        self.matrix[0, 2] = self.Displaymatrixbox02.value()
        self.matrix[1, 0] = self.Displaymatrixbox10.value()
        self.matrix[1, 1] = self.Displaymatrixbox11.value()
        self.matrix[1, 2] = self.Displaymatrixbox12.value()
        self.matrix[2, 0] = self.Displaymatrixbox20.value()
        self.matrix[2, 1] = self.Displaymatrixbox21.value()
        self.matrix[2, 2] = self.Displaymatrixbox22.value()

        self.vector[0, 0] = self.Vectorxdisplaybox0.value()
        self.vector[1, 0] = self.Vectorxdisplaybox1.value()
        self.vector[2, 0] = self.Vectorxdisplaybox2.value()

        self.openGLWidget.matrix = self.matrix
        self.openGLWidget.vector1 = self.vector
        self.openGLWidget.vector2 = self.matrix.dot(self.vector)
        self.openGLWidget.displayflag = 1
        self.openGLWidget.updateflag = 1

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())