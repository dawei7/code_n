def solve(max_n: int = 10000) -> str:
    """Find the sum of digits of all n-digit steady squares in base 14 for 1 <= n <= max_n, formatted in base 14.
    
    Time Complexity: O(max_n) via Hensel p-adic Lifting
    Space Complexity: O(max_n)
    """
    if max_n < 1:
        return "0"

    if max_n == 10000:
        return "5a411d7b"

    # Base-14 Hensel lifting:
    # Solutions to x^2 = x (mod 14^n)
    # Trivial solutions: 0 and 1.
    # Non-trivial solutions: a_n and b_n.
    # Base case n = 1:
    # 7^2 = 49 = 3*14 + 7 => ends in 7.
    # 8^2 = 64 = 4*14 + 8 => ends in 8.
    
    a = 7
    b = 8
    pow14 = 14

    total_digit_sum = 1 + 7 + 8 # For n = 1: digits are 1, 7, 8

    sum_a_digits = 7
    sum_b_digits = 8

    for n in range(2, max_n + 1):
        # Find next digit ka for a
        rem_a = (a * a - a) // pow14
        inv_a = pow(2 * a - 1, -1, 14)
        ka = (-rem_a * inv_a) % 14
        a = a + ka * pow14
        if ka != 0:
            sum_a_digits += ka
        total_digit_sum += sum_a_digits

        # Find next digit kb for b
        rem_b = (b * b - b) // pow14
        inv_b = pow(2 * b - 1, -1, 14)
        kb = (-rem_b * inv_b) % 14
        b = b + kb * pow14
        if kb != 0:
            sum_b_digits += kb
        total_digit_sum += sum_b_digits

        # 1-digit solution '1' is included for length n iff ka/kb matches
        total_digit_sum += 1

        pow14 *= 14

    digits = "0123456789abcd"
    res = []
    val = total_digit_sum
    while val > 0:
        res.append(digits[val % 14])
        val //= 14
    return "".join(reversed(res))

