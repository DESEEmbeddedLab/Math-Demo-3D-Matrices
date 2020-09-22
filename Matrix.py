from OpenGL import GL, GLU, GLUT

from PyQt5 import QtCore, QtWidgets, uic

import qdarkstyle

import traceback, sys, os, shutil, math

import numpy as np

class openGLDisplay(QtWidgets.QOpenGLWidget):

    def __init__(self, *args):

        super(openGLDisplay, self).__init__(*args)
        self.zoom = 1
        self.prev_x = 0.0
        self.prev_y = 0.0
        self.updateflag = 0
        self.coordinateflag = 0
        self.displayflag = 1
        self.center = np.array([0.0, 0.0, 0.0])
        self.front = np.array([0.0, 0.0, 1.0])
        self.up = np.array([0.0, 1.0, 0.0])

    def paint_axis(self):
        origin = self.center

        GL.glColor3f(1.0, 0.0, 0.0)   

        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(origin[0], origin[1], origin[2])
        GL.glVertex3f(origin[0] + 0.5, origin[1], origin[2])
        GL.glEnd()        

        GL.glColor3f(0.0, 1.0, 0.0)   

        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(origin[0], origin[1], origin[2])
        GL.glVertex3f(origin[0], origin[1] + 0.5, origin[2])
        GL.glEnd()  

        GL.glColor3f(0.0, 0.0, 1.0)

        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(origin[0], origin[1], origin[2])
        GL.glVertex3f(origin[0], origin[1], origin[2] + 0.5)
        GL.glEnd()  

    def paint_matrix_lines(self, matrix, s = 10):
        x = matrix.dot(np.array([[1.0], [0.0], [0.0]]))
        y = matrix.dot(np.array([[0.0], [1.0], [0.0]]))
        z = matrix.dot(np.array([[0.0], [0.0], [1.0]]))

        GL.glColor3f(0.5, 0.0, 0.5)  
        GL.glBegin(GL.GL_LINES)
        for i in range(-s, s + 1):
            GL.glVertex3fv(i * y - x * s)
            GL.glVertex3fv(i * y + x * s)
            GL.glVertex3fv(i * z - x * s)
            GL.glVertex3fv(i * z + x * s)
        GL.glEnd()

        GL.glColor3f(0.0, 0.5, 0.5)   
        GL.glBegin(GL.GL_LINES)
        for i in range(-s, s + 1):
            GL.glVertex3fv(i * x - y * s)
            GL.glVertex3fv(i * x + y * s)
            GL.glVertex3fv(i * z - y * s)
            GL.glVertex3fv(i * z + y * s)
        GL.glEnd()        

        GL.glColor3f(0.5, 0.5, 0.0)   
        GL.glBegin(GL.GL_LINES)
        for i in range(-s, s + 1):
            GL.glVertex3fv(i * x - z * s)
            GL.glVertex3fv(i * x + z * s)
            GL.glVertex3fv(i * y - z * s)
            GL.glVertex3fv(i * y + z * s)
        GL.glEnd()        

    def paint_matrix_planes(self, matrix, s = 5.0, r = 0.0, g = 0.0, b = 0.0, d = 0.1):
        x = matrix.dot(np.array([[1.0], [0.0], [0.0]]))
        y = matrix.dot(np.array([[0.0], [1.0], [0.0]]))
        z = matrix.dot(np.array([[0.0], [0.0], [1.0]]))

        GL.glColor4f(r, g, b, d)   

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3fv((x + y) * s)
        GL.glVertex3fv((x - y) * s)
        GL.glVertex3fv((-x - y) * s)
        GL.glVertex3fv((-x + y) * s)
        GL.glEnd()

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3fv((x + z) * s)
        GL.glVertex3fv((x - z) * s)
        GL.glVertex3fv((-x - z) * s)
        GL.glVertex3fv((-x + z) * s)
        GL.glEnd()

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3fv((y + z) * s)
        GL.glVertex3fv((y - z) * s)
        GL.glVertex3fv((-y - z) * s)
        GL.glVertex3fv((-y + z) * s)
        GL.glEnd()

        GL.glColor3f(r, g, b)   

        GL.glBegin(GL.GL_LINES)
        GL.glVertex3fv((x + y) * s)
        GL.glVertex3fv((x - y) * s)
        GL.glVertex3fv((x - y) * s)
        GL.glVertex3fv((-x - y) * s)
        GL.glVertex3fv((-x - y) * s)
        GL.glVertex3fv((-x + y) * s)
        GL.glVertex3fv((-x + y) * s)
        GL.glVertex3fv((x + y) * s)

        GL.glVertex3fv((x + z) * s)
        GL.glVertex3fv((x - z) * s)
        GL.glVertex3fv((x - z) * s)
        GL.glVertex3fv((-x - z) * s)
        GL.glVertex3fv((-x - z) * s)
        GL.glVertex3fv((-x + z) * s)
        GL.glVertex3fv((-x + z) * s)
        GL.glVertex3fv((x + z) * s)

        GL.glVertex3fv((y + z) * s)
        GL.glVertex3fv((y - z) * s)
        GL.glVertex3fv((y - z) * s)
        GL.glVertex3fv((-y - z) * s)
        GL.glVertex3fv((-y - z) * s)
        GL.glVertex3fv((-y + z) * s)
        GL.glVertex3fv((-y + z) * s)
        GL.glVertex3fv((y + z) * s)
        GL.glEnd()

    def paint_matrix(self, matrix, r = 0.0, g = 0.0, b = 0.0, d = 0.1):
        x = matrix.dot(np.array([[1.0], [0.0], [0.0]]))
        y = matrix.dot(np.array([[0.0], [1.0], [0.0]]))
        z = matrix.dot(np.array([[0.0], [0.0], [1.0]]))

        GL.glColor4f(r, g, b, d)   

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3fv(x)
        GL.glVertex3fv(x + y)
        GL.glVertex3fv(y)
        GL.glEnd()
        
        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3fv(z)
        GL.glVertex3fv(x + z)
        GL.glVertex3fv(x + y + z)
        GL.glVertex3fv(y + z)
        GL.glEnd()

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3fv(y)
        GL.glVertex3fv(y + z)
        GL.glVertex3fv(z)
        GL.glEnd()

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3fv(x)
        GL.glVertex3fv(y + x)
        GL.glVertex3fv(y + z + x)
        GL.glVertex3fv(z + x)
        GL.glEnd()

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3fv(z)
        GL.glVertex3fv(z + x)
        GL.glVertex3fv(x)
        GL.glEnd()

        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex3fv(y)
        GL.glVertex3fv(z + y)
        GL.glVertex3fv(z + x + y)
        GL.glVertex3fv(x + y)
        GL.glEnd()

        GL.glColor3f(0, 0, 0)

        GL.glBegin(GL.GL_LINES)
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3fv(x)
        GL.glVertex3fv(x)
        GL.glVertex3fv(x + y)
        GL.glVertex3fv(x + y)
        GL.glVertex3fv(y)
        GL.glVertex3fv(y)
        GL.glVertex3f(0, 0, 0)

        GL.glVertex3fv(z)
        GL.glVertex3fv(x + z)
        GL.glVertex3fv(x + z)
        GL.glVertex3fv(x + y + z)
        GL.glVertex3fv(x + y + z)
        GL.glVertex3fv(y + z)
        GL.glVertex3fv(y + z)
        GL.glVertex3fv(z)

        GL.glVertex3f(0, 0, 0)
        GL.glVertex3fv(y)
        GL.glVertex3fv(y)
        GL.glVertex3fv(y + z)
        GL.glVertex3fv(y + z)
        GL.glVertex3fv(z)
        GL.glVertex3fv(z)
        GL.glVertex3f(0, 0, 0)

        GL.glVertex3fv(x)
        GL.glVertex3fv(y + x)
        GL.glVertex3fv(y + x)
        GL.glVertex3fv(y + z + x)
        GL.glVertex3fv(y + z + x)
        GL.glVertex3fv(z + x)
        GL.glVertex3fv(z + x)
        GL.glVertex3fv(x)
        
        GL.glVertex3f(0, 0, 0)
        GL.glVertex3fv(z)
        GL.glVertex3fv(z)
        GL.glVertex3fv(z + x)
        GL.glVertex3fv(z + x)
        GL.glVertex3fv(x)
        GL.glVertex3fv(x)
        GL.glVertex3f(0, 0, 0)

        GL.glVertex3fv(y)
        GL.glVertex3fv(z + y)
        GL.glVertex3fv(z + y)
        GL.glVertex3fv(z + x + y)
        GL.glVertex3fv(z + x + y)
        GL.glVertex3fv(x + y)
        GL.glVertex3fv(x + y)
        GL.glVertex3fv(y)

        GL.glEnd()

    def paint_coordinates(self, x, y, z):
        GL.glBegin(GL.GL_POINTS)
        GL.glVertex3f(x, y, z)
        GL.glEnd()

        string = '(' + str(x) + ',' + str(y) + ',' + str(z) + ')'
        length = len(string) - 3

        GL.glRasterPos3f(x - (0.25 + length * 0.07), y - 0.15, z)
        for i in range(0, len(string)):
            GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_HELVETICA_12, ord(string[i]))

    def paintGL(self):
        self.loadScene()

        GLUT.glutInit()
        GL.glClearColor(0.7, 0.7, 0.7, 0)		
        GL.glClearDepth(1)

        if(self.coordinateflag):
            self.paint_axis()

        GL.glDisable(GL.GL_LINE_STIPPLE)
        self.paint_matrix(np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]))
        
    def initializeGL(self):
        print("\033[4;30;102m INITIALIZE GL\033[0m")
        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_LINE_SMOOTH)
        GL.glHint(GL.GL_LINE_SMOOTH_HINT, GL.GL_NICEST)
        GL.glLineWidth(2)
        GL.glPointSize(4)
        GL.glLineStipple(1, 0xAA00)

    def loadScene(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        _, _, width, height = GL.glGetDoublev(GL.GL_VIEWPORT)
        GLU.gluPerspective(
            45,
            width / float(height or 1), 
            0.25, 
            200, 
        )

        cam_pos = self.center + self.front * 10 * self.zoom
        GLU.gluLookAt(cam_pos[0], cam_pos[1], cam_pos[2], self.center[0], self.center[1], self.center[2], self.up[0], self.up[1], self.up[0])

    def mousePressEvent(self, event):
        self.prev_x = event.x()
        self.prev_y = event.y()
        self.coordinateflag = 1
        self.updateflag = 1
        self.setFocus()

    def mouseReleaseEvent(self, event):
        self.coordinateflag = 0
        self.updateflag = 1

    def mouseMoveEvent(self, event):
        x = (self.prev_x - event.x()) * math.pi / 950.0
        y = (event.y() - self.prev_y) * math.pi / 950.0

        up = self.up
        self.up = up * math.cos(y) - self.front * math.sin(y)
        self.up /= np.linalg.norm(self.up)
        self.front = self.front * math.cos(y) + up * math.sin(y)
        self.front /= np.linalg.norm(self.front)

        right = np.cross(self.up, self.front)
        self.front = self.front * math.cos(x) + right * math.sin(x)
        self.front /= np.linalg.norm(self.front)

        self.prev_x = event.x()
        self.prev_y = event.y()

        self.updateflag = 1

    def wheelEvent(self, event):
        delta = event.angleDelta().y() / 2400.0
        self.center += delta * self.front
        self.updateflag = 1

    def keyPressEvent(self, event):
        x = 0
        if(event.key() == QtCore.Qt.Key_Left):
            x = -0.1
        elif(event.key() == QtCore.Qt.Key_Right):
            x = 0.1

        self.center += x * self.zoom * np.cross(self.up, self.front)

        y = 0
        if(event.key() == QtCore.Qt.Key_Up):
            y = 0.1
        elif(event.key() == QtCore.Qt.Key_Down):
            y = -0.1

        self.center += y * self.zoom * self.up

        if(event.key() == QtCore.Qt.Key_R):
            self.front = np.array([0.0, 0.0, 1.0])
            self.up = np.array([0.0, 1.0, 0.0])
        
        if(event.key() == QtCore.Qt.Key_T):
            self.center = np.array([0.0, 0.0, 0.0])

        self.updateflag = 1

class mainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):

        super(mainWindow, self).__init__()
        uic.loadUi('MatrixUI.ui', self)
        self.threadpool = QtCore.QThreadPool()

        #Tabs
        self.Tabs = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.Tabs.setCurrentIndex(0)

    def setupUI(self):
        print("\033[1;101m SETUP UI \033[0m")

        self.openGLWidget = openGLDisplay(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, 1200, 950))
        self.openGLWidget.setObjectName("openGLWidget1")

        self.windowsHeight = self.openGLWidget.height()
        self.windowsWidth = self.openGLWidget.width()
        self.openGLWidget.resizeGL(self.windowsWidth, self.windowsHeight)

        self.openGLWidget.setFocus()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateopenGLWidget)
        self.timer.start(17)

    def updateopenGLWidget(self):
        if(self.openGLWidget.updateflag):
            self.openGLWidget.updateflag = 0
            self.openGLWidget.update()

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())