# Maximum Sum Circular Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 918 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/) |

## Problem Description
### Goal

Given a circular integer array `nums`, find the maximum possible sum of a non-empty subarray. Circular means the last position connects to the first: the next position after `nums[i]` is `nums[(i + 1) % n]`, and the previous position is `nums[(i - 1 + n) % n]`.

A chosen subarray must remain contiguous in that circular order and may include each position of the fixed array at most once. Return the greatest sum among all such non-empty subarrays.

### Function Contract
**Inputs**

- `nums`: an array of $n$ integers, where $1 \le n \le 3 \cdot 10^4$ and each value lies between $-3 \cdot 10^4$ and $3 \cdot 10^4$, inclusive.

**Return value**

The maximum sum of a non-empty subarray that may stay within the ordinary array bounds or wrap once from the end to the beginning.

### Examples
**Example 1**

- Input: `nums = [1,-2,3,-2]`
- Output: `3`
- Explanation: The single-element subarray `[3]` is optimal.

**Example 2**

- Input: `nums = [5,-3,5]`
- Output: `10`
- Explanation: The wrapping subarray joins the final and initial `5`.

**Example 3**

- Input: `nums = [-3,-2,-3]`
- Output: `-2`
- Explanation: A non-empty answer is required, so the largest single value is optimal.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate non-wrapping and wrapping shapes**

Every valid circular subarray has one of two forms. It either lies entirely inside the ordinary array, or it wraps across the boundary and consists of a suffix plus a prefix. Standard maximum-subarray dynamic programming finds the best non-wrapping sum in one pass.

For a wrapping choice, consider the elements not selected. They form one ordinary contiguous middle subarray. If the total array sum is $T$ and that excluded middle has sum $M$, the wrapping sum is $T-M$. Maximizing it therefore means excluding the minimum-sum ordinary subarray.

**Track both Kadane recurrences together**

Maintain the best sum ending at the current position for both a maximum subarray and a minimum subarray. For each new value, either start a new subarray there or extend the previous ending subarray. Also accumulate the total sum and the best maximum and minimum seen anywhere.

The answer is the larger of the best ordinary maximum and `total - minimum_sum`. There is one necessary exception: when every value is negative, the minimum subarray is the entire array, and subtracting it would represent an empty selection with sum zero. In that case, return the ordinary maximum, which is the least negative single value. These two structural cases cover every legal circular subarray, so their best valid result is globally optimal.

#### Complexity detail

Let $n$ be the length of `nums`. One pass updates a constant number of sums for each element, producing $O(n)$ time. The algorithm stores only the running total and constant-size dynamic-programming state, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Enumerate every circular start and length:** Incrementally summing all $n^2$ candidate subarrays is correct but takes $O(n^2)$ time.
- **Doubled array with a monotonic deque:** Prefix sums over two copies plus a deque can enforce the length-at-most-$n$ rule in $O(n)$ time, but it uses $O(n)$ space and more machinery.
- **All-negative input:** The complement formula would choose the empty subarray; return the ordinary maximum instead.
- **Single element:** The only legal non-empty subarray is the element itself.
- **Zeros:** A zero may be the best answer when every other value is negative.
- **At most one full traversal:** A circular subarray cannot reuse an index, so it may contain no more than $n$ elements.

</details>
