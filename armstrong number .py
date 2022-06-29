while True:
try:
    while True:
        a=input(" bir sayı giriniz:")
        liste=[]
        for i in a:
            liste.append(i)
        if len(liste)==3:
            x=(int(liste[0])**3)+(int(liste[1])**3)+(int(liste[2])**3)
            if x==int(a):
                print("armstrong sayısı")
            else:
                print("armstrong sayısı değil")
        elif len(liste)==4:
            x=(int(liste[0])**4)+(int(liste[1])**4)+(int(liste[2])**4)+(int(liste[3])**4)
            if x==int(a):
                print("armstrong sayısı")
            else:
                print("armstrong sayısı değil")
        else:
            print("lütfen 3 veya 4 basamaklı bir sayı giriniz")
except:
    print("HATA!!")
    print("tekrar deneyiniz")
