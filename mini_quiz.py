puan = 0
soru1 = int(input("Üçgenin iç açilari toplami kaçtir? "))
if soru1 == 180 :
    print("Doğru cevap")
    puan += 20
else :
    print("Yanlis cevap")
    
  

soru2 = int(input("256 nin karekökü kaçtir? "))
if soru2 == 16 :
    print("Doğru cevap")
    puan += 20
else :
    print("Yanlis cevap")
    
    

soru3 = int(input("6 + 5 * 7 = "))
if soru3 == 41 :
    print("Doğru cevap")
    puan += 20
else :
    print("Yanlis cevap")
    
    

soru4 = int(input("19 un karesi kaçtir? "))
if soru4 == 361 :
    print("Doğru cevap")
    puan += 20
else :
    print("Yanlis cevap")
    


soru5 = int(input("1090 +10 kaçtir? "))
if soru5 == 1100 :
    print("Doğru cevap")
    puan += 20
else :
    print("Yanlis cevap")


print(f"Puaniniz : {puan}")