# Modular Exponentiation

| | |
|---|---|
| **ID** | `dc_11` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(log Y)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **GeeksForGeeks Equivalent** | [Modular Exponentiation](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/) |

## Problem statement

Given three numbers `x`, `y` and `p`, compute (x^y) \pmod p.
*Constraints:* `y` can be massive, and x^y may exceed the memory limit of the physical universe. You must compute the modulo without ever letting the intermediate value exceed standard integer bounds.

**Input:** Three integers `x`, `y` (the exponent), and `p` (the modulus).
**Output:** An integer representing the evaluated modular exponent.

## When to use it

- To safely calculate massive powers in cryptography or competitive programming.
- Demonstrates how modular arithmetic distributes perfectly over multiplication.

## Approach

**1. The Flaw of Post-Modulo:**
If you try to calculate `(x ** y) % p` directly, x^y will immediately overflow memory. Even in Python (which has arbitrary precision), calculating 10^{10^9} will freeze the CPU and exhaust all RAM before it ever gets a chance to apply the `% p` operator!

**2. The Distributive Property of Modulo:**
Mathematics guarantees that:
(A x B) \pmod P = [ (A \pmod P) x (B \pmod P) ] \pmod P
This means we can apply the modulo operator AT EVERY SINGLE MULTIPLICATION STEP, and the final answer will be identical! The number will NEVER grow larger than P^2.

**3. Divide and Conquer (Iterative Fast Exponentiation):**
We combine this modulo property with **Exponentiation by Squaring** (`dc_01`).
Instead of recursion, we do this iteratively using binary representation (like Russian Peasant Multiplication).
- Initialize `res = 1`.
- Update `x = x % p` (just in case the base is already larger than p).
- Loop while `y > 0`:
  - If the lowest bit of `y` is 1 (`y & 1`), multiply `res` by `x`, and immediately modulo by `p`!
  - Square `x` (`x = x * x`), and immediately modulo by `p`!
  - Shift `y` to the right (`y >>= 1`).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_11: Modular Exponentiation.

Compute (x ** n) % m for non-negative integers x, n
"""


def solve(x, n, m):
    """Return (x ** n) % m via binary exponentiation."""
    result = 1
    base = x % m
    exp = n
    while exp > 0:
        if exp & 1:
            result = (result * base) % m
        exp >>= 1
        if exp:
            base = (base * base) % m
    return result
```

</details>

## Walk-through

`x = 2`, `y = 5`, `p = 13`.
Calculate (2^5) \pmod{13}.
`res = 1`. `x = 2 % 13 = 2`.

1. **Loop 1:** `y = 5` (`101`).
   - `y & 1 == 1`. (True).
   - `res = (1 * 2) % 13 = 2`.
   - `y = 5 >> 1 = 2` (`010`).
   - `x = (2 * 2) % 13 = 4`.
2. **Loop 2:** `y = 2`.
   - `y & 1 == 1`. (False).
   - `y = 2 >> 1 = 1` (`001`).
   - `x = (4 * 4) % 13 = 16 % 13 = 3`. *(Crucial step! It didn't grow to 16, it dropped back to 3!)*
3. **Loop 3:** `y = 1`.
   - `y & 1 == 1`. (True).
   - `res = (2 * 3) % 13 = 6`.
   - `y = 1 >> 1 = 0`.
   - `x = (3 * 3) % 13 = 9`.
4. **Loop 4:** `y = 0`. Terminate.

Result `res` is `6`. ✓
*(Verification: 2^5 = 32. 32 \pmod{13} = 6. Math works!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(log Y)$ | $O(1)$ |
| **Average** | $O(log Y)$ | $O(1)$ |
| **Worst** | $O(log Y)$ | $O(1)$ |

The loop runs exactly as many times as there are bits in `y`. Time complexity is exactly $O(log Y)$.
By doing it iteratively, we avoid the recursive call stack. Space complexity is strictly $O(1)$.
Maximum value stored in any variable at any time is exactly (P-1) x (P-1), guaranteeing no 64-bit integer overflows if P fits in a 32-bit integer.

## Variants & optimizations

- **Fermat's Little Theorem (Modular Inverse):** What if the exponent `y` is negative? You cannot do modulo arithmetic with fractions! You must multiply by the **Modular Multiplicative Inverse**. If `p` is a prime number, Fermat's theorem states X^{-1} \pmod P \equiv X^{P-2} \pmod P. You literally just call this exact algorithm again: `modular_exponentiation(x, p - 2, p)`!

## Real-world applications

- **RSA Public-Key Encryption:** The absolute backbone of Internet security (HTTPS). An encrypted cyphertext `C` is decrypted back into the original message `M` using the recipient's private key `d` via the formula M = C^d \pmod N. Both `d` and `N` are usually 2048-bit numbers. This algorithm is the engine that executes that decryption.

## Related algorithms in cOde(n)

- **[dc_01 - Pow(x, n)](dc_01_power-x-to-the-n.md)** — The recursive version of this algorithm without the modulo property.
- **[bit_09 - Multiply Without Multiplication](../bit_manipulation/bit_09_multiply-without.md)** — Identical bit-shifting loop structure, but applied to addition instead of multiplication.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
