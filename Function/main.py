# -*- coding: utf-8 -*-
# To God be the Glory, great things He hath done

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot; import sys

class Bible(QObject):
    
    def __init__(self):
        
        QObject.__init__(self)
        
app = QGuiApplication(sys.argv)
bible = Bible()
engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty('Bible', bible)
engine.load('..\\UI\\ui.qml')
engine.quit.connect(app.quit)
sys.exit(app.exec_())