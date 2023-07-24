n=int(input("enter the digits : "))
num=int(input("enter the number : "))
num1=str(num)

if(len(num1)!=n):
    print("invalid")

else:
    temp=num
    sum1=0
   
while(temp>0):
    digit=temp%10
    sum1=sum1+digit*digit*digit
    temp=temp//10

if num==sum1:
    print("armstrong")

else:
    print("not armstrong")
    

