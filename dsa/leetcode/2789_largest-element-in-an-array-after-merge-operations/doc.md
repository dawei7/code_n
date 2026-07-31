# Largest Element in an Array after Merge Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2789 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` containing positive integers. You may repeatedly choose an index `i` with $0 \le i < \lvert\texttt{nums}\rvert - 1$ whenever `nums[i] <= nums[i + 1]`.

For one operation, replace the right element by `nums[i] + nums[i + 1]` and delete the left element. The array therefore becomes one element shorter, and the newly formed sum may participate in later operations. Perform any number of legal operations and return the largest element value that can possibly appear in the final array.

### Function Contract

**Inputs**

- `nums`: A non-empty array of positive integers, with $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return the maximum element value attainable after any sequence of allowed adjacent merges.

### Examples

**Example 1**

- Input: `nums = [2, 3, 7, 9, 3]`
- Output: `21`
- Explanation: Merge $2$ into $3$, then $7$ into $9$, and finally $5$ into $16$. The array becomes `[21, 3]`, and no larger value can be formed.

**Example 2**

- Input: `nums = [5, 3, 3]`
- Output: `11`
- Explanation: The two threes first merge into $6$. The leading $5$ can then merge into that value, leaving `[11]`.
