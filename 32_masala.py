print("\nArifmetik progressiyaning birinchi hadi A1=1 ga, ayirmasi esa d=1 ga teng!")
n=int(input("Ushbu arifmetik progressiyaning nechanchi hadini bilmoqchisiz: n => "))
if n>0:
    Ao=1
    d=1
    An=Ao+(n-1)*d
    print(f"\nUshbu arifmetik progressiyaning {n}-hadi {An} ga teng.")   
else:
    print("n sonini musbat kiriting!")    
# for i in range(2,n,d):
#     print(i)
for i in range(Ao,An+1,d):
    print(i, end=("; "))