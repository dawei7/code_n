# Degree of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 697 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/degree-of-an-array/) |

## Problem Description
### Goal
Given a nonempty array of non-negative integers `nums`, define its degree as the maximum frequency of any one element in the entire array.

Find and return the smallest possible length of a contiguous subarray that has the same degree as `nums`. The subarray may focus on any element tied for the full array's maximum frequency, but it must contain all occurrences needed to reach that frequency within one continuous range; deleting internal positions is not allowed.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- The length of the shortest contiguous subarray with the same degree as `nums`

### Examples
**Example 1**

- Input: `nums = [1,2,2,3,1]`
- Output: `2`

**Example 2**

- Input: `nums = [1,2,2,3,1,4,2]`
- Output: `6`

**Example 3**

- Input: `nums = [1,2,1,3,3]`
- Output: `2`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(U)$

<details>
<summary>Approach</summary>

#### General

**A degree-achieving subarray must contain every copy of one leader**

Suppose a value occurs `d` times, where `d` is the array's degree. Any subarray with degree `d` must include all `d` copies of some value; otherwise no value inside it can occur `d` times. For a chosen leader, the shortest such interval is exactly from its first occurrence through its last.

**Track first positions and growing counts**

Scan once from left to right. Record an index the first time a value appears, increment its count at every appearance, and compute its current span as `index - first[value] + 1`.

**Update degree and shortest span together**

If the new count exceeds the best degree seen so far, this value is the only current leader, so replace both the degree and answer with its count and span. If the count ties the degree, minimize the answer with its span.

**Why an online update finds the final interval**

Every value that reaches the final degree triggers an update on its last occurrence, at which point its recorded span is exactly its first-to-last interval. No lower-frequency value can support a subarray of the final degree. Taking the minimum over those triggered spans therefore returns precisely the shortest valid subarray.

#### Complexity detail

The scan performs expected constant-time hash-map work per element, for $O(n)$ time. The first-position and count maps store one entry for each of `U` distinct values, using $O(U)$ space.

#### Alternatives and edge cases

- **Store count, first, and last separately:** make one pass to collect all three statistics and a second pass over distinct values to choose the shortest degree leader; it has the same asymptotic bounds.
- **Sort indexed values:** group equal values after sorting `(value, index)` pairs; this takes $O(n \log n)$ time and must preserve original indices for spans.
- **Rescan for every distinct value:** count and locate each candidate with a full array scan; it is correct but can take $O(nU)$ time.
- When every value is distinct, the degree is `1` and one element is sufficient.
- When all values are equal, only the complete array has the required degree.
- Several values may tie for the degree; their first-to-last spans, not their numeric values, decide the answer.

</details>
