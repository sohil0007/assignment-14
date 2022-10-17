L = [eval(x) for x in input("Enter list elements :").split(",")]
print(L)

ele = eval(input("Enter an element :"))

index=0

for i in L:
    if i==ele:
        print(index,end=" ")
    index+=1
