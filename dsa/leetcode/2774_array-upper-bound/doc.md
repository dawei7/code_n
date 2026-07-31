# Array Upper Bound

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2774 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [2774. Array Upper Bound](https://leetcode.com/problems/array-upper-bound/) |

## Problem Description

### Goal

Extend JavaScript's `Array` prototype with a method named `upperBound`. The receiving array contains numbers sorted in ascending order and may include duplicate values. Calling `nums.upperBound(target)` must locate the final occurrence of the supplied target number.

Return that occurrence's zero-based index. If no array element equals `target`, return `-1`. The method must work on every valid numeric array, including arrays whose matching values occupy the first or last positions, and it should exploit the sorted order to meet the requested logarithmic running time.

### Function Contract

**Inputs**

- `nums`: A non-empty ascending array of $n$ numbers that receives `upperBound` through `Array.prototype`.
- `target`: The number whose last occurrence is requested.

The inputs satisfy $1 \le n \le 10^4$ and $-10^4 \le \texttt{nums}[i],\texttt{target} \le 10^4$.

**Return value**

Return the greatest index $i$ for which `nums[i] === target`, or `-1` when no such index exists.

### Examples

**Example 1**

- Input: `nums = [3, 4, 5], target = 5`
- Output: `2`
- Explanation: The target appears at the final array index.

**Example 2**

- Input: `nums = [1, 4, 5], target = 2`
- Output: `-1`
- Explanation: No element equals `2`.

**Example 3**

- Input: `nums = [3, 4, 6, 6, 6, 6, 7], target = 6`
- Output: `5`
- Explanation: The duplicate run of `6` ends at index `5`.
