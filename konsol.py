import os
import sys

def guncelle_denetle():
    os.system("sudo apt-get update")

def guncelle():
    os.system("sudo apt-get upgrade")

def diskleri_listele():
    os.system("sudo fdisk -l")

def takvim():
    os.system("cal")

def temizle():
    os.system("clear")


print("konsole v1.0")

while True:
    print("****************************")
    print("Güncellemeri denetle = 1")
    print("Güncelle = 2")
    print("Diskleri listele = 3")
    print("Takvimi göster   = 4")
    print("Temizlemek için  = 5")
    print("Çıkmak için = q")
    print("****************************")
    islem = input("İşleminizi belirtin:")
    if islem == "1":
        guncelle_denetle()

    elif islem == "2":
        guncelle()

    elif islem == "3":
        diskleri_listele()

    elif islem == "4":
        takvim()

    elif islem == "5":
        temizle()

    elif islem == "q" or "Q":
        print("Çıkış yapıldı.")
        break

    else:
        print("Tekrar dene...")


	
