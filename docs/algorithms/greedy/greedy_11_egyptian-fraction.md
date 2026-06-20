# Egyptian Fraction

| | |
|---|---|
| **ID** | `greedy_11` |
| **Category** | greedy |
| **Complexity (required)** | $O(log(denominator)$) Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 2/10 |
| **GeeksForGeeks Equivalent** | [Greedy Algorithm for Egyptian Fraction](https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/) |

## Problem statement

Every positive fraction \frac{N}{D} (where N < D) can be represented as sum of unique unit fractions. A unit fraction is a fraction whose numerator is 1 and whose denominator is a positive integer.
For example, \frac{2}{3} = \frac{1}{2} + \frac{1}{6}.
Given N and D, find an Egyptian Fraction representation. (Note: there can be multiple valid representations, any valid sequence of unit fractions is acceptable).

**Input:** Two integers, `numerator` and `denominator`.
**Output:** A list of integers representing the denominators of the unit fractions.

## When to use it

- Mathematical trivia / specific math puzzle interviews.
- Uses a pure Greedy algorithm developed by Fibonacci.

## Approach

**The Greedy Choice (Fibonacci's Algorithm):**
At every step, we want to subtract the *largest possible unit fraction* from our current fraction.
How do we find the largest unit fraction \frac{1}{X} that is strictly \le \frac{N}{D}?
We just take the ceiling of \frac{D}{N}!
X = \lceil \frac{D}{N} \rceil.

Once we find X, we subtract \frac{1}{X} from \frac{N}{D}.
\frac{N}{D} - \frac{1}{X} = \frac{N \cdot X - D}{D \cdot X}.
This new fraction becomes our new \frac{N}{D}. We repeat the process until the numerator N becomes 1 (or 0).

**Why it works:**
Fibonacci mathematically proved that the numerator N in the remainder strictly decreases with every step. Therefore, the algorithm is guaranteed to terminate in a finite number of steps, yielding exactly unique unit fractions.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_11: Egyptian Fraction.

Every positive rational number ``p/q`` can be written as the sum
of distinct unit fractions (1/d). The greedy algorithm picks the
smallest unit fraction not smaller than the remainder, which is
``1 / ceil(q / p)``. Stop when the remainder hits zero; cap the
loop at q+1 steps so a degenerate input can't run forever.
"""


def solve(p, q):
    if p <= 0 or q <= 0:
        return []
    result = []
    for _ in range(q + 1):
        if p == 0:
            break
        d = (q + p - 1) // p  # ceil(q / p)
        result.append(d)
        p = p * d - q
        q = q * d
        # Reduce to keep numbers small.
        from math import gcd
        g = gcd(p, q) or 1
        p //= g
        q //= g
    return result
```

</details>

## Walk-through

`n = 6`, `d = 14`. (Fraction \frac{6}{14}).

1. `x = ceil(14 / 6) = ceil(2.33) = 3`.
   - Append `3`. (Our first unit fraction is \frac{1}{3}).
   - Remainder: \frac{6}{14} - \frac{1}{3} = \frac{18 - 14}{42} = \frac{4}{42}.
   - Simplify \frac{4}{42} -> \frac{2}{21}.
   - New state: `n = 2`, `d = 21`.
2. `x = ceil(21 / 2) = ceil(10.5) = 11`.
   - Append `11`. (Our next unit fraction is \frac{1}{11}).
   - Remainder: \frac{2}{21} - \frac{1}{11} = \frac{22 - 21}{231} = \frac{1}{231}.
   - Simplify: Already \frac{1}{231}.
   - New state: `n = 1`, `d = 231`.
3. `x = ceil(231 / 1) = 231`.
   - Append `231`.
   - Remainder: \frac{1}{231} - \frac{1}{231} = 0.
   - New state: `n = 0`, loop terminates.

Result: `[3, 11, 231]`.
Verification: \frac{1}{3} + \frac{1}{11} + \frac{1}{231} = \frac{77 + 21 + 1}{231} = \frac{99}{231} = \frac{9 x 11}{21 x 11} = \frac{9}{21} = \frac{3}{7} = \frac{6}{14}. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The number of terms (and thus loop iterations) is generally bounded by $O(\log N)$ or $O(N)$ depending on the specific arithmetic properties of the numerator. Each iteration involves $O(log(\min(n,d)$)) time to compute the GCD for simplification.
Space complexity is $O(1)$ to store local variables, ignoring the output array.

## Variants & optimizations

- **Sylvester's Sequence:** If you run this algorithm on \frac{N}{D} = \frac{N}{N+1}, it generates Sylvester's sequence, where the denominators grow double-exponentially! If you don't simplify the fraction using `math.gcd` at every step, the variables `n` and `d` will quickly overflow 64-bit integer limits.

## Real-world applications

- **Ancient Egyptian Mathematics:** The Rhind Mathematical Papyrus (1650 BC) shows ancient Egyptians lacked a notation for general fractions (like 3/4). They ONLY had symbols for unit fractions (like 1/2, 1/3, 1/4). To write 3/4, they were literally forced to use this algorithm and write it as "1/2 and 1/4".

## Related algorithms in cOde(n)

- **[math_01 - GCD (Euclidean Algorithm)](../math/math_01_gcd.md)** — The Euclidean algorithm running under the hood of `math.gcd()`, required to prevent integer overflow.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
