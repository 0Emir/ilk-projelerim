import random
sayi = random.randint(1,100)
tahmin = 0
while tahmin != sayi :
    tahmin = int(input("1-100 arasinda bir sayi tahmin et : "))
    if tahmin <sayi :
        print("daha büyük bir sayi gir: ")
    elif tahmin>sayi:
        print("daha küçük bir sayi gir: ")
    else:
        print("tebrikler doğru tahmin")
        