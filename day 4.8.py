def roman_to_int(s):
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for symbol in s[::-1]:
        value = roman_to_int_map[symbol]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    
    return total

# Example usage
roman_numeral = "MCMXCIV"
result = roman_to_int(roman_numeral)
print(result)  # Output: 1994


