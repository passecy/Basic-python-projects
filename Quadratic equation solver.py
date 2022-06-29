def p(a,b,c):
    delta=b*b-4*a*c
    if(delta<0):
        print("reel kök bulunamadı")
        return
    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/2*a
    return (x1,x2)
while True:
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
	
    x=p(a,b,c)
    print(x)
