n = int(input("Enter a number :"))

print("enter",n,"numbers")

L = []
i=n
while i>0:
    x = L.append(int(input()))
    i-=1

print("the sum is :",sum(L)) 