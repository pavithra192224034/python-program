def delchar(s, c):
    if len(c) != 1:
        return s
    
    result = ''
    for char in s:
        if char != c:
            result += char
    
    return result

# Example usage
input_str = "banana"
char_to_delete = "a"
result = delchar(input_str, char_to_delete)
print(result)  # Output: "bnn"
