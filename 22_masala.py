x=float(input(" x haqiqiy sonni kiriting x => "))
n=int(input(" n > 0 butun sonni kiriting n => "))
from math import factorial
if n>0:
    s=1
    for y in range(1,n+1):
        s=s+(x**y)/factorial(y)
    print(s)
else:
    print(" n > 0 butun sonni kiriting.")