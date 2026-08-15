# Minimum Runes to Add to Cast Spell

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3383 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/) |

## Problem Description

### Goal

A spell contains `n` focus points numbered from $0$ through $n-1$. Some focus points listed in `crystals` hold an energy source. Existing directed runes are described by corresponding entries of `flowFrom` and `flowTo`: magic can travel along each rune from `flowFrom[i]` to `flowTo[i]`.

A focus point can participate in the cast if it contains a crystal or can receive magic through a directed path originating at a crystal. Alice may add new directed runes between focus points. Added runes can extend the energized region further, just like the existing ones.

Return the minimum number of directed runes that must be added so every focus point becomes energized.

### Function Contract

**Inputs**

- `n`: The number of focus points, labeled from $0$ to $n-1$.
- `crystals`: A nonempty list of focus points that initially contain crystals.
- `flowFrom`: The source endpoints of the existing directed runes.
- `flowTo`: The corresponding destination endpoints of those runes.

Let $m=\lvert\texttt{flowFrom}\rvert=\lvert\texttt{flowTo}\rvert$. The constraints are $2\leq n\leq10^5$, $1\leq\lvert\texttt{crystals}\rvert\leq n$, and $1\leq m\leq\min(2\cdot10^5,n(n-1)/2)$. Every endpoint is a valid focus point, no rune is a self-loop, and all existing directed runes are distinct.

**Return value**

- The minimum number of new directed runes needed to make every focus point reachable from at least one crystal.

### Examples

#### Example 1

- **Input:** `n = 6, crystals = [0], flowFrom = [0,1,2,3], flowTo = [1,2,3,0]`
- **Output:** `2`
- **Explanation:** The crystal energizes the cycle containing points zero through three, while isolated points four and five each need a new incoming rune.

#### Example 2

- **Input:** `n = 7, crystals = [3,5], flowFrom = [0,1,2,3,5], flowTo = [1,2,0,4,6]`
- **Output:** `1`
- **Explanation:** The two crystals already energize points three through six. One new rune into the separate cycle containing zero, one, and two energizes that entire cycle.
