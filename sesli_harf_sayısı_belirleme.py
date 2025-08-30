sayac = 0
sesli_harfler = "aeıioöuüAEIİOÖUÜ"
cümle = input("Lütfen cümlenizi giriniz ")
for harf in cümle :
    if harf in sesli_harfler:
        sayac += 1
print(f"Sesli harf sayısı: {sayac}")