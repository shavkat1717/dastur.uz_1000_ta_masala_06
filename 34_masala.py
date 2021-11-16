n=int(input("\nFibonachchi sonlar ketma-ketligining nechta hadini bilmoqchisiz: n => "))
if n>0:
    a=1
    b=2
    print(f"{a}")
    print(f"{b}")
    for x in range(3,n+1):
        c=(a+2*b)/3
        print(f"{c}")
        a=b
        b=c
else:
    print("n sonini musbat kiriting!")