import pandas as pd
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def personel_bilgileri_iste():
    personel_no = input("No: ")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    departman = input("Departman: ")
    maas = float(input("Maaş: "))
    return personel_no, ad, soyad, departman, maas

def doktor_bilgileri_iste():
    print("Doktor Bilgilerini Gir")
    personel_no, ad, soyad, departman, maas = personel_bilgileri_iste()
    uzmanlik = input("Uzmanlık: ")
    deneyim_yili = int(input("Deneyim Yılı: "))
    hastane = input("Hastane: ")
    return personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane

def hemsire_bilgileri_iste():
    print("Hemşire Bilgilerini Gir")
    personel_no, ad, soyad, departman, maas = personel_bilgileri_iste()
    calisma_saati = int(input("Çalışma Saati: "))
    sertifika = input("Sertifika: ")
    hastane = input("Hastane: ")
    return personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane

def hasta_bilgileri_iste():
    print("Hasta Bilgilerini Gir")
    hasta_no = input("Hasta No: ")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    dogum_tarihi = input("Doğum Tarihi (YYYY-AA-GG): ")
    hastalik = input("Hastalık: ")
    tedavi = input("Tedavi: ")
    return hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi


def main():
    try:
        # Personel nesneleri oluşturma
        print("Personel Bilgilerini Gir")
        personel1 = Personel(*personel_bilgileri_iste())
        print("Personel Bilgilerini Gir")
        personel2 = Personel(*personel_bilgileri_iste())


        # Doktor nesneleri oluşturma
        doktor1 = Doktor(*doktor_bilgileri_iste())
        doktor2 = Doktor(*doktor_bilgileri_iste())
        doktor3 = Doktor(*doktor_bilgileri_iste())

        # Hemşire nesneleri oluşturma
        hemsire1 = Hemsire(*hemsire_bilgileri_iste())
        hemsire2 = Hemsire(*hemsire_bilgileri_iste())
        hemsire3 = Hemsire(*hemsire_bilgileri_iste())

        # Hasta nesneleri oluşturma
        hasta1 = Hasta(*hasta_bilgileri_iste())
        hasta2 = Hasta(*hasta_bilgileri_iste())
        hasta3 = Hasta(*hasta_bilgileri_iste())

        # Nesneleri listeye ekleme
        personeller = [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3]
        hastalar = [hasta1, hasta2, hasta3]

        # Personel bilgilerini yazdırma
        print("\nPersonel Bilgileri:")
        for personel in personeller:
            print(personel)

        # Hasta bilgilerini yazdırma
        print("\nHasta Bilgileri:")
        for hasta in hastalar:
            print(hasta)
        
        # Pandas DataFrame oluşturma
        data = []
        for personel in personeller:
            data.append([personel.get_personel_no(), personel.get_ad(), personel.get_soyad(), personel.get_departman(),
                         personel.get_maas(),
                         getattr(personel, 'get_uzmanlik', lambda: 0)(),
                         getattr(personel, 'get_deneyim_yili', lambda: 0)(),
                         getattr(personel, 'get_hastane', lambda: 0)(),
                         getattr(personel, 'get_calisma_saati', lambda: 0)(),
                         getattr(personel, 'get_sertifika', lambda: 0)()])

        for hasta in hastalar:
            data.append(
                [hasta.get_hasta_no(), hasta.get_ad(), hasta.get_soyad(), 0, 0, 0, 0, 0, hasta.get_dogum_tarihi(),
                 hasta.get_hastalik(), hasta.get_tedavi()])

        df = pd.DataFrame(data,
                          columns=["No", "Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yili", "Hastane",
                                   "Calisma Saati", "Sertifika", "Dogum Tarihi", "Hastalik", "Tedavi"])

        df.fillna(0, inplace=True)
        # Uzmanlık alanlarına göre doktor sayıları
        print("\nUzmanlık alanlarına göre doktor sayıları:")
        print(df[df['Uzmanlik'] != 0].groupby('Uzmanlik').size())

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısı
        print("\n5 yıldan fazla deneyime sahip doktorların toplam sayısı:")
        print(df[(df['Deneyim Yili'] > 5)].shape[0])

        # Hasta adına göre alfabetik sıralama
        print("\nHasta adına göre alfabetik sıralama:")
        print(df.sort_values(by='Ad'))

        # Maaşı 7000 TL üzerinde olan personeller
        print("\nMaaşı 7000 TL üzerinde olan personeller:")
        print(df[df['Maas'] > 7000])

        # 1990 ve sonrası doğumlu hastalar
        print("\n1990 ve sonrası doğumlu hastalar:")
        print(df[pd.to_datetime(df['Dogum Tarihi'], errors='coerce') >= pd.Timestamp('1990-01-01')])

        # Yeni DataFrame oluşturma
        yeni_df = df[["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yili", "Hastalik", "Tedavi"]]
        print("\nYeni DataFrame:")
        print(yeni_df)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


if __name__ == "__main__":
    main()
    
