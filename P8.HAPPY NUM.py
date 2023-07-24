def happy(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=digit**2+sum
        temp=temp//10
    return sum


n=int(input("enter a number :"))
result=n
while result!=1 and result!=4:
    result=(happy(result))
if result==1:
    print("true")
elif result==4:
    print("false")
