# end keyword: " " içine \n yazılmadığı sürece bir alt satırdaki argümanı, alt satırdan değil
# devam argüman olarak ekrana basar.
"""
print("Hayatta","En","Hakiki")#end="\n" yazılmasa bile arka planda \n çalışacağı için bir alt satıra geçecektir.
print("Mürşit","İlimdir")
print("-------------------------")

print("Hayatta","En","Hakiki", end="\n")# end="\n" alt satıra geç anlamındadır. 
print("Mürşit","İlimdir")
print("-------------------------")

print("Hayatta","En","Hakiki", end="→") # end=""→" alt satıra geçme anlamındadır. 
print("Mürşit","İlimdir")
print("-------------------------")

print("Hayatta","En","Hakiki", end="*****") # end="*" alt satıra geçme anlamındadır. 
print("Mürşit","İlimdir")
print("-------------------------")
"""

# sep keyword:
"""
print("Hayatta","En","Hakiki","Mürşit","İlimdir")#sep kullanılmazsa da argümanlar arası default olarak boşluk bırakır.
print("-------------------------")
print("Hayatta","En","Hakiki","Mürşit","İlimdir",sep=" ")# sep=" " argümanlar arası boşluk ekler.
print("-------------------------")
print("Hayatta","En","Hakiki","Mürşit","İlimdir",sep="*")# sep="*" argümanlar arası * ekler.
"""

# istanbul-teknopark
# ecodation>>eğitim>>kurumları.ben neredeyim? 
# yazdıralım:

print("İstanbul","teknopark",sep="-")# burada end="\n" kullanmaya gerek yok zaten default olarak alt satıra geçecektir.
print("ecodation","eğitim","kurumları",sep=">>",end=".")
print("ben neredeyim?")