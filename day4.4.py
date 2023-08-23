def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Convert to lowercase and remove non-alphanumeric characters
    return s == s[::-1]  # Compare the string with its reverse

# Example usage
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str))  # Output: True
