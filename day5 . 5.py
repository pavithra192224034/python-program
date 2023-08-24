def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
            
    return left

# Example usage
nums = [1, 2, 3, 1]  # Modify the input array as needed
peak_index = findPeakElement(nums)
print(f"The peak element is at index: {peak_index}")
