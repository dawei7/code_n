# Minimum Penalty for a Shop

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2483 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-penalty-for-a-shop/) |

## Problem Description

### Goal

A shop records whether customers arrive during each hour in a zero-indexed string `customers`. The character `"Y"` means customers arrive in that hour, while `"N"` means no customers arrive.

The shop may close at any hour $j$ from $0$ through $n$, where $n$ is the length of the log. Closing at hour $j$ means hours before $j$ are open and hour $j$ itself is already closed. Each open hour with no customers adds one penalty point, and each closed hour with customers also adds one penalty point.

Return the earliest closing hour whose total penalty is minimum.

### Function Contract

**Inputs**

- `customers`: A nonempty string containing only `"Y"` and `"N"`.

Let $n = \lvert\texttt{customers}\rvert$. The constraints satisfy $1 \le n \le 10^5$.

**Return value**

Return the smallest integer $j$ with $0 \le j \le n$ that minimizes

$$
\#\{i < j : \texttt{customers[i]} = \texttt{"N"}\}
+
\#\{i \ge j : \texttt{customers[i]} = \texttt{"Y"}\}.
$$

### Examples

**Example 1**

- Input: `customers = "YYNY"`
- Output: `2`
- Explanation: Closing at hour `2` or `4` gives penalty $1$, so the earlier hour is returned.

**Example 2**

- Input: `customers = "NNNNN"`
- Output: `0`
- Explanation: Closing immediately avoids every penalty.

**Example 3**

- Input: `customers = "YYYY"`
- Output: `4`
- Explanation: Remaining open through every recorded hour gives penalty $0$.
