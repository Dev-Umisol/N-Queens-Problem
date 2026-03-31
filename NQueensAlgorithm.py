def dfs_n_queens(n):
    """
    Implementing N-Queens Problem to place N queens on an NxN chessboard so that no two queens attack each other
    Args: n: Number of queens
    Return: solutions: 
    """
    if n < 1:
        return []
    
    # Helper function to check if placing the queen in the next row is safe
    def is_safe(state, col):
        for index, value in enumerate(state):
            if value == col or abs(len(state) - index) == abs(col - value): # <-- checks for same column and diagonal
                return False    
        return True
    
    solutions = [] # Store all valid arrangements
    stack = [[]] # starting state (no queens)
    
    while stack:
        current_state = stack.pop() #list of columns positions for queens placed so far
        
        if len(current_state) == n:
            solutions.append(current_state)
        else:
            for queen in range(0, n):
                if is_safe(current_state, queen):
                    stack.append(current_state + [queen])
    return sorted(solutions)

# --> Example Usage <--
print(dfs_n_queens(1))
print(dfs_n_queens(2))
print(dfs_n_queens(3))
print(dfs_n_queens(4))
print(dfs_n_queens(5))

print(len(dfs_n_queens(5)))
print(len(dfs_n_queens(8)))