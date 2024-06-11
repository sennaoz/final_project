import Personel

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        # Hemşire sınıfının yapıcı metodu, üst sınıf Personel'in yapıcı metodunu çağırır.
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati  # Hemşirenin çalışma saatini özel (private) bir değişken olarak saklar.
        self.__sertifika = sertifika  # Hemşirenin sertifikasını özel bir değişken olarak saklar.
        self.__hastane = hastane  # Hemşirenin çalıştığı hastaneyi özel bir değişken olarak saklar.

        # Hemşirenin çalışma saatini döndüren getter metodu.
        def get_calisma_saati(self):
            return self.__calisma_saati
        
        # Hemşirenin çalışma saatini ayarlayan setter metodu.
        def set_calisma_saati(self, calisma_saati):
            self.__calisma_saati = calisma_saati
            
        # Hemşirenin sertifikasını döndüren getter metodu.
        def get_sertifika(self):
            return self.__sertifika
        
        # Hemşirenin sertifikasını ayarlayan setter metodu.
        def set_sertifika(self, sertifika):
            self.__sertifika = sertifika
        
        # Hemşirenin çalıştığı hastaneyi döndüren getter metodu.
        def get_hastane(self):
            return self.__hastane
        
        # Hemşirenin çalıştığı hastaneyi ayarlayan setter metodu.
        def set_hastane(self, hastane):
            self.__hastane = hastane

        # Hemşirenin maaşını belirli bir oranla arttıran metot.
        def maas_arttir(self, oran):
            self.set_maas(self.get_maas() * (1 + oran / 100))

        # Hemşirenin bilgilerini anlamlı bir string formatında döndüren özel __str__ metodu.
        def __str__(self):
            return super().__str__() + f", Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
