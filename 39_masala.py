a=int(input("a butun sonni kiriting: a => "))
b=int(input("b butun sonni kiriting: b => "))
if b>a:
    s=0
    for i in range(a+1,b):
        for p in range(1,i+1):
            print(i,end=("; "))
else:
    print("b > a shartiga e'tibor bering!")