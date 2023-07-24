n=int(input("enter the digits : "))
num=int(input("enter the number : "))
num1=str(num)
if(len(num1)!=n):
    print("invalid")
else:
    temp=num
    sum=0
while(temp>0):
    digit=temp%10
    sum=sum+digit
    temp=temp//10

print("Total = ",sum)

