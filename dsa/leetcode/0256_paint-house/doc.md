# Paint House

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 256 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-house/) |

## Problem Description
### Goal
Houses stand in a row, and each row of `costs` gives the price of painting that house red, blue, or green. Choose exactly one color for every house, with the restriction that adjacent houses cannot receive the same color.

Return the minimum total cost across all valid color assignments. A locally cheapest color may need to be avoided because of the neighboring choice, and the same color can be reused after at least one differently colored house. The function returns only the optimal cost, not the chosen color sequence. When there are no houses, return `0`.

### Function Contract
**Inputs**

- `costs`: one `[red, blue, green]` cost row per house

**Return value**

The minimum valid total cost, or zero for no houses.

### Examples
**Example 1**

- Input: `costs = [[17,2,17],[16,16,5],[14,3,19]]`
- Output: `10`

**Example 2**

- Input: `costs = [[7,6,2]]`
- Output: `2`

**Example 3**

- Input: `costs = []`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Each color state excludes one previous color**

Track the cheapest valid prefix ending in each of the three colors. To paint the next house red, add its red cost to the smaller prior blue/green total, and analogously for the other colors.

After processing house `i`, each state is the minimum cost of every valid coloring through `i` whose final color is that state's color.

**Three optimal prefixes are sufficient for the next decision**

Any valid coloring ending in red must previously end in blue or green; there is no other legal predecessor. Adding the red cost to the cheaper of those two optimal prefixes therefore produces the cheapest red-ending prefix. The same exhaustive transition holds for the other colors. Induction keeps all three states optimal, and the cheapest final state is the global optimum.

#### Complexity detail

Three constant-time transitions are performed per house for $O(n)$ time. Three scalar totals use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate colorings:** explores exponentially many assignments.
- **Recompute every prefix:** remains correct but can cost $O(n^2)$.
- An empty input costs zero; a single house uses its cheapest color.

</details>
