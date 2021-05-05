import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ConfSettings(self):
    # Eğer kullanıcı deviation girerse girdiği değeri alıcaz
    # Eğer girmesse default olan 0 ı kabul edicez
    if self.window_conf.ui.line_c1.text():
        self.Cyl1 = int(self.window_conf.ui.line_c1.text())
    else:
        self.Cyl1 = 0  # özellikle int bıraktım yoksa boş bırakırsa hata veriyor.

    if self.window_conf.ui.line_c2.text():
        self.Cyl2 = int(self.window_conf.ui.line_c2.text())
    else:
        self.Cyl2 = 0
    if self.window_conf.ui.line_c3.text():
        self.Cyl3 = int(self.window_conf.ui.line_c3.text())
    else:
        self.Cyl3 = 0
    if self.window_conf.ui.line_c4.text():
        self.Cyl4 = int(self.window_conf.ui.line_c4.text())
    else:
        self.Cyl4 = 0
    if self.window_conf.ui.line_c5.text():
        self.Cyl5 = int(self.window_conf.ui.line_c5.text())
    else:
        self.Cyl5 = 0
    if self.window_conf.ui.line_c6.text():
        self.Cyl6 = int(self.window_conf.ui.line_c6.text())
    else:
        self.Cyl6 = 0
    if self.window_conf.ui.line_c7.text():
        self.Cyl7 = int(self.window_conf.ui.line_c7.text())
    else:
        self.Cyl7 = 0
    if self.window_conf.ui.line_c8.text():
        self.Cyl8 = int(self.window_conf.ui.line_c8.text())
    else:
        self.Cyl8 = 0


def Settings(self):
    if self.window_conf.ui.line_cylinder_default.text():
        self.line_cylinder_default = int(self.window_conf.ui.line_cylinder_default.text())
    else:
        self.line_cylinder_default = 0
    # self.line_cylinder_default = int(self.window_conf.ui.line_cylinder_default.text())


def AlarmDurumu(self):
    #Farklı makineler için kullanılacak yapıcı fonksiyonumuz
    #gereksiz if elseden kurtulduk
    # ilk çalıştırmada gelen veri 0 olacağı için tüm işleyişi if durumuna göre çalıştırıyoruz.
    def deneme(default, gercek, datalist, ikon, db):
        self.min = default - gercek
        self.max = default + gercek
        if default != 0:
            if datalist in self.Deviation(self.min, self.max):
                logger.info("2 Değer aralığın içinde")
                ikon.setPixmap(self.icon_succ)
            elif datalist > self.max:
                logger.info("2 Üstünde değer" + str(default))
                ikon.setPixmap(self.icon_error)
                self.update_monitoring(text=str(db[0])+"."+str(db[1])+"SİLİNDİR 2 Üstünde değer   :" + self.veritabani[db[0]][db[1]])
            elif datalist < self.min:
                logger.info("2 Altında değer")
                ikon.setPixmap(self.icon_error)
                self.update_monitoring(text=str(db[0])+"."+str(db[1])+" SİLİNDİR 2 Altında değer   :" + self.veritabani[db[0]][db[1]])
            else:
                logger.info("ELse durumu çalıştı hata oluştu.")
                ikon.setPixmap(self.icon_error)
        else:
            # artık ilk açıldığında hata simgesi gözükmüyor bug mu özellik mi hadi bakim :D
            logger.info("gelen değer 0")
            ikon.setPixmap(self.icon_error)

    """
    Herbir modül için eklenmesi gerekenler::
    min ve maxlar ve ona denk gelen Main.py deki değerleri
    self.datalist::İtemleri  text="" ile eklediğimizde başındaki numaralara göre veri tabanı yerini gösteriyo.
    """

    deneme(self.line_cylinder_default, self.Cyl1, self.datalist[0], self.window_conf.ui.lab_icon, db=[4, 2])
    deneme(self.line_cylinder_default, self.Cyl2, self.datalist[1], self.window_conf.ui.lab_icon_2, db=[5, 3])
    # Geliştirme aşamasında... şuana kadar hata almadım aşağıdaki yapıda diğer makineler eklenebilir silindirler için...
    deneme(self.line_cylinder_default, self.Cyl3, self.datalist[2], self.window_conf.ui.lab_icon_3, db=[6, 2])
    deneme(self.line_cylinder_default, self.Cyl4, self.datalist[3], self.window_conf.ui.lab_icon_4, db=[6, 2])
    deneme(self.line_cylinder_default, self.Cyl5, self.datalist[4], self.window_conf.ui.lab_icon_5, db=[6, 2])
    deneme(self.line_cylinder_default, self.Cyl6, self.datalist[5], self.window_conf.ui.lab_icon_6, db=[6, 2])
    deneme(self.line_cylinder_default, self.Cyl7, self.datalist[6], self.window_conf.ui.lab_icon_7, db=[6, 2])
    deneme(self.line_cylinder_default, self.Cyl8, self.datalist[7], self.window_conf.ui.lab_icon_8, db=[6, 2])
