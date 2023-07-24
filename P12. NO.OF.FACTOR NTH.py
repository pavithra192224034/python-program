num=int(input("Enter an number : "))
f=[]
for i in range(1,num):
        if(num%i==0):
            f.append(i)
print("The factor of ",num," = ",f)
length=len(f)
print("The length of the list is ",length)


n=int(input("Enter inside list : "))
if(n>length):
        print("invalid ! enter new number ")
        n1=int(input("Enter the nth number :"))
        print(n," factor is = ",f[n-1])
else:
        print(n," factor is  = ",f[n-1])
