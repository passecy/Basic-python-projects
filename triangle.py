def program(liste):
    if len (liste)==3:
        a=liste[0]
        b=liste[1]
        c=liste[2]
        if((a+b>c)and(b+c>a)and(a+c>b)and(a-b<c)and(b-c<a)and(a-c<b)):
            print("şekil:")
            if((a==b)and(a==c)and(b==c)):
                print("eşkenar üçgen")
            elif(((a==b)or(b==c)or(a==c))and((a!=b)or(b!=c)or(a!=c))):
                print("ikizkenar üçgen")
            else:
                print("çeşitkenar üçgen")
        else:
            print("şekil bir üçgen oluşturmuyor")
    elif len(liste)==4:
        d=liste[0]
        f=liste[1]
        e=liste[2]
        g=liste[3]
        if((d==f)and(d==e)and(d==g)):
            print("şekil bir kare veya eşkenar dörtgen")
        else:
            print("şekil yamuk,paralelkenar... vs olabilir")
while True:
    x=int(input("eleman sayısı:"))
    if(x==3):
        a=int(input("ilk kenar:"))
        b=int(input("ikinci kenar:"))
        c=int(input("üçüncü kenar:"))
        program([a,b,c])
    elif(x==4):
        d=int(input("ilk kenar:"))
        e=int(input("ikinci kenar:"))
        f=int(input("üçüncü kenar:"))
        g=int(input("dördüncü kenar:"))
        program([d,e,f,g])
    else:
        print("tekrar deneyiniz")
