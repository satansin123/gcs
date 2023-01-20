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

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):


        super(MainWindow, self).__init__(*args, **kwargs)
        self.window_width, self.window_height=1200,1000
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size:15px;
            }
        ''')

		#self.serial = Serial()
        self.buffer = []
        self.setWindowTitle("GCS")
        self.w = None
        self.counter = 0




        # Menu 1-------------------------------------------------------------------------------------
        self.logo = QLabel()
        logo_image = QPixmap('./image.jpeg')
        logo_image = logo_image.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.logo.setPixmap(logo_image)
        self.MENU1_label = QLabel('TEAM ID:1020')

        MENU1_layout = QVBoxLayout()
        MENU1_layout.addWidget(self.logo, stretch=1)
        MENU1_layout.addWidget(self.MENU1_label)

        self.MENU1_widget = QtWidgets.QWidget()
        self.MENU1_widget.setLayout(MENU1_layout)
        self.MENU1_widget.setMinimumSize(200,40)
        self.MENU1_widget.setStyleSheet("background-color: grey")

        #MENU_2---------------------------------------------------------------------------------------
        self.MENU2_mission_time = QLabel('Mission Time:')
        self.MENU2_packet_count = QLabel('Packet Count:')

        MENU2_layout = QVBoxLayout()
        MENU2_layout.addWidget(self.MENU2_mission_time)
        MENU2_layout.addWidget(self.MENU2_packet_count)

        self.MENU2_widget = QtWidgets.QWidget()
        self.MENU2_widget.setLayout(MENU2_layout)
        self.MENU2_widget.setMinimumSize(170,40)
        self.MENU2_widget.setStyleSheet("background-color: rgb(200,100,150)")

        #menu3---------------------------------------------------------------------------------------------
        self.MENU3_mode = QLabel('Mode:')
        self.MENU3_state = QLabel('State:')

        MENU3_layout = QVBoxLayout()
        MENU3_layout.addWidget(self.MENU3_mode)
        MENU3_layout.addWidget(self.MENU3_state)

        self.MENU3_widget = QtWidgets.QWidget()
        self.MENU3_widget.setLayout(MENU3_layout)
        self.MENU3_widget.setMinimumSize(100,40)
        self.MENU3_widget.setStyleSheet("background-color: grey")

        #menu4----------------------------------------------------------------------------------------------
        self.MENU4_HS_deployed = QLabel('HS Deployed:')
        self.MENU4_PC_deployed = QLabel('PC Deployed:')

        MENU4_layout = QVBoxLayout()
        MENU4_layout.addWidget(self.MENU4_HS_deployed)
        MENU4_layout.addWidget(self.MENU4_PC_deployed)

        self.MENU4_widget = QtWidgets.QWidget()
        self.MENU4_widget.setLayout(MENU4_layout)
        self.MENU4_widget.setMinimumSize(180,40)
        self.MENU4_widget.setStyleSheet("background-color: grey")
        #menu5-------------------------------------------------------------------------------------------------
        self.MENU5_mast_raised = QLabel('Mast Raised:')
        self.MENU5_extra = QLabel('Extra:')

        MENU5_layout = QVBoxLayout()
        MENU5_layout.addWidget(self.MENU5_mast_raised)
        MENU5_layout.addWidget(self.MENU5_extra)

        self.MENU5_widget = QtWidgets.QWidget()
        self.MENU5_widget.setLayout(MENU5_layout)
        self.MENU5_widget.setMinimumSize(180,40)
        self.MENU5_widget.setStyleSheet("background-color: grey")

#---------------------------------------------------------------------------------------
#MENU_widget
        MENU_layout = QHBoxLayout()
        MENU_layout.addWidget(self.MENU1_widget)
        MENU_layout.addWidget(self.MENU2_widget)
        MENU_layout.addWidget(self.MENU3_widget)
        MENU_layout.addWidget(self.MENU4_widget)
        MENU_layout.addWidget(self.MENU5_widget)
        self.MENU_widget = QtWidgets.QWidget()
        self.MENU_widget.setLayout(MENU_layout)
        self.MENU_widget.setMinimumSize(800,30)
        self.MENU_widget.setStyleSheet("background-color: grey")

#-------------------------------------------------------------------------------------------------------------------
        # graph1
        #self.PAYLOAD_label = QLabel('PAYLOAD', self)
        #self.PAYLOAD_label.setStyleSheet("color: white;")
        self.graphPressure = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Pressure"
        	}], True, 200, "", "Pressure (Pa)")

        self.graphTemprature = graph([
        	{
        		"color": (255, 0, 0),
        		"name": "Temprature"
        	}], False, 20, "", "Temperature")

        self.graphAltitude = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Altitude"
        	}], True, 200, "", "Altitude")


        GRAPH1_layout = QHBoxLayout()
        #PAYLOAD_layout.addWidget(self.PAYLOAD_label)
        GRAPH1_layout.addWidget(self.graphPressure.graphWidget)
        GRAPH1_layout.addWidget(self.graphTemprature.graphWidget)
        GRAPH1_layout.addWidget(self.graphAltitude.graphWidget)



        self.GRAPH1_widget = QtWidgets.QWidget()
        self.GRAPH1_widget.setLayout(GRAPH1_layout)
        self.GRAPH1_widget.setMinimumSize(800,400)
        self.GRAPH1_widget.setStyleSheet("""
        .QWidget {
            border: 2px solid white;
            }
        """)
        #self.GRAPH1_widget.setStyleSheet("background-color: white")

#----------------------------------------------------------------------------------------
#GRAPH2

        self.graphVoltage = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "Voltage"
        	}], True, 200, "", "Voltage")

        self.graphGps_Altitude = graph([
        	{
        		"color": (255, 0, 0),
        		"name": "Gps_Altitude"
        	}], False, 20, "", "Gps_Altitude")

        self.graphTiltXY = graph([
        	{
        		"color": (0, 0, 255),
        		"name": "TiltXY"
        	}], True, 200, "", "TiltXY")


        GRAPH2_layout = QHBoxLayout()
        #PAYLOAD_layout.addWidget(self.PAYLOAD_label)
        GRAPH2_layout.addWidget(self.graphVoltage.graphWidget)
        GRAPH2_layout.addWidget(self.graphGps_Altitude.graphWidget)
        GRAPH2_layout.addWidget(self.graphTiltXY.graphWidget)



        self.GRAPH2_widget = QtWidgets.QWidget()
        self.GRAPH2_widget.setLayout(GRAPH2_layout)
        self.GRAPH2_widget.setMinimumSize(800,400)
        self.GRAPH2_widget.setStyleSheet("""
        .QWidget {
            border: 2px solid white;
            }
        """)
        self.map = mapWidget()

#create gps layout and then add main layout in horizntal to main layout

##---------------------------------------------------
                # add widgets


        MAIN_layout = QVBoxLayout()

        # add widgets
        MAIN_layout.addWidget(self.MENU_widget)
        #MAIN_layout.addWidget(self.CONTAINER_widget)``
        MAIN_layout.addWidget(self.GRAPH1_widget)
        MAIN_layout.addWidget(self.GRAPH2_widget)
        self.MAIN_widget = QtWidgets.QWidget()
        self.MAIN_widget.setLayout(MAIN_layout)
        self.MAIN_widget.setStyleSheet("background-color: black")
        #self.setCentralWidget(self.MAIN_widget)

#gpswidget
    #mapwidget
        self.map = mapWidget()
        self.map.update(17,78)
    #----------------------------------------------------------------------------------
    #telemetry widget
        #cmd
        self.tele_cmd = QLabel('tele_cmd:')
        self.tele_text= QLabel('tele_text')
        tele_layout = QVBoxLayout()
        tele_layout.addWidget(self.tele_cmd)
        tele_layout.addWidget(self.tele_text)


        self.tele_widget = QtWidgets.QWidget()
        self.tele_widget.setLayout(tele_layout)
        self.tele_widget.setStyleSheet("background-color: #005975")



        #twends----------------
        gps_layout = QVBoxLayout()

        # add widgets
        gps_layout.addWidget(self.map)

        gps_layout.addWidget(self.tele_widget)

        self.gps_widget = QtWidgets.QWidget()
        self.gps_widget.setLayout(gps_layout)
        self.gps_widget.setMinimumSize(500,400)
        self.gps_widget.setStyleSheet("background-color: black")

        all_layout = QHBoxLayout()

        # add widgets
        all_layout.addWidget(self.MAIN_widget)
        #MAIN_layout.addWidget(self.CONTAINER_widget)``
        all_layout.addWidget(self.gps_widget)
        self.all_widget = QtWidgets.QWidget()
        self.all_widget.setLayout(all_layout)
        self.all_widget.setStyleSheet("background-color: black")
        self.setCentralWidget(self.all_widget)




        self.packet_count = 0
        self.number = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.update)
        self.timer.start()






app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
