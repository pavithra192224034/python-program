num=int(input("Enter an number : "))
f=[]
for i in range(1,num):
        if(num%i==0):
            f.append(i)
print("The factor of ",num," = ",f)
length=len(f)
print("The length of the list is ",length+1)

n=int(input("Enter inside list : "))

print(*f[0:n])    
