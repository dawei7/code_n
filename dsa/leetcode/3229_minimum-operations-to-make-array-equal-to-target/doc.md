# Minimum Operations to Make Array Equal to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3229 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/) |

## Problem Description

### Goal

You are given two positive-integer arrays, `nums` and `target`, with the same length. One operation selects any contiguous subarray of `nums` and either increments every selected element by $1$ or decrements every selected element by $1$.

Different operations may choose different subarrays and directions. Return the minimum number of operations needed in total to make `nums` exactly equal to `target`.

### Function Contract

**Inputs**

- `nums`: The starting array, with $1 \leq \lvert\texttt{nums}\rvert \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^8$.
- `target`: The desired array, where $\lvert\texttt{target}\rvert = \lvert\texttt{nums}\rvert$ and $1 \leq \texttt{target[i]} \leq 10^8$.

**Return value**

Return the minimum number of subarray increment or decrement operations required to transform `nums` into `target`.

### Examples

#### Example 1

- **Input:** `nums = [3, 5, 1, 2]`, `target = [4, 6, 2, 4]`
- **Output:** `2`
- **Explanation:** Increment the whole array once, then increment only its final element.

#### Example 2

- **Input:** `nums = [1, 3, 2]`, `target = [2, 1, 4]`
- **Output:** `5`
- **Explanation:** The three required changes have alternating directions, so no operation can serve two adjacent positions.

#### Example 3

- **Input:** `nums = [5, 5, 5]`, `target = [6, 8, 7]`
- **Output:** `4`
- **Explanation:** Three nested increment layers reach the middle position, while one additional shared layer covers all three positions.
