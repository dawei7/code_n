# Karatsuba Multiplication

| | |
|---|---|
| **ID** | `dc_04` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N^1.58)$ Time, $O(N)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Karatsuba algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm) |

## Problem statement

Given two extremely large numbers `X` and `Y` represented as strings (or massive integer arrays), multiply them. Assume the numbers have N digits and cannot fit into standard 64-bit integer variables.
Return the product.

**Input:** Two integers (or strings) `x` and `y`.
**Output:** Their product.

## When to use it

- To multiply exceptionally large numbers (BigInts) faster than the traditional "Grade School" multiplication method.
- A classic theoretical computer science problem demonstrating how algebra can mathematically eliminate recursive calls to achieve sub-quadratic time bounds.

## Approach

**1. The Grade School Approach ($O(N^2)$):**
When we multiply two N-digit numbers by hand, we multiply every digit of the top number by every digit of the bottom number. For two 4-digit numbers, this requires 4 x 4 = 16 single-digit multiplications. This is firmly $O(N^2)$ time complexity.

**2. Naive Divide and Conquer ($O(N^2)$):**
Let's split both numbers in half.
If X = 1234, we can write it as 12 x 10^2 + 34.
Let X = a x 10^{N/2} + b
Let Y = c x 10^{N/2} + d

If we multiply them algebraically:
X x Y = (a \cdot 10^{N/2} + b) x (c \cdot 10^{N/2} + d)
X x Y = ac \cdot 10^N + (ad + bc) \cdot 10^{N/2} + bd

To solve this equation, we need to calculate 4 separate recursive multiplications: ac, ad, bc, and bd.
According to the Master Theorem, T(N) = 4T(N/2) + $O(N)$ evaluates to exactly $O(N^2)$. We haven't improved the speed at all!

**3. The Karatsuba Magic Trick ($O(N^{1.58})$):**
In 1960, Anatoly Karatsuba realized we don't actually need to calculate ad and bc separately!
Notice that:
(a + b) x (c + d) = ac + ad + bc + bd

If we subtract ac and bd from that result, we are left with exactly (ad + bc)!
(ad + bc) = (a + b)(c + d) - ac - bd

Why is this revolutionary?
Because we already HAVE TO calculate ac and bd for the outer parts of the main equation!
Instead of 4 recursive multiplications (ac, ad, bc, bd), Karatsuba only requires **3** recursive multiplications:
1. Z_0 = ac
2. Z_1 = bd
3. Z_2 = (a+b) x (c+d)

The middle term is then just Z_2 - Z_0 - Z_1.
The new recurrence relation is T(N) = 3T(N/2) + $O(N)$.
By the Master Theorem, the time complexity is $O(N^{log_2(3)$}), which is roughly $O(N^{1.585})$!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_04: Karatsuba Multiplication.

Multiply two non-negative integers using Karatsuba's
"""


def solve(x, y, n):
    """Karatsuba multiplication: x * y.

    Recursive 3-way multiplication beats the schoolbook 4-way
    multiplication by trading one extra add/subtract for one
    fewer recursive product.
    """
    if x < 10 or y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    half = m // 2
    pow10 = 10 ** half
    a, b = divmod(x, pow10)
    c, d = divmod(y, pow10)
    ac = solve(a, c, n)
    bd = solve(b, d, n)
    ad_bc = solve(a + b, c + d, n) - ac - bd
    return ac * 10 ** (2 * half) + ad_bc * 10 ** half + bd
```

</details>

## Walk-through

`x = 1234`, `y = 5678`.
`n = 4`, `m = 2`.
`a = 12`, `b = 34`.
`c = 56`, `d = 78`.

1. **Calculate Z_0 = a x c:**
   `z0 = karatsuba(12, 56)`. *(Recurses down to single digits and returns 672)*.
2. **Calculate Z_1 = b x d:**
   `z1 = karatsuba(34, 78)`. *(Returns 2652)*.
3. **Calculate Z_2 = (a+b) x (c+d):**
   `z2 = karatsuba(46, 134)`. *(Returns 6164)*.

4. **Calculate Middle Term (ad + bc):**
   `middle_term = z2 - z0 - z1` = 6164 - 672 - 2652 = 2840.
   *(Check: 12 x 78 + 34 x 56 = 936 + 1904 = 2840. The math works perfectly!)*

5. **Reassemble:**
   `Result` = z_0 x 10^4 + middle\_term x 10^2 + z_1
   `Result` = 672 x 10000 + 2840 x 100 + 2652
   `Result` = 6720000 + 284000 + 2652 = 7006652.

Result is `7006652`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^1.58)$ | $O(N)$ |
| **Average** | $O(N^1.58)$ | $O(N)$ |
| **Worst** | $O(N^1.58)$ | $O(N)$ |

The algorithm makes 3 recursive calls on inputs of half the size.
By the Master Theorem, T(N) = 3T(N/2) + $O(N)$ -> $O(N^{log_2(3)$}) ~= $O(N^{1.585})$.
Space complexity is $O(\log N)$ for the recursion depth, but because creating new massive integers/strings at each depth takes $O(N)$ space, the overall space complexity is tightly bounded at $O(N)$.

## Variants & optimizations

- **Base Thresholding:** For very small numbers (e.g. N < 32), the overhead of recursion, function calls, and splitting is actually *slower* than just doing the hardware-accelerated Grade School $O(N^2)$ multiplication! Modern BigInt libraries (like Python's) use Grade School for small numbers, switch to Karatsuba for medium numbers, and switch to Toom-Cook or Schönhage-Strassen (FFT) for numbers with millions of digits.
- **Binary Splitting:** Instead of splitting by powers of 10, real implementations split by powers of 2 (or 2^{32}) to allow the use of lightning-fast bitwise shifts (`>>`) instead of expensive division (`//`) and modulo (`%`).

## Real-world applications

- **Cryptography & BigInt Libraries:** Almost all standard library implementations of arbitrary-precision integers (like Python's `int` or Java's `BigInteger`) automatically engage Karatsuba logic under the hood when multiplying extremely large numbers.

## Related algorithms in cOde(n)

- **[dc_06 - Strassen Matrix Multiplication](dc_06_strassen-matrix-multiplication.md)** — The exact same "algebraic elimination of a recursive call" concept, but applied to 2D matrices to reduce $O(N^3)$ down to $O(N^{2.8})$.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
