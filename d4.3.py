def smaller_than_current(nums):
    counts = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if j != i and nums[j] < nums[i]:
                count += 1
        counts.append(count)
    return counts

# Example usage
nums = [8, 1, 2, 2, 3]
result = smaller_than_current(nums)
print(result)  # Output: [4, 0, 1, 1, 3]
