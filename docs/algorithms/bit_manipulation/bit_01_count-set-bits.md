# Count Set Bits (Brian Kernighan's Algorithm)

| | |
|---|---|
| **ID** | `bit_01` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(K)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) |

## Problem statement

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Input:** An unsigned integer `n`.
**Output:** An integer representing the count of '1' bits in `n`.

## When to use it

- To count the set bits (1s) of a number optimally.
- It is the absolute foundation for almost all Bit Manipulation problems.

## Approach

**1. The Naive Approach:**
We could repeatedly check the least significant bit (LSB) using `n & 1`, and then right-shift the number `n >>= 1`. This takes exactly 32 iterations for a 32-bit integer, regardless of whether it has one `1` bit or thirty `1` bits.

**2. Brian Kernighan's Algorithm:**
Can we jump directly from one `1` bit to the next, skipping all the `0`s? Yes!
Consider the mathematical operation `n - 1`. What does subtracting 1 do in binary?
It flips all the bits starting from the rightmost `1` bit to the very end of the number!
For example, if `n = 12` (`1100` in binary):
`n - 1 = 11` (`1011` in binary).
Notice that the rightmost `1` in `n` (at the 2s place) flipped to a `0`, and all the `0`s to its right flipped to `1`s.

If we perform a bitwise AND between `n` and `n - 1`:
`n & (n - 1)`
`1100 & 1011 = 1000`.
The rightmost `1` bit has been completely erased!

**3. The Strategy:**
We simply run `n = n & (n - 1)` in a loop. Every time we execute this line, exactly one `1` bit is deleted. We increment a counter each time.
When `n` hits 0, the loop terminates!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_01: Count Set Bits.

Count the number of 1-bits in the binary
"""


def solve(n):
    """Count the 1-bits in n (Hamming weight)."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

</details>

## Walk-through

`n = 14` (Binary: `1110`). `count = 0`.

1. **Loop 1:**
   - `n != 0`. `count = 1`.
   - `n - 1` = `13` (`1101`).
   - `n = 1110 & 1101 = 1100` (`12`). (The rightmost 1 was erased!)
2. **Loop 2:**
   - `n != 0`. `count = 2`.
   - `n - 1` = `11` (`1011`).
   - `n = 1100 & 1011 = 1000` (`8`).
3. **Loop 3:**
   - `n != 0`. `count = 3`.
   - `n - 1` = `7` (`0111`).
   - `n = 1000 & 0111 = 0000` (`0`).
4. **Loop 4:**
   - `n == 0`. Loop terminates.

Result: `count = 3`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(K)$ | $O(1)$ |
| **Worst** | $O(K)$ | $O(1)$ |

*Where K is the number of '1' bits in the integer.*
In the absolute worst case (a number like `0xFFFFFFFF`), it takes 32 iterations for a 32-bit integer, making it technically $O(1)$ relative to the size of the input number. However, asymptotically, it strictly bounds to $O(K)$ iterations, making it vastly superior to the naive $O(log n)$ shift approach for sparse bitmasks.
Space is strictly $O(1)$.

## Variants & optimizations

- **Built-in Functions:** Most modern languages have hardware-accelerated instructions for this. In Python, use `n.bit_count()`. In C++, use `__builtin_popcount(n)`. In Java, use `Integer.bitCount(n)`. These compile to a single CPU instruction (like `POPCNT` on x86) and execute in literally 1 CPU cycle.
- **Extracting the Lowest Set Bit:** If you only want to *isolate* the lowest set bit instead of erasing it, use `n & -n`. For `n = 12` (`1100`), `n & -n` yields `4` (`0100`). This is heavily used in Fenwick Trees (`fenwick_01`)!

## Real-world applications

- **Cryptography / Hashing:** Calculating the Hamming Distance between two hashes to detect bit-rot, error corruption, or image similarity (e.g. perceptual hashing).
- **Chess Engines (Bitboards):** Instantly calculating how many legal moves a piece has by counting the `1`s on a 64-bit integer board representation.

## Related algorithms in cOde(n)

- **[bit_02 - Power of Two Check](bit_02_power-of-two-check.md)** — Uses the exact same `n & (n - 1)` trick but evaluates it without a loop!
- **[fenwick_01 - Binary Indexed Tree](../fenwick/fenwick_01_binary-indexed-tree.md)** — Relies on extracting the lowest set bit (`n & -n`) to calculate tree array offsets.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
