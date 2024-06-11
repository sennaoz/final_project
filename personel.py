class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        # Personel sınıfının yapıcı metodu. Personelin numarasını, adını, soyadını, departmanını ve maaşını alır ve atar.
        self.__personel_no = personel_no  # Personel numarasını özel (private) bir değişken olarak saklar.
        self.__ad = ad  # Personelin adını özel bir değişken olarak saklar.
        self.__soyad = soyad  # Personelin soyadını özel bir değişken olarak saklar.
        self.__departman = departman  # Personelin çalıştığı departmanı özel bir değişken olarak saklar.
        self.__maas = maas  # Personelin maaşını özel bir değişken olarak saklar.

        # Personel numarasını döndüren getter metodu.
        def get_personel_no(self):
            return self.__personel_no
        
        # Personel numarasını ayarlayan setter metodu.
        def set_personel_no(self, personel_no):
            self.__personel_no = personel_no

        # Personelin adını döndüren getter metodu.
        def get_ad(self):
            return self.__ad
        
        # Personelin adını ayarlayan setter metodu.
        def set_ad(self, ad):
            self.__ad = ad
        
        # Personelin soyadını döndüren getter metodu.
        def get_soyad(self):
            return self.__soyad
        
        # Personelin soyadını ayarlayan setter metodu.
        def set_soyad(self, soyad):
            self.__soyad = soyad

        # Personelin çalıştığı departmanı döndüren getter metodu.
        def get_departman(self):
            return self.__departman
        
        # Personelin çalıştığı departmanı ayarlayan setter metodu.
        def set_departman(self, departman):
            self.__departman = departman
        
        # Personelin maaşını döndüren getter metodu.
        def get_maas(self):
            return self.__maas
        
        # Personelin maaşını ayarlayan setter metodu.
        def set_maas(self, maas):
            self.__maas = maas

        # Personel bilgilerini anlamlı bir string formatında döndüren özel __str__ metodu.
        def __str__(self):
            return f"Personel No: {self.__personel_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Departman: {self.__departman}, Maas: {self.__maas}"
