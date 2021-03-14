  
#region ram_steak_heap
"""
a = 1
b = 2
a = b
b = 1
print(a)
"""
#endregion


#region steak_heap_aciklama

#steak: ram'daki steak hafıza alanı
"""
→sayısal veri tipleri saklanır;
-int
-float
-boolean(0,1)
→value types diye geçer.
→steak bölgesi adresi kopyalamaz, adres içerisindeki değeri kopyalar.
"""
#heap: ram'deki heap alanı
"""
→object veri tipleri ram'deki heap alanında saklanır.
-list
-object
-str
→referance types denir.
"""
#endregion