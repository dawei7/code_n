# Maximize the Minimum Powered City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2528 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Queue, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-minimum-powered-city/) |

## Problem Description

### Goal

There are $n$ cities indexed from $0$ to $n-1$. The integer `stations[i]` is the number of power stations already built in city $i$. Every station has range `r`: a station in city $i$ supplies each city $j$ satisfying $\lvert i-j\rvert \le r$. A city's power is the total number of existing stations that supply it.

The government may build `k` additional stations and distribute them among the cities in any way; multiple new stations may be placed in the same city, and each has the same range `r`. Choose their locations to make the least-powered city as powerful as possible, and return that maximum achievable minimum power.

### Function Contract

**Inputs**

- `stations`: The existing station counts for the cities in index order.
- `r`: The inclusive distance covered by every station.
- `k`: The number of additional stations available.

Let $n = \lvert\texttt{stations}\rvert$. The constraints are $1 \le n \le 10^5$, $0 \le \texttt{stations[i]} \le 10^5$, $0 \le r \le n-1$, and $0 \le k \le 10^9$.

**Return value**

Return the greatest possible value of the minimum city power after placing the additional stations optimally.

### Examples

#### Example 1

- **Input:** `stations = [1, 2, 4, 5, 0], r = 1, k = 2`
- **Output:** `5`
- **Explanation:** Placing both new stations at city `1` produces city powers whose minimum is `5`, and no placement can make that minimum larger.

#### Example 2

- **Input:** `stations = [4, 4, 4, 4], r = 0, k = 3`
- **Output:** `4`
- **Explanation:** With range zero, raising all four cities above `4` would require at least four additional stations.
