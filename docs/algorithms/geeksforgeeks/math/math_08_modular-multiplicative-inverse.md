# Modular Multiplicative Inverse

| | |
|---|---|
| **ID** | `math_08` |
| **Category** | math |
| **Complexity (required)** | $O(log M)$ Time, $O(1)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Modular Multiplicative Inverse](https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/) |

## Problem statement

Given an integer A and a modulo M. Find the modular multiplicative inverse of A modulo M.
The modular inverse is an integer X such that:
(A x X) \equiv 1 \pmod M
The value of X must be in the range [1, M-1]. If the inverse does not exist, return `-1`.

**Input:** Two integers `A` and `M`.
**Output:** An integer `X`.

## When to use it

- **Modular Division:** In programming, `(A + B) % M` and `(A * B) % M` are perfectly safe. But `(A / B) % M` is MATHEMATICALLY INVALID! You cannot apply modulo to fractions. To perform modular division \frac{A}{B} \pmod M, you MUST rewrite it as (A x B^{-1}) \pmod M, where B^{-1} is the Modular Multiplicative Inverse of B!
- Used extensively in Combinatorics (e.g. calculating `nCr % M` requires dividing by factorials).

## Approach 1: Fermat's Little Theorem (Easier, but M MUST be prime)

Fermat's Little Theorem states that if M is a prime number, then for any integer A not divisible by M:
A^{M-1} \equiv 1 \pmod M

If we divide both sides by A, we get:
A^{M-2} \equiv A^{-1} \pmod M

This is an incredible shortcut! The inverse A^{-1} is literally just A raised to the power of M-2!
We can calculate A^{M-2} \pmod M in $O(log M)$ time using **Modular Exponentiation (`math_03`)**.
*Constraint:* This ONLY works if M is prime. If M is composite (e.g., M=100), Fermat's Little Theorem completely fails.

## Approach 2: Extended Euclidean Algorithm (Works for ANY M)

What if M is not prime? We return to the definition:
(A x X) \equiv 1 \pmod M

By the definition of modulo, if something leaves a remainder of 1 when divided by M, it means it is a multiple of M, plus 1.
A \cdot X = M \cdot Y + 1
Rearranging:
A \cdot X - M \cdot Y = 1

Does this equation look familiar? It is Bézout's Identity: A \cdot x + B \cdot y = \text{GCD}(A, B)!
In our equation, the GCD is `1`!
This proves that a modular inverse ONLY EXISTS if A and M are coprime (their GCD is 1).
If \text{GCD}(A, M) = 1, we just run the **Extended Euclidean Algorithm (`math_07`)** on A and M. The coefficient `x` returned by the algorithm is literally our answer!

*(Note: The algorithm might return a negative `x`. Because we are in modulo arithmetic, we just add M to it to make it positive: `(x % M + M) % M`).*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_08: Modular Multiplicative Inverse.

Given a and m (with gcd(a, m) = 1), find x such
"""


def solve(a, m):
    """Return a^-1 mod m using extended Euclidean."""
    if m == 1:
        return 0
    # Reduce a mod m first.
    a = a % m
    if a == 0:
        return 0  # no inverse
    # Extended gcd of (a, m).
    old_r, r = a, m
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    # old_r = gcd(a, m); old_s is the coefficient of a.
    if old_r != 1:
        return 0  # no inverse
    # Normalize to [0, m).
    return old_s % m
```

</details>

## Walk-through

Find inverse of A=3 modulo M=11.

**Method 1 (Fermat):**
Since 11 is prime: Calculate 3^{11-2} \pmod{11} -> 3^9 \pmod{11}.
3^2 = 9.
3^4 = 81 \equiv 4 \pmod{11}.
3^8 = 16 \equiv 5 \pmod{11}.
3^9 = 3^8 x 3^1 = 5 x 3 = 15 \equiv 4 \pmod{11}.
Result: `4`. ✓
Check: (3 x 4) \pmod{11} = 12 \pmod{11} = 1. It works!

**Method 2 (Extended Euclidean):**
A = 3, M = 11.
1. `ext_gcd(3, 11)` calls `ext_gcd(11, 3)`.
2. `ext_gcd(11, 3)` calls `ext_gcd(3, 2)`.
3. `ext_gcd(3, 2)` calls `ext_gcd(2, 1)`.
4. `ext_gcd(2, 1)` calls `ext_gcd(1, 0)`. (Base case returns `1, 1, 0`).
5. Unwinding:
   - `ext_gcd(2, 1)`: x=0, y=1-(2//1)*0 = 1. Returns `1, 0, 1`.
   - `ext_gcd(3, 2)`: x=1, y=0-(3//2)*1 = -1. Returns `1, 1, -1`.
   - `ext_gcd(11, 3)`: x=-1, y=1-(11//3)*-1 = 4. Returns `1, -1, 4`.
   - `ext_gcd(3, 11)`: x=4, y=-1-(3//11)*4 = -1. Returns `1, 4, -1`.

Result `x = 4`. It's positive, so `4 % 11 = 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log M)$ | $O(1)$ or $O(\log M)$ |
| **Worst** | $O(\log M)$ | $O(1)$ or $O(\log M)$ |

Fermat's method relies on Modular Exponentiation, which takes $O(log(\text{Exponent})$) -> $O(log M)$ time, and $O(1)$ space.
The Extended Euclidean method takes $O(log(\min(A, M)$)) -> $O(log A)$ time, and $O(log A)$ space for the recursion stack.

## Variants & optimizations

- **Array Inverse Pre-computation:** If you need to find the inverse of *every* number from 1 to N modulo M, calling `O(\log M)` for each number takes $O(N log M)$. There is a DP mathematical trick that calculates all N inverses in $O(N)$ linear time!
`inv[i] = M - (M // i) * inv[M % i] % M`

## Real-world applications

- **Cryptography:** Used everywhere in public-key cryptography algorithms (RSA, Diffie-Hellman, Elliptic Curve) where operations take place in massive finite fields modulo P.

## Related algorithms in cOde(n)

- **[math_03 - Modular Exponentiation](math_03_modular-exponentiation.md)** — The dependency for Fermat's Little Theorem.
- **[math_07 - Extended Euclidean](math_07_extended-euclidean-algorithm.md)** — The dependency for the universal approach.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
