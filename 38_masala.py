n=int(input("n > 0 butun sonni kiriting: n => "))
if n>0:
    s=0
    t=n
    p=1
    for i in range(1,n+1):
        for j in range(t,0,-1):
            p=p*i
        s=s+p 
        p=1
        t=t-1
    print(s)        
else:
    print("n > 0 shartga e'tibor bering!")
