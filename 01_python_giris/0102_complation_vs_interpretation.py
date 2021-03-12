"""
compilation(Derleme);
av:
1- Compile edilmiş kodların execute(.exe yani machine code'ye çevrilmesi) işlemi hızlıdır.
2- Compiler sadece kod yazılan pc de olması yeter, son kullanıcıda olmasına gerek yok.
3- Compile edilen kodlar makine diline çevrileceği için son kullanıcının bu kodları anlaması zordur,
kodların manipülasyonları o yüzden zordur
(kullanıcı main.exe kodunu görür source file'yi değil bu yüzden .exe kodunu anlayıp değiştirmek zor olacaktır.).

dez:
1- Compile işlemi, derleme işlemi anı yavaştır, ilk anda uzun sürebilir.
2- Compiler, donanım platformuna göre farklılık gösterir, platform bağımlıdır özetle.
(yani windowsta execute edilen bir source file linuxta veya başka bir işletim sisteminde çalışmaz.)

-------------------------------------------------------------------------------------------

interpretation(Yorumlama);
av:
1- Kodu yazar ve çalıştırırız, ek derleme süresi istemez.
2- Platform bağımlı değildir, her donanımda, her işletim sisteminde çalışır, ayrı ayrı derleyiciler istemez,
tek ihtiyaç duyduğu runtime'da ikenyani çalışma anında interpreter olsun bitti gitti,
o da python kütüphanelerinde var zaten.

dez:
1- Tüm kaynağı run-time'de iken tüketir, çalışma anı yavaştır.
2- Hem kodu yazan kişinin, hemde son kullanıcının bilgisayarında interpreter yani kütüphane olmalı.
"""