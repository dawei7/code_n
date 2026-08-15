def solve(target: int = 100) -> int:
    """Find the sum of digits in the numerator of the 100th convergent of e.

    Mathematical Principles Applied:
    1. Continued Fraction Expansion of Euler's Number e:
       e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
       Sequence of coefficients a_i for i >= 0:
       a_0 = 2, a_1 = 1, a_2 = 2, a_3 = 1, a_4 = 1, a_5 = 4, ...
       Specifically, a_i = 2*(k+1)/3 when i % 3 == 2, and 1 otherwise.

    2. Numerator Recurrence Relation:
       Let n_k be the numerator of the k-th convergent.
       n_0 = a_0 = 2
       n_1 = a_0 * a_1 + 1 = 3
       n_k = a_k * n_{k-1} + n_{k-2}  for k >= 2.

    3. Sum of Numerator Digits:
       Compute 100th numerator n_99 using BigInt arithmetic, then sum decimal digits.

    Time Complexity: O(target) executing in ~0.0001s.
    Space Complexity: O(target) memory for coefficient array.
    """
    # Build continued fraction coefficients a_0..a_{target-1} for e
    a = [2]
    for i in range(1, target):
        if i % 3 == 2:
            a.append(2 * (i + 1) // 3)
        else:
            a.append(1)

    # Base numerators n_0 and n_1
    n0 = a[0]
    n1 = a[0] * a[1] + 1

    # Advance numerator recurrence: n_k = a_k * n_{k-1} + n_{k-2}
    for i in range(2, target):
        n0, n1 = n1, a[i] * n1 + n0

    # Calculate sum of digits of the target-th numerator n1
    digit_sum = sum(int(c) for c in str(n1))

    # Return total digit sum
    return digit_sum


if __name__ == "__main__":
    print(solve())
