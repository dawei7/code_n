# Extended Euclidean Algorithm

| | |
|---|---|
| **ID** | `math_07` |
| **Category** | math |
| **Complexity (required)** | $O(log(min(A, B)$)) Time, $O(log(min(A, B)$)) Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) |

## Problem statement

Given two integers A and B. Find their Greatest Common Divisor (GCD).
Additionally, find the integer coefficients x and y such that:
A \cdot x + B \cdot y = \text{GCD}(A, B)
(This equation is known as Bézout's identity).

**Input:** Two integers `a` and `b`.
**Output:** A tuple of three integers `(gcd, x, y)`.

## When to use it

- You almost never use this just to find the GCD.
- You use this specifically because you desperately need the coefficients x and y to solve Linear Diophantine Equations or find the Modular Multiplicative Inverse (`math_08`).

## Approach

**1. The Recursive GCD Foundation:**
Recall the standard Euclidean algorithm (`math_01`): \text{GCD}(A, B) = \text{GCD}(B, A \pmod B).
The base case is when B = 0. In this case, \text{GCD}(A, 0) = A.
If we plug this base case into Bézout's identity:
A \cdot x + 0 \cdot y = A.
Clearly, this equation is solved when **x = 1** and **y = 0**!
This gives us our base case coefficients!

**2. The Unwinding Math (The "Extended" part):**
Suppose our recursive call `extended_gcd(B, A % B)` successfully returns the tuple `(gcd, x1, y1)`.
This means we mathematically know that:
B \cdot x_1 + (A \pmod B) \cdot y_1 = \text{GCD}

We want to rewrite this equation so it looks like A \cdot x + B \cdot y.
How can we rewrite (A \pmod B)?
In integer arithmetic, A \pmod B = A - B \cdot \lfloor \frac{A}{B} \rfloor.
Substitute this into the equation:
B \cdot x_1 + (A - B \cdot \lfloor \frac{A}{B} \rfloor) \cdot y_1 = \text{GCD}

Expand and group by A and B:
B \cdot x_1 + A \cdot y_1 - B \cdot \lfloor \frac{A}{B} \rfloor \cdot y_1 = \text{GCD}
A \cdot (y_1) + B \cdot (x_1 - \lfloor \frac{A}{B} \rfloor \cdot y_1) = \text{GCD}

Look at the grouping! We have perfectly matched the format A \cdot x + B \cdot y!
Therefore, the new coefficients we pass up the recursion tree are:
- x = y_1
- y = x_1 - \lfloor \frac{A}{B} \rfloor \cdot y_1

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_07: Extended Euclidean Algorithm.

Given two non-negative integers a and b (not both
"""


def solve(a, b):
    """Extended Euclidean: a*x + b*y = gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t
```

</details>

## Walk-through

`A = 30`, `B = 20`.

1. `extended_gcd(30, 20)`:
   - Calls `extended_gcd(20, 30 % 20)` -> `extended_gcd(20, 10)`.
2. `extended_gcd(20, 10)`:
   - Calls `extended_gcd(10, 20 % 10)` -> `extended_gcd(10, 0)`.
3. `extended_gcd(10, 0)`:
   - Base case! `b == 0`.
   - Returns `(10, 1, 0)`. (gcd=10, x1=1, y1=0).
4. Unwinding to `extended_gcd(20, 10)`:
   - `a = 20`, `b = 10`. `x1 = 1`, `y1 = 0`.
   - `x = y1 = 0`.
   - `y = x1 - (a // b) * y1` -> `1 - (20 // 10) * 0` -> `1 - 2 * 0 = 1`.
   - Returns `(10, 0, 1)`.
5. Unwinding to `extended_gcd(30, 20)`:
   - `a = 30`, `b = 20`. `x1 = 0`, `y1 = 1`.
   - `x = y1 = 1`.
   - `y = x1 - (a // b) * y1` -> `0 - (30 // 20) * 1` -> `0 - 1 * 1 = -1`.
   - Returns `(10, 1, -1)`.

Result: `gcd = 10`, `x = 1`, `y = -1`.
Verify Bézout's identity: 30 \cdot (1) + 20 \cdot (-1) = 30 - 20 = 10. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log(\min(A, B)$)) | $O(\log(\min(A, B)$)) |
| **Worst** | $O(\log(\min(A, B)$)) | $O(\log(\min(A, B)$)) |

The number of recursive calls is exactly identical to the standard Euclidean algorithm, meaning time complexity is bounded by $O(log(\min(A,B)$)).
Because this unwinds from the bottom up, it is natively implemented using recursion, meaning space complexity requires $O(log(\min(A,B)$)) depth on the call stack.
*(It can be implemented iteratively to achieve $O(1)$ space, but the logic is much harder to memorize).*

## Variants & optimizations

- **Linear Diophantine Equations:** If asked to find ANY integer solution (X, Y) to the equation A \cdot X + B \cdot Y = C:
  1. Calculate `gcd, x, y = extended_gcd(A, B)`.
  2. If C is not perfectly divisible by `gcd`, mathematically NO integer solution exists!
  3. If it is divisible, the answer is X = x \cdot (C / \text{gcd}) and Y = y \cdot (C / \text{gcd}).

## Real-world applications

- **Public Key Cryptography:** Absolutely essential for computing the private key `d` in the RSA algorithm, where `d` is the modular multiplicative inverse of `e` modulo \phi(n).

## Related algorithms in cOde(n)

- **[math_01 - GCD Euclidean](math_01_gcd-euclidean.md)** — The simpler, standard GCD algorithm.
- **[math_08 - Modular Multiplicative Inverse](math_08_modular-multiplicative-inverse.md)** — The primary reason the Extended Euclidean algorithm is taught in computer science algorithms.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
