from OpenGL import GL, GLU, GLUT

from PyQt5 import QtCore, QtWidgets, uic

import qdarkstyle

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

        self.Eigenvalue1box = self.findChild(QtWidgets.QLineEdit, 'Eigenvalue1box')
        self.Eigenvalue2box = self.findChild(QtWidgets.QLineEdit, 'Eigenvalue2box')
        self.Eigenvalue3box = self.findChild(QtWidgets.QLineEdit, 'Eigenvalue3box')

        self.Eigenvector1box = self.findChild(QtWidgets.QTextEdit, 'Eigenvector1box')
        self.Eigenvector2box = self.findChild(QtWidgets.QTextEdit, 'Eigenvector2box')
        self.Eigenvector3box = self.findChild(QtWidgets.QTextEdit, 'Eigenvector3box')

        self.Displaymatrixbutton = self.findChild(QtWidgets.QPushButton, 'Displaymatrixbutton')
        self.Displaymatrixbutton.clicked.connect(self.Displaymatrixbuttonclicked)

        #Rotation
        self.Rotationvectorbox0 = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationvectorbox0')
        self.Rotationvectorbox1 = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationvectorbox1')
        self.Rotationvectorbox2 = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationvectorbox2')

        self.Rotationanglebox = self.findChild(QtWidgets.QDoubleSpinBox, 'Rotationanglebox')

        self.Rotationcalculatebutton = self.findChild(QtWidgets.QPushButton, 'Rotationcalculatebutton')        
        self.Rotationcalculatebutton.clicked.connect(self.Rotationcalculatebuttonclicked)

        #Inverse
        self.Displayinversematrixbox00 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_2')
        self.Displayinversematrixbox01 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_2')
        self.Displayinversematrixbox02 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_2')
        self.Displayinversematrixbox10 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_2')
        self.Displayinversematrixbox11 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_2')
        self.Displayinversematrixbox12 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_2')
        self.Displayinversematrixbox20 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_2')
        self.Displayinversematrixbox21 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_2')
        self.Displayinversematrixbox22 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_2')

        self.Displayinvmatrixbox00 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox00_3')
        self.Displayinvmatrixbox01 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox01_3')
        self.Displayinvmatrixbox02 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox02_3')
        self.Displayinvmatrixbox10 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox10_3')
        self.Displayinvmatrixbox11 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox11_3')
        self.Displayinvmatrixbox12 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox12_3')
        self.Displayinvmatrixbox20 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox20_3')
        self.Displayinvmatrixbox21 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox21_3')
        self.Displayinvmatrixbox22 = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaymatrixbox22_3')

        self.Displaydeterminantbox = self.findChild(QtWidgets.QDoubleSpinBox, 'Displaydeterminantbox')

        self.Calculateinversematrixbutton = self.findChild(QtWidgets.QPushButton, 'Calculateinversematrixbutton')
        self.Calculateinversematrixbutton.clicked.connect(self.Calculateinversematrixbuttonclicked)
        self.Displayinversematrixbutton = self.findChild(QtWidgets.QPushButton, 'Displayinversematrixbutton')
        self.Displayinversematrixbutton.clicked.connect(self.Displayinversematrixbuttonclicked)
        self.Displayinversematrixbutton.setDisabled(True)

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
        self.inversematrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.invmatrix = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        self.vector = np.array([[0.0],[0.0],[0.0]])
        self.Displaymatrix_0()
        self.Displaymatrixeigen()
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
        self.Displaymatrixeigen()

        self.openGLWidget.matrix = copy.deepcopy(self.matrix)
        self.openGLWidget.vector1 = copy.deepcopy(self.vector)
        self.openGLWidget.vector2 = copy.deepcopy(self.matrix.dot(self.vector))
        self.openGLWidget.displayflag = 1
        self.openGLWidget.updateflag = 1

    def Rotationcalculatebuttonclicked(self):
        rotatevector = np.array([[self.Rotationvectorbox0.value()], [self.Rotationvectorbox1.value()], [self.Rotationvectorbox2.value()]])
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

        self.matrix[0, 0] = x[0, 0]
        self.matrix[0, 1] = y[0, 0]
        self.matrix[0, 2] = z[0, 0]
        self.matrix[1, 0] = x[1, 0]
        self.matrix[1, 1] = y[1, 0]
        self.matrix[1, 2] = z[1, 0]
        self.matrix[2, 0] = x[2, 0]
        self.matrix[2, 1] = y[2, 0]
        self.matrix[2, 2] = z[2, 0]

        self.Displaymatrix_0()

    def Calculateinversematrixbuttonclicked(self):
        self.inversematrix[0, 0] = self.Displayinversematrixbox00.value()
        self.inversematrix[0, 1] = self.Displayinversematrixbox01.value()
        self.inversematrix[0, 2] = self.Displayinversematrixbox02.value()
        self.inversematrix[1, 0] = self.Displayinversematrixbox10.value()
        self.inversematrix[1, 1] = self.Displayinversematrixbox11.value()
        self.inversematrix[1, 2] = self.Displayinversematrixbox12.value()
        self.inversematrix[2, 0] = self.Displayinversematrixbox20.value()
        self.inversematrix[2, 1] = self.Displayinversematrixbox21.value()
        self.inversematrix[2, 2] = self.Displayinversematrixbox22.value()

        self.inversematrixdeterminant = np.linalg.det(self.inversematrix)
        self.Displaydeterminantbox.setValue(self.inversematrixdeterminant)

        if(self.inversematrixdeterminant != 0):
            self.invmatrix = np.linalg.inv(self.inversematrix)

            self.Displayinvmatrixbox00.setValue(self.invmatrix[0, 0])
            self.Displayinvmatrixbox01.setValue(self.invmatrix[0, 1])
            self.Displayinvmatrixbox02.setValue(self.invmatrix[0, 2])
            self.Displayinvmatrixbox10.setValue(self.invmatrix[1, 0])
            self.Displayinvmatrixbox11.setValue(self.invmatrix[1, 1])
            self.Displayinvmatrixbox12.setValue(self.invmatrix[1, 2])
            self.Displayinvmatrixbox20.setValue(self.invmatrix[2, 0])
            self.Displayinvmatrixbox21.setValue(self.invmatrix[2, 1])
            self.Displayinvmatrixbox22.setValue(self.invmatrix[2, 2])

            self.Displayinversematrixbutton.setDisabled(False)
            self.openGLWidget.matrix = copy.deepcopy(self.inversematrix)
            self.openGLWidget.displayflag = 2
            self.openGLWidget.updateflag = 1

    def Displayinversematrixbuttonclicked(self):
        if(self.inversematrixdeterminant != 0):
            self.openGLWidget.matrix = copy.deepcopy(self.invmatrix)
            self.openGLWidget.displayflag = 2
            self.openGLWidget.updateflag = 1

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())