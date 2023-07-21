def findsqrt(x):
  if x<2:
    return x

  y=x
  z=(y+(x/y))/2

  while abs(y-z)>=0.000001:
       y=z
       z=(y+(x/y))/2

  return z
if __name__=='__main__':
   n=4

   ans=int(findsqrt(n))
   print(ans)
