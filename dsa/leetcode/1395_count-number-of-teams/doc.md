# Count Number of Teams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1395 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/count-number-of-teams/) |

## Problem Description

### Goal

Soldiers stand in a row, and `rating[i]` gives the distinct rating of the soldier at position `i`. A team consists of three soldiers selected at indices $i < j < k$, so their order in the row must be preserved.

The team is valid when its ratings are strictly increasing, with $\texttt{rating[i]} < \texttt{rating[j]} < \texttt{rating[k]}$, or strictly decreasing, with $\texttt{rating[i]} > \texttt{rating[j]} > \texttt{rating[k]}$. Return the number of valid teams. A soldier may participate in more than one team.

### Function Contract

**Inputs**

- `rating`: an array of $n$ pairwise distinct ratings, where $3 \le n \le 1000$ and $1 \le \texttt{rating[i]} \le 10^5$.

**Return value**

- The number of increasing or decreasing index-ordered triples.

### Examples

**Example 1**

- Input: `rating = [2,5,3,4,1]`
- Output: `3`

**Example 2**

- Input: `rating = [2,1,3]`
- Output: `0`

**Example 3**

- Input: `rating = [1,2,3,4]`
- Output: `4`
