a=float(input("Daraja asosini kiriting: a => "))
n=int(input("Darajani yani: n > 0 butun sonni kiriting n => "))
if n>0:
    s=0
    for x in range(1,n+1):
        s=s+(((-1)**x)*a**x)
    print(s+1)
else:
    print(" n > 0 butun sonni kiriting.")