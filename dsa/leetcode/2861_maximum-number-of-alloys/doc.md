# Maximum Number of Alloys

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2861 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-alloys/) |

## Problem Description

### Goal

A company works with $n$ types of metal and owns $k$ machines for producing alloys. Machine $i$ has its own recipe: producing one alloy with that machine consumes `composition[i][j]` units of metal type $j$.

The company initially owns `stock[j]` units of metal $j$. Any additional unit of that metal can be purchased for `cost[j]` coins, and at most `budget` coins may be spent. Choose one machine and determine the greatest number of alloys it can produce within the available stock and purchasing budget. Every produced alloy must use that same machine; recipes from different machines cannot be mixed.

### Function Contract

**Inputs**

- `n`: The number of metal types.
- `k`: The number of machines.
- `budget`: The maximum number of coins available for additional metal.
- `composition`: A $k \times n$ matrix whose row `composition[i]` gives machine $i$'s per-alloy metal requirements.
- `stock`: The currently available amount of each metal.
- `cost`: The purchase price of one additional unit of each metal.

The input satisfies $1 \le n,k \le 100$, $0 \le \texttt{budget} \le 10^8$, and `composition` has $k$ rows of length $n$. Every recipe entry is between $1$ and $100$. Both `stock` and `cost` have length $n$, with $0 \le \texttt{stock[j]} \le 10^8$ and $1 \le \texttt{cost[j]} \le 100$.

**Return value**

- Return the maximum number of alloys obtainable with one chosen machine without spending more than `budget`.

### Examples

**Example 1**

- Input: `n = 3, k = 2, budget = 15, composition = [[1, 1, 1], [1, 1, 10]], stock = [0, 0, 0], cost = [1, 2, 3]`
- Output: `2`
- Explanation: With the first machine, two alloys require two units of every metal. Buying them costs `2 * 1 + 2 * 2 + 2 * 3 = 12`, which fits the budget; no machine can produce three alloys.

**Example 2**

- Input: `n = 3, k = 2, budget = 15, composition = [[1, 1, 1], [1, 1, 10]], stock = [0, 0, 100], cost = [1, 2, 3]`
- Output: `5`
- Explanation: The second machine can use the stocked third metal. Buying five units of each of the first two metals costs `5 * 1 + 5 * 2 = 15`.

**Example 3**

- Input: `n = 2, k = 3, budget = 10, composition = [[2, 1], [1, 2], [1, 1]], stock = [1, 1], cost = [5, 5]`
- Output: `2`
- Explanation: The third machine needs one unit of each metal per alloy. The initial stock supplies the first alloy, and the missing units for a second alloy cost exactly `10` coins.
