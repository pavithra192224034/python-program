def reversebits(num,bitsize):
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse +(bitsize-len(reverse))*'0'
    print(int(reverse,2))
if __name__=='__main__':
    num=2
    bitsize=32
    reversebits(num,bitsize)
