# Minimum Bit Flips to Convert Number

| | |
|---|---|
| **ID** | `bit_06` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(K)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) |

## Problem statement

A bit flip of a number `x` is choosing a bit in the binary representation of `x` and flipping it from either `0` to `1` or `1` to `0`.
Given two integers `start` and `goal`, return the minimum number of bit flips to convert `start` to `goal`.

**Input:** Two integers `start` and `goal`.
**Output:** An integer representing the minimum number of bit flips.

## When to use it

- To measure the **Hamming Distance** between two integers.
- A classic, trivially simple combination of two fundamental bit manipulation techniques (XOR + Counting Set Bits).

## Approach

**1. Identifying the Differing Bits:**
If we want to know how many bits we need to flip to turn `A` into `B`, we first need to identify EXACTLY which bits are different between `A` and `B`.
Which bitwise operator outputs a `1` if two bits are different, and a `0` if they are the same?
**XOR (`^`)!**
If we calculate `difference = start ^ goal`, the binary representation of `difference` will have a `1` at every position where `start` and `goal` disagreed, and a `0` where they agreed.

**2. Counting the Differing Bits:**
Now that we have a number (`difference`) representing all the disagreements, the problem is literally just "Count the number of `1` bits in this integer".
We already solved this using Brian Kernighan's Algorithm (`bit_01`)!
We simply repeatedly execute `difference = difference & (difference - 1)` and increment a counter until `difference` hits 0.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_06: Bit Flips to Convert.

Given two non-negative integers a and b, return
"""


def solve(a, b):
    """Return the number of bit flips to convert a to b (Hamming distance)."""
    return bin(a ^ b).count("1")
```

</details>

## Walk-through

`start = 10` (`1010`), `goal = 7` (`0111`).

1. **Calculate XOR:**
   - `difference = 1010 ^ 0111 = 1101` (`13`).
   - The differing bits are highlighted by the `1`s.
2. **Count Set Bits (13 = 1101):**
   - Loop 1: `difference > 0`. `flips = 1`.
     `difference = 1101 & 1100 = 1100` (`12`).
   - Loop 2: `difference > 0`. `flips = 2`.
     `difference = 1100 & 1011 = 1000` (`8`).
   - Loop 3: `difference > 0`. `flips = 3`.
     `difference = 1000 & 0111 = 0000` (`0`).
   - Loop 4: `difference == 0`. Loop terminates.

Result `flips = 3`. ✓ (Bits 0, 1, and 3 needed flipping).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(K)$ | $O(1)$ |
| **Worst** | $O(K)$ | $O(1)$ |

*Where K is the number of bits that are different (the Hamming Distance).*
The XOR takes exactly 1 CPU cycle. The Brian Kernighan loop takes K iterations, making it $O(K)$.
If using built-in hardware instructions like `.bit_count()`, the total time collapses to strictly $O(1)$.
Space complexity is strictly $O(1)$.

## Variants & optimizations

- **Hamming Distance between strings:** If `start` and `goal` are strings of identical length (e.g., DNA sequences `"GATTACA"` and `"GCATACG"`), you cannot XOR them directly. You must iterate through the strings character by character and count `if start[i] != goal[i]`. This takes $O(N)$ time.

## Real-world applications

- **Error-Correcting Codes:** In telecommunications (like Wi-Fi or 5G), the Hamming Distance calculates exactly how much noise/corruption occurred during packet transmission, which determines if a forward-error correction (like a Reed-Solomon code) can recover the data or if a retransmission is needed.
- **Machine Learning Classification:** Finding the K-Nearest Neighbors (KNN) in categorical spaces by measuring the Hamming Distance between categorical one-hot encoded bit-vectors.

## Related algorithms in cOde(n)

- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — The core foundational algorithm utilized here.
- **[bit_03 - Single Number (XOR)](bit_03_single-number-xor.md)** — Further exploration of XOR properties.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
