n = int(input("Enter a number :"))

print("enter",n,"numbers")

L = []
i=n
while i>0:
    x = L.append(int(input()))
    i-=1

L.sort()

print("the smallest number is :",L[0]) 