n=int(input("n > 0 butun sonni kiriting: n => "))
if n>0:
    s=0
    for i in range(1,n+1):
        print(i)
        for j in range(n,0,-1):
            print(j)
            s=s+pow(i,j)
            print(s)
else:
    print("n > 0 shartga e'tibor bering!")