# Single Number III

| | |
|---|---|
| **ID** | `bit_05` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Single Number III](https://leetcode.com/problems/single-number-iii/) |

## Problem statement

Given an integer array `nums`, in which exactly **two** elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

**Input:** An integer array `nums`.
**Output:** An array of two integers representing the unique numbers.

## When to use it

- To demonstrate absolute mastery over XOR properties and bit isolation.
- This is a combination of two famous bit tricks: The XOR array collapse (`bit_03`) AND Brian Kernighan's lowest-set-bit isolation (`bit_01`).

## Approach

**1. The Initial XOR Collapse:**
If we XOR every number in the array together (just like in Single Number I), all the paired numbers will cancel out to `0`.
What's left over? Let the two unique numbers be A and B.
The final result will be `xor_sum = A ^ B`.
Because A and B are unique numbers, A \neq B. This means `xor_sum` CANNOT be 0. There MUST be at least one bit set to `1` in `xor_sum`!

**2. The Meaning of a '1' Bit in XOR:**
What does a `1` bit mean in an XOR result? It means that for that specific bit position, A and B had DIFFERENT values! (One of them had a `1`, the other had a `0`).
If we can isolate *any* `1` bit from `xor_sum`, we have found a distinguishing feature between A and B.

**3. Isolating the Bit (Brian Kernighan's variant):**
To isolate the absolute lowest (rightmost) `1` bit of any number, we use the magic trick:
`diff_bit = xor_sum & -xor_sum`
(Note: In two's complement arithmetic, `-n` is equivalent to `~n + 1`. ANDing them together zeroes out everything except the lowest set bit).

**4. Splitting the Array:**
Now we have a `diff_bit` (e.g. `00100`). We know for a fact that A has a `1` at this position, and B has a `0` at this position (or vice versa).
We can iterate through the original array again and split the numbers into two completely separate buckets:
- Bucket 1: Numbers that have a `1` at the `diff_bit` position (`(num & diff_bit) != 0`).
- Bucket 2: Numbers that have a `0` at the `diff_bit` position (`(num & diff_bit) == 0`).

**5. The Final Cancellation:**
A will go entirely into Bucket 1. B will go entirely into Bucket 2.
What about the paired numbers? Because paired numbers are identical, they will ALWAYS have identical bits! Thus, the pairs will BOTH fall into Bucket 1, or BOTH fall into Bucket 2!
Now, Bucket 1 contains A surrounded by pairs. Bucket 2 contains B surrounded by pairs.
We just run the standard Single Number I XOR trick on both buckets independently to reveal A and B!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_05: Single Number III.

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the two elements that appear exactly once (sorted)."""
    xor_all = 0
    for v in arr:
        xor_all ^= v
    diff_bit = xor_all & -xor_all
    a, b = 0, 0
    for v in arr:
        if v & diff_bit:
            a ^= v
        else:
            b ^= v
    return sorted([a, b])
```

</details>

## Walk-through

`nums = [1, 2, 1, 3, 2, 5]`. (Unique numbers are 3 and 5).

1. **Step 1 (XOR Collapse):**
   - `xor_sum = 1^2^1^3^2^5`
   - `1`s cancel. `2`s cancel.
   - `xor_sum = 3 ^ 5`. (`011 ^ 101 = 110`). `xor_sum = 6`.
2. **Step 2 (Isolate Bit):**
   - `diff_bit = 6 & -6`.
   - `6` is `0110`. `-6` is `...11111010`.
   - `0110 & 1010 = 0010`. `diff_bit = 2`.
   - (This proves the 2nd bit from the right is DIFFERENT between 3 and 5).
3. **Step 3 (Split & XOR):**
   - Initialize `a = 0`, `b = 0`.
   - `num = 1 (001)`: `1 & 2 == 0`. Bucket B. `b = 0 ^ 1 = 1`.
   - `num = 2 (010)`: `2 & 2 != 0`. Bucket A. `a = 0 ^ 2 = 2`.
   - `num = 1 (001)`: `1 & 2 == 0`. Bucket B. `b = 1 ^ 1 = 0`. (Pair canceled!).
   - `num = 3 (011)`: `3 & 2 != 0`. Bucket A. `a = 2 ^ 3 = 1`.
   - `num = 2 (010)`: `2 & 2 != 0`. Bucket A. `a = 1 ^ 2 = 3`. (Pair canceled!).
   - `num = 5 (101)`: `5 & 2 == 0`. Bucket B. `b = 0 ^ 5 = 5`.

Result `a = 3`, `b = 5`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The array is traversed exactly twice. Bitwise operations are $O(1)$. Total time is strictly $O(N)$.
Space complexity is $O(1)$ because we only use integer variables `xor_sum`, `diff_bit`, `a`, and `b`.

## Variants & optimizations

- **Avoiding integer overflow:** In languages with strict 32-bit signed integers (like Java/C++), taking `-xor_sum` when `xor_sum == Integer.MIN_VALUE` causes an overflow error! You must explicitly check for `MIN_VALUE` or cast to a 64-bit integer before isolation. (Python dynamically scales integer precision, avoiding this).

## Real-world applications

- **Distributed Networking (Gossip Protocols):** Reconciling synchronization states between two massive databases. By exchanging XOR signatures of datasets, a server can isolate exactly which two records are out of sync without transmitting the entire multi-gigabyte dataset over the network!

## Related algorithms in cOde(n)

- **[bit_03 - Single Number (XOR)](bit_03_single-number-xor.md)** — The foundational prerequisite algorithm.
- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Explains the magic behind the `n & -n` bit isolation technique.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
