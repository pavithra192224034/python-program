n=input("number:")
dig=len(n)
if(dig%2==0):
    half=int(dig/2)
    n1=int(n[:half])
    n2=int(n[half:])
    sum=n1+n2
    sq=sum**2
    num=int(n)
    if(num==sq):
        print("tech")
    else:
        print("not tech")
else:
    print("not tech")
