# Karatsuba Multiplication

| | |
|---|---|
| **ID** | `math_04` |
| **Category** | math |
| **Complexity (required)** | $O(N^{1.58})$ Time, $O(\log N)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Karatsuba algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm) |

## Problem statement

Given two massively large integers X and Y with N digits. Calculate their product X x Y.
Standard long multiplication takes $O(N^2)$ time.
Optimize this using Anatoly Karatsuba's Divide and Conquer approach.

**Input:** Two integers X and Y (or string representations of massive numbers).
**Output:** An integer (or string) representing their product.

## When to use it

- When asked to multiply two numbers that exceed standard 64-bit bounds (e.g. 10,000 digits long) faster than the brute-force nested loop approach.
- *Trivia:* Discovered in 1960, this was the FIRST multiplication algorithm ever proven to be asymptotically faster than the $O(N^2)$ method taught in grade school!

## Approach

**1. The Divide Step:**
Suppose we want to multiply two 4-digit numbers: X = 1234 and Y = 5678.
We can split them down the middle into 2-digit halves:
X = 12 \cdot 10^2 + 34 -> X = A \cdot 10^m + B
Y = 56 \cdot 10^2 + 78 -> Y = C \cdot 10^m + D
Where m = N / 2 (half the digits).

**2. The Standard Expansion ($O(N^2)$):**
If we multiply them algebraically:
X x Y = (A \cdot 10^m + B) x (C \cdot 10^m + D)
X x Y = AC \cdot 10^{2m} + (AD + BC) \cdot 10^m + BD

To solve this, we must compute FOUR separate recursive multiplications:
1. AC
2. AD
3. BC
4. BD
Because T(N) = 4T(N/2) + $O(N)$, the Master Theorem yields $O(N^2)$. We haven't improved anything!

**3. The Karatsuba Insight (The Magic Step):**
Karatsuba realized we don't actually need to calculate AD and BC separately! We only care about their SUM: (AD + BC).
What happens if we multiply the sum of the halves together?
(A+B) x (C+D) = AC + AD + BC + BD

Notice that this new product contains exactly the middle term (AD + BC) that we need, plus AC and BD which we *already* have to compute anyway!
Therefore, we can isolate the middle term with subtraction:
(AD + BC) = (A+B) x (C+D) - AC - BD

We now only need THREE recursive multiplications instead of four:
1. Z_2 = AC
2. Z_0 = BD
3. Z_1 = (A+B) x (C+D)
The middle term is just Z_1 - Z_2 - Z_0.
The final equation is:
X x Y = Z_2 \cdot 10^{2m} + (Z_1 - Z_2 - Z_0) \cdot 10^m + Z_0

Because T(N) = 3T(N/2) + $O(N)$, the Master Theorem yields $O(N^{log_2 3})$ ~= $O(N^{1.585})$.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for math_04: Karatsuba Multiplication.

Recursive divide and conquer: split each number into halves,
compute 3 half-sized products (instead of 4), combine.
"""


def solve(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    power = 10 ** half
    a, b = divmod(x, power)
    c, d = divmod(y, power)
    ac = solve(a, c)
    bd = solve(b, d)
    ad_bc = solve(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + ad_bc * power + bd
```

</details>

## Walk-through

X = 1234, Y = 5678. N=4, m=2.
A = 12, B = 34.
C = 56, D = 78.

1. Compute Z_2 = AC = 12 x 56 = 672.
2. Compute Z_0 = BD = 34 x 78 = 2652.
3. Compute Z_1 = (A+B) x (C+D) = (46) x (134) = 6164.
4. Compute middle term: Z_1 - Z_2 - Z_0 = 6164 - 672 - 2652 = 2840.

Reassemble:
= 672 x 10^4 + 2840 x 10^2 + 2652
= 6720000 + 284000 + 2652
= 7006652.

Check: 1234 x 5678 = 7006652. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^{\log_2 3})$ | $O(\log N)$ |
| **Average** | $O(N^{\log_2 3})$ \approx $O(N^{1.58})$ | $O(\log N)$ |
| **Worst** | $O(N^{\log_2 3})$ | $O(\log N)$ |

By reducing 4 recursive branches to 3, the time complexity according to the Master Theorem drops from $O(N^2)$ to $O(N^{1.58})$.
While 1.58 doesn't seem much smaller than 2.0, for a 10,000-digit number, $O(N^2)$ is 100,000,000 operations, while $O(N^{1.58})$ is barely 2,100,000 operations (a 50x speedup).
Space complexity is bounded by the recursion stack depth, which splits N in half at each step, yielding $O(\log N)$ space.

## Variants & optimizations

- **Toom-Cook Multiplication:** Karatsuba splits the number into 2 pieces (reducing 4 mults to 3). Toom-3 splits the number into 3 pieces (reducing 9 mults to 5), yielding $O(N^{1.46})$. Toom-Cook can split into arbitrary K pieces.
- **Schönhage–Strassen Algorithm:** For astronomically massive numbers (e.g. millions of digits), the Fast Fourier Transform (FFT) is used to multiply numbers in $O(N log N log(log N)$) time!

## Real-world applications

- **Python Internal Integer Engine:** Python natively supports infinitely large integers. Under the hood, if you multiply two numbers smaller than 70 decimal digits, Python uses $O(N^2)$ grade-school math. But the exact moment the numbers cross 70 digits, Python's C-backend automatically switches to using the Karatsuba algorithm!

## Related algorithms in cOde(n)

- **[math_05 - Big Integer Addition](math_05_big-integer-add-strings.md)** — The string-based addition logic strictly required to implement Karatsuba in languages that don't support infinite-precision integers natively.
- **[divide_conquer_04 - Merge Sort](../divide_conquer/dc_04_merge-sort.md)** — The classic recursive "split in half and solve" paradigm that Karatsuba leverages.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
