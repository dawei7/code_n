# Number of Unique Flavors After Sharing K Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2107 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [number-of-unique-flavors-after-sharing-k-candies](https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/) |

## Problem Description

### Goal

You have a 0-indexed array `candies`, where each integer identifies one candy's flavor. To share with your little sister, you must select exactly `k` consecutive candies and give her that entire contiguous block. The candies before and after the selected block are the ones you keep.

Different choices of the shared block can remove different occurrences of repeated flavors. Choose its starting position so that the candies left with you contain as many unique flavors as possible, and return that maximum count. When `k = 0`, the shared block is empty and you keep every candy; when `k` equals the array length, you keep none.

### Function Contract

**Inputs**

- `candies`: A 0-indexed integer array of length $n$, where $0 \le n \le 10^5$ and $1 \le \texttt{candies[i]} \le 10^5$.
- `k`: The exact number of consecutive candies to share, where $0 \le k \le n$.

**Return value**

Return the maximum number of unique flavors among the candies kept after sharing one consecutive block of length `k`.

### Examples

**Example 1**

- Input: `candies = [1, 2, 2, 3, 4, 3], k = 3`
- Output: `3`
- Explanation: Share the block `[2, 2, 3]` at indices $1$ through $3$. The kept flavors are `[1, 4, 3]`, all distinct.

**Example 2**

- Input: `candies = [2, 2, 2, 2, 3, 3], k = 2`
- Output: `2`
- Explanation: A suitable shared block leaves at least one candy of flavors $2$ and $3`.

**Example 3**

- Input: `candies = [2, 4, 5], k = 0`
- Output: `3`
- Explanation: No candies are shared, so all three unique flavors remain.
