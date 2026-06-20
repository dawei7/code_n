# Missing Number

| | |
|---|---|
| **ID** | `bit_10` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Missing Number](https://leetcode.com/problems/missing-number/) |

## Problem statement

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Input:** An integer array `nums` of length `n`.
**Output:** An integer representing the missing number.

## When to use it

- To demonstrate the commutative and self-canceling properties of XOR in a slightly different context than `Single Number`.
- When you need to find a single discrepancy between a known "expected" sequence and an "actual" sequence.

## Approach

**1. The Mathematical Approach (Gauss's Formula):**
The sum of the first `N` numbers is mathematically defined as: \text{Expected Sum} = \frac{n(n + 1)}{2}.
If we iterate through the array and calculate the \text{Actual Sum}, the missing number is simply \text{Expected Sum} - \text{Actual Sum}.
*Why might this fail in an interview?* If N is incredibly large (e.g., 10^5), the mathematical sum could cause integer overflow in languages like Java or C++!

**2. The XOR Approach:**
We know from `bit_03` that any number XOR'd with itself cancels out to `0` (`A ^ A = 0`).
If we have the expected sequence `[0, 1, 2, 3]` and the actual sequence `[0, 1, 3]`, what happens if we XOR ALL of these numbers together simultaneously?
`Expected = 0 ^ 1 ^ 2 ^ 3`
`Actual   = 0 ^ 1 ^     3`
`Result   = (0^0) ^ (1^1) ^ 2 ^ (3^3)`
`Result   =   0   ^   0   ^ 2 ^   0`
`Result   = 2`!

Every number present in the array will pair up perfectly with its corresponding index number in the expected sequence and cancel out! The ONLY number left standing will be the missing number, because it had no twin in the actual array to cancel it out.

**3. Execution:**
Initialize a variable `missing = len(nums)`. (Because the loop indices only go from `0` to `n-1`, we must manually throw the final expected number `n` into the XOR accumulator).
Loop `i` from `0` to `n-1`.
`missing ^= i ^ nums[i]`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_10: Missing Number.

Given an array arr of n distinct integers in
"""


def solve(arr, n):
    """Find the missing integer in arr (length n, values in [0, n])."""
    # XOR all values and all indices 0..n; the missing value
    # is the survivor.
    result = n  # include the index n in the XOR
    for i, v in enumerate(arr):
        result ^= i ^ v
    return result
```

</details>

## Walk-through

`nums = [3, 0, 1]`. N = 3.
Initial `missing = 3`.

1. **i = 0:**
   - `missing ^= 0` (Expected index) -> `3 ^ 0 = 3`
   - `missing ^= nums[0]` (`3`) -> `3 ^ 3 = 0` (The '3's canceled out!)
2. **i = 1:**
   - `missing ^= 1` (Expected index) -> `0 ^ 1 = 1`
   - `missing ^= nums[1]` (`0`) -> `1 ^ 0 = 1` (The '0's canceled out implicitly)
3. **i = 2:**
   - `missing ^= 2` (Expected index) -> `1 ^ 2 = 3`
   - `missing ^= nums[2]` (`1`) -> `3 ^ 1 = 2` (The '1's canceled out!)

Result `missing = 2`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The array is traversed exactly once. Bitwise XOR operations take $O(1)$ time. Total time complexity is strictly $O(N)$.
Only one integer variable `missing` is used. Space complexity is $O(1)$.
Unlike the mathematical sum formula, XOR operations NEVER overflow integer limits.

## Variants & optimizations

- **Find the Duplicate Number:** You are given an array of size N+1 containing numbers in the range [1, N]. There is exactly ONE duplicate number. Can you use XOR? *NO!* Because the duplicate number might appear 3 times, or 4 times, breaking the XOR cancellation rules. You must use Floyd's Cycle Detection (Tortoise and Hare) or Binary Search.

## Real-world applications

- **Network Packet Loss Detection:** When transmitting a sequential stream of UDP packets (labeled 1 to N), the receiver can maintain a running XOR checksum. If exactly one packet is dropped, the XOR checksum immediately reveals its ID without having to scan the entire received list!

## Related algorithms in cOde(n)

- **[bit_03 - Single Number (XOR)](bit_03_single-number-xor.md)** — The foundational prerequisite algorithm.
- **[two_pointers_03 - Find the Duplicate Number](../two_pointers/two_pointers_03_find-the-duplicate-number.md)** — The problem that looks identical but strictly cannot be solved with bit manipulation.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
