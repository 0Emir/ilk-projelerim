print("Basit Hesap Makinesi")
print("İşlemler : ")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

seçim = input("Lütfen yapmak istediğiniz işlemi seçin: (1/2/3/4) ")

sayi1 = float(input("Lütfen ilk sayıyı girin "))
sayi2 = float(input("Lütfen ikinci sayıyı girin "))

if seçim == "1":
    print(f"Sonuç : {sayi1 + sayi2}")
elif seçim == "2":
    print(f"Sonuç : {sayi1 - sayi2}")
elif seçim == "3":
    print(f"Sonuç : {sayi1 * sayi2}")
elif seçim == "4":
    if sayi2 == 0:
        print("0'a bölünme hatası (İkinci saı sıfır olmamalı)")
    else:
        print(f"Sonuç : {sayi1 / sayi2}")
else :
    print("Geçersiz Seçim!")