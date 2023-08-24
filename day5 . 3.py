def numSquares(n):
    # Create a list to store the least number of perfect square numbers for each value from 0 to n
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Generate all perfect squares less than or equal to n
    squares = [i * i for i in range(1, int(n**0.5) + 1)]
    
    # Iterate through each value from 1 to n
    for i in range(1, n + 1):
        for square in squares:
            if square <= i:
                dp[i] = min(dp[i], dp[i - square] + 1)
            else:
                break
    
    return dp[n]

# Example usage
n = int(input("Enter an integer: "))
result = numSquares(n)
print(f"The least number of perfect square numbers that sum to {n} is: {result}")



