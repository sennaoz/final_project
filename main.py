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
