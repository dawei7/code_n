# Count Largest Group

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1399 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/count-largest-group/) |

## Problem Description

### Goal

Consider every integer from $1$ through $n$, inclusive. Place two integers in the same group exactly when the sums of their decimal digits are equal. For example, `13` belongs to the group for digit sum `4`.

After all integers have been assigned, find the greatest group size. Return how many distinct digit-sum groups have that size. The requested result is the number of groups tied for largest, not the number of integers inside one largest group.

### Function Contract

**Inputs**

- `n`: the inclusive upper bound, where $1 \le n \le 10^4$.

Let $d$ be the number of decimal digits in $n$.

**Return value**

- The number of digit-sum groups whose cardinality equals the maximum group cardinality.

### Examples

**Example 1**

- Input: `n = 13`
- Output: `4`

**Example 2**

- Input: `n = 2`
- Output: `2`

**Example 3**

- Input: `n = 15`
- Output: `6`
