# Bitwise AND of Numbers Range

| | |
|---|---|
| **ID** | `bit_11` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(1)$ Time, $O(1)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |

## Problem statement

Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

**Input:** Two integers `left` and `right` (0 \le \text{left} \le \text{right} \le 2^{31} - 1).
**Output:** An integer representing the bitwise AND of the range.

## When to use it

- To demonstrate advanced binary pattern recognition.
- When you need to summarize or mask a massive contiguous range of numbers instantly without looping.

## Approach

**1. The Flaw of Looping:**
The naive approach is to run a `for` loop from `left` to `right`, performing a running `AND` operation.
If `left = 0` and `right = 2147483647`, the loop will execute 2 billion times and throw a Time Limit Exceeded (TLE) error! We need an $O(1)$ mathematical solution.

**2. The Binary Pattern:**
Let's look at the range from `9` to `12`:
`09` = `0000 1001`
`10` = `0000 1010`
`11` = `0000 1011`
`12` = `0000 1100`

If we bitwise AND all of these numbers, what happens?
Any column that has even ONE `0` will collapse to `0` in the final result!
Notice the rightmost bits. As numbers increment, the lower bits flip incredibly fast. Between `9` and `12`, the rightmost 3 bits have all experienced at least one `0` and one `1`. Therefore, they will ALL become `0`!
Now look at the higher bits. The bits `0000 1...` have NEVER changed! They are perfectly identical across all numbers in the range!

**3. The Strategy (Common Prefix):**
The bitwise AND of a continuous range of numbers will simply be the **Longest Common Prefix** of the binary representations of `left` and `right`, with the rest of the bits filled with `0`s!
How do we isolate the common prefix?
We simply right-shift (`>>`) BOTH `left` and `right` simultaneously until they are perfectly equal! We keep track of how many times we shifted them in a counter `shifts`.
Once they are equal, we have found the common prefix! We then left-shift (`<<`) the prefix back up by `shifts` to restore its original magnitude, which naturally fills the lower bits with `0`s!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_11: Bitwise AND of Range.

Given two non-negative integers left and right
"""


def solve(left, right):
    """Return AND of all integers in [left, right] (the common prefix)."""
    shift = 0
    # While left and right differ, shift them both right by 1
    # (and count the shifts) to find the common prefix.
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
```

</details>

## Walk-through

`left = 9` (`1001`), `right = 12` (`1100`). `shifts = 0`.

1. **Loop 1:** `9 < 12`.
   - `left = 9 >> 1 = 4` (`100`)
   - `right = 12 >> 1 = 6` (`110`)
   - `shifts = 1`
2. **Loop 2:** `4 < 6`.
   - `left = 4 >> 1 = 2` (`10`)
   - `right = 6 >> 1 = 3` (`11`)
   - `shifts = 2`
3. **Loop 3:** `2 < 3`.
   - `left = 2 >> 1 = 1` (`1`)
   - `right = 3 >> 1 = 1` (`1`)
   - `shifts = 3`
4. **Loop 4:** `1 < 1` FALSE. Loop terminates.

**Final Step:**
- Return `left << shifts` -> `1 << 3` = `8` (`1000`).

Result is `8`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(1)$ | $O(1)$ |
| **Worst** | $O(1)$ | $O(1)$ |

The `while` loop executes exactly as many times as there are differing bits in the binary strings. For a 32-bit integer, this loop runs at most 32 times.
Since 32 operations is a constant ceiling regardless of the actual numerical difference between `left` and `right` (even if the difference is 2 billion), the time complexity is strictly $O(1)$.
Space complexity is $O(1)$.

## Variants & optimizations

- **Brian Kernighan's Variant:** Instead of right-shifting, we can use the trick that erases the lowest set bit! While `left < right`, we just do `right = right & (right - 1)`. This violently chops off the fluctuating lower bits of `right` until it is forced down to perfectly match `left` (or drop below it, matching the common prefix). This eliminates the need for a `shifts` counter entirely! `return right`.

## Real-world applications

- **Subnet Masking (CIDR Notation):** In IP networking, determining the network address that a range of IP addresses belongs to is mathematically identical to finding the longest common binary prefix of the lowest and highest IPs in the range. The resulting bitwise AND *is* the Subnet Mask!

## Related algorithms in cOde(n)

- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Explains the `n & (n - 1)` trick used in the optimized variant.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
