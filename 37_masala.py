n=int(input("n > 0 butun sonni kiriting: n => "))
s=0
for i in range(1,n+1):
    s=s+pow(i, i)
print(s)