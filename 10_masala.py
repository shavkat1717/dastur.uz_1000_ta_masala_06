n=int(input("n>0 butun sonni kiriting n => "))
if n>0:
    s=0
    for x in range(1,n+1):
        print(x, end="; ")
        s=s+(x**(-1))
    else:
        print(f"\nYig'indi: {s} ga teng ekan!\nSikl tugadi...")
else:
    print("Diqqat! Masala shartiga ko'ra n>0 bo'lsin!")            