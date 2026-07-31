# Maximum Total Subarray Value II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3691 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Segment Tree, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-ii/) |

## Problem Description
### Goal

Choose exactly `k` distinct nonempty subarrays of `nums`. Two choices are distinct when their left or right endpoint differs; selected intervals may otherwise overlap freely. For each chosen subarray, calculate its maximum element minus its minimum element, then add the `k` resulting values.

Return the greatest total obtainable. Unlike the related version that permits repeated endpoints, the same interval cannot be selected twice, so the answer must combine the `k` largest values among all $n(n+1)/2$ distinct subarrays rather than multiplying one best value.

### Function Contract

**Inputs**

- `nums`: A nonempty list of $n$ integers, where $1 \le n \le 5\cdot10^4$ and $0 \le \texttt{nums[i]} \le 10^9$.
- `k`: The exact number of distinct subarrays to select, satisfying $1 \le k \le \min(10^5, n(n+1)/2)$.

**Return value**

Return the maximum possible sum of the ranges of exactly `k` distinct subarrays. The result may exceed 32-bit integer range.

### Examples

**Example 1**

- Input: `nums = [1, 3, 2], k = 2`
- Output: `4`

The intervals `[1, 3]` and `[1, 3, 2]` are distinct and each has range 2.

**Example 2**

- Input: `nums = [4, 2, 5, 1], k = 3`
- Output: `12`

Three different intervals contain both 5 and 1 and each contribute 4.

**Example 3**

- Input: `nums = [1, 2, 3], k = 6`
- Output: `4`

Selecting every subarray contributes ranges `2, 1, 1, 0, 0, 0`.
