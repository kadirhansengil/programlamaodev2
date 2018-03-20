# programlamaodev2
#1.soru
def kdCiro(x,y,z,a,s):
    kdCiro=x-(y+z+a+s)
    return kdCiro
x=int(input('Toplam satış miktarını giriniz:'))
y=int(input('Hammadde maliyetini giriniz:'))
z=int(input('Bakım onarım giderlerini giriniz:'))
a=int(input('Sevkiyat giderlerini giriniz:'))
s=int(input('Satın alınan hizmet giderlerini giriniz:'))
k=kdCiro(x,y,z,a,s)
print('Katma Değer Cironuz:',k)
if(k)>1000:
    print('Katma Değer Cironuz Yüksek')
elif(k)<500:
    print('Katma Değer Cironuz Düşük')
else:
    print('Katma Değer Cironuz Normal')

#2.soru
def mcSuresi16(x,y):
    mcSuresi16=x/y
    return mcSuresi16
x=int(170)
y=int(50)
m=mcSuresi16(x,y)
print('2016 Yılı Müşterilerle Çalışma Süreniz:',m)
def mcSuresi17(a,s):
    mcSuresi17=a/s
    return mcSuresi17
a=int(220)
s=int(70)
k=mcSuresi17(a,s)
print('2017 Yılı Müşterilerle Çalışma Süreniz:',k)
def mcFarkı(m,k):
    mcFarkı=k-m
    return mcFarkı
f=mcFarkı(m,k)
print('2017 ve 2016 Yılları Arasındaki Müşterilerle Çalışma Süresi Farkı:',f)

#3.soru
def ilk6Aygelir(x,y,z):
    ilk6Aygelir=(x+y+z)
    return ilk6Aygelir
x=int(input('Yazılım Gelirini Giriniz:'))
y=int(input('Finansman Gelirini Giriniz:'))
z=int(input('Ürün Satış Gelirini Giriniz:'))
k=ilk6Aygelir(x,y,z)
print('İlk 6 Aylık Geliriniz:',k)
def ilk6Aygider(a,s,d):
    ilk6Aygider=a+s+d
    return ilk6Aygider
a=int(input('Çalışan Maaşlarını Giriniz:'))
s=int(input('Kira Giderlerini Giriniz:'))
d=int(input('Donanım Maliyetini Giriniz:'))
g=ilk6Aygider(a,s,d)
print('İlk 6 Aylık Gideriniz:',g)
def ilk6Aykar(k,g):
    ilk6Aykar=k-g
    return ilk6Aykar
r=ilk6Aykar(k,g)
print('İlk 6 Aylık Karınız:',r)
def son6Aygelir(x,y,z,a):
    son6Aygelir=x+y+z+a
    return son6Aygelir
x=int(input('Yazılım Gelirinizi Giriniz:'))
y=int(input('Sponsorluk Gelirini Giriniz:'))
z=int(input('Ürün Satış Gelirini Giriniz:'))
a=int(input('E Ticaret Gelirinizi Giriniz:'))
c=son6Aygelir(x,y,z,a)
print('Son 6 Aylık Geliriniz:',c)
def son6Aygider(x,y,z):
    son6Aygider=x+y+z
    return son6Aygider
x=int(input('Çalışan Maaşlarını Giriniz:'))
y=int(input('Kira Giderlerini Giriniz:'))
z=int(input('Donanım Maliyetini Giriniz:'))
v=son6Aygider(x,y,z)
print('İlk 6 Aylık Gideriniz:',v)
def son6Aykar(c,v):
    son6Aykar=c-v
    return son6Aykar
b=son6Aykar(c,v)
print('Son 6 Aylık Karınız:',b)
if r-b>5000:
    print("İşletme Çok Karlı")
elif 1000<r-b<5000:
    print('İşletme Karı Normal')
else:
    print('İşletme Yeterince Karda Değil')
    
#4.soru
def donembasıStok(x,y,z):
    global basStok
    basStok=x+y+z
    return basStok
x=int(input("Dönem Başı Koltuk Sayınız:"))
y=int(input("Dönem Başı Yatak Sayısınız:"))
z=int(input("Dönem Başı Dolap Sayınız:"))
k=donembasıStok(x,y,z)
print("Dönembaşı Stoğunuz:",k)
def donemsonuStok(x,y,z):
    sonStok=(x+15)+(y+5)+(z+5)
    return sonStok

b=donemsonuStok(x,y,z)
print("Dönemsonu Stoğunuz:",b)
def ortalamaStok(k,b):
    ortStok=(k+b)/2
    return ortStok
r=ortalamaStok(k,b)
print("1 Yıllık Ortalama Stoğunuz:",r)






