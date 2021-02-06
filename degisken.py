import logging
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

def ConfSettings(self):
        #Kullanıcı Deviation QLineEdit girişlerini değişken ataması ile tutuyoruz 
        #self.SEAWATERTEMP_Deviation=self.window_conf.ui.lineEdit.text()
        if self.window_conf.ui.line_c1.text():
            self.Cyl1=int(self.window_conf.ui.line_c1.text())
        else:
            self.Cyl1="0"

        if self.window_conf.ui.line_c2.text():
            self.Cyl2=int(self.window_conf.ui.line_c2.text())
        else:
            self.Cyl2="0"
        if self.window_conf.ui.line_c3.text():
            self.Cyl3=int(self.window_conf.ui.line_c3.text())
        else:
            self.Cyl3="0"
        if self.window_conf.ui.line_c4.text():
            self.Cyl4=int(self.window_conf.ui.line_c4.text())
        else:
            self.Cyl4="0"
        if self.window_conf.ui.line_c5.text():
            self.Cyl5=int(self.window_conf.ui.line_c5.text())
        else:
            self.Cyl5="0"
        if self.window_conf.ui.line_c6.text():
            self.Cyl6=int(self.window_conf.ui.line_c6.text())
        else:
            self.Cyl6="0"
        if self.window_conf.ui.line_c7.text():
            self.Cyl7=int(self.window_conf.ui.line_c7.text())
        else:
            self.Cyl7="0"
        if self.window_conf.ui.line_c8.text():
            self.Cyl8=int(self.window_conf.ui.line_c8.text())
        else:
            self.Cyl8="0"


def AlarmDurumu(self):
    """
    Herbir modül için eklenmesi gerekenler::
    min ve maxlar ve ona denk gelen Main.py deki değerleri
    self.datalist::İtemleri  text="" ile eklediğimizde başındaki numaralara göre veri tabanı yerini gösteriyo.
    """
    #--------------------  CYLİNDER 1
    self.min_c1=self.line_cylinder_default-self.Cyl1
    self.max_c1=self.line_cylinder_default+self.Cyl1
    if self.datalist[0] in self.Deviation(self.min_c1,self.max_c1):
        logger.info("Değer aralığın içinde")
        self.window_conf.ui.lab_icon.setPixmap(self.icon_succ)
    elif self.datalist[0] > self.max_c1:
        logger.info("Üstünde değer")
        self.window_conf.ui.lab_icon.setPixmap(self.icon_error)
    else:
        logger.info("Altında bir değer")
        self.window_conf.ui.lab_icon.setPixmap(self.icon_error)
        self.update_monitoring(text="4.2 silindir 1 Altında değer   :" + self.veritabanı[4][2])
    #------------------CYLINDER 2
    
    self.min_c2=self.line_cylinder_default-self.Cyl2
    self.max_c2=self.line_cylinder_default+self.Cyl2
    if self.datalist[0] in self.Deviation(self.min_c2,self.max_c2):
        logger.info("2 Değer aralığın içinde")
        self.window_conf.ui.lab_icon.setPixmap(self.icon_succ)
    elif self.datalist[0] > self.max_c2:
        logger.info("2 Üstünde değer")
        self.window_conf.ui.lab_icon.setPixmap(self.icon_error)
    else:
        logger.info("2 Altında bir değer")
        self.window_conf.ui.lab_icon.setPixmap(self.icon_error)
        self.update_monitoring(text="5.3 SİLİNDİR 2 Altında değer   :" + self.veritabanı[5][3])