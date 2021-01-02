import sys,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import *
from untitled import Ui_Form
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
#import matplotlib.pyplot as plt
#import numpy as np
#import time,random

class Worker(QRunnable):


    @pyqtSlot()
    def run(self):

        """print("Thread start")

        print("Thread complete")"""

class Conf(QtWidgets.QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(Conf, self).__init__(parent)
        self.ui = Ui_Form() #tasarım içindeki isim alanlarına burdan ulaşıcaz.

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.ui.setupUi(self))
        self.setLayout(self.main_layout)

        ############timer monitoring################







class MainWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)
        #self.resize(50, 50)
        ###########################################################
        #Bu alan daha önceden hazırlanan subclass ların ana Widget içinde yüklemesini yapıyor
        #Subclass özelliklerini kullanmak için çağırılan sınıf ismini kullanmak gerekiyor.
        self.window_conf=Conf(parent=self)
        ###################Ön tanımlı değerler##################3
        self.SEAWATERTEMP="1000"
        #################serial port bindings#####################
        self.serial = QSerialPort()
        self.serial.readyRead.connect(self.receive)
        self.serial.setPortName("COM7")
        self.serial.setBaudRate(9600)
        ########################timing#########################
        #Kesintisiz veri okuma için zamanlayıcıya bağladık receive fonksiyonunu
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.receive)
        #self.timer.timeout.connect(self.update_monitoring)
        self.timer.start()

        ########################timing#########################
        """# Kesintisiz veri okuma için zamanlayıcıya bağladık receive fonksiyonunu
        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(2147483646)
        self.timer1.timeout.connect(self.update_monitoring)
        # self.timer.timeout.connect(self.update_monitoring)
        #self.date = QtCore.QDateTime.currentDateTime()
        self.timer1.start()"""



        ########################BUTTON EVENTS############################
        self.window_conf.ui.pb_inputsetting.clicked.connect(self.ManualSettings)

        ##########################################################

        self.indexItem = 1
        self.threadpool = QThreadPool()



    def ManualSettings(self):
        self.SEAWATERTEMP=self.window_conf.ui.Line_SeaTemp.text()

    def receive(self):
        #Ayrı bir iş parçacığı altında sürekli signal yakalaması yapıyoruz
        #Döngü sonunda self.updated_parameters() fonksiyonunu çağırıyoruz.
        #
        worker = Worker()
        self.threadpool.start(worker)
        self.date = QtCore.QDateTime.currentDateTime()
        self.serial.open(QIODevice.ReadWrite)
        while self.serial.canReadLine():
            #print(self.serial.open(QtCore.QIODevice.ReadWrite))

            self.text = self.serial.readLine().data().decode()
            self.text = self.text.rstrip('\r\n')
            self.a = float(self.text[-5:])
            #print(self.a)
            self.updated_parameters()

            #self.update_monitoring()


            #self.baslat(100-self.a)

    def updated_parameters(self):
        #Arduniodan gelen veriler bu fonksiyon altında güncellenecektir.
        #Değişmesini istediğin isim alanını untitled dki isme göre çağır
        #Örnek:: self.window_conf.ui.label_10.setText(str(self.a))
        #
        zone1=self.window_conf.ui.label_32.setText(str(self.a))
        self.window_conf.ui.label_40.setText(str(self.a))

        if self.a>int(self.SEAWATERTEMP):
            self.update_monitoring(text="su sıcaklığı artma belirtisi Şunları yapın:"+
                                   "Suyu kontrol et"+str(self.date.currentDateTime()))
        #print(self.window_conf.ui.label_10.text)
        else:
            return

    def update_monitoring(self,text="onur"):

        item = QtWidgets.QListWidgetItem()
        self.window_conf.ui.listWidget.addItem(item)
        item = self.window_conf.ui.listWidget.item(self.indexItem)  # isim alanına dikkat et
        item.setText(text)
        #item.setText("Value Temperature"+str(self.a)+str(self.date))

        
        self.indexItem =1+ self.indexItem


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())