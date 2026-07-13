# Third Maximum Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 414 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/third-maximum-number/) |

## Problem Description
### Goal
Given a nonempty integer array, rank its distinct values from largest to smallest. Duplicate occurrences occupy only one distinct rank, regardless of how often they appear in the input.

Return the value at the third distinct rank when at least three different values exist. If there are fewer than three distinct values, return the overall maximum instead. Negative values, zero, and the smallest representable integer must be treated as ordinary candidates rather than sentinel states. The task returns a value, not its source index or frequency.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array

**Return value**

- Return the third distinct maximum when it exists; otherwise return the overall maximum.

### Examples
**Example 1**

- Input: `nums = [3,2,1]`
- Output: `1`

**Example 2**

- Input: `nums = [1,2]`
- Output: `2`

**Example 3**

- Input: `nums = [2,2,3,1]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track three ordered distinct maxima**

Maintain `first`, `second`, and `third`, initially absent. Ignore a value equal to any occupied slot because duplicates do not change distinct rank.

**Insert a new value at its rank**

If the value exceeds `first`, shift the previous first and second values down and install it. Otherwise compare with `second`, then `third`, shifting only the lower ranks affected by the insertion.

**Choose the required fallback**

After one scan, an occupied `third` is exactly the third-largest distinct value. If it is absent, there were only one or two distinct values, and `first` is the required maximum.

**Why the three slots remain correct**

Initially they represent the maxima of an empty prefix. Ignoring duplicates preserves that property. Inserting a new distinct value into the first position it exceeds and shifting lower ranks is the standard ordered insertion step, so induction keeps the slots equal to the three greatest distinct values of every processed prefix.

#### Complexity detail

Each of the `n` values undergoes a constant number of comparisons and assignments, giving $O(n)$ time. Three optional numeric slots use $O(1)$ space.

#### Alternatives and edge cases

- **Set plus descending sort:** is concise but takes $O(n \log n)$ time and $O(n)$ space.
- **Keep a set capped at three values:** insert each distinct value and remove the minimum when necessary; it also has linear time and constant-size storage.
- **Explicit insertion-sort of all distinct values:** can take $O(n^2)$ time.
- Duplicate maxima count only once.
- Negative values retain their ordinary numeric ordering.
- Fewer than three distinct values trigger the maximum fallback.
- Sentinel numeric values are unsafe because the full integer range is valid; use absence markers.

</details>
