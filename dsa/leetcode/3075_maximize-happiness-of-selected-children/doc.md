# Maximize Happiness of Selected Children

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3075 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-happiness-of-selected-children/) |

## Problem Description

### Goal

There are $n$ children in a queue, and `happiness[i]` is child $i$'s initial happiness value. Select exactly $k$ children over $k$ turns and maximize the sum of the happiness values they have at the moments they are selected.

After each turn, every child that has not yet been selected loses one happiness point if their current value is positive. A happiness value never becomes negative: a child already at zero stays at zero. The selected child is removed from the later decrements.

Return the greatest total obtainable by choosing the selection order optimally.

### Function Contract

**Inputs**

- `happiness`: A list of $n$ positive integers containing the children's initial happiness values.
- `k`: The number of children that must be selected, where $1 \le k \le n$.

The length satisfies $1 \le n \le 2 \cdot 10^5$, and every initial happiness value lies from $1$ through $10^8$.

**Return value**

- The maximum sum of the current happiness values collected while selecting exactly $k$ children.

### Examples

#### Example 1

- **Input:** `happiness = [1, 2, 3]`, `k = 2`
- **Output:** `4`
- **Explanation:** Select the child worth `3`; the remaining values become `[0, 1]`. Selecting the child now worth `1` gives `3 + 1 = 4`.

#### Example 2

- **Input:** `happiness = [1, 1, 1, 1]`, `k = 2`
- **Output:** `1`
- **Explanation:** The first selection contributes `1`, after which every unselected child has happiness zero, so the second contributes `0`.

#### Example 3

- **Input:** `happiness = [2, 3, 4, 5]`, `k = 1`
- **Output:** `5`
- **Explanation:** With one turn, selecting the child with the largest initial happiness is optimal.
