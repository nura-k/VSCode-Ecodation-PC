#region aritmetik-operatorler
#aritmetik operatörler
"""
1 → +  toplama
2 → -  çıkarma
3 → *  çarpma
4 → /  bölme
5 → // tam bölme
6 → ** üst alma
7 → %  mod alma
"""
#endregion 

#region +/- binary
"""
print(3+3)
print(6-3)
print(3-6)
print(0.15-15)
print(.15-15)
print(9-6.) 
print(9+6.) 
"""
#endregion

#region +/- unary işaret
#unery işaret, sayının işaretini gösterir.
"""
print(+2)
print(-2)
""" 
#endregion

#region */ 
"""
print(4*4) 
print(.4*4) 
print(type(.4*4)) 
print(9/3)
print(9/2) 
print(type(9/2)) 
print(17/.4) 
#print(10/0) burada hata verir.
"""
#endregion

#region ** üst alma
"""
print(4**4)
print(2**4)
print(16**0.5)
print(16**(1/2))
print(type(16**0.5))
"""
#endregion

#region // - tam bölme
"""
print(15%4)
print(15%2)
print(8%3)
print(15%0)#ZeroDivisionError: hatası verir.
"""
#endregion

#region operator_oncelikleri
"""
1→ +,-      unary
2→ **       üst alma
3→ *, /, %  çarpma, bölme, mod alma
4→ +, -     toplama çıkarma
"""

"""
print(3+4*5)     
print(15%4*2)      # % left-side binding
print(15%4%2)      # % left-side binding
print(2**2**3)     # ** right-side binding
"""
#endregion


#region pratikler
"""
print(10*(8*3)/(8%3))

print(3-5/7+2*3*7-2/(3+5))

print((5/1**2)**0.5)

print((1+3)**(1/2)-(2**2)/(1**2))

print(3**2 + 1**2 + 3/1)
"""
#endregion