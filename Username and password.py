#Name and Password check
Ad="Emirhan"
Soyad="Yolcu"

x=input("Adınız:")
y=input("Soyadınız:")

if((x==Ad)and(y==Soyad)):
    print("Welcome")
elif((x!=Ad)and(y==Soyad)):
    print("Adınızı yanlış girdiniz.")
elif((x==Ad)and(y!=Soyad)):
    print("Soyadınızı yanlış girdiniz.")
else:
    print("Tekrar deneyiniz.")
