# Removing Minimum and Maximum From Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2091 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) |

## Problem Description

### Goal

You are given a zero-indexed array `nums` whose integer values are distinct. Consequently, the array has one uniquely positioned minimum element and one uniquely positioned maximum element; when the array has length one, that sole element serves as both.

One deletion removes the current first element or the current last element. Perform deletions until both original extreme elements have been removed, and return the minimum possible number of deletions. Other elements may be removed along with them.

### Function Contract

**Input**

- `nums`: an array of $n$ distinct integers.
- $1 \le n \le 10^5$ and $-10^5 \le \texttt{nums}[i] \le 10^5$.

**Return value**

Return the minimum number of front and back deletions needed to remove both the minimum and maximum elements.

### Examples

**Example 1**

- Input: `nums = [2, 10, 7, 5, 4, 1, 8, 6]`
- Output: `5`
- Explanation: Remove two elements from the front to include `10` and three from the back to include `1`.

**Example 2**

- Input: `nums = [0, -4, 19, 1, 8, -2, -3, 5]`
- Output: `3`
- Explanation: Removing the first three elements removes both extremes.

**Example 3**

- Input: `nums = [101]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reducing deletions to two fixed indices**

Scan once to locate the unique minimum and maximum. Let `left` be the smaller of their indices and `right` the larger. The values themselves no longer matter: a sequence of end deletions succeeds exactly when it removes both of these positions.

**The only three useful endpoint strategies**

Any successful plan belongs to one of three forms:

- Remove a prefix through `right`, costing `right + 1`.
- Remove a suffix beginning at `left`, costing `n - left`.
- Remove a prefix through `left` and a suffix beginning at `right`, costing `left + 1 + n - right`.

Taking the minimum of these quantities covers removing both from the front, both from the back, or one from each side.

**Why no fourth strategy can be better**

If a plan deletes from both ends, its removed prefix must reach at least one extreme and its removed suffix must reach the other; extending either side farther is unnecessary. If both extremes are reached from the same side, the farther index fixes the required count. Thus every optimal plan can be shortened to one of the three boundary-tight strategies above.

#### Complexity detail

Finding both extreme indices takes one pass over $n$ elements, and evaluating the three formulas is constant work. The time is $O(n)$ and the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Sort value-index pairs:** Sorting identifies the extreme positions but costs $O(n \log n)$ time and extra storage.
- **Simulate every deletion sequence:** Branching between front and back explores many equivalent prefixes and suffixes despite only three final boundary patterns mattering.
- **Repeated extreme searches:** Comparing every element with every other element finds the extremes correctly but takes $O(n^2)$ time.
- With one element, a single deletion removes both the minimum and maximum.
- When the extremes are already the two endpoints, two deletions are sufficient.
- The smaller value need not be at `left`; indices are ordered independently of values.

</details>
