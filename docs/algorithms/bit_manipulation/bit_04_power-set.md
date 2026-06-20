# Power Set (Bitwise Optimization)

| | |
|---|---|
| **ID** | `bit_04` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(N * 2^N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Subsets](https://leetcode.com/problems/subsets/) |

## Problem statement

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
*Constraint:* You must solve this entirely iteratively without using Recursion or Backtracking.

**Input:** An integer array `nums`.
**Output:** A list of lists, where each inner list is a valid subset.

## When to use it

- To generate combinations blazingly fast in a competitive programming environment where recursive overhead causes Time Limit Exceeded (TLE) errors.
- It proves your understanding of how binary numbers inherently map to choice states.

## Approach

**1. The Binary Mapping:**
In the Backtracking approach (`backtrack_01`), we made an "Include" or "Exclude" decision for every single element. That's 2 choices per element.
Notice that a binary number also has exactly 2 states per bit: `1` (Include) and `0` (Exclude)!
If an array has N=3 elements, there are exactly 2^3 = 8 subsets.
Let's count from `0` to `7` in binary:
- `0` = `000` -> Exclude all -> `[]`
- `1` = `001` -> Include 3rd -> `[nums[2]]`
- `2` = `010` -> Include 2nd -> `[nums[1]]`
- `3` = `011` -> Include 2nd, 3rd -> `[nums[1], nums[2]]`
- `4` = `100` -> Include 1st -> `[nums[0]]`
- `5` = `101` -> Include 1st, 3rd -> `[nums[0], nums[2]]`
- `6` = `110` -> Include 1st, 2nd -> `[nums[0], nums[1]]`
- `7` = `111` -> Include all -> `[nums[0], nums[1], nums[2]]`

Every single number from 0 to 2^N - 1 perfectly represents a unique, valid subset!

**2. The Bitmask Strategy:**
1. Calculate the total number of subsets: `total = 1 << n`. (This is 2^N).
2. Loop a variable `mask` from `0` up to `total - 1`.
3. For a specific `mask`, we need to find which bits are set to `1`.
   We loop an index `i` from `0` to `n - 1`.
   To check if the i-th bit of `mask` is a `1`, we shift a `1` left by `i` positions (`1 << i`), and do a bitwise AND!
   If `(mask & (1 << i)) != 0`, we include `nums[i]` in our current subset!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_04: Power Set.

Return every subset of the input list as a list
"""


def solve(arr, n):
    """Return every subset of arr as a list of lists."""
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result
```

</details>

## Walk-through

`nums = [A, B, C]`. N=3.
`total_subsets = 1 << 3 = 8`.

1. **mask = 0 (`000`):**
   - i=0: `000 & 001 == 0`. Skip.
   - i=1: `000 & 010 == 0`. Skip.
   - i=2: `000 & 100 == 0`. Skip.
   - Result appends: `[]`.
2. **mask = 3 (`011`):**
   - i=0: `011 & 001 == 1`. Include `nums[0] (A)`.
   - i=1: `011 & 010 == 2`. Include `nums[1] (B)`.
   - i=2: `011 & 100 == 0`. Skip.
   - Result appends: `[A, B]`.
3. **mask = 5 (`101`):**
   - i=0: `101 & 001 == 1`. Include `A`.
   - i=1: `101 & 010 == 0`. Skip.
   - i=2: `101 & 100 == 4`. Include `C`.
   - Result appends: `[A, C]`.
4. ... repeats up to `mask = 7`.

Result: `[[], [A], [B], [A,B], [C], [A,C], [B,C], [A,B,C]]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N * 2^N)$ | $O(1)$ |
| **Average** | $O(N * 2^N)$ | $O(1)$ |
| **Worst** | $O(N * 2^N)$ | $O(1)$ |

The outer loop runs exactly 2^N times. The inner loop runs exactly N times. The bitwise checks are $O(1)$. Total time is perfectly bounded to $O(N x 2^N)$. This is much faster in practice than recursion because it avoids function call stack overhead.
Space complexity is $O(1)$ auxiliary memory! (We do not count the output array taking $O(N x 2^N)$ space). The recursive backtracking solution requires $O(N)$ auxiliary stack space.

## Variants & optimizations

- **Combinations of specific size K (Gosper's Hack):** If you only want subsets of exactly size K (e.g. 3 elements), doing a full 2^N loop is extremely wasteful! Gosper's Hack is a bitwise magic formula that takes a bitmask with K ones, and calculates the *lexicographically next* bitmask with exactly K ones in strictly $O(1)$ time! You just initialize `mask = (1 << k) - 1`, and then loop `mask = gospers_hack(mask)` until it exceeds 2^N.

## Real-world applications

- **State Compression:** In highly complex DP problems (like the Traveling Salesperson Problem), an array of visited cities `[True, False, True]` is compressed into a single integer `5` (`101`). This allows the state to be used directly as an array index (`dp[5]`) for lightning-fast memory access.

## Related algorithms in cOde(n)

- **[backtrack_01 - Subsets](../backtracking/backtrack_01_subset-sum-decision.md)** — The recursive solution to the exact same problem.
- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Core bit masking concepts.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
