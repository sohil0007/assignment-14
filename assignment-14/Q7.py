a = [10,20,30,"Sohil",40,3+4j,50,5.5]

L=[]
for i in a:
    if type(i)==int:
        L.append(i)

print(L)

