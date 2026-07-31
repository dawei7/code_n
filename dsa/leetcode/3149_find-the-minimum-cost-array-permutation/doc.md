# Find the Minimum Cost Array Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3149 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-minimum-cost-array-permutation/) |

## Problem Description
### Goal
The input `nums` is a permutation of the integers from $0$ through $n-1$. Consider another permutation `perm` of those same integers. Its score is cyclic: for every position $i$, compare `perm[i]` with the value of `nums` indexed by the next permutation element, where the element after `perm[n - 1]` is `perm[0]`.

Thus each contribution is $\lvert \texttt{perm[i]}-\texttt{nums[perm[(i+1) \bmod n]]}\rvert$. Return a permutation having the smallest possible total score. If several permutations share that minimum, return the lexicographically smallest one.

### Function Contract
**Inputs**

- `nums`: A permutation of `[0, 1, ..., n - 1]`, where $2 \le n \le 14$.

**Return value**

Return the lexicographically smallest permutation of `[0, 1, ..., n - 1]` among all permutations with minimum cyclic score.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2]`
- Output: `[0, 1, 2]`
- Explanation: Its score is `abs(0 - nums[1]) + abs(1 - nums[2]) + abs(2 - nums[0]) = 0 + 1 + 1 = 2`.

**Example 2**

- Input: `nums = [0, 2, 1]`
- Output: `[0, 2, 1]`
- Explanation: Its cyclic contributions are `abs(0 - nums[2])`, `abs(2 - nums[1])`, and `abs(1 - nums[0])`, totaling `2`.

**Example 3**

- Input: `nums = [2, 0, 3, 1]`
- Output: `[0, 1, 3, 2]`
