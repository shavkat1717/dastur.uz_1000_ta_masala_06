a=float(input("Daraja asosini kiriting: a => "))
n=int(input("Darajani yani: n > 0 butun sonni kiriting n => "))
if n>0:
    s=1
    for x in range(1,n+1):
        s=a**x
    print(s)
else:
    print(" n > 0 butun sonni kiriting.")