def solve(variables: list[list[int]], target: int) -> list[int]:
    """
    Computes the indices of variables that satisfy ((a^b % 10)^c % m) == target.
    Uses Python's built-in pow(a, b, m) for efficient modular exponentiation.
    """
    result = []
    
    for i, (a, b, c, m) in enumerate(variables):
        # Step 1: Calculate (a^b % 10)
        # Step 2: Calculate (result_of_step1^c % m)
        # We use the three-argument pow(base, exp, mod) for efficiency.
        val = pow(a, b, 10)
        final_val = pow(val, c, m)
        
        if final_val == target:
            result.append(i)
            
    return result
