#region leylek_uygulamasi
print("""
    Leylek Uygulamasına Hoş Geldiniz!!!
    Sürüş Ücreti → 0.59/dk
""")
s = int(input("sürüş için geçen süre (saat)\t : "))
d = int(input("sürüş için geçen süre (dakika)\t : "))
toplamDakika = s*60
toplamDakika += d
toplamTutar = 0.59 * toplamDakika
print(f"Sürüş için geçen süre (saat)\t: {s}")
print(f"Sürüş için geçen süre (dakika)\t: {d}")
print(f"sürüşün toplam süresi {s}:{d} - {toplamDakika} dakika da bitmiştir")
print(f"kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")
#endregion

#region ornek
"""
adim=int(input(Lütfen günlük ortalama adım sayınızı giriniz:))
günlükKalori=adim*1
print("Harcanan Kalori:")
print(f"Günlük Harcanan Kalori:{günlükKalori}")
print(f"Haftalık Harcanan Kalori:{(günlükKalori*7)}")
print(f"Aylık Harcanan Kalori:{(günlükKalori*30)}")
"""
#endregion