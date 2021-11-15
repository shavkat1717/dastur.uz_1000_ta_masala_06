n=int(input(" n > 0 butun sonni kiriting n => "))
if n>0:
    from math import factorial
    s=0
    for x in range(1,n+1):
        s=s+factorial(x)
    print(s)
else:
    print(" n > 0 butun sonni kiriting.")