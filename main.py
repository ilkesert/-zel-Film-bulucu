import webbrowser
import requests
from bs4 import BeautifulSoup

print("hangi tür film izlemek istiyorsunuz")
print(" Animasyon, Aile, Belgesel, Bilimkurgu, Blu ray, Çizgifilm, Dram, Fantastik,Gerilim, Gizem, Hindistan, Komedi, Korku, Macera, Polisiye, Psikoloji, Romantik, Savaş, Suç, Tarih, Batılı tarz, Yerli, Yeşilçam, Üç boyutlu")
filmturu = input("Yukarıdaki türlerden hangisinden film izlemek istersiniz ?")

if filmturu == "Animasyon":
    filmturu1 = str(4)
elif filmturu == "Aile":
    filmturu1 = str(32)
elif filmturu == "Belgesel":
    filmturu1 = str(25)
elif filmturu == "Bilimkurgu" or "Bilim kurgu":
    filmturu1 = str(5)
elif filmturu == "Blu Ray":
    filmturu1 = str(23)
elif filmturu == "Çizgifilm" or "Çizgi film":
    filmturu1 = str(20)
elif filmturu == "Dram":
    filmturu1 = str(6)
elif filmturu == "Fantastik":
    filmturu1 = str(7)
elif filmturu == "Gerilim":
    filmturu1 = str(8)
elif filmturu == "Gizem":
    filmturu1 = str(34)
elif filmturu == "Hindistan":
    filmturu1 = str(28)
elif filmturu == "Komedi":
    filmturu1 = str(9)
elif filmturu == "Korku":
    filmturu1 = str(10)
elif filmturu == "Macera":
    filmturu1 = str(11)
elif filmturu == "Polisiye":
    filmturu1 = str(12)
elif filmturu == "Psikoloji":
    filmturu1 = str(13)
elif filmturu == "Romantik":
    filmturu1 = str(14)
elif filmturu == "Savaş":
    filmturu1 = str(15)
elif filmturu == "Suç":
    filmturu1 = str(31)
elif filmturu == "Tarih":
    filmturu1 = str(33)
elif filmturu == "Batılı tarz":
    filmturu1 = str(16)
elif filmturu == "Yerli":
    filmturu1 = str(18)
elif filmturu == "Yeşilçam":
    filmturu1 = str(21)
elif filmturu == "Üç Boyutlu":
    filmturu1 = str(24)
print("Madem tür seçtin peki türkçe dublaj mı altyazılı mı olsun ? Altyazılı ise 'Altyazı' Türkçe dublaj ise 'Dublaj' yazınız")
diltercihi = input("Lütfen giriş yapınız")

if diltercihi == "Dublaj":
    diltercihi = "td"
elif diltercihi == "Altyazı":
    diltercihi = "ay"

print("Pekala şimdi de puanlamasını yapalım kaç puan üstü istersiniz 3 ila 9 arası giriş yapınız")
puanlama = str(input("Giriş yapınız"))
print("Hangi yıla ait Film izlemek isteriniz 2021 ile 1980 arası bir yıl seçiniz eğer daha öncesini isterseniz 'Eski Çağ' yazınız")
yili = str(input("Giriş yapınız "))
print("Son olarak görüntünüz HD olsun mu olmasın mı")
netlik = input("HD isterseniz HD yazınız diğeri ise Diğer yazınız")

if netlik == "HD":
    netlik1 = str(1)
else:
    netlik1 = str(0)

webbrowser.open_new_tab("https://www.fullhdfilmizlesene.com/filmrobot/?tarz="+diltercihi+"&tur="+filmturu1+"&yil="+yili+"&imdb="+puanlama+"x&hd=" +netlik1)




