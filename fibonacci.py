def Sumfibo (n):
    if (n==0 or n==1):
        return n
    else:
        return Sumfibo(n-1)+Sumfibo(n-2)
n=int(input("Enter the no of fibo nos:"))
print("Fibo sequence:")
for i in range (n):
    print(Sumfibo(i))
sum=0
for i in range(n):
    sum+=Sumfibo(i)
print("Sum of n fibo sequnce:",sum) 
    