import math


def solve() -> int:
    """Find sum of all numbers equal to the sum of the factorial of their digits.
    
    Time Complexity: O(limit * log10(limit))
    Space Complexity: O(1)
    """
    facts = [math.factorial(d) for d in range(10)]
    limit = 7 * facts[9]  # 2540160

    total = 0
    for i in range(10, limit):
        if i == sum(facts[int(c)] for c in str(i)):
            total += i
    return total
