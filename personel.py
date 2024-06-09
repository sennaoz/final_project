class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas
#class personel oluşturuldu
        def get_personel_no(self):
            return self.__personel_no
        def set_personel_no(self, personel_no):
            self.__personel_no = personel_no