# Champagne Tower

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 799 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/champagne-tower/) |

## Problem Description

### Goal

Champagne glasses form a triangular tower, with one glass in row `0`, two in row `1`, and so on. Each glass holds one cup; any amount above one cup overflows equally into the two glasses immediately below it.

Pour `poured` cups into the top glass and let all overflow propagate downward. Return how full the zero-indexed glass `(query_row, query_glass)` becomes, capped at `1.0` because excess continues to lower rows. Empty capacity in one branch does not flow sideways into another glass.

### Function Contract

**Inputs**

- `poured`: the nonnegative number of cups poured into the top glass.
- `query_row`: the zero-based row containing the queried glass.
- `query_glass`: the zero-based position within that row.

**Return value**

- The queried glass's fill amount, capped at `1.0` because a glass holds one cup.

### Examples

**Example 1**

- Input: `poured = 1, query_row = 1, query_glass = 1`
- Output: `0.0`
- Explanation: The top glass is exactly full, so nothing reaches the second row.

**Example 2**

- Input: `poured = 2, query_row = 1, query_glass = 1`
- Output: `0.5`
- Explanation: One excess cup leaves the top and splits equally between its two children.

**Example 3**

- Input: `poured = 4, query_row = 2, query_glass = 1`
- Output: `0.5`
- Explanation: Each glass in row one receives `1.5` cups and sends `0.25` cup to the middle glass below.

### Required Complexity

- **Time:** $O(r^2)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Propagate excess instead of retained liquid**

Keep the amount arriving at each glass in the current row. A glass retains at most one cup, so only `max(0, amount - 1) / 2` flows into each child. Adding this overflow to positions `j` and $j + 1$ of the next row automatically combines contributions from the two parents of an interior glass.

**Stop at the queried row**

Begin with `[poured]` for row zero and build one new row at a time until reaching `query_row`. Every transfer uses only the completed row above, so earlier rows can be discarded. Return the queried arrival amount capped at one.

For row zero, the stored amount is exactly what was poured. If a stored row is correct, applying the capacity rule to every glass sends exactly half of each excess along each downward edge; summing at the child therefore gives its exact incoming amount. Induction makes the queried row correct, and capping its arrival models the glass's capacity.

#### Complexity detail

Let `r = query_row`. The algorithm processes $1 + 2 + \ldots + r$ glasses, taking $O(r^2)$ time. It stores only the current and next rows, each of length at most $r + 1$, for $O(r)$ auxiliary space.

#### Alternatives and edge cases

- **In-place reverse update:** A single length-$r + 2$ array can be updated from right to left, preserving the same time and space bounds with fewer allocations.
- **Full triangular table:** Storing every row makes the recurrence visually direct but uses $O(r^2)$ space when only one queried row is needed.
- **List-backed recursive memoization:** Caching states in per-row lists is correct, but linearly searching those lists adds another factor of `r` to the work.
- **Uncached recursion:** Computing both parent amounts recursively repeats the same subproblems and can take exponential time.
- **No overflow:** If a glass receives at most one cup, it contributes zero to both children.
- **Edge glasses:** They have only one possible parent, while interior glasses combine two contributions.
- **Overfilled query:** Return `1.0`, not its total incoming amount.
- **Top glass:** For `query_row = 0`, the result is simply `min(1, poured)`.

</details>
