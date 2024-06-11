class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        # Hasta sınıfının yapıcı metodu, hastanın numarasını, adını, soyadını, doğum tarihini, hastalığını ve tedavisini alır ve atar.
        self.__hasta_no = hasta_no  # Hastanın numarasını özel (private) bir değişken olarak saklar.
        self.__ad = ad  # Hastanın adını özel bir değişken olarak saklar.
        self.__soyad = soyad  # Hastanın soyadını özel bir değişken olarak saklar.
        self.__dogum_tarihi = dogum_tarihi  # Hastanın doğum tarihini özel bir değişken olarak saklar.
        self.__hastalik = hastalik  # Hastanın hastalığını özel bir değişken olarak saklar.
        self.__tedavi = tedavi  # Hastanın tedavisini özel bir değişken olarak saklar.

        # Hastanın numarasını döndüren getter metodu.
        def get_hasta_no(self):
            return self.__hasta_no
        
        # Hastanın numarasını ayarlayan setter metodu.
        def set_hasta_no(self, hasta_no):
            self.__hasta_no = hasta_no
        
        # Hastanın adını döndüren getter metodu.
        def get_ad(self):
            return self.__ad
        
        # Hastanın adını ayarlayan setter metodu.
        def set_ad(self, ad):
            self.__ad = ad

        # Hastanın soyadını döndüren getter metodu.
        def get_soyad(self):
            return self.__soyad
        
        # Hastanın soyadını ayarlayan setter metodu.
        def set_soyad(self, soyad):
            self.__soyad = soyad
        
        # Hastanın doğum tarihini döndüren getter metodu.
        def get_dogum_tarihi(self):
            return self.__dogum_tarihi
        
        # Hastanın doğum tarihini ayarlayan setter metodu.
        def set_dogum_tarihi(self, dogum_tarihi):
            self.__dogum_tarihi = dogum_tarihi
        
        # Hastanın hastalığını döndüren getter metodu.
        def get_hastalik(self):
            return self.__hastalik
        
        # Hastanın hastalığını ayarlayan setter metodu.
        def set_hastalik(self, hastalik):
            self.__hastalik = hastalik

        # Hastanın tedavisini döndüren getter metodu.
        def get_tedavi(self):
            return self.__tedavi
        
        # Hastanın tedavisini ayarlayan setter metodu.
        def set_tedavi(self, tedavi):
            self.__tedavi = tedavi

        # Tedavi süresini hesaplayan metot. Burada örnek olarak tedavi uzunluğunun iki katı kadar süre hesaplanıyor.
        def tedavi_suresi_hesapla(self):
            return len(self.__tedavi) * 2  
        
        # Hastanın bilgilerini anlamlı bir string formatında döndüren özel __str__ metodu.
        def __str__(self):
            return f"Hasta No: {self.__hasta_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"
