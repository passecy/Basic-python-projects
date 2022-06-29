while True:
    try:
        while True:
            a=int(input("bir sayı giriniz:"))
            b=0
            for x in range (1,a):
                if(a%x==0):
                    b=x+b
            if(b==a):
                print("mükemmel sayı")
            else:
                print("Mükemmel sayı değil")
    except:
        print("HATA!! ")
        print("Tekrar Deneyiniz")
