def solve(forts: list[int]) -> int:
    max_captured = 0
    last_idx = -1
    
    for i, fort in enumerate(forts):
        if fort != 0:
            # If we find a fort and it's different from the last one seen,
            # we have a potential capture sequence.
            if last_idx != -1 and forts[last_idx] != fort:
                # The number of zeros between last_idx and i is (i - last_idx - 1)
                max_captured = max(max_captured, i - last_idx - 1)
            
            # Update the last seen non-empty fort index
            last_idx = i
            
    return max_captured
