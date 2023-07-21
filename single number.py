def singlenumber(nums):
    count=0
    for i in nums:
        count=count^i
        return count
nums=[4,1,2,1,2]
print(singlenumber(nums))
