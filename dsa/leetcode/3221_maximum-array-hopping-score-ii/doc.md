# Maximum Array Hopping Score II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3221 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-array-hopping-score-ii/) |

## Problem Description

### Goal

You are given an integer array `nums`. Begin at index `0` and make one or more forward hops until reaching the last index. A hop from index $i$ to a strictly later index $j$ contributes $(j-i)\cdot\texttt{nums[j]}$ to the score.

You may choose any increasing sequence of visited indices as long as it starts at `0` and ends at the final element. Return the maximum total score achievable across all such hopping paths. The value at the departure index does not affect a hop; only its distance and the destination value do.

### Function Contract

**Inputs**

- `nums`: A list of integers with $2 \leq \lvert\texttt{nums}\rvert \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^5$.

**Return value**

Return the maximum hopping score obtainable when the final visited index is $\lvert\texttt{nums}\rvert-1$.

### Examples

**Example 1**

- Input: `nums = [1, 5, 8]`
- Output: `16`
- Explanation: Hopping directly from index `0` to index `2` scores `2 * 8 = 16`.

**Example 2**

- Input: `nums = [4, 5, 2, 8, 9, 1, 3]`
- Output: `42`
- Explanation: The path `0 -> 4 -> 6` scores `4 * 9 + 2 * 3 = 42`.

**Example 3**

- Input: `nums = [9, 8, 7, 6]`
- Output: `21`
- Explanation: Visiting every later index scores `8 + 7 + 6`.
