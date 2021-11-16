n=int(input("\nFibonachchi sonlar ketma-ketligining nechta hadini bilmoqchisiz: n => "))
if n>0:
    a=1
    b=1
    print(f"{a}")
    print(f"{b}")
    for x in range(3,n+1):
        c=a+b
        print(f"{c}")
        a=b
        b=c
else:
    print("n sonini musbat kiriting!")