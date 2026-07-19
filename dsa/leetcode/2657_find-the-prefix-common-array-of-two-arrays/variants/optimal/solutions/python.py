def solve(A: list[int], B: list[int]) -> list[int]:
    n = len(A)
    
    # seen_A[x] is True if x has appeared in A[0...i]
    # seen_B[x] is True if x has appeared in B[0...i]
    # Values are 1-indexed from 1 to n, so arrays of size n+1 are used.
    seen_A = [False] * (n + 1)
    seen_B = [False] * (n + 1)
    
    # Stores the current count of common elements in prefixes A[0...i] and B[0...i]
    common_count = 0
    
    # The result array C, initialized with zeros
    C = [0] * n
    
    # Iterate through the arrays A and B simultaneously
    for i in range(n):
        val_A = A[i]
        val_B = B[i]
        
        # Process the element from array A
        # If val_A has not been seen in A's prefix before
        if not seen_A[val_A]:
            seen_A[val_A] = True  # Mark val_A as seen in A's prefix
            # If val_A was already present in B's prefix, it now becomes common
            if seen_B[val_A]:
                common_count += 1
        
        # Process the element from array B
        # If val_B has not been seen in B's prefix before
        if not seen_B[val_B]:
            seen_B[val_B] = True  # Mark val_B as seen in B's prefix
            # If val_B was already present in A's prefix, it now becomes common
            # Note: If val_A == val_B, the first block (processing val_A) might
            # not increment common_count if val_A was not yet in seen_B.
            # The second block (processing val_B) will then correctly increment
            # common_count because seen_A[val_B] (which is seen_A[val_A]) would be True.
            if seen_A[val_B]:
                common_count += 1
        
        # Store the current common count for the prefix ending at index i
        C[i] = common_count
        
    return C
