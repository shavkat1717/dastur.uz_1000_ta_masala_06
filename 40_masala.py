a=int(input("a butun sonni kiriting: a => "))
b=int(input("b butun sonni kiriting: b => "))
if b>a:
    s=1
    for i in range(a,b+1):
        for j in range(1,s+1):
            print(i,end=("; "))
        s=s+1
else:
    print("b > a shartiga e'tibor bering!")