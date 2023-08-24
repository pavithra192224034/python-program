def length_of_last_word(s):
    # Remove trailing and leading spaces
    s = s.strip()
    
    # Split the string into words
    words = s.split()
    
    # Check if there are any words in the string
    if len(words) == 0:
        return 0
    
    # Return the length of the last word
    return len(words[-1])

# Example usage
input_string = "Hello world"
result = length_of_last_word(input_string)
print(result)  



