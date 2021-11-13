a=int(input("Istalgan 1-butun sonni kiriting a => "))
b=int(input("Istalgan 2-butun sonni kiriitng: b => "))
if b>a:
    s=1
    for x in range(a,b+1):
        print(x, end="; ")
        s=s*x
    else:
        print(f"\n{a} dan {b} gacha bo'lgan butun sonlar ko'paytmasi: {s} ga teng ekan!")
        print("Sikl tugadi!")
else:
    print("Diqqat! Masala shartiga ko'ra a soni b sonidan kichik bo'lsin!")            