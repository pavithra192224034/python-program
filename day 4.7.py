def count_sorted_vowel_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Create a 2D DP array where dp[i][j] represents the count of sorted vowel strings of length i ending with vowel j
    dp = [[0] * len(vowels) for _ in range(n + 1)]
    
    # Initialize base cases
    for j in range(len(vowels)):
        dp[1][j] = 1
    
    # Fill in the DP array
    for i in range(2, n + 1):
        for j in range(len(vowels)):
            dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1))
    
    # Sum up the counts for all ending vowels to get the total count of sorted vowel strings of length n
    total_count = sum(dp[n])
    
    return total_count

# Example usage
n = 2
result = count_sorted_vowel_strings(n)
print(result)  # Output: 15





