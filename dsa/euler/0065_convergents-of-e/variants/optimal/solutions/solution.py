def solve(target: int = 100) -> int:
    """Find the sum of digits in the numerator of the target-th convergent of e.
    
    Time Complexity: O(target)
    Space Complexity: O(1)
    """
    a = [2]
    for i in range(1, target):
        if i % 3 == 2:
            a.append(2 * (i + 1) // 3)
        else:
            a.append(1)

    n0 = a[0]
    n1 = a[0] * a[1] + 1

    for i in range(2, target):
        n0, n1 = n1, a[i] * n1 + n0

    return sum(int(c) for c in str(n1))
