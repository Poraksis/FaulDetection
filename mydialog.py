from PyQt5 import QtCore,QtGui,QtWidgets


class Ui_Dialog(object):
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400,200)
        self.label=QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20,70,360,71))
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self,Dialog):
        Dialog.setWindowTitle("Bilgilendirme")
        self.label.setText("""
        
        Bu ekran bilgilendir me amaçlı veritabanı bilgilerini göstermektedir

        Lütfen dikkate alın
        
        """)