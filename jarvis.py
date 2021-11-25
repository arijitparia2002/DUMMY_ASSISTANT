from jarvisUI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import main
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        main.run_jarvis()

startFunction = MainThread()

class GuiStart(QMainWindow):

    def __init__(self):
        super().__init__()
        #make jarvis_ui object
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.start.clicked.connect(self.startFunction)
        self.jarvis_ui.exit.clicked.connect(self.close)


    def startFunction(self):
        #code for starting the gif
        self.jarvis_ui.movies_core = QtGui.QMovie(".\\reactor4.gif")
        self.jarvis_ui.core.setMovie(self.jarvis_ui.movies_core)
        self.jarvis_ui.movies_core.start()


        startFunction.start()

app = QApplication(sys.argv)
GUI_jarvis = GuiStart()
GUI_jarvis.show()
exit(app.exec_())