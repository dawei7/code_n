# Minimum Cost to Cut a Stick

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1547 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) |

## Problem Description
### Goal
A wooden stick has length `n` and is marked at every position in `cuts`. Every marked position must eventually be cut. Performing a cut costs the current length of the particular stick segment being cut, not the length of the original stick.

You may perform the required cuts in any order. Earlier choices determine the segment containing each later mark and therefore change later costs. Return the minimum possible total cost after all requested cuts have been made.

### Function Contract
**Inputs**

- `n`: the original stick length, where $2 \le n \le 10^6$.
- `cuts`: $c$ distinct integer positions strictly inside the stick, where $1 \le c \le \min(n-1, 100)$ and $1 \le \texttt{cuts[i]} \le n-1$. The input order is arbitrary.

**Return value**

The minimum sum of segment lengths paid while performing every requested cut.

### Examples
**Example 1**

- Input: `n = 7, cuts = [1, 3, 4, 5]`
- Output: `16`
- Explanation: One optimal order is `3, 5, 1, 4`, with costs $7+4+3+2=16$.

**Example 2**

- Input: `n = 9, cuts = [5, 6, 1, 4, 2]`
- Output: `22`
- Explanation: Reordering the five required cuts avoids repeatedly paying for unnecessarily long pieces.

**Example 3**

- Input: `n = 5, cuts = [2, 4]`
- Output: `8`
- Explanation: Cutting at position two first costs five, then cutting the remaining length-three piece at position four costs three.
