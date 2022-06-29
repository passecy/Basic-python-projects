#asal olmayan sayı toplamlarını bulma
sayı=int(input("bir sayı giriniz:"))
sayı1=0
sayı2=0
sayı3=0
sayı4=0
for i in range(2,sayı+1):
    sayı1=0
    for v in range(2,i):
        if(i%v==0):
            sayı1+=1
    if(sayı1==0):
        sayı3+=i
for x in range(0,sayı+1):
    sayı4+=x
print(sayı4-sayı3)
