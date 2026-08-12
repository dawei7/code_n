def solve() -> int:
    """Find largest 1 to 9 pandigital 9-digit number formed as concatenated product.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    target = set("123456789")
    max_pandigital = 918273645  # Base candidate from x=9, (1..5)

    # 4-digit x starting with 9 (n=2 gives 4 + 5 = 9 digits)
    for x in range(9876, 9213, -1):
        s = f"{x}{x * 2}"
        if len(s) == 9 and set(s) == target:
            val = int(s)
            if val > max_pandigital:
                max_pandigital = val
                break

    return max_pandigital
