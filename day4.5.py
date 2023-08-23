def min_jumps_to_end(nums):
    n = len(nums)
    if n == 0:
        return -1
    
    jumps = [float('inf')] * n
    jumps[0] = 0
    
    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    
    if jumps[n - 1] == float('inf'):
        return -1
    else:
        return jumps[n - 1]

# Example usage
nums = [2, 3, 1, 1, 4]
result = min_jumps_to_end(nums)
print(result)  # Output: 2



