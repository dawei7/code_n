# Number of Subarrays with Bounded Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 795 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) |

## Problem Description

### Goal

Given an integer array `nums` and bounds `left` and `right`, consider every nonempty contiguous subarray and find its maximum element.

Return the number of subarrays whose maximum lies in the inclusive interval `[left, right]`. A candidate must contain at least one value greater than or equal to `left` and no value greater than `right`. Subarrays are counted by index range, so equal value sequences at different positions contribute separately.

### Function Contract

**Inputs**

- `nums`: a nonempty list of positive integers.
- `left`: the lower allowed maximum.
- `right`: the upper allowed maximum, with `left <= right`.

**Return value**

- The number of contiguous subarrays having `left <= maximum <= right`.

### Examples

**Example 1**

- Input: `nums = [2,1,4,3], left = 2, right = 3`
- Output: `3`
- Explanation: `[2]`, `[2,1]`, and `[3]` have valid maxima.

**Example 2**

- Input: `nums = [2,9,2,5,6], left = 2, right = 8`
- Output: `7`
- Explanation: The `9` splits the array; seven subarrays in the remaining segments contain a value in the allowed interval.

**Example 3**

- Input: `nums = [1,2,3], left = 1, right = 3`
- Output: `6`
- Explanation: Every nonempty subarray is valid.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count valid subarrays by their right endpoint**

Track `last_too_large`, the most recent index whose value exceeds `right`, and `last_in_range`, the most recent index whose value lies in `[left, right]`. Values below `left` update neither position.

**Choose every legal starting index**

For a subarray ending at the current index to be valid, it must start after `last_too_large` and at or before `last_in_range`. The number of such starts is `last_in_range - last_too_large` when the in-range index is newer; add that quantity to the answer.

Starting after the too-large value guarantees every element is at most `right`. Starting no later than the latest in-range value guarantees the subarray contains a value at least `left`, while every later element that is not in range is below `left`. These conditions are exactly equivalent to a maximum in `[left, right]`, so each valid subarray is counted once at its unique ending index.

#### Complexity detail

The scan processes each of the `n` elements once, taking $O(n)$ time. It stores two indices and the running total, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Difference of upper-bound counts:** Count subarrays with maximum at most `right` and subtract those with maximum below `left`; two linear run-length scans give the same result.
- **Monotonic stack:** Contribution counting by each element's maximum span is possible but unnecessarily complex here.
- **Enumerate all subarrays:** Updating a running maximum for every start is correct but takes $O(n^2)$ time.
- **All values below `left`:** No subarray contains a qualifying maximum.
- **Value above `right`:** It resets the earliest allowed starting boundary.
- **Values equal to a bound:** Both `left` and `right` are inclusive and update `last_in_range`.
- **Trailing small values:** They extend every valid subarray whose latest qualifying value remains after the last too-large value.

</details>
