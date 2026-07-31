# Reach End of Array With Max Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3282 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Reach End of Array With Max Score](https://leetcode.com/problems/reach-end-of-array-with-max-score/) |

## Problem Description

### Goal

Begin at index `0` of an integer array and eventually reach its last index. From a current index $i$, a jump may land at any later index $j>i$; backward jumps and staying in place are not allowed.

A jump from $i$ to $j$ contributes $(j-i)\cdot\texttt{nums}[i]$ points, using the value at the departure index for every crossed position. The total score is the sum over all jumps in the path. Return the greatest total obtainable on reaching index $n-1$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, each at most $10^5$, with $1 \le n \le 10^5$.

**Return value**

Return the maximum total jump score for a forward path from index `0` to index `n - 1`. For a one-element array, the start is already the destination and the score is `0`.

### Examples

**Example 1**

- Input: `nums = [1, 3, 1, 5]`
- Output: `7`
- Explanation: Jump from index `0` to `1`, then from `1` to `3`, scoring `1 + 6`.

**Example 2**

- Input: `nums = [4, 3, 1, 3, 2]`
- Output: `16`
- Explanation: Jumping directly from index `0` to `4` scores `4 * 4`.

**Example 3**

- Input: `nums = [5]`
- Output: `0`
- Explanation: No jump is required.
