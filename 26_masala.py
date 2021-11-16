x=float(input(" |x|<1 haqiqiy sonni kiriting x = "))
n=int(input(" n > 0 darajani kiriting n = "))
import math
if n>0 and math.fabs(x)<1:
    s=x
    for i in range(1,n+1):
        s=s+pow(-1,i)*pow(x, 2*i+1)/(2*i+1)
    print(s)
else:
    print("Shart: n > 0 va |x| < 1 ga e'tibor bering!")