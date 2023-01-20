from QSwitchControl import SwitchControl
from PyQt5 import QtWidgets, QtCore, QtWidgets
import sys
import os
from random import randint
from plot import graph
from map_plot import mapWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QApplication, QWidget, QLineEdit , QListWidget, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect, QPropertyAnimation

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height=1200,800
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 30px;
            }
        ''')
        global self.layout1
        self.layout=QHBoxLayout()
        self.setLayout(self.layout)

        self.layout1=QVBoxLayout()
        self.layout2=QVBoxLayout()

        self.layout.addLayout(self.layout1,3)
        self.layout.addLayout(self.layout2,7)

        #column1
        self.logo = QLabel()
        logo_image = QPixmap('./image.jpeg')
        logo_image = logo_image.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.logo.setPixmap(logo_image)
        self.MENU1_label = QLabel('TEAM ID:1020')

        self.layout1.addWidget(self.logo, stretch=1)
        self.layout1.addWidget(self.MENU1_label)

        self.MENU1_widget = QtWidgets.QWidget()
        self.MENU1_widget.setLayout(layout1)
        self.MENU1_widget.setStyleSheet("background-color: #005975")
        #column2

        self.btn2 = QPushButton("start")
        self.layout2.addWidget(self.btn2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("closing window")
