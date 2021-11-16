x=float(input(" |x|<1 haqiqiy sonni kiriting x = "))
n=int(input(" n > 0 darajani kiriting n = "))
import math
if n>0 and math.fabs(x)<1:
    s=0
    surat=1
    maxraj=1
    for i in range(1,n+1):
        surat=surat*(2*i-1)*math.pow(x,2*i+1)
        maxraj=maxraj*(2*i)*(2*i+1)
        s=s+surat/maxraj
    print(s)
else:
    print("Shart: n > 0 va |x| < 1 ga e'tibor bering!")