# Number of Unequal Triplets in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2475 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-unequal-triplets-in-array/) |

## Problem Description

### Goal

Given a 0-indexed array `nums` of positive integers, count index triplets `(i, j, k)` with $0 \le i < j < k < n$. The index ordering means that each choice of three array positions is counted once.

The values stored at the three selected positions must be pairwise distinct: `nums[i] != nums[j]`, `nums[i] != nums[k]`, and `nums[j] != nums[k]`. Return the number of triplets satisfying both the index and value conditions.

### Function Contract

**Inputs**

- `nums`: An array of positive integers with $3 \le n = \lvert\texttt{nums}\rvert \le 100$ and $1 \le \texttt{nums}[i] \le 1000$.

**Return value**

Return an integer equal to the number of increasing index triplets whose three values are pairwise distinct.

### Examples

#### Example 1

- **Input:** `nums = [4,4,2,4,3]`
- **Output:** `3`
- **Explanation:** Choosing the value `4` from any of its three positions together with `2` and `3` produces one valid index triplet.

#### Example 2

- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `0`
- **Explanation:** Three pairwise distinct values cannot be selected.

#### Example 3

- **Input:** `nums = [1,2,3]`
- **Output:** `1`
- **Explanation:** The only three positions contain three distinct values.
