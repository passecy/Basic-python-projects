while True:
    listea=[]
    listeb=[]
    listec=[]
    a=int(input("a:"))
    b=int(input("b:"))

    for i in range(1,a+1):
        if a%i==0:
            listea.append(i)
    for x in range(1,b+1):
        if b%x==0:
            listeb.append(x)

    for c in range(0,len(listea)):
        for d in range(0,len(listeb)):
            if(listea[c]==listeb[d]):
                listec.append(listea[c])
    print(listec[-1])
