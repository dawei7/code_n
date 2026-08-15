# Minimum Impossible OR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2568 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-impossible-or](https://leetcode.com/problems/minimum-impossible-or/) |

## Problem Description

### Goal

An integer is expressible from `nums` when it equals the bitwise OR of a non-empty subsequence of the array. The selected indices must retain their original order, although bitwise OR is unaffected by that ordering.

Return the smallest positive, nonzero integer that is not expressible. Values may be selected only once through their array positions, and any unselected elements are ignored.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- The smallest positive integer that cannot be formed as the bitwise OR of a subsequence of `nums`.

### Examples

#### Example 1

- **Input:** `nums = [2, 1]`
- **Output:** `4`
- **Explanation:** The values $1$ and $2$ are present, and their OR forms $3$; no subsequence can form $4$.

#### Example 2

- **Input:** `nums = [5, 3, 2]`
- **Output:** `1`
- **Explanation:** Every available value has a bit other than the least significant bit, so none can produce exactly $1$.

#### Example 3

- **Input:** `nums = [1, 2, 4, 8]`
- **Output:** `16`
- **Explanation:** Every positive value below $16$ can be assembled from the four available single-bit values, while $16$ itself cannot.
