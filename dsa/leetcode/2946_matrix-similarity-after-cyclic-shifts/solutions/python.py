def solve(mat: list[list[int]], k: int) -> bool:
    """
    Determines if the matrix is similar to itself after cyclic shifts.
    Even rows are shifted left by k, odd rows are shifted right by k.
    """
    m = len(mat)
    n = len(mat[0])
    
    # The effective shift is k % n
    shift = k % n
    
    if shift == 0:
        return True
        
    for i in range(m):
        for j in range(n):
            # For even rows, left shift: new_idx = (j - shift) % n
            # For odd rows, right shift: new_idx = (j + shift) % n
            # We check if mat[i][j] == mat[i][new_idx]
            if i % 2 == 0:
                if mat[i][j] != mat[i][(j + shift) % n]:
                    return False
            else:
                if mat[i][j] != mat[i][(j - shift) % n]:
                    return False
                    
    return True
