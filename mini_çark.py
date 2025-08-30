import random
seçenek1 = input("İlk seçeneği giriniz ")
seçenek2 = input("İkinci seçeneği giriniz ")
seçenek3 = input("Üçüncü seçeneği giriniz ")
seçenek4 = input("Dördüncü seçeneği giriniz ")
seçenek5 = input("Beşinci seçeneği giriniz ")

çark = [f"{seçenek1}", f"{seçenek2}" , f"{seçenek3}" , f"{seçenek4}", f"{seçenek5}"]

sonuç = random.choice(çark)
print(f"Sonuç : {sonuç}")