# Maximum Number of Jumps to Reach the Last Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2770 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [2770. Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) |

## Problem Description

### Goal

You begin at index $0$ of a 0-indexed integer array `nums`. From the current index $i$, you may jump forward to any index $j$ with $i<j$ when the value change satisfies $-\texttt{target} \le \texttt{nums}[j]-\texttt{nums}[i] \le \texttt{target}$. Every jump must move to a strictly larger index, although it may skip any number of positions.

Among all valid sequences that finish at the final index $n-1$, return the greatest possible number of jumps. The objective is to maximize the number of edges in the route, not to minimize travel. If no valid sequence can reach the final index, return $-1$.

### Function Contract

**Inputs**

- `nums`: An integer list of length $n$, where $2 \le n \le 1000$ and $-10^9 \le \texttt{nums}[i] \le 10^9$.
- `target`: The inclusive maximum absolute difference allowed by a jump, with $0 \le \texttt{target} \le 2\cdot10^9$.

**Return value**

Return the maximum number of valid jumps needed by any route from index $0$ to index $n-1$, or $-1$ when the destination is unreachable.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 6, 4, 1, 2], target = 2`
- **Output:** `3`
- **Explanation:** One longest valid route uses indices $0 \to 1 \to 3 \to 5$.

#### Example 2

- **Input:** `nums = [1, 3, 6, 4, 1, 2], target = 3`
- **Output:** `5`
- **Explanation:** Every consecutive jump is valid, so all six indices can be visited.

#### Example 3

- **Input:** `nums = [1, 3, 6, 4, 1, 2], target = 0`
- **Output:** `-1`
- **Explanation:** No forward route reaches the final value while requiring equal endpoint values for every jump.
