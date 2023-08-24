def generate_binomial_triangle(n):
    triangle = [[0] * (i+1) for i in range(n)]
    
    for i in range(n):
        triangle[i][0] = 1  # First element in each row is 1
        
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle[i][i] = 1  # Last element in each row is 1
        
    return triangle

def sum_of_nth_row(triangle, row_number):
    if row_number < 1 or row_number > len(triangle):
        return None
    
    return sum(triangle[row_number - 1])

# Example usage
num_rows = int(input("Enter the number of rows: "))
binomial_triangle = generate_binomial_triangle(num_rows)

row_number = int(input("Enter the row number: "))
sum_row = sum_of_nth_row(binomial_triangle, row_number)

if sum_row is None:
    print("Invalid row number.")
else:
    print(f"Sum of elements in row {row_number}: {sum_row}")



