# Binary Subarrays With Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 930 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/) |

## Problem Description

### Goal

Given a binary array `nums` and an integer `goal`, count the non-empty subarrays whose elements sum to exactly `goal`.

A subarray is a contiguous part of the original array. Two subarrays with the same sequence of values still count separately when they occupy different index ranges.

Equivalently, count every index pair $(\ell,r)$ with $0 \le \ell \le r < n$ for which the sum of `nums[ell:r + 1]` is `goal`. The selected range must contain at least one element. In particular, when `goal` is zero, every contiguous range consisting only of zeros contributes to the answer.

### Function Contract

**Inputs**

- `nums`: a binary array of length $n$, where $1 \le n \le 3 \cdot 10^4$ and every element is either `0` or `1`.
- `goal`: the required subarray sum, where $0 \le \texttt{goal} \le n$.

**Return value**

Return the number of non-empty contiguous subarrays of `nums` whose sum is exactly `goal`.

### Examples

**Example 1**

- Input: `nums = [1,0,1,0,1], goal = 2`
- Output: `4`

**Example 2**

- Input: `nums = [0,0,0,0,0], goal = 0`
- Output: `15`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Replace exact counting with two at-most counts.** Because every array value is nonnegative, the number of subarrays with sum exactly `goal` equals the number with sum at most `goal` minus the number with sum at most `goal - 1`. Define a helper that computes the at-most quantity with a sliding window.

**Maintain the longest valid left range for each right endpoint.** Extend the window by adding `nums[right]`. While its sum exceeds the chosen limit, remove `nums[left]` and advance `left`. After that adjustment, every subarray ending at `right` and starting anywhere from `left` through `right` has sum at most the limit. There are `right - left + 1` such subarrays, so add that number to the helper result.

**Subtract away all smaller sums.** `at_most(goal)` includes exactly the desired subarrays plus those with smaller sums. Those smaller subarrays are precisely what `at_most(goal - 1)` counts. Their difference therefore leaves only sum `goal`. For `goal == 0`, the second limit is negative; no non-empty binary subarray can meet it, so the helper returns zero immediately. Monotonicity of nonnegative sums guarantees that each pointer only moves forward and that no valid start before `left` can re-enter later.

#### Complexity detail

Each at-most pass advances `right` through all $n$ positions and advances `left` at most $n$ times. Two passes therefore take $O(n)$ time. The window sum, pointers, and counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix-sum frequencies:** Record how often each earlier prefix sum occurred and add the frequency of `prefix - goal` at each position. This is also $O(n)$ time but uses $O(n)$ space.
- **Enumerate every start and end:** Accumulating each subarray sum directly is correct but requires $O(n^2)$ time in the worst case.
- **Goal zero:** Runs of zeros contribute many overlapping subarrays; the negative-limit guard makes the at-most subtraction handle them correctly.
- **Goal larger than the total sum:** No exact-sum subarray exists, and both at-most counts become equal.
- **Single-element input:** The one subarray is counted exactly when that bit equals `goal`.

</details>
