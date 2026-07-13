# Maximum Average Subarray I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 643 |
| Difficulty | Easy |
| Topics | Array, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/) |

## Problem Description
### Goal
Given an integer array `nums` with `n` elements and an integer `k`, consider every contiguous subarray whose length is equal to `k`. Compute each candidate's arithmetic average from the sum of exactly those `k` consecutive values.

Return the maximum average value among all candidates. The selected elements must form one contiguous range rather than an arbitrary subsequence, and the length cannot be shorter or longer than `k`. A floating-point answer with calculation error less than $10^{-5}$ is accepted.

### Function Contract
**Inputs**

- `nums`: a nonempty list of integers
- `k`: the fixed subarray length, with `1 <= k <= len(nums)`

**Return value**

- The maximum average as a floating-point number

### Examples
**Example 1**

- Input: `nums = [1,12,-5,-6,50,3]`, `k = 4`
- Output: `12.75`

**Example 2**

- Input: `nums = [5]`, `k = 1`
- Output: `5.0`

**Example 3**

- Input: `nums = [-5,-2,-3,-4]`, `k = 2`
- Output: `-2.5`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Maximize the sum before dividing**

Every candidate contains the same positive number `k` of elements. Therefore, their averages have the same ordering as their sums, so division is needed only once after finding the maximum window sum.

**Initialize the first complete window**

Sum the first `k` values and use that as both the current and best sum. This is important when all values are negative: starting the best at zero would incorrectly prefer a nonexistent empty window.

**Slide by exchanging two endpoints**

When the window moves one position right, add the entering value and subtract the value exactly `k` positions behind it. Update the best sum after each exchange. Every length-`k` window is reached once without resumming its shared interior.

**Why no candidate is missed**

The initial window begins at index zero. Each subsequent iteration advances its start by one and maintains exactly the sum of that next window through one addition and subtraction. The sequence visits every legal start index through $N - k$, so the greatest recorded sum, divided by `k`, is the required maximum average.

#### Complexity detail

The initial sum reads `k` values, and the sliding loop reads each remaining value once, for $O(N)$ total time. The current sum, best sum, and indices use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix sums:** each window sum becomes a difference of two prefix values in $O(1)$ time, but the prefix array uses $O(N)$ extra space.
- **Resum every window:** directly sums each length-`k` slice and is correct, but can take $O(Nk)$ time.
- **Binary search an average threshold:** is useful for variable-length variants, but adds unnecessary complexity when the length is fixed.
- When $k = 1$, the answer is the largest element.
- When $k = N$, the only candidate is the entire array.
- All-negative input requires initializing from a real window rather than zero.
- Fractional and negative averages must use ordinary division after choosing the best sum.

</details>
