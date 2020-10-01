from OpenGL import GL, GLU, GLUT

from PyQt5 import QtCore, QtWidgets, uic

import qdarkstyle, qdarkgraystyle

import traceback, sys, os, shutil, math, copy

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
        self.Displaymatrixbox = []
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21'))
        self.Displaymatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22'))

        self.Matrixcopy = self.findChild(QtWidgets.QPushButton, 'Matrixcopy')
        self.Matrixcopy.clicked.connect(self.Matrixcopyclicked)
        self.Matrixpaste = self.findChild(QtWidgets.QPushButton, 'Matrixpaste')
        self.Matrixpaste.clicked.connect(self.Matrixpasteclicked)

        self.Vectorxdisplaybox0 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxdisplaybox0')
        self.Vectorxdisplaybox1 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxdisplaybox1')
        self.Vectorxdisplaybox2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxdisplaybox2')

        self.Eigenvalue1box = self.findChild(QtWidgets.QLineEdit, 'Eigenvalue1box')
        self.Eigenvalue2box = self.findChild(QtWidgets.QLineEdit, 'Eigenvalue2box')
        self.Eigenvalue3box = self.findChild(QtWidgets.QLineEdit, 'Eigenvalue3box')

        self.Eigenvector1box = self.findChild(QtWidgets.QTextEdit, 'Eigenvector1box')
        self.Eigenvector2box = self.findChild(QtWidgets.QTextEdit, 'Eigenvector2box')
        self.Eigenvector3box = self.findChild(QtWidgets.QTextEdit, 'Eigenvector3box')

        self.Displaydeterminantbox_2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaydeterminantbox_2')

        self.Displaymatrixbutton = self.findChild(QtWidgets.QPushButton, 'Displaymatrixbutton')
        self.Displaymatrixbutton.clicked.connect(self.Displaymatrixbuttonclicked)

        #Rotation
        self.Rotationvectorbox0 = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationvectorbox0')
        self.Rotationvectorbox1 = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationvectorbox1')
        self.Rotationvectorbox2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationvectorbox2')

        self.Rotationanglebox = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationanglebox')

        self.Rotationxybox = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationxybox')
        self.Rotationzxbox = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationzxbox')
        self.Rotationyzbox = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationyzbox')

        self.Rotationquatapplybutton = self.findChild(QtWidgets.QPushButton, 'Rotationquatapplybutton')        
        self.Rotationquatapplybutton.clicked.connect(self.Rotationquatapplybuttonclicked)
        self.Rotationquatcalculatebutton = self.findChild(QtWidgets.QPushButton, 'Rotationquatcalculatebutton')        
        self.Rotationquatcalculatebutton.clicked.connect(self.Rotationquatcalculatebuttonclicked)

        #Reflection
        self.Reflectionvectorbox0 = self.findChild(QtWidgets.QDoubleSpinBox, 'Reflectionvectorbox0')
        self.Reflectionvectorbox1 = self.findChild(QtWidgets.QDoubleSpinBox, 'Reflectionvectorbox1')
        self.Reflectionvectorbox2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Reflectionvectorbox2')

        self.Reflectionapplybutton = self.findChild(QtWidgets.QPushButton, 'Reflectionapplybutton')        
        self.Reflectionapplybutton.clicked.connect(self.Reflectionapplybuttonclicked)

        self.Reflectioncalculatebutton = self.findChild(QtWidgets.QPushButton, 'Reflectioncalculatebutton')        
        self.Reflectioncalculatebutton.clicked.connect(self.Reflectioncalculatebuttonclicked)

        #Inverse
        self.Displayinversematrixbox = []
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_2'))
        self.Displayinversematrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_2'))

        self.Matrixcopy_2 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_2')
        self.Matrixcopy_2.clicked.connect(self.Matrixcopy_2clicked)
        self.Matrixpaste_2 = self.findChild(QtWidgets.QPushButton, 'Matrixpaste_2')
        self.Matrixpaste_2.clicked.connect(self.Matrixpaste_2clicked)

        self.Displayinvmatrixbox = []
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_3'))
        self.Displayinvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_3'))

        self.Matrixcopy_3 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_3')
        self.Matrixcopy_3.clicked.connect(self.Matrixcopy_3clicked)

        self.Displaydeterminantbox = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaydeterminantbox')

        self.Calculateinversematrixbutton = self.findChild(QtWidgets.QPushButton, 'Calculateinversematrixbutton')
        self.Calculateinversematrixbutton.clicked.connect(self.Calculateinversematrixbuttonclicked)
        self.Displayinversematrixbutton = self.findChild(QtWidgets.QPushButton, 'Displayinversematrixbutton')
        self.Displayinversematrixbutton.clicked.connect(self.Displayinversematrixbuttonclicked)
        self.Displayinversematrixbutton.setDisabled(True)

        #Cramer's rule
        self.Displaycramersmatrixbox = []
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_6'))
        self.Displaycramersmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_6'))

        self.Matrixcopy_4 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_4')
        self.Matrixcopy_4.clicked.connect(self.Matrixcopy_4clicked)
        self.Matrixpaste_3 = self.findChild(QtWidgets.QPushButton, 'Matrixpaste_3')
        self.Matrixpaste_3.clicked.connect(self.Matrixpaste_3clicked)

        self.Vectorbdisplaybox0 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorbdisplaybox0')
        self.Vectorbdisplaybox1 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorbdisplaybox1')
        self.Vectorbdisplaybox2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorbdisplaybox2')

        self.Displaycramersdeterminantbox = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaycramersdeterminantbox')

        self.Displaycram1matrixbox = []
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_7'))
        self.Displaycram1matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_7'))

        self.Matrixcopy_5 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_5')
        self.Matrixcopy_5.clicked.connect(self.Matrixcopy_5clicked)

        self.Displaycram2matrixbox = []
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_8'))
        self.Displaycram2matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_8'))

        self.Matrixcopy_6 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_6')
        self.Matrixcopy_6.clicked.connect(self.Matrixcopy_6clicked)

        self.Displaycram3matrixbox = []
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_9'))
        self.Displaycram3matrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_9'))

        self.Matrixcopy_7 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_7')
        self.Matrixcopy_7.clicked.connect(self.Matrixcopy_7clicked)

        self.Vectorxcramdisplaybox0 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxcramdisplaybox0')
        self.Vectorxcramdisplaybox1 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxcramdisplaybox1')
        self.Vectorxcramdisplaybox2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Vectorxcramdisplaybox2')

        self.Calculatecramersbutton = self.findChild(QtWidgets.QPushButton, 'Calculatecramersbutton')
        self.Calculatecramersbutton.clicked.connect(self.Calculatecramersbuttonclicked)

        self.Displaycramers1matrixbutton = self.findChild(QtWidgets.QPushButton, 'Displaycramers1matrixbutton')
        self.Displaycramers1matrixbutton.setDisabled(True)
        self.Displaycramers1matrixbutton.clicked.connect(self.Displaycramers1matrixbuttonclicked)

        self.Displaycramers2matrixbutton = self.findChild(QtWidgets.QPushButton, 'Displaycramers2matrixbutton')
        self.Displaycramers2matrixbutton.setDisabled(True)
        self.Displaycramers2matrixbutton.clicked.connect(self.Displaycramers2matrixbuttonclicked)

        self.Displaycramers3matrixbutton = self.findChild(QtWidgets.QPushButton, 'Displaycramers3matrixbutton')
        self.Displaycramers3matrixbutton.setDisabled(True)
        self.Displaycramers3matrixbutton.clicked.connect(self.Displaycramers3matrixbuttonclicked)

        #SVD
        self.Displaysvdmatrixbox = []
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_10'))
        self.Displaysvdmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_10'))

        self.Matrixcopy_8 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_8')
        self.Matrixcopy_8.clicked.connect(self.Matrixcopy_8clicked)
        self.Matrixpaste_4 = self.findChild(QtWidgets.QPushButton, 'Matrixpaste_4')
        self.Matrixpaste_4.clicked.connect(self.Matrixpaste_4clicked)
        
        self.Displayumatrixbox = []
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_11'))
        self.Displayumatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_11'))

        self.Matrixcopy_9 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_9')
        self.Matrixcopy_9.clicked.connect(self.Matrixcopy_9clicked)

        self.Displaysmatrixbox = []
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_12'))
        self.Displaysmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_12'))

        self.Matrixcopy_10 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_10')
        self.Matrixcopy_10.clicked.connect(self.Matrixcopy_10clicked)

        self.Displayvmatrixbox = []
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_13'))
        self.Displayvmatrixbox.append(self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_13'))

        self.Matrixcopy_11 = self.findChild(QtWidgets.QPushButton, 'Matrixcopy_11')
        self.Matrixcopy_11.clicked.connect(self.Matrixcopy_11clicked)

        self.Calculatesvdbutton = self.findChild(QtWidgets.QPushButton, 'Calculatesvdbutton')
        self.Calculatesvdbutton.clicked.connect(self.Calculatesvdbuttonclicked)
        self.Animatesvdbutton = self.findChild(QtWidgets.QPushButton, 'Animatesvdbutton')
        self.Animatesvdbutton.clicked.connect(self.Animatesvdbuttonclicked)
        self.Animatesvdbutton.setDisabled(True)
        
        self.Displayumatrixbutton = self.findChild(QtWidgets.QPushButton, 'Displayumatrixbutton')
        self.Displayumatrixbutton.clicked.connect(self.Displayumatrixbuttonclicked)
        self.Displayumatrixbutton.setDisabled(True)
        self.Displaysmatrixbutton = self.findChild(QtWidgets.QPushButton, 'Displaysmatrixbutton')
        self.Displaysmatrixbutton.clicked.connect(self.Displaysmatrixbuttonclicked)
        self.Displaysmatrixbutton.setDisabled(True)
        self.Displayvmatrixbutton = self.findChild(QtWidgets.QPushButton, 'Displayvmatrixbutton')
        self.Displayvmatrixbutton.clicked.connect(self.Displayvmatrixbuttonclicked)
        self.Displayvmatrixbutton.setDisabled(True)

    def setupUI(self):
        print("\033[1;101m SETUP UI \033[0m")

        self.openGLWidget = GLwidget.openGLDisplay(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(15, 15, 1200, 950))
        self.openGLWidget.setObjectName("openGLWidget")

        self.windowsHeight = self.openGLWidget.height()
        self.windowsWidth = self.openGLWidget.width()
        self.openGLWidget.resizeGL(self.windowsWidth, self.windowsHeight)

        self.openGLWidget.setFocus()

        self.matrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])

        self.inversematrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.invmatrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.vector = np.array([[0.0],[0.0],[0.0]])

        self.matrixbuffer = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])

        self.cramersmatrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.cram1matrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.cram2matrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.cram3matrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])

        self.svdmatrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])

        self.Displaymatrix_0()
        self.Displaymatrixeigen()
        self.Displaydeterminantbox_2.setValue(np.linalg.det(self.matrix))
        self.openGLWidget.matrix = copy.deepcopy(self.matrix)
        self.openGLWidget.displayflag = 1
        self.openGLWidget.updateflag = 1

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateopenGLWidget)
        self.timer.start(17)

    def updateopenGLWidget(self):
        if(self.openGLWidget.updateflag):
            self.openGLWidget.updateflag = 0
            self.openGLWidget.update()

    def Matrixset(self, matrix, dispbox):
        matrix[0, 0] = dispbox[0].value()
        matrix[0, 1] = dispbox[1].value()
        matrix[0, 2] = dispbox[2].value()
        matrix[1, 0] = dispbox[3].value()
        matrix[1, 1] = dispbox[4].value()
        matrix[1, 2] = dispbox[5].value()
        matrix[2, 0] = dispbox[6].value()
        matrix[2, 1] = dispbox[7].value()
        matrix[2, 2] = dispbox[8].value() 

    def Displayset(self, matrix, dispbox):
        dispbox[0].setValue(matrix[0, 0])
        dispbox[1].setValue(matrix[0, 1])
        dispbox[2].setValue(matrix[0, 2])
        dispbox[3].setValue(matrix[1, 0])
        dispbox[4].setValue(matrix[1, 1])
        dispbox[5].setValue(matrix[1, 2])
        dispbox[6].setValue(matrix[2, 0])
        dispbox[7].setValue(matrix[2, 1])
        dispbox[8].setValue(matrix[2, 2])

    def Matrixcopyclicked(self):
        self.Matrixset(self.matrixbuffer, self.Displaymatrixbox) 

    def Matrixpasteclicked(self):
        self.Displayset(self.matrixbuffer, self.Displaymatrixbox)

    def Displaymatrixeigen(self):
        w, v = np.linalg.eig(self.matrix)

        eig1 = np.array([v[:, 0]])
        eig2 = np.array([v[:, 1]])
        eig3 = np.array([v[:, 2]])

        self.Eigenvalue1box.setText(str(np.around(w[0], 4)))
        self.Eigenvalue2box.setText(str(np.around(w[1], 4)))
        self.Eigenvalue3box.setText(str(np.around(w[2], 4)))

        self.Eigenvector1box.setText(str(np.around(eig1.T, 4)))
        self.Eigenvector2box.setText(str(np.around(eig2.T, 4)))
        self.Eigenvector3box.setText(str(np.around(eig3.T, 4)))

    def Displaymatrix_0(self):
        self.Displayset(self.matrix, self.Displaymatrixbox)

        self.Vectorxdisplaybox0.setValue(self.vector[0, 0])
        self.Vectorxdisplaybox1.setValue(self.vector[1, 0])
        self.Vectorxdisplaybox2.setValue(self.vector[2, 0])

    def Displaymatrixbuttonclicked(self):
        self.Matrixset(self.matrix, self.Displaymatrixbox)

        self.vector[0, 0] = self.Vectorxdisplaybox0.value()
        self.vector[1, 0] = self.Vectorxdisplaybox1.value()
        self.vector[2, 0] = self.Vectorxdisplaybox2.value()
        self.Displaymatrixeigen()
        self.Displaydeterminantbox_2.setValue(np.linalg.det(self.matrix))

        self.openGLWidget.matrix = copy.deepcopy(self.matrix)
        self.openGLWidget.vector1 = copy.deepcopy(self.vector)
        self.openGLWidget.vector2 = copy.deepcopy(self.matrix.dot(self.vector))
        self.openGLWidget.displayflag = 1
        self.openGLWidget.updateflag = 1

    def Rotationquatcalculate(self):
        rotatevector = np.array([[self.Rotationvectorbox0.value()], [self.Rotationvectorbox1.value()], [self.Rotationvectorbox2.value()]])
        if(np.linalg.norm(rotatevector) == 0):
            return np.identity(3)
        rotatevector /= np.linalg.norm(rotatevector)
        angle = self.Rotationanglebox.value() * math.pi / 180.0

        x = np.array([[1.0], [0.0], [0.0]])
        x1 = rotatevector.T.dot(x) * rotatevector
        x2 = x - x1
        if(np.linalg.norm(x2) > 0):
            x3 = np.cross(x2.T / np.linalg.norm(x2), rotatevector.T).T
            x = x2 * math.cos(angle) + x3 * math.sin(angle) * np.linalg.norm(x2) + x1

        y = np.array([[0.0], [1.0], [0.0]])
        y1 = rotatevector.T.dot(y) * rotatevector
        y2 = y - y1
        if(np.linalg.norm(y2) > 0):
            y3 = np.cross(y2.T / np.linalg.norm(y2), rotatevector.T).T
            y = y2 * math.cos(angle) + y3 * math.sin(angle) * np.linalg.norm(y2) + y1

        z = np.array([[0.0], [0.0], [1.0]])
        z1 = rotatevector.T.dot(z) * rotatevector
        z2 = z - z1
        if(np.linalg.norm(z2) > 0):
            z3 = np.cross(z2.T / np.linalg.norm(z2), rotatevector.T).T
            z = z2 * math.cos(angle) + z3 * math.sin(angle) * np.linalg.norm(z2) + z1

        matrix = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        matrix[0, 0] = x[0, 0]
        matrix[0, 1] = y[0, 0]
        matrix[0, 2] = z[0, 0]
        matrix[1, 0] = x[1, 0]
        matrix[1, 1] = y[1, 0]
        matrix[1, 2] = z[1, 0]
        matrix[2, 0] = x[2, 0]
        matrix[2, 1] = y[2, 0]
        matrix[2, 2] = z[2, 0]

        return matrix

    def Rotationquatcalculatebuttonclicked(self):
        self.matrix = self.Rotationquatcalculate()
        try:
            theta = -math.asin(-self.matrix[2, 0])
            phi = -math.atan2(self.matrix[2, 1], self.matrix[2, 2])
            psi = -math.atan2(self.matrix[1, 0], self.matrix[0, 0])
        except:
            phi = psi = theta = 0
        self.Rotationxybox.setValue(psi * 180 / math.pi)
        self.Rotationzxbox.setValue(theta * 180 / math.pi)
        self.Rotationyzbox.setValue(phi * 180 / math.pi)
        self.Displaymatrix_0()

    def Rotationquatapplybuttonclicked(self):
        matrix = self.Rotationquatcalculate()
        try:
            theta = -math.asin(-matrix[2, 0])
            phi = -math.atan2(matrix[2, 1], matrix[2, 2])
            psi = -math.atan2(matrix[1, 0], matrix[0, 0])
        except:
            phi = psi = theta = 0
        self.Rotationxybox.setValue(psi * 180 / math.pi)
        self.Rotationzxbox.setValue(theta * 180 / math.pi)
        self.Rotationyzbox.setValue(phi * 180 / math.pi)
        self.Matrixset(self.matrix, self.Displaymatrixbox)
        self.matrix = self.matrix.dot(matrix)
        self.Displaymatrix_0()

    def Reflectioncalculate(self):
        reflectvector = np.array([[self.Reflectionvectorbox0.value()], [self.Reflectionvectorbox1.value()], [self.Reflectionvectorbox2.value()]])
        if(np.linalg.norm(reflectvector) == 0):
            return np.identity(3)
        reflectvector /= np.linalg.norm(reflectvector)

        x = np.array([[1.0], [0.0], [0.0]])
        x1 = reflectvector.T.dot(x) * reflectvector
        x = x - 2 * x1

        y = np.array([[0.0], [1.0], [0.0]])
        y1 = reflectvector.T.dot(y) * reflectvector
        y = y - 2 * y1

        z = np.array([[0.0], [0.0], [1.0]])
        z1 = reflectvector.T.dot(z) * reflectvector
        z = z - 2 * z1

        matrix = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        matrix[0, 0] = x[0, 0]
        matrix[0, 1] = y[0, 0]
        matrix[0, 2] = z[0, 0]
        matrix[1, 0] = x[1, 0]
        matrix[1, 1] = y[1, 0]
        matrix[1, 2] = z[1, 0]
        matrix[2, 0] = x[2, 0]
        matrix[2, 1] = y[2, 0]
        matrix[2, 2] = z[2, 0]

        return matrix

    def Reflectioncalculatebuttonclicked(self):
        self.matrix = self.Reflectioncalculate()
        self.Displaymatrix_0()

    def Reflectionapplybuttonclicked(self):
        matrix = self.Reflectioncalculate()
        self.Matrixset(self.matrix, self.Displaymatrixbox)
        self.matrix = self.matrix.dot(matrix)
        self.Displaymatrix_0()

    def Matrixcopy_2clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displayinversematrixbox)

    def Matrixpaste_2clicked(self):
        self.Displayset(self.matrixbuffer, self.Displayinversematrixbox)
    
    def Matrixcopy_3clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displayinvmatrixbox)

    def Calculateinversematrixbuttonclicked(self):
        self.Matrixset(self.inversematrix, self.Displayinversematrixbox)

        self.inversematrixdeterminant = np.linalg.det(self.inversematrix)
        self.Displaydeterminantbox.setValue(self.inversematrixdeterminant)

        if(self.inversematrixdeterminant != 0):
            self.invmatrix = np.linalg.inv(self.inversematrix)

            self.Displayset(self.invmatrix, self.Displayinvmatrixbox)

            self.Displayinversematrixbutton.setDisabled(False)
            self.openGLWidget.matrix = copy.deepcopy(self.inversematrix)
            self.openGLWidget.displayflag = 2
            self.openGLWidget.updateflag = 1

    def Displayinversematrixbuttonclicked(self):
        if(self.inversematrixdeterminant != 0):
            self.openGLWidget.matrix = copy.deepcopy(self.invmatrix)
            self.openGLWidget.displayflag = 2
            self.openGLWidget.updateflag = 1

    def Calculatecramersbuttonclicked(self):
        self.Matrixset(self.cramersmatrix, self.Displaycramersmatrixbox)
        determinant = np.linalg.det(self.cramersmatrix)
        self.Displaycramersdeterminantbox.setValue(determinant)

        if(determinant != 0):
            vectorb = np.array([[0.0], [0.0], [0.0]])
            vectorb[0] = self.Vectorbdisplaybox0.value()
            vectorb[1] = self.Vectorbdisplaybox1.value()
            vectorb[2] = self.Vectorbdisplaybox2.value()

            self.cram1matrix = copy.deepcopy(self.cramersmatrix)
            self.cram1matrix[0, 0] = vectorb[0]
            self.cram1matrix[1, 0] = vectorb[1]
            self.cram1matrix[2, 0] = vectorb[2]

            self.cram2matrix = copy.deepcopy(self.cramersmatrix)
            self.cram2matrix[0, 1] = vectorb[0]
            self.cram2matrix[1, 1] = vectorb[1]
            self.cram2matrix[2, 1] = vectorb[2]

            self.cram3matrix = copy.deepcopy(self.cramersmatrix)
            self.cram3matrix[0, 2] = vectorb[0]
            self.cram3matrix[1, 2] = vectorb[1]
            self.cram3matrix[2, 2] = vectorb[2]

            self.Displayset(self.cram1matrix, self.Displaycram1matrixbox)
            self.Displayset(self.cram2matrix, self.Displaycram2matrixbox)
            self.Displayset(self.cram3matrix, self.Displaycram3matrixbox)

            self.Vectorxcramdisplaybox0.setValue(np.linalg.det(self.cram1matrix) / determinant)
            self.Vectorxcramdisplaybox1.setValue(np.linalg.det(self.cram2matrix) / determinant)
            self.Vectorxcramdisplaybox2.setValue(np.linalg.det(self.cram3matrix) / determinant)

            self.Displaycramers1matrixbutton.setDisabled(False)
            self.Displaycramers2matrixbutton.setDisabled(False)
            self.Displaycramers3matrixbutton.setDisabled(False)

    def Displaycramers1matrixbuttonclicked(self):
        self.openGLWidget.matrix = self.cram1matrix
        self.openGLWidget.displayflag = 2
        self.openGLWidget.updateflag = 1

    def Displaycramers2matrixbuttonclicked(self):
        self.openGLWidget.matrix = self.cram2matrix
        self.openGLWidget.displayflag = 2
        self.openGLWidget.updateflag = 1

    def Displaycramers3matrixbuttonclicked(self):
        self.openGLWidget.matrix = self.cram3matrix
        self.openGLWidget.displayflag = 2
        self.openGLWidget.updateflag = 1

    def Matrixcopy_4clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displaycramersmatrixbox)

    def Matrixpaste_3clicked(self):
        self.Displayset(self.matrixbuffer, self.Displaycramersmatrixbox)

    def Matrixcopy_5clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displaycram1matrixbox)

    def Matrixcopy_6clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displaycram2matrixbox)

    def Matrixcopy_7clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displaycram3matrixbox)

    def Calculatesvdbuttonclicked(self):
        self.Matrixset(self.svdmatrix, self.Displaysvdmatrixbox)
        u, s, v = np.linalg.svd(self.svdmatrix)
        I = np.identity(3)
        I[0, 0] = s[0]
        I[1, 1] = s[1]
        I[2, 2] = s[2]
        s = I
        v = v.T
        self.Displayset(u, self.Displayumatrixbox)
        self.Displayset(s, self.Displaysmatrixbox)
        self.Displayset(v, self.Displayvmatrixbox)
        self.umatrix = u
        self.vmatrix = v
        self.smatrix = s
        #print(u.dot(s.dot(v.T)))

        self.Animatesvdbutton.setDisabled(False)
        self.Displayumatrixbutton.setDisabled(False)
        self.Displaysmatrixbutton.setDisabled(False)
        self.Displayvmatrixbutton.setDisabled(False)
        self.openGLWidget.matrix = self.svdmatrix
        self.openGLWidget.displayflag = 2
        self.openGLWidget.updateflag = 1

    def Animatesvdbuttonclicked(self):
        self.openGLWidget.matrix = self.svdmatrix
        self.openGLWidget.umatrix = self.umatrix
        self.openGLWidget.smatrix = self.smatrix
        self.openGLWidget.vmatrix = self.vmatrix

        self.openGLWidget.framecount = 0
        self.openGLWidget.displayflag = 3
        self.openGLWidget.updateflag = 1

    def Displayumatrixbuttonclicked(self):
        self.openGLWidget.matrix = self.umatrix
        self.openGLWidget.displayflag = 2
        self.openGLWidget.updateflag = 1

    def Displaysmatrixbuttonclicked(self):
        self.openGLWidget.matrix = self.smatrix
        self.openGLWidget.displayflag = 2
        self.openGLWidget.updateflag = 1

    def Displayvmatrixbuttonclicked(self):
        self.openGLWidget.matrix = self.vmatrix
        self.openGLWidget.displayflag = 2
        self.openGLWidget.updateflag = 1

    def Matrixcopy_8clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displaysvdmatrixbox)

    def Matrixpaste_4clicked(self):
        self.Displayset(self.matrixbuffer, self.Displaysvdmatrixbox)

    def Matrixcopy_9clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displayumatrixbox)

    def Matrixcopy_10clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displaysmatrixbox)

    def Matrixcopy_11clicked(self):
        self.Matrixset(self.matrixbuffer, self.Displayvmatrixbox)

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())