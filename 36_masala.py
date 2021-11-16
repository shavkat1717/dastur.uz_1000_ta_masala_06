n=int(input("n > 0 butun sonni kiriting: n => "))
k=int(input("k > 0 butun sonni kiriting: k => "))
s=0
for i in range(1,n+1):
    s=s+pow(i, k)
print(s)
    