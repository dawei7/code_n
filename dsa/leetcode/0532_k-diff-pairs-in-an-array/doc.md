# K-diff Pairs in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 532 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/k-diff-pairs-in-an-array/) |

## Problem Description
### Goal
Given an integer array `nums` and a nonnegative integer `k`, a k-diff pair consists of values `(nums[i], nums[j])` whose absolute difference is exactly `k`, using two distinct indices.

Return the number of unique k-diff pairs. Pairs are unique by their values rather than by index choices, and reversing the same two values does not create another result. When $k = 0$, a value qualifies only if it occurs at least twice; when $k > 0$, duplicate occurrences must not multiply an already counted value pair.

### Function Contract
**Inputs**

- `nums`: an integer array that may contain duplicate values
- `k`: a nonnegative target difference

**Return value**

- The number of distinct value pairs `(a, b)` with $a < b$ and $b - a = k$, or repeated-value pairs when $k = 0$

### Examples
**Example 1**

- Input: `nums = [3, 1, 4, 1, 5], k = 2`
- Output: `2`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5], k = 1`
- Output: `4`

**Example 3**

- Input: `nums = [1, 3, 1, 5, 4], k = 0`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count values rather than index pairs**

Build a frequency map for the array. The answer concerns distinct value pairs, so repeated occurrences should establish availability without multiplying the result.

**Handle positive differences in one direction**

When $k > 0$, iterate over distinct values `value` and test whether `value + k` exists. This canonical lower-to-higher direction finds every valid unordered pair once and avoids both reversed duplicates and repeated-index combinations.

**Treat zero difference as a duplicate test**

When $k = 0$, a pair requires two separate occurrences of the same value. Count exactly those frequency-map entries whose frequency is at least two. Presence alone is insufficient in this case.

**Why the count is exact**

Every positive-`k` pair has a unique smaller member, and the lookup performed for that member finds its larger partner exactly once. Every zero-`k` pair corresponds to one value with at least two occurrences, which contributes once regardless of its exact frequency. Thus no valid value pair is omitted or duplicated.

#### Complexity detail

Building the frequency map and scanning its at most `n` keys take expected $O(n)$ time. The map stores at most `n` distinct values, so space is $O(n)$.

#### Alternatives and edge cases

- **Sort plus two pointers:** uses $O(n \log n)$ time and can use less auxiliary space, but duplicates require careful skipping.
- **Seen set plus result-pair set:** supports expected $O(n)$ time in one pass, though storing canonical result tuples is more machinery than frequency counting.
- **Enumerate every index pair:** can deduplicate answers with a set but takes $O(n^2)$ time.
- **$k = 0$:** only values occurring at least twice contribute.
- **Many duplicates:** each distinct value pair is counted once, not once per index combination.
- **Negative values:** the `value + k` lookup works without special handling.
- **No matching pair:** returns zero after all distinct values are checked.

</details>
