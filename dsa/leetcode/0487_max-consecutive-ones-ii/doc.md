# Max Consecutive Ones II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 487 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/max-consecutive-ones-ii/) |

## Problem Description
### Goal
Given a binary array, choose one contiguous subarray and optionally change at most one `0` within it to `1`. All other values remain unchanged, and the selected positions must be consecutive rather than joined across an unselected gap.

Return the maximum possible number of consecutive `1` values after that single permitted flip. A window containing no zero is valid without using the change, while a window with two zeroes cannot be made all ones. If the array contains only zeroes, one position can form a run of length one; the function returns only the best length.

### Function Contract
**Inputs**

- `nums`: a nonempty binary array

**Return value**

- The maximum possible consecutive-one length after at most one flip

### Examples
**Example 1**

- Input: `nums = [1, 0, 1, 1, 0]`
- Output: `4`

**Example 2**

- Input: `nums = [1, 0, 1, 1, 0, 1]`
- Output: `4`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reframe one flip as one allowed zero**

A segment can become all ones with at most one flip exactly when it contains no more than one zero. The problem is therefore a longest-window problem.

**Expand and repair the window**

Advance the right boundary and count zeros entering the window. When the count reaches two, move the left boundary until the older zero leaves. The restored window is valid and can update the best length.

**Why the left boundary is monotonic**

For each right endpoint, shrinking only until validity returns leaves the smallest possible left endpoint and thus the longest valid window ending there. A discarded prefix contains the extra zero and can never become valid again as the right boundary moves farther right.

**Allow no flip when none is needed**

A window containing zero zeros already satisfies the at-most-one condition, so an all-one array correctly returns its full length.

#### Complexity detail

Each boundary advances at most `n` times, giving $O(n)$ total time. The boundaries, zero count, and best length use $O(1)$ extra space.

#### Alternatives and edge cases

- **Two-state dynamic programming:** tracks runs ending at each position with zero flips and with at most one flip.
- **Store zero indices:** moving past the older of the last two zeros is another constant-space window form.
- **Restart from every index:** is correct but takes $O(n^2)$ time on all ones.
- **All ones:** no flip is required.
- **All zeros:** only one position can become one.
- **Single element:** both zero and one yield length one.
- **Boundary zeros:** move past the older zero rather than shrinking by only one position.

</details>
