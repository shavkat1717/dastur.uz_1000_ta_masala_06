a=float(input("1 kg konfetning narxini kiriting a => "))
b=2/10
if a>0:
    for x in range(1,2):
        for y in range(2,11):
            if y%2==0:
                z=y/10
                print(f"{x+z} kilogramm konfetning narxi {a*(x+z)} so'm turadi.")
else:
    print("Konfetning narxi nol yoki manfiy bo'lishi mumkin emas!")