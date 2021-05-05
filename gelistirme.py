while self.serial.canReadLine():
    # gelen veriyi denetleyip bağlantı kontrolü yap.
    logger.info(self.serial.open(QtCore.QIODevice.ReadWrite))
    self.data = self.serial.readLine().data().decode("utf-8")
    self.alist = self.data.split(':')
    self.alist = self.alist[:-1]
    self.datamap = map(int, self.alist)
    self.datalist = list(self.datamap)
    logger.info("Receive fonksiyonu datalist : %s", self.datalist)

    self.updated_parameters()


    except UnicodeDecodeError:
    logger.info("İlk bağlantıda bir hata oldu")
    self.window_conf.ui.frame_2.setStyleSheet("background-color:red;\n"
                                              "border-radius:15px;")