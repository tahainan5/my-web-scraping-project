
# 2. DERECEDEN BİR BİLİNMEYENLİ BİR DENKLEMİN KÖKLERİNİ BULMA 

print("""
********************************
denklem : ax^2 + bx + c

deltayi hesaplama : b**2 - 4*a*c

birinci kök: (-b - delta ** 0.5) / (2*a)
ikinci kök: (-b + delta ** 0.5) / (2*a)

********************************
""")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)


print("Birinci Kök: {}\nİkinci Kök: {}".format(x1, x2))