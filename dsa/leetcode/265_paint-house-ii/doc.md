# Paint House II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 265 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-house-ii/) |

## Problem Description
### Goal
Houses stand in a row, and the $n \times k$ matrix `costs` gives the price of painting each house with each of `k` available colors. Choose exactly one color per house, with adjacent houses required to use different colors.

Return the minimum total cost among all valid color assignments. A color's meaning is determined by its column and can be reused on nonadjacent houses. A locally cheapest choice may block a cheaper option for the next house, so all neighbor constraints must be satisfied together. Return `0` when there are no houses, and return only the optimal cost rather than the selected color sequence.

### Function Contract
**Inputs**

- `costs`: an `n × k` matrix of painting costs

**Return value**

The minimum cost of a valid coloring, or zero when there are no houses.

### Examples
**Example 1**

- Input: `costs = [[1,5,3],[2,9,4]]`
- Output: `5`

**Example 2**

- Input: `costs = [[8,2,6,4]]`
- Output: `2`

**Example 3**

- Input: `costs = []`
- Output: `0`

### Required Complexity

- **Time:** $O(nk)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**One forbidden color makes two minima sufficient**

For each completed row, remember the smallest total, its color, and the second-smallest total. A new color adds its cost to the smallest prior total unless that total used the same color; then it uses the second smallest.

After each house, the DP value for every color is the cheapest valid prefix ending in that color. The two retained minima are exactly the best and second-best values of that row.

**Excluding the current color selects the right predecessor**

A prefix ending in color `c` may extend every previous color except `c`. If the cheapest prior state uses another color, it is plainly the best allowed predecessor. If it uses `c`, removing that single forbidden state makes the second-cheapest prior state optimal. Each transition is therefore exact, and induction makes the minimum of the last row globally optimal.

#### Complexity detail

Each of `n` rows performs constant work for each of `k` colors, giving $O(nk)$ time. The current DP row uses $O(k)$ space.

#### Alternatives and edge cases

- **Compare every prior color:** takes $O(nk^2)$.
- No houses cost zero; one house chooses its cheapest color. Native constraints provide enough colors for multiple houses.

</details>
