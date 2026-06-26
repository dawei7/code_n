# Modular Exponentiation (Binary Exponentiation)

| | |
|---|---|
| **ID** | `math_03` |
| **Category** | math |
| **Complexity (required)** | $O(log E)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Pow(x, n)](https://leetcode.com/problems/powx-n/) |

## Problem statement

Given a base B, an exponent E, and a modulo M.
Calculate (B^E) \pmod M efficiently.
(If the problem does not specify a modulo, assume M = \infty to just calculate B^E).

**Input:** Three integers `B`, `E`, and `M`.
**Output:** An integer representing the result.

## When to use it

- To calculate massive exponents where standard $O(E)$ multiplication `for i in range(E)` would Time Limit Exceed.
- When B^E is so astronomically large (e.g. 10^{1000}) that it would crash the language's memory if you didn't apply the modulo M dynamically during calculation.

## Approach

**1. The Flaw of Linear Multiplication:**
To calculate 3^{10}, you multiply 3 x 3 x 3... ten times. If E = 10^9, this requires one billion operations!

**2. The Power of Halving (Divide and Conquer):**
Notice that 3^{10} can be split exactly in half!
3^{10} = 3^5 x 3^5.
If we calculate 3^5 just ONCE and store it in a variable X, we can get 3^{10} by simply doing X x X. We instantly skipped 4 multiplications!
What about an odd exponent like 3^5? It doesn't split evenly.
But we can extract one base out: 3^5 = 3 x 3^4.
And 3^4 is even! It perfectly splits into 3^2 x 3^2.

**3. The Binary Exponentiation Algorithm:**
We can evaluate this from the bottom up by looking at the binary representation of the exponent E.
We maintain a running `result` (initialized to 1).
While E > 0:
- If E is odd (i.e., `E % 2 == 1`), we multiply our running `result` by the current `base`.
- Then, we absolutely MUST square our `base` (B = B x B) because we are moving to the next power of 2!
- Finally, we integer-divide our exponent in half (E = E // 2).

**4. The Modulo Injection:**
Mathematical property of modulo: (X x Y) \pmod M = ((X \pmod M) x (Y \pmod M)) \pmod M.
Because of this, we can freely apply `% M` to our `result` and our `base` at every single multiplication step! This perfectly prevents the variables from ever exceeding the size of M^2, making it memory-safe for any language.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_03: Modular Exponentiation.

Repeated squaring. Maintain a result and a base. At each bit
of exp, square the base; if the bit is set, multiply the
result by the base. Take mod after every multiplication to
keep numbers small. O(log exp) time.
"""


def solve(base, exp, mod):
    if mod == 1:
        return 0
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result
```

</details>

## Walk-through

Calculate 3^{13} \pmod{100}.
B = 3, E = 13, M = 100. `result = 1`.
Binary of 13 is `1101` (8 + 4 + 1).

1. `E = 13`. Odd!
   - `result = (1 * 3) % 100 = 3`.
   - `B = (3 * 3) % 100 = 9`.
   - `E = 13 // 2 = 6`.
2. `E = 6`. Even.
   - `B = (9 * 9) % 100 = 81`.
   - `E = 6 // 2 = 3`.
3. `E = 3`. Odd!
   - `result = (3 * 81) % 100 = 243 % 100 = 43`.
   - `B = (81 * 81) % 100 = 6561 % 100 = 61`.
   - `E = 3 // 2 = 1`.
4. `E = 1`. Odd!
   - `result = (43 * 61) % 100 = 2623 % 100 = 23`.
   - `B = (61 * 61) % 100 = 3721 % 100 = 21`.
   - `E = 1 // 2 = 0`.
5. `E = 0`. Loop terminates!

Result: `23`. ✓
*(Calculation verification: 3^{13} = 1594323. Modulo 100 is indeed `23`! We calculated it in exactly 4 loop iterations instead of 13).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log E)$ | $O(1)$ |
| **Average** | $O(\log E)$ | $O(1)$ |
| **Worst** | $O(\log E)$ | $O(1)$ |

Because we divide the exponent E by 2 at every single step, the `while` loop executes exactly \lfloorlog_2(E)\rfloor + 1 times. The time complexity is strictly $O(log E)$. This turns a billion operations ($O(10^9)$) into just 30 operations ($O(log_2(10^9)$))!
The space complexity is $O(1)$ for the iterative approach.

## Variants & optimizations

- **Matrix Exponentiation:** You can apply the EXACT same halving logic to Square Matrices! If you want to compute the N-th Fibonacci number in $O(\log N)$ time, you can define a state transition matrix and exponentiate it to the power of N using this exact `while` loop! You just replace the scalar multiplication `*` with a Matrix Multiplication function!

## Real-world applications

- **Diffie-Hellman Key Exchange:** The mathematical core of secure internet traffic (HTTPS/TLS) relies on two computers securely agreeing on a secret key over a public network. This is done by transmitting massive numbers using Modular Exponentiation g^a \pmod p, where p is a 2048-bit prime.

## Related algorithms in cOde(n)

- **[math_08 - Modular Multiplicative Inverse](math_08_modular-multiplicative-inverse.md)** — If you need to perform Modular *Division* (e.g. (A / B) \pmod M), you must calculate (A x B^{-1}) \pmod M. Fermat's Little Theorem states B^{-1} \equiv B^{M-2} \pmod M. To calculate B^{M-2}, you use this exact Modular Exponentiation algorithm!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
