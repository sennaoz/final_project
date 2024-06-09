import Personel
class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

        def get_calisma_saati(self):
            return self.__calisma_saati
        def set_calisma_saati(self, calisma_saati):
            self.__calisma_saati = calisma_saati
            
        def get_sertifika(self):
            return self.__sertifika
        def set_sertifika(self, sertifika):
            self.__sertifika = sertifika