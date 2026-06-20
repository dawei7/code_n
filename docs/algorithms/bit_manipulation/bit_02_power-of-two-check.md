# Power of Two Check

| | |
|---|---|
| **ID** | `bit_02` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(1)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Power of Two](https://leetcode.com/problems/power-of-two/) |

## Problem statement

Given an integer `n`, write a function to determine if it is a power of two.
An integer `n` is a power of two, if there exists an integer `x` such that n == 2^x.

**Input:** An integer `n`.
**Output:** A boolean: `True` if `n` is a power of two, `False` otherwise.

## When to use it

- As a one-line magic trick in interviews to demonstrate low-level bit manipulation fluency.
- A foundational property required for solving harder bit manipulation constraints.

## Approach

**1. The Mathematical Property:**
What does a power of two look like in binary?
- 2^0 = 1 -> `0001`
- 2^1 = 2 -> `0010`
- 2^2 = 4 -> `0100`
- 2^3 = 8 -> `1000`

Notice the pattern? A power of two in binary ALWAYS has exactly **one single `1` bit**!

**2. The Bitwise Trick:**
We already know Brian Kernighan's algorithm (`bit_01`)! The operation `n & (n - 1)` erases the rightmost `1` bit from `n`.
If `n` is a power of two, it ONLY has one `1` bit. Therefore, erasing its rightmost `1` bit will completely obliterate the number, turning it into exactly `0`!
If `n` is NOT a power of two, it has multiple `1` bits. Erasing one of them will leave the others intact, so the result will be `> 0`.

**3. Edge Cases:**
Is `0` a power of two? No! There is no x where 2^x = 0.
However, if we do `0 & (0 - 1)`, in most languages this evaluates to `0`, which would falsely trigger our check! Therefore, we must explicitly verify that `n > 0` before doing the bitwise operation.
Similarly, negative numbers cannot be powers of two in this context.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_02: Power of Two Check.

Return True iff the input n is a power of two.
"""


def solve(n):
    """True iff n is a power of two (n >= 1)."""
    return n > 0 and (n & (n - 1)) == 0
```

</details>

## Walk-through

**Example 1:** `n = 8` (`1000`).
1. `8 > 0` (True).
2. `n - 1 = 7` (`0111`).
3. `8 & 7` -> `1000 & 0111 = 0000` (`0`).
4. `0 == 0` (True). Result: `True`. ✓

**Example 2:** `n = 10` (`1010`).
1. `10 > 0` (True).
2. `n - 1 = 9` (`1001`).
3. `10 & 9` -> `1010 & 1001 = 1000` (`8`).
4. `8 == 0` (False). Result: `False`. ✓

**Example 3:** `n = 0`.
1. `0 <= 0` (True). Returns `False` immediately. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(1)$ | $O(1)$ |
| **Worst** | $O(1)$ | $O(1)$ |

This is the fastest possible theoretical execution. It requires exactly one conditional check and one bitwise `AND` operation, running in exactly $O(1)$ CPU cycles.
Space complexity is strictly $O(1)$.

## Variants & optimizations

- **Power of Four:** Given an integer, check if it is a power of 4 (4^0, 4^1, 4^2\dots). A power of 4 is ALWAYS a power of 2, so it must pass the `(n & (n - 1)) == 0` test. Additionally, the single `1` bit must be positioned on an **even index** (0, 2, 4...). We can check this by doing a bitwise `AND` with a mask of alternating bits `01010101...` (`0x55555555`).
  `return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) == n`.

## Real-world applications

- **Memory Allocators:** OS Kernels and memory pools (like `malloc`) often pad memory requests to the nearest power of two to prevent fragmentation. This check verifies if the request is already perfectly aligned.
- **Hash Maps:** The internal array capacity of a HashMap (like Java's `HashMap`) is always maintained as a power of two so that the modulo operation `hash % capacity` can be heavily optimized to a lightning-fast bitwise `AND`: `hash & (capacity - 1)`.

## Related algorithms in cOde(n)

- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Introduces the core `n & (n - 1)` trick used here.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
