# Find Good Days to Rob the Bank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2100 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) |

## Problem Description

### Goal

The days are numbered from $0$, and `security[i]` gives the number of guards working on day `i`. A day is considered good only if it has at least `time` earlier days and `time` later days available for inspection.

Across the `time` days leading into a good day, including the comparison with that day, guard counts must be non-increasing. Starting from that day and continuing through the following `time` days, guard counts must be non-decreasing. In other words, day `i` is good exactly when

$$
\texttt{security[i-time]} \ge \cdots \ge \texttt{security[i]}
\le \cdots \le \texttt{security[i+time]}.
$$

Return all zero-based indices that satisfy these conditions. Their output order does not matter.

### Function Contract

Let $n$ be the number of days.

**Inputs**

- `security`: a list of $n$ non-negative guard counts, where $1 \le n \le 10^5$ and $0 \le \texttt{security[i]} \le 10^5$.
- `time`: the number of required days on each side, where $0 \le \texttt{time} \le 10^5$.

**Return value**

Return every index whose preceding `time` comparisons are non-increasing and whose following `time` comparisons are non-decreasing.

### Examples

**Example 1**

- Input: `security = [5,3,3,3,5,6,2]`, `time = 2`
- Output: `[2,3]`
- Explanation: Around day `2`, $5 \ge 3 \ge 3 \le 3 \le 5$; around day `3`, $3 \ge 3 \ge 3 \le 5 \le 6$.

**Example 2**

- Input: `security = [1,1,1,1,1]`, `time = 0`
- Output: `[0,1,2,3,4]`
- Explanation: With no required days on either side, every index qualifies.

**Example 3**

- Input: `security = [1,2,3,4,5,6]`, `time = 2`
- Output: `[]`
- Explanation: No eligible center has two non-increasing days leading into it.
