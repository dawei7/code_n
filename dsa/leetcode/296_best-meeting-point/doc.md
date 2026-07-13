# Best Meeting Point

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 296 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-meeting-point/) |

## Problem Description
### Goal
Given a nonempty binary grid, each cell marked `1` contains one person. Choose a grid cell where everyone will meet; the meeting location may be occupied or empty. Travel distance is Manhattan distance, the sum of horizontal and vertical coordinate differences.

Return the minimum possible sum of distances from all people to one meeting cell. Each person contributes independently, and diagonal movement offers no shortcut under this metric. The function returns only the smallest total, not the meeting coordinates. The grid contains at least one person, and its rectangular dimensions define all candidate cells.

### Function Contract
**Inputs**

- `grid`: a nonempty rectangular binary matrix

**Return value**

The minimum total Manhattan distance from all `1` cells to one meeting cell.

### Examples
**Example 1**

- Input: `grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]`
- Output: `6`

**Example 2**

- Input: `grid = [[1]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,1]]`
- Output: `1`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Separate the two coordinates**

Manhattan distance is additive:
`abs(row - r) + abs(column - c)`. Choosing the meeting row does not affect the column cost, and choosing the meeting column does not affect the row cost. The two-dimensional optimization is therefore two independent one-dimensional problems.

**The one-dimensional optimum is a median**

For sorted coordinates, moving a candidate point toward the middle decreases distance to more points on the far side than it increases distance to points already passed. The total absolute deviation stops decreasing at a median. Thus any median occupied row and any median occupied column form an optimal meeting point; the point itself need not contain a person.

Collect rows by scanning the grid row by row, which naturally produces sorted row coordinates. Collect columns with the column loop outermost, which produces sorted column coordinates without an additional sort. Pick the middle entry of each list and sum the two absolute-deviation totals.

For occupied cells `(0,0)`, `(0,4)`, and `(2,2)`, the row coordinates are `[0,0,2]` and columns are `[0,2,4]`. Their medians give `(0,2)`, with distances $2 + 2 + 2 = 6$.

**Why optimizing each axis is sufficient**

For any meeting cell `(r,c)`, the total is $\operatorname{row\_cost}(r) + \operatorname{column\_cost}(c)$. Replacing `r` by a row median cannot increase the first term and leaves the second unchanged; replacing `c` by a column median does the symmetric thing. The resulting pair therefore has cost no greater than any original cell and is globally optimal.

#### Complexity detail

Both collection scans inspect all `mn` cells, and the final sums visit each of the `k` occupied cells, for $O(mn)$ time. The coordinate lists use $O(k)$ space. No coordinate sort is required because the traversal orders are chosen deliberately.

#### Alternatives and edge cases

- **Try every grid cell:** computing its distance to every person costs $O(mn \cdot k)$.
- **Collect coordinates in arbitrary order and sort:** remains correct but adds $O(k \log k)$ time unnecessarily.
- With one person the distance is zero. With an even number of people, every coordinate between the two middle coordinates is optimal; choosing either stored median is sufficient.

</details>
