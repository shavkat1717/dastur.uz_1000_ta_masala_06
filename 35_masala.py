n=int(input("\nKetma-ketlikning nechta hadini bilmoqchisiz: n => "))
if n>2:
    a=1
    b=2
    c=3
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")
    for x in range(4,n+1):
        d=(c+b-2*a)
        print(f"{d}")
        a=b
        b=c
        c=d
else:
    print("n>2 shart bo'yicha son kiriting!")