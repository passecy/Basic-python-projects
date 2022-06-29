try:
    while True:
        a=int(input("a:"))
        b=int(input("b:"))
        c=((a*b)+1)
        liste=[]
        for i in range(1,c):
            if (i%a==0)and(i%b==0):
                print(i)
                break
except:
    print("HATA!!")
