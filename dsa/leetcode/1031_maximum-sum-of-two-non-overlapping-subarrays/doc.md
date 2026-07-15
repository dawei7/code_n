# Maximum Sum of Two Non-Overlapping Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1031 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums` and two lengths `firstLen` and `secondLen`, choose two non-overlapping subarrays: one with length `firstLen` and the other with length `secondLen`.

The `firstLen` subarray may appear before or after the `secondLen` subarray. Return the maximum possible sum of all elements in the two chosen subarrays.

A subarray is a contiguous part of the original array; elements cannot be skipped within either choice.

### Function Contract

**Inputs**

- `nums`: an array of $N$ integers, where `first_len + second_len <= len(nums) <= 1000` and $0 \le \texttt{nums[i]} \le 1000$.
- `first_len`: the length of one required subarray, where $1 \le \texttt{first_len} \le 1000$.
- `second_len`: the length of the other required subarray, where $1 \le \texttt{second_len} \le 1000$.
- The two lengths satisfy $2 \le \texttt{first_len}+\texttt{second_len} \le 1000$.

**Return value**

- The maximum combined sum of two non-overlapping subarrays with the specified lengths.

### Examples

**Example 1**

- Input: `nums = [0,6,5,2,2,5,1,9,4], first_len = 1, second_len = 2`
- Output: `20`
- Explanation: Choose `[9]` and `[6,5]`.

**Example 2**

- Input: `nums = [3,8,1,3,2,1,8,9,0], first_len = 3, second_len = 2`
- Output: `29`
- Explanation: Choose `[3,8,1]` and `[8,9]`.

**Example 3**

- Input: `nums = [2,1,5,6,0,9,5,0,3,8], first_len = 4, second_len = 3`
- Output: `31`
- Explanation: Choose `[5,6,0,9]` and `[0,3,8]`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Make every window sum constant-time:** Build a prefix array with `prefix[i]` equal to the sum before index `i`. A length-`length` window starting at `left` then has sum `prefix[left + length] - prefix[left]`.

**Solve one left-to-right ordering:** Suppose the `left_len` window must precede the `right_len` window. Scan each possible `right_start`. Maintain `best_left`, the greatest sum of a `left_len` window ending no later than `right_start`. Combining it with the current right window considers the best valid pair for that boundary without overlap.

**Evaluate both possible orders:** Run the scan once with `first_len` on the left and once with `second_len` on the left. The maximum of those results covers every legal pair because two non-overlapping subarrays must have one entirely before the other.

For a fixed ordering and right boundary, `best_left` contains every feasible left window seen so far and retains the greatest one. Thus the scan chooses the optimal pair for each right window. Taking all right windows and both orders proves the final maximum is global.

#### Complexity detail

Building prefix sums costs $O(N)$ time and space. Each ordered scan advances across the array once, with $O(1)$ work per position, so both scans together remain $O(N)$ time. The prefix array uses $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Rolling window sums:** Maintain the current left and right sums directly to achieve $O(N)$ time and $O(1)$ auxiliary space, at the cost of more index bookkeeping.
- **Enumerate every window pair:** Prefix sums make each pair evaluation constant-time, but there are $O(N^2)$ pairs.
- **Only one fixed order:** This misses answers where the `second_len` window must occur first.
- **Exact total length:** When the lengths sum to $N$, both subarrays together cover the entire array and the answer is its total sum.
- **Zero values:** The method does not rely on strictly positive contributions.
- **Overlap trap:** Individually largest windows may overlap; the maintained boundary prevents combining them.

</details>
