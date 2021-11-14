n=int(input(" n > 0 butun sonni kiriting n => "))
if n>0:
    s=1
    for x in range(1,n+1):
        y=x/10
        s=s*(1+y)
    print(s)
else:
    print(" n > 0 butun sonni kiriting.")