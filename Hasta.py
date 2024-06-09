class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

        def get_hasta_no(self):
            return self.__hasta_no
        def set_hasta_no(self, hasta_no):
            self.__hasta_no = hasta_no
        
        def get_ad(self):
            return self.__ad
        def set_ad(self, ad):
            self.__ad = ad

        def get_soyad(self):
            return self.__soyad
        def set_soyad(self, soyad):
            self.__soyad = soyad

    