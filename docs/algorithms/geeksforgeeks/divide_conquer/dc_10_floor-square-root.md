# Sqrt(x) (Floor Square Root)

| | |
|---|---|
| **ID** | `dc_10` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) |

## Problem statement

Given a non-negative integer `x`, compute and return the square root of `x`.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

**Input:** A non-negative integer `x`.
**Output:** An integer representing the floor of the square root.

## When to use it

- To prove you can apply Binary Search to a continuous mathematical range, rather than an array of discrete objects.
- It introduces the concept of searching an "Answer Space" (Decrease and Conquer).

## Approach

**1. The "Answer Space":**
We don't have an array to search through. But we do know that the square root of X MUST lie somewhere between 0 and X.
Therefore, our "array" is literally just the continuous sequence of integers [0, 1, 2 \dots X].
Because this sequence is inherently sorted, we can apply Binary Search!

**2. The Binary Search Logic:**
- `low = 0`, `high = x`.
- Find `mid`.
- Calculate `square = mid * mid`.
- If `square == x`: We found the exact square root! Return `mid`.
- If `square < x`: `mid` is too small. But wait, since we want the *floor* of the square root, `mid` might actually be the correct answer if the next integer's square is too big! We store `mid` in a variable `ans`, and then search higher (`low = mid + 1`).
- If `square > x`: `mid` is too big. The answer MUST be smaller. Search lower (`high = mid - 1`).

**3. Edge Cases:**
If X = 0 or X = 1, the square root is just X. You can handle this directly at the top of the function to avoid mathematical anomalies.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_10: Floor Square Root.

Given a non-negative integer n, return floor(sqrt(n)).
"""


def solve(n):
    """Return floor(sqrt(n)) via binary search (D&C style)."""
    if n < 2:
        return n
    lo, hi, res = 1, n, 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq <= n:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res
```

</details>

## Walk-through

`x = 8`. `low = 1`, `high = 4` (since 8/2=4).

1. **Loop 1:**
   - `mid = (1 + 4) // 2 = 2`.
   - `square = 2 * 2 = 4`.
   - `4 < 8`. It's a candidate! `ans = 2`.
   - Move higher: `low = 2 + 1 = 3`.
2. **Loop 2:**
   - `mid = (3 + 4) // 2 = 3`.
   - `square = 3 * 3 = 9`.
   - `9 > 8`. Strictly too large.
   - Move lower: `high = 3 - 1 = 2`.
3. **Loop 3:**
   - `low (3) <= high (2)` is FALSE. Loop ends.

Result `ans` is `2`. ✓ (Since 2^2 = 4 and 3^2 = 9, the floor of \sqrt{8} is 2).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(log x)$ | $O(1)$ |
| **Worst** | $O(log x)$ | $O(1)$ |

The search space starts at x/2 and is divided in half repeatedly. The time complexity is exactly $O(log X)$.
No extra arrays are allocated. Space complexity is $O(1)$.

## Variants & optimizations

- **Newton-Raphson Method:** A calculus-based optimization that converges quadratically rather than logarithmically. Given an initial guess r = x, you repeatedly update the guess using r = \frac{1}{2} (r + \frac{x}{r}) until r x r \le x. It requires floating point division but is blindingly fast and mathematically elegant.
- **Finding Exact Floating-Point Square Root:** If the question asks for the square root to 5 decimal places instead of the floor, you cannot use integer division. You initialize `low = 0.0`, `high = max(1.0, x)`. You loop `while (high - low) > 0.00001` (your precision threshold) and calculate `mid = (low + high) / 2.0`.

## Real-world applications

- **Computer Graphics (Lighting Models):** Calculating the Euclidean distance vector between a light source and a pixel normal requires massive amounts of Square Root calls. Hardware graphics pipelines often use extremely clever bit-hacks (like the famous Fast Inverse Square Root `0x5f3759df` from Quake III) to approximate Newton's Method instantly.

## Related algorithms in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — The exact identical core logic, just applied to a virtual integer space rather than an array.
- **[math_01 - Fast Exponentiation](../math/math_01_fast-exponentiation.md)** — Another mathematical divide-and-conquer algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
