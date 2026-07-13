# Continuous Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 523 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/continuous-subarray-sum/) |

## Problem Description
### Goal
Given a nonempty integer array `nums` and a positive integer `k`, choose a contiguous subarray containing at least two elements. Its sum qualifies when it equals $n \cdot k$ for some integer `n`, including $n = 0$.

Return `True` if any such subarray exists and `False` otherwise. The selected elements must occupy consecutive positions, cannot wrap, and cannot be replaced by an arbitrary subsequence. A zero sum is divisible by `k`, while a one-element match is excluded by the minimum-length rule. The function returns only feasibility, not the interval or multiplier.

### Function Contract
**Inputs**

- `nums`: an array of nonnegative integers
- `k`: a positive integer divisor

**Return value**

- `True` if some length-at-least-two contiguous subarray sums to a multiple of `k`; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [23, 2, 4, 6, 7], k = 6`
- Output: `True`

**Example 2**

- Input: `nums = [23, 2, 6, 4, 7], k = 6`
- Output: `True`

**Example 3**

- Input: `nums = [23, 2, 6, 4, 7], k = 13`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(\min(n, k))$

<details>
<summary>Approach</summary>

#### General

**Turn subarray divisibility into equal prefix remainders**

Let `prefix[i]` be the sum through index `i`. A subarray after an earlier prefix `j` has sum `prefix[i] - prefix[j]`. This difference is divisible by `k` exactly when the two prefix sums have the same remainder modulo `k`.

**Remember the earliest index for each remainder**

Initialize remainder zero at virtual index `-1`, representing the empty prefix. As the running remainder is updated, check whether it was seen at an index at least two positions earlier. If so, the elements between those prefix boundaries form a valid subarray.

**Do not replace an earlier occurrence**

Store a remainder only on its first appearance. An earlier index provides the largest possible gap for every later match; replacing it could hide a valid length-two-or-more interval. The virtual `-1` entry likewise allows a divisible prefix ending at index one or later.

**Why absence of a match proves failure**

Every contiguous subarray is the difference of two prefix sums. If a qualifying subarray existed, its boundary prefixes would have equal remainders and an index gap equal to the subarray length, so the scan would detect it at the later boundary. Exhausting the array therefore rules out all candidates.

#### Complexity detail

The scan performs expected $O(1)$ hash work for each of `n` values, giving $O(n)$ time. There are at most $n + 1$ observed prefixes and at most `k` distinct remainders, so space is $O(\min(n, k))$.

#### Alternatives and edge cases

- **Enumerate every subarray sum:** is correct but takes $O(n^2)$ time even with a running inner sum.
- **Prefix-sum array plus pair checks:** avoids repeated addition but still examines quadratically many boundary pairs.
- **Delayed remainder set:** can enforce the two-element minimum by adding the previous remainder after each check, with the same linear bounds.
- **Two zeros:** form a sum of zero, which is divisible by every positive `k`.
- **Match one index apart:** represents a one-element subarray and must be rejected.
- **Divisible prefix:** is detected through the virtual remainder-zero prefix.
- **Remainder collisions:** only the earliest index needs to be retained.

</details>
