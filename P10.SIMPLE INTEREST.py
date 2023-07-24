p=int(input("enter rate "))
y=int(input("enter year "))
c=input("citizen (s/n) ")
g=input("citizen (m/f) ")
if (c=="s" or g=="m"):
    roi=p*y*12/100
    print(roi)
elif (c=="s" or g=="f"):
    roi=p*y*15/100
    print(roi)
else:
    roi=p*y*10/100
    print(roi)

