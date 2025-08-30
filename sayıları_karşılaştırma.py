x = int(input("İlk sayiyi giriniz "))
y = int(input("İkinci sayiyi giriniz "))
z = int(input("Üçüncü sayiyi giriniz "))
if   x > y and x > z :
    print(f"En büyük sayi {x} dir")
elif y > x and y >  z:
    print(f"En büyük sayi {y} dir")
else  :
    print(f"En büyük sayi {z} dir")
if   x < y and x < z :
    print(f"En küçük sayi {x} dir")
elif y < x and y < z:
    print(f"En küçük sayi {y} dir")
else :
    print(f"En küçük sayi {z} dir")