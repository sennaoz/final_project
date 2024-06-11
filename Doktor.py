from Personel import Personel  # Personel sınıfını içe aktarır

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        # Doktor sınıfının kurucusu, Personel sınıfının kurucusunu çağırır ve ek özellikler tanımlar
        super().__init__(personel_no, ad, soyad, departman, maas)  # Personel sınıfının kurucusunu çağırır
        self.__uzmanlik = uzmanlik  # Uzmanlık alanını belirler
        self.__deneyim_yili = deneyim_yili  # Deneyim yılı alanını belirler
        self.__hastane = hastane  # Hastane alanını belirler

    def get_uzmanlik(self):
        # Uzmanlık alanını döndürür
        return self.__uzmanlik
    
    def get_deneyim_yili(self):
        # Deneyim yılı alanını döndürür
        return self.__deneyim_yili

    def get_hastane(self):
        # Hastane alanını döndürür
        return self.__hastane
    
    def set_hastane(self, hastane):
        # Hastane alanını ayarlar
        self.__hastane = hastane

    def set_uzmanlik(self, uzmanlik):
        # Uzmanlık alanını ayarlar
        self.__uzmanlik = uzmanlik
    
    def set_deneyim_yili(self, deneyim_yili):
        # Deneyim yılı alanını ayarlar
        self.__deneyim_yili = deneyim_yili

    def maas_arttir(self, oran):
        # Maaşı belirli bir oranla artırır
        yeni_maas = self.get_maas() * (1 + oran / 100)  # Yeni maaşı hesaplar
        self.set_maas(yeni_maas)  # Yeni maaşı ayarlar

    def __str__(self):
        # Doktor nesnesinin string temsilini döndürür
        return f"{super().__str__()}, Uzmanlık: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane}"
