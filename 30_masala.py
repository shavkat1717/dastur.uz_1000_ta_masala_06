a=int(input("Sonlar o'qidagi A nuqtani (haqiqiy sonni) kiriting A => "))
b=int(input("Sonlar o'qidagi B nuqtani (haqiqiy sonni) kiriting B => "))
n=int(input("n > 0 butun sonni kiriting n => "))
if n>0:
    import math
    l=math.fabs(a-b)
    print(f"{a} va {b} nuqtalar orasidagi masofa: {l} ga teng!\nEndi uni {n} ta bo'lakka bo'lamiz:\n")
    q=math.floor(l/n)
    for x in range(a,b+1,q):
        print(1-math.sin(x))
else:
    print("n sonini musbat kiriting!")    