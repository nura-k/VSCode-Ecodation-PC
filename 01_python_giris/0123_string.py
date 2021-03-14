"""
a="A"
b="B"
c="C"
yazdır=a + b + c
print(yazdır)"""

"""
print("istanbul"*3)
print("-"*50)"""

"""
okulTuru="ATP"
seviye=11
print(okulTuru + " "+ str(seviye))
"""

"""
rakam=int(input("lütfen 0-9 arası sayı giriniz:\t"))
print("girdiğiniz rakamın bir fazlası {}".format(rakam+1))
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam+1)))
"""

"""
s1= int(input("lütfen sayı giriniz:"))
s2= int(input("lütfen sayı giriniz:"))
print(f"girdiğiniz sayıların toplamı {s1+s2}")
print(f"girdiğiniz sayıların toplamı {s1}+{s2}={s1+s2}")
"""
"""
s1 = int(input("lütfen 1 sayı giriniz:"))
s2= int(input("lütfen 2. sayıyı giriniz:"))
s3= int(input("lütfen 3. sayıyı giriniz:"))
print(f"{4},{6},{8} sayıların ortalaması {((s1+s2+s3)/3)}")"""


print(
    """
    leylek uygulamasına hoş geldiniz!!
    sürüş ücreti = 0.59/dk
    """
)
s = int(input("sürüş için geçen süre(saat)\t\t:"))
d = int(input("sürüş için geçen süre(dakika)\t\t:"))
toplamDakika = s*60
toplamDakika += d
toplamTutar = 0.59*toplamDakika
print(f"sürüş için geçen süre (saat)\t {s}")
print(f"sürüş için geçen süre (dakika)\t {d}")
print(f"sürüşün toplam süresi  {s}:{d} - {toplamDakika}")
print(f"kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")