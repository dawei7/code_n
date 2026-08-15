# Maximum Array Hopping Score I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3205 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-array-hopping-score-i/) |

## Problem Description

### Goal

Start at index `0` of `nums` and reach its final index through one or more forward hops. From a current index `i`, a hop may land at any index `j` with $j>i$.

Landing at `j` earns `(j - i) * nums[j]` points. The value at the starting index does not itself earn points; every hop is weighted by the value at its destination.

Choose the increasing sequence of visited indices that maximizes the total score, and return that maximum.

### Function Contract

**Inputs**

- `nums`: An array of positive integers with $2 \le \lvert\texttt{nums}\rvert \le 10^3$ and $1 \le \texttt{nums}[i] \le 10^5$.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- The greatest total score obtainable while hopping from index `0` to index `n - 1`.

### Examples

#### Example 1

- **Input:** `nums = [1,5,8]`
- **Output:** `16`
- **Explanation:** Hopping directly from `0` to `2` scores `(2 - 0) * 8 = 16`, which beats visiting index `1` first.

#### Example 2

- **Input:** `nums = [4,5,2,8,9,1,3]`
- **Output:** `42`
- **Explanation:** The hops `0 -> 4 -> 6` score `(4 - 0) * 9 + (6 - 4) * 3 = 42`.
