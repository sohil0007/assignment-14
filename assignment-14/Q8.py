L = [eval(x) for x in input("Enter list elements :").split(",")]
print(L)

ele = eval(input("Enter an element :"))

count=0

for i in L:
    if i==ele:
        count+=1

print("element {} has occured {} times".format(ele,count))