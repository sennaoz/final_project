import pandas as pd  # Pandas kütüphanesini içe aktarır
from Personel import Personel  # Personel sınıfını içe aktarır
from Doktor import Doktor  # Doktor sınıfını içe aktarır
from Hemsire import Hemsire  # Hemsire sınıfını içe aktarır
from Hasta import Hasta  # Hasta sınıfını içe aktarır

def personel_bilgileri_iste():
    # Personel bilgilerini kullanıcıdan alır
    personel_no = input("No: ")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    departman = input("Departman: ")
    maas = float(input("Maaş: "))
    return personel_no, ad, soyad, departman, maas

def doktor_bilgileri_iste():
    # Doktor bilgilerini kullanıcıdan alır
    print("Doktor Bilgilerini Gir")
    personel_no, ad, soyad, departman, maas = personel_bilgileri_iste()
    uzmanlik = input("Uzmanlık: ")
    deneyim_yili = int(input("Deneyim Yılı: "))
    hastane = input("Hastane: ")
    return personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane

def hemsire_bilgileri_iste():
    # Hemşire bilgilerini kullanıcıdan alır
    print("Hemşire Bilgilerini Gir")
    personel_no, ad, soyad, departman, maas = personel_bilgileri_iste()
    calisma_saati = int(input("Çalışma Saati: "))
    sertifika = input("Sertifika: ")
    hastane = input("Hastane: ")
    return personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane

def hasta_bilgileri_iste():
    # Hasta bilgilerini kullanıcıdan alır
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
        data = []  # Boş bir liste oluşturur
        for personel in personeller:
            # Personel bilgilerini listeye ekler
            data.append([
                personel.get_personel_no(),
                personel.get_ad(),
                personel.get_soyad(),
                personel.get_departman(),
                personel.get_maas(),
                getattr(personel, 'get_uzmanlik', lambda: 0)(),  # Uzmanlık bilgisi
                getattr(personel, 'get_deneyim_yili', lambda: 0)(),  # Deneyim yılı
                getattr(personel, 'get_hastane', lambda: 0)(),  # Hastane bilgisi
                getattr(personel, 'get_calisma_saati', lambda: 0)(),  # Çalışma saati
                getattr(personel, 'get_sertifika', lambda: 0)(),  # Sertifika bilgisi
                0, 0, 0  # Hasta sütunları için boş değerler
            ])

        for hasta in hastalar:
            # Hasta bilgilerini listeye ekler
            data.append([
                hasta.get_hasta_no(),
                hasta.get_ad(),
                hasta.get_soyad(),
                0, 0, 0, 0, 0, 0, 0,
                hasta.get_dogum_tarihi(),  # Doğum tarihi
                hasta.get_hastalik(),  # Hastalık bilgisi
                hasta.get_tedavi()  # Tedavi bilgisi
            ])

        # DataFrame oluşturur
        df = pd.DataFrame(data, columns=[
            "No", "Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yili", "Hastane",
            "Calisma Saati", "Sertifika", "Dogum Tarihi", "Hastalik", "Tedavi"
        ])

        df.fillna(0, inplace=True)  # Eksik verileri 0 ile doldurur

        # Maaşı 7000 TL üzerinde olan personeller
        print("\nMaaşı 7000 TL üzerinde olan personeller:")
        print(df[df['Maas'] > 7000])

        # Uzmanlık alanlarına göre doktor sayıları
        print("\nUzmanlık alanlarına göre doktor sayıları:")
        print(df[df['Uzmanlik'] != 0].groupby('Uzmanlik').size())

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısı
        print("\n5 yıldan fazla deneyime sahip doktorların toplam sayısı:")
        print(df[(df['Deneyim Yili'] > 5)].shape[0])

        # Hasta adına göre alfabetik sıralama
        print("\nHasta adına göre alfabetik sıralama:")
        print(df.sort_values(by='Ad'))

        # 1990 ve sonrası doğumlu hastalar
        print("\n1990 ve sonrası doğumlu hastalar:")
        print(df[pd.to_datetime(df['Dogum Tarihi'], errors='coerce') >= pd.Timestamp('1990-01-01')])

        # Yeni DataFrame oluşturma
        yeni_df = df[["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yili", "Hastalik", "Tedavi"]]
        print("\nYeni DataFrame:")
        print(yeni_df)
    except Exception as e:
        # Hata durumunda hata mesajını yazdırır
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()  # Ana fonksiyonu çalıştırır
