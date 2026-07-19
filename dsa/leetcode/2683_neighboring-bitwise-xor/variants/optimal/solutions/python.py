def solve(derived: list[int]) -> bool:
    """
    Determines if a binary array 'original' can be constructed such that
    derived[i] = original[i] XOR original[(i + 1) % n] for all i.

    The problem reduces to checking if the XOR sum of all elements in 'derived' is 0.
    This is because:
    original[(i + 1) % n] = original[i] XOR derived[i]

    By repeatedly applying this, we find:
    original[k] = original[0] XOR derived[0] XOR derived[1] XOR ... XOR derived[k-1]

    For the cyclic condition to hold, the last element derived[n-1] must satisfy:
    derived[n-1] = original[n-1] XOR original[0]

    Substituting the expression for original[n-1]:
    derived[n-1] = (original[0] XOR (derived[0] XOR ... XOR derived[n-2])) XOR original[0]

    Since X XOR X = 0, the original[0] terms cancel out:
    derived[n-1] = derived[0] XOR derived[1] XOR ... XOR derived[n-2]

    This implies that the XOR sum of all elements in 'derived' must be 0:
    derived[0] XOR derived[1] XOR ... XOR derived[n-2] XOR derived[n-1] = 0

    If this condition holds, an 'original' array can always be constructed (e.g., by
    setting original[0] = 0 and propagating values). If it doesn't hold, no such
    'original' array exists.

    Args:
        derived: A list of integers (0 or 1) representing the derived array.

    Returns:
        True if a valid original array can be constructed, False otherwise.
    """
    xor_sum = 0
    for x in derived:
        xor_sum ^= x
    return xor_sum == 0
