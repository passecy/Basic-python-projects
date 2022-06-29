#kullanıcı adı ve şifre
ad="emir"
şifre="yolcu"

while(True):
    x = input("Ad:")
    y = input("Şifre:")
    if((x==ad)and(y==şifre)):
        print("Hoşgeldiniz")
        break
    elif((x!=ad)and(y==şifre)):
        print("Adınız bulunamadı")
    elif((x==ad)and(y!=şifre)):
        print("Şifrenizi yanlış girdiniz")
        print("şifrenizi değiştirmek için PAROLA yazınız")
        cevap=input()
        if(cevap=="PAROLA"):
            cevap=input("yeni şifrenizi giriniz:")
            şifre=cevap
            print("şifreniz değiştirildi")

    else:
        print("tekrar deneyiniz")
