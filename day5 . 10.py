def reverse_words(s):
    words = s.split()
    reversed_words = reversed(words)
    reversed_string = " ".join(reversed_words)
    return reversed_string

# Example usage
input_string = input("Enter the input string: ")
reversed_result = reverse_words(input_string)
print("Reversed words:", reversed_result)
