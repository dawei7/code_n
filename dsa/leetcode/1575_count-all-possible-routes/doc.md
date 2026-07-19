# Count All Possible Routes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1575 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/count-all-possible-routes/) |

## Problem Description
### Goal

There are $N$ cities on a number line. City `i` is located at coordinate `locations[i]`, and every coordinate is distinct. A journey begins at the city indexed by `start` with a fixed amount of `fuel`, and its destination is the city indexed by `finish`.

From the current city `i`, a route may move to any different city `j`. That move consumes exactly $\lvert\texttt{locations[i]}-\texttt{locations[j]}\rvert$ units of fuel. Fuel may never become negative, cities may be visited repeatedly, and a route may continue traveling after visiting `finish`.

Count every route that is at `finish` after zero or more moves without spending more than the available fuel. Stopping at different visits produces different valid routes; in particular, the empty route counts when `start == finish`. Return the total modulo $1{,}000{,}000{,}007$.

### Function Contract
**Inputs**

- `locations`: An array of $N$ distinct integer coordinates, where $2 \le N \le 100$ and $1 \le \texttt{locations[i]} \le 10^9$.
- `start`: The zero-based index of the starting city, where $0 \le \texttt{start} < N$.
- `finish`: The zero-based index of the destination city, where $0 \le \texttt{finish} < N$.
- `fuel`: The initial fuel amount, where $1 \le \texttt{fuel} \le 200$.

**Return value**

Return the number of valid routes from `start` to `finish`, modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `locations = [2, 3, 6, 8, 4], start = 1, finish = 3, fuel = 5`
- Output: `4`

**Example 2**

- Input: `locations = [4, 3, 1], start = 1, finish = 0, fuel = 6`
- Output: `5`

**Example 3**

- Input: `locations = [5, 2, 1], start = 0, finish = 2, fuel = 3`
- Output: `0`
