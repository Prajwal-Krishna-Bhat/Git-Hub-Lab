a=[2]
n=int(input("Enter range"))
for i in range(2,n):
    count=0
    for x in a:
        if i%x==0:
            count+=1
            break
    if count==0:
        a.append(i)
        print(i)
print(len(a))
p=len(a)
print("Ratio",p/n)