n=int(input(" n > 0 butun sonni kiriting n => "))
if n>0:
    s=0
    for x in range(1,n+1):
        y=(2*x-1)
        s=s+y
    print(s)
else:
    print(" n > 0 butun sonni kiriting.")