import sys,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QFrame ,QDialog,QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from untitled2 import Ui_Form
import sqlite3
from mydialog import Ui_Dialog
import logging
from degisken import *


logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)



class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        

class Worker(QRunnable):
    @pyqtSlot()
    def run(self):
        logger.info("Worker Class")

class Conf(QtWidgets.QWidget,Ui_Form):
    """
    Uygulamanın Grfik arayüzünü çağırıyor XML dosyasını Mainwindow
    içinde window_conf ismi ile çağırıyoruz  
    """
    def __init__(self,parent=None):
        super(Conf, self).__init__(parent)
        self.ui = Ui_Form() #tasarım içindeki isim alanlarına burdan ulaşıcaz.
        
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.ui.setupUi(self))
        self.setLayout(self.main_layout)
        
        







class MainWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)
        self.window_conf=Conf(parent=self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #-----> MINIMIZE BUTTON OF DIALOGBOX
        self.window_conf.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.window_conf.ui.bn_close.clicked.connect(lambda: self.close())
        self.window_conf.ui.bn_expand.clicked.connect(lambda: self.Fullekran())

        # WIDGET TO MOVE
        self.dragPos=QtCore.QPoint()



        #Icons
        self.icon_succ = QPixmap('C:/Users/Admin/Desktop/adunio denemeler/Main Project/Assests/success.png')
        self.icon_error = QPixmap('C:/Users/Admin/Desktop/adunio denemeler/Main Project/Assests/Error.png')
        self.icon_hint = QPixmap('C:/Users/Admin/Desktop/adunio denemeler/Main Project/Assests/hint.png')
        


        ###################Ön tanımlı değerler##################3
        self.Cyl1=0
        self.Cyl2=0
        self.Cyl3=0
        self.Cyl4=0
        self.Cyl5=0
        self.Cyl6=0
        self.Cyl7=0
        self.Cyl8=0
        self.line_cylinder_default=0
        
        #################serial port bindings#####################
        self.serial = QSerialPort()
        #self.serial.readyRead.connect(self.receive)
        self.serial.setPortName("COM6")
        self.serial.setBaudRate(9600)
        
        ###########################DATABASE######################

        self.conn = sqlite3.connect('Alarms.db')
        self.cursor = self.conn.execute("SELECT id, category,issue,Solution from Alarm")
        
        
        ########################timing#########################
        """
        QtCore.QTimer() Function setup
        """
        self.timer = QtCore.QTimer()
        self.timer.setInterval(850)
        self.timer.timeout.connect(self.receive)
        #self.timer.timeout.connect(self.statu)
        self.timer.start()

        ########################timing#########################
        
        ########################BUTTON EVENTS############################
        self.window_conf.ui.pb_inputsetting.clicked.connect(self.ManualSettings)
        #item click eventleri listwidget üzerinden yapılabiliyor
        self.window_conf.ui.listWidget.itemDoubleClicked.connect(self.doubleClickItem)

        #################### PANEL  POMPA ###########################
        self.window_conf.ui.savebn_c1.clicked.connect(self.ConfSettings)
        ##########################################################

        self.indexItem = 1
        self.threadpool = QThreadPool()
        self.veritabanı=[i for i in self.cursor]
        
        
            
                 
    

    def Fullekran(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def mousePressEvent(self,event):
            self.dragPos = event.globalPos()   #INITIAL POSOTION OF THE DIALOGBOX
    def mouseMoveEvent(self,event):
            # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def ConfSettings(self):
        #degiskenler fonksiyonundan tanımlı line text değerlerini aldık
        #hepsi integer değerinde 
        ConfSettings(self)

        
        
    def ManualSettings(self):
        #initte tanımladığımız alanlar kullanıcı tarafından değiştirilcekse bu şekilde 
        #aynı değişkene farklı bir değer verdik
        self.line_cylinder_default=int(self.window_conf.ui.line_cylinder_default.text())
        
        
        

    def receive(self):
        """
        Under a worker object we making continuasly process not to be affected by OS thread
        At the end of function we trigger self.updated_parameters() .
        """
        

        worker = Worker()
        self.threadpool.start(worker)
        self.date = QtCore.QDateTime.currentDateTime()
        self.serial.open(QtCore.QIODevice.ReadWrite)
        
        while self.serial.canReadLine():
            
            logger.info(self.serial.open(QtCore.QIODevice.ReadWrite))
            self.data = self.serial.readLine().data().decode("utf-8")
            self.alist = self.data.split(':')
            self.alist = self.alist[:-1]
            self.datamap=map(int,self.alist)
            self.datalist=list(self.datamap)
            logger.info("Receive fonksiyonu datalist : %s",self.datalist)
            
            self.updated_parameters()
            
        

    def updated_parameters(self):
        """
        Arduniodan gelen veriler bu fonksiyon altında güncellenecektir.
        Değişmesini istediğin isim alanını untitled dki isme göre çağır
        Örnek:: self.window_conf.ui.label_10.setText(str(self.a))
        """
        self.VeriPlaces()#En altta ekranda güncellenen labelleri bu şekilde koyduk
        AlarmDurumu(self)#degiskenler.AlarmDurumu(self)  bakmak için çağrılan dosyaya git

    def update_monitoring(self,text="blank"):
        #Eğer alarmlık bir durum varsa AlarmDurumu(self) fonksiyonu bu fonksiyonu trigger ediyor.
        self.item =QtWidgets.QListWidgetItem()
        self.window_conf.ui.listWidget.addItem(self.item)
        self.item = self.window_conf.ui.listWidget.item(self.indexItem)  # isim alanına dikkat et
        self.item.setText(text)
        self.item.setIcon(QtGui.QIcon(self.icon_hint))
        self.indexItem =1+ self.indexItem
        
    def Deviation(self,a,b):
        return range(a,b)

    def doubleClickItem(self):
        #ilk elemana tıklandığında çökme yapıyordu onu fixlemek için boş döndürdüm
        if self.window_conf.ui.listWidget.currentItem().text()[:3]=="0.0":
            return
        
        infoitemdata=self.window_conf.ui.listWidget.currentItem().text()
        infoitemdata=infoitemdata[:3]
        infoitemdata=infoitemdata.split(".")
        self.datamap=map(int,infoitemdata)
        self.datalist=list(self.datamap)
        self.bilgi=self.veritabanı[self.datalist[0]][self.datalist[1]]
        self.ShowItemMenu()
    def ShowItemMenu(self):
        self.mydialog=MyDialog()
        self.mydialog.ui.label.setText(self.bilgi)
        self.mydialog.show()


    def VeriPlaces(self):
        self.window_conf.ui.lab_c1.setText(str(self.datalist[0]))
        self.window_conf.ui.lab_c2.setText(str(self.datalist[1]))
        self.window_conf.ui.lab_c3.setText(str(self.datalist[2]))
        self.window_conf.ui.lab_c4.setText(str(self.datalist[3]))
        self.window_conf.ui.lab_c5.setText(str(self.datalist[4]))
        self.window_conf.ui.lab_c6.setText(str(self.datalist[5]))
        self.window_conf.ui.lab_c7.setText(str(self.datalist[6]))
        self.window_conf.ui.lab_c8.setText(str(self.datalist[7]))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())