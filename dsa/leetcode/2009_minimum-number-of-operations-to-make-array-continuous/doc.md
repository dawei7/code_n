# Minimum Number of Operations to Make Array Continuous

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2009 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) |

## Problem Description

### Goal

In one operation, choose any position in the integer array `nums` and replace
its value with any integer.

An array of length $N$ is continuous only when all its elements are unique and
the difference between its maximum and minimum equals $N-1$. These conditions
mean its values form every integer in one interval of length $N$, although
their array order is irrelevant. Determine the minimum number of replacements
needed to make `nums` continuous.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le10^5$ and
  $1\le\texttt{nums[i]}\le10^9$.

**Return value**

Return the smallest number of array positions whose values must be replaced.

### Examples

**Example 1**

- Input: `nums = [4, 2, 5, 3]`
- Output: `0`
- Explanation: The four unique values already span from $2$ through $5$.

**Example 2**

- Input: `nums = [1, 2, 3, 5, 6]`
- Output: `1`
- Explanation: Replacing `6` with `4` produces one continuous interval.

**Example 3**

- Input: `nums = [1, 10, 100, 1000]`
- Output: `3`
- Explanation: Keep `1` and replace the other positions with `2`, `3`, and
  `4`.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Maximize the values that can remain unchanged.** Any continuous result is a
set of $N$ consecutive integers. If its minimum is $x$, an existing distinct
value can stay only when it lies in $[x,x+N-1]$. Duplicate occurrences cannot
both remain because the final values must be unique. Therefore, after sorting
the distinct input values, the problem becomes finding the largest number that
fit in any interval of width $N-1$.

**Sweep all candidate intervals with one window.** Maintain indices `left` and
`right` into the sorted distinct values. For each `left`, advance `right` while
the value there is less than `values[left] + N`. The window then contains
exactly the distinct values that can remain unchanged when its first value is
the final minimum. Its replacement count is
`N - (right - left)`. Take the minimum across all left endpoints, and never
move `right` backward.

For any final continuous interval, its unchanged input values form one such
window, so no solution can keep more elements than the largest window.
Conversely, every window can be completed by replacing all other positions
with the missing integers from its length-$N$ interval. Thus subtracting the
largest feasible distinct count from $N$ gives exactly the optimum.

#### Complexity detail

Here $N$ is the length of `nums`. Deduplication and sorting take
$O(N\log N)$ time. Each window pointer advances at most once across the
distinct values, adding $O(N)$ time. The distinct-value collection uses
$O(N)$ space.

#### Alternatives and edge cases

- **Restart a scan for every minimum:** Testing every sorted value and walking
  forward from it is correct but takes $O(N^2)$ time on dense inputs.
- **Binary search each right boundary:** Searching for `value + N` from every
  left endpoint takes $O(N\log N)$ after sorting, matching the overall bound
  but doing more repeated work than the sliding window.
- Duplicate occurrences beyond the first always require replacement, even
  when their shared value lies inside the chosen interval.
- A one-element array is already continuous.
- Values may be as large as $10^9$; the method depends on their order and
  differences, not on allocating an array across the value domain.

</details>
