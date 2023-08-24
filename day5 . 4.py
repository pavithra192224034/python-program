def can_divide(prod, summation):
    return prod % summation == 0

def main():
    t = int(input("Enter the number of test cases: "))  # Number of test cases
    
    for _ in range(t):
        a, b = map(int, input("Enter two integers separated by space: ").split())
        product = a * b
        summation = a + b
        
        if can_divide(product, summation):
            print("YEAH")
        else:
            print("NAH")

if __name__ == "__main__":
    main()



