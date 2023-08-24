
def min_swaps_to_chessboard(board):
    n = len(board)
    
    # Check if the matrix can be converted into a valid chessboard
    for i in range(n):
        for j in range(n):
            if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                return -1
    
    row_sum = sum(board[0])
    col_sum = sum(board[i][0] for i in range(n))
    
    row_swap = n - row_sum if row_sum > n // 2 else row_sum
    col_swap = n - col_sum if col_sum > n // 2 else col_sum
    
    if n % 2 == 1:
        if row_swap % 2 == 1:
            row_swap = n - row_swap
        if col_swap % 2 == 1:
            col_swap = n - col_swap
    
    return (row_swap + col_swap) // 2

# Example usage
n = int(input("Enter the size of the matrix (N): "))
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = min_swaps_to_chessboard(matrix)
print(f"Minimum number of swaps to form a valid chessboard: {result}")



