import itertools
n=input("enter number : ")
n1=list(itertools.permutations(n))
b=(["".join(a) for a in n1])
print(*b)
