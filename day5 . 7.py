def longest_substring(s, k):
    if len(s) == 0 or k > len(s):
        return 0
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char, count in char_count.items():
        if count < k:
            return max(longest_substring(subs, k) for subs in s.split(char))
    
    return len(s)

# Example usage
s = input("Enter a string: ")
k = int(input("Enter an integer k: "))

result = longest_substring(s, k)
print(f"The length of the longest substring with at least {k} repeating characters is: {result}")




