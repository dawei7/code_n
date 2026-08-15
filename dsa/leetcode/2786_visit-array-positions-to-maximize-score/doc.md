# Visit Array Positions to Maximize Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2786 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a positive integer `x`. You begin at index $0$, so `nums[0]` is always included in the score.

From a visited index $i$, you may next visit any index $j$ with $i<j$. Visiting an index adds its array value to the score. When two consecutive visited values have different parity—one even and the other odd—the move also subtracts `x`. Moving between values of the same parity has no penalty.

Choose any increasing sequence of visited indices that starts at $0$ and return the maximum total score. Indices may be skipped, and parity refers to whether each integer is even or odd.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.
- `x`: The positive score penalty for changing parity between consecutive visited values, where $1 \le x \le 10^6$.

**Return value**

Return the greatest score obtainable by an increasing sequence of visited indices that includes index $0$.

### Examples

#### Example 1

- **Input:** `nums = [2,3,6,1,9,2]`, `x = 5`
- **Output:** `13`
- **Explanation:** Visiting indices `0 -> 2 -> 3 -> 4` scores `2 + 6 + 1 + 9 - 5 = 13`. Only the move from `6` to `1` changes parity.

#### Example 2

- **Input:** `nums = [2,4,6,8]`, `x = 3`
- **Output:** `20`
- **Explanation:** All four values are even, so visiting every index earns their full sum without a penalty.

#### Example 3

- **Input:** `nums = [1,100]`, `x = 10`
- **Output:** `91`
- **Explanation:** Index $0$ is mandatory. Moving to the even value changes parity, but `1 + 100 - 10` is better than stopping at the first index.
