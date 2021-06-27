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
    ######################### Seperator Girdileri ##########################
    if self.window_conf.ui.line_feedPump.text():
        self.line_feedPump = int(self.window_conf.ui.line_feedPump.text())
    else:
        self.line_feedPump = 0
    if self.window_conf.ui.line_afterFilter.text():
        self.line_afterFilter = int(self.window_conf.ui.line_afterFilter.text())
    else:
        self.line_afterFilter = 0
    if self.window_conf.ui.line_sealWater.text():
        self.line_sealWater = int(self.window_conf.ui.line_sealWater.text())
    else:
        self.line_sealWater = 0
    if self.window_conf.ui.line_openingWater.text():
        self.line_openingWater = int(self.window_conf.ui.line_openingWater.text())
    else:
        self.line_openingWater = 0
    if self.window_conf.ui.line_inputSeperator.text():
        self.line_inputSeperator = int(self.window_conf.ui.line_inputSeperator.text())
    else:
        self.line_inputSeperator = 0
    if self.window_conf.ui.line_closeWater.text():
        self.line_closeWater = int(self.window_conf.ui.line_closeWater.text())
    else:
        self.line_closeWater = 0
    if self.window_conf.ui.line_cleanFuelOutput.text():
        self.line_cleanFuelOutput = int(self.window_conf.ui.line_cleanFuelOutput.text())
    else:
        self.line_cleanFuelOutput = 0
    if self.window_conf.ui.line_fuelTemperature.text():
        self.line_fuelTemperature = int(self.window_conf.ui.line_fuelTemperature.text())
    else:
        self.line_fuelTemperature = 0







def Settings(self):
    if self.window_conf.ui.line_cylinder_default.text():
        self.line_cylinder_default = int(self.window_conf.ui.line_cylinder_default.text())
    else:
        self.line_cylinder_default = 0
    if self.window_conf.ui.line_hfo_default.text():
        self.line_hfo_default = int(self.window_conf.ui.line_hfo_default.text())
    else:
        self.line_hfo_default = 0
    if self.window_conf.ui.line_do_default.text():
        self.line_do_default = int(self.window_conf.ui.line_do_default.text())
    else:
        self.line_do_default = 0
    ############### Separator Defaults ###########33
    if self.window_conf.ui.default_feedPump.text():
        self.default_feedPump = int(self.window_conf.ui.default_feedPump.text())
    else:
        self.default_feedPump = 0
    if self.window_conf.ui.default_afterFilter.text():
        self.default_afterFilter = int(self.window_conf.ui.default_afterFilter.text())
    else:
        self.default_afterFilter = 0
    if self.window_conf.ui.default_sealWater.text():
        self.default_sealWater = int(self.window_conf.ui.default_sealWater.text())
    else:
        self.default_sealWater = 0
    if self.window_conf.ui.default_openingWater.text():
        self.default_openingWater = int(self.window_conf.ui.default_openingWater.text())
    else:
        self.default_openingWater = 0
    if self.window_conf.ui.default_inputSeperator.text():
        self.default_inputSeperator = int(self.window_conf.ui.default_inputSeperator.text())
    else:
        self.default_inputSeperator = 0
    if self.window_conf.ui.default_closeWater.text():
        self.default_closeWater = int(self.window_conf.ui.default_closeWater.text())
    else:
        self.default_closeWater = 0
    if self.window_conf.ui.default_cleanFuelOutput.text():
        self.default_cleanFuelOutput = int(self.window_conf.ui.default_cleanFuelOutput.text())
    else:
        self.default_cleanFuelOutput = 0
    if self.window_conf.ui.default_fuelTemperature.text():
        self.default_fuelTemperature = int(self.window_conf.ui.default_fuelTemperature.text())
    else:
        self.default_fuelTemperature = 0
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
            # ....
            logger.info("gelen değer 0")
            ikon.setPixmap(self.icon_error)

    """
    Herbir modül için eklenmesi gerekenler::
    min ve maxlar ve ona denk gelen Main.py deki değerleri
    self.datalist::İtemleri  text="" ile eklediğimizde başındaki numaralara göre veri tabanı yerini gösteriyo.
    """

    deneme(self.line_cylinder_default, self.Cyl1, self.datalist[0], self.window_conf.ui.lab_icon, db=[4, 2])
    deneme(self.line_cylinder_default, self.Cyl2, self.datalist[1], self.window_conf.ui.lab_icon_2, db=[5, 3])
    deneme(self.line_cylinder_default, self.Cyl3, self.datalist[2], self.window_conf.ui.lab_icon_3, db=[1, 2])
    deneme(self.line_cylinder_default, self.Cyl4, self.datalist[3], self.window_conf.ui.lab_icon_4, db=[3, 2])
    deneme(self.line_cylinder_default, self.Cyl5, self.datalist[4], self.window_conf.ui.lab_icon_5, db=[5, 2])
    deneme(self.line_cylinder_default, self.Cyl6, self.datalist[5], self.window_conf.ui.lab_icon_6, db=[3, 2])
    deneme(self.line_cylinder_default, self.Cyl7, self.datalist[6], self.window_conf.ui.lab_icon_7, db=[5, 2])
    deneme(self.line_cylinder_default, self.Cyl8, self.datalist[7], self.window_conf.ui.lab_icon_8, db=[4, 2])
    # seperator modül kayıtları
    deneme(self.default_feedPump, self.line_feedPump, self.datalist[8], self.window_conf.ui.lab_icon_10, db=[6, 2])
    deneme(self.default_inputSeperator, self.line_inputSeperator, self.datalist[9], self.window_conf.ui.lab_icon_10, db=[9, 2])
    deneme(self.default_closeWater, self.line_closeWater, self.datalist[10], self.window_conf.ui.lab_icon_10, db=[8, 2])
    deneme(self.default_afterFilter, self.line_afterFilter, self.datalist[11], self.window_conf.ui.lab_icon_10, db=[7, 2])
    deneme(self.default_sealWater, self.line_sealWater, self.datalist[12], self.window_conf.ui.lab_icon_10, db=[10, 2])
    deneme(self.default_openingWater, self.line_openingWater, self.datalist[13], self.window_conf.ui.lab_icon_10, db=[7, 2])
    deneme(self.default_cleanFuelOutput, self.line_cleanFuelOutput, self.datalist[14], self.window_conf.ui.lab_icon_10, db=[9, 2])
    deneme(self.default_fuelTemperature, self.line_fuelTemperature, self.datalist[15], self.window_conf.ui.lab_icon_10, db=[6, 2])
