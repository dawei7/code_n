def solve() -> int:
    """Find sum of all products whose identity multiplicand * multiplier = product is 1..9 pandigital.
    
    Time Complexity: O(A * B)
    Space Complexity: O(1)
    """
    products = set()
    target_digits = set("123456789")

    # Case 1: 1-digit * 4-digit = 4-digit
    for a in range(1, 10):
        for b in range(1234, 9876 // a + 1):
            p = a * b
            s = f"{a}{b}{p}"
            if len(s) == 9 and set(s) == target_digits:
                products.add(p)

    # Case 2: 2-digit * 3-digit = 4-digit
    for a in range(12, 99):
        for b in range(123, 9876 // a + 1):
            p = a * b
            s = f"{a}{b}{p}"
            if len(s) == 9 and set(s) == target_digits:
                products.add(p)

    return sum(products)
