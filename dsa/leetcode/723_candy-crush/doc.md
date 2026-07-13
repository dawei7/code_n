# Candy Crush

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 723 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/candy-crush/) |

## Problem Description
### Goal
Given a board of candy types, identify every horizontal or vertical run containing at least three equal candies. During one round, crush all candies belonging to any qualifying run simultaneously, including candies that participate in both a horizontal and vertical run.

After the crush, let the remaining candies in each column fall downward and fill vacated cells above them with zeroes. Repeat detection, simultaneous crushing, and gravity until the board is stable and no qualifying run remains. Return that final board; do not let one marked removal hide another run from the same round.

### Function Contract
**Inputs**

- `board`: a rectangular integer matrix in which positive values identify candy types and zero represents an empty cell

**Return value**

- The stable board after all simultaneous crush-and-gravity rounds, with empty cells above the remaining candies in each column

### Examples
**Example 1**

- Input: `board = [[1,1,1],[2,3,4],[5,6,7]]`
- Output: `[[0,0,0],[2,3,4],[5,6,7]]`

**Example 2**

- Input: `board = [[1,2,1],[2,1,2],[1,2,1]]`
- Output: `[[1,2,1],[2,1,2],[1,2,1]]`

**Example 3**

- Input: `board = [[1,2,1],[2,2,2],[1,2,1]]`
- Output: `[[0,0,0],[1,0,1],[1,0,1]]`

### Required Complexity

- **Time:** $O(Rmn)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Mark every match before changing positions**

Scan all horizontal and vertical triples. When three adjacent absolute values match and are nonzero, negate all three cells. Longer and intersecting runs are fully marked because their overlapping triples are all encountered. Negative values preserve the candy type for later overlap checks while recording that the cell must be crushed.

**Use absolute values during the marking phase**

A candy may already be negative because a horizontal triple marked it before the vertical scan, or because an earlier overlapping triple reached it. Comparing absolute values lets every simultaneous match see the original board state rather than treating an earlier mark as a removal.

**Compact each column in one downward pass**

After marking completes, write positive candies from bottom to top into the lowest available positions of their column. Fill all remaining positions above them with zero. This performs the entire gravity step without repeated one-row swaps.

**Why repeating reaches exactly the stable board**

Each round marks precisely every candy belonging to a current run and removes all marks simultaneously before gravity. Column compaction preserves the relative order of surviving candies. A nonempty round removes at least three candies, so repetition must terminate; termination occurs exactly when a full scan finds no legal run.

#### Complexity detail

For `m` rows, `n` columns, and `R` simulation rounds including the final stability scan, marking and gravity take $O(mn)$ time per round, for $O(Rmn)$ total time. Marks reuse the sign bit and compaction uses only indices, so the in-place algorithm needs $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Separate crush matrix:** record matched cells in an `m × n` boolean grid; it is clear but uses $O(mn)$ additional space.
- **Repeated one-row gravity swaps:** bubble candies through empty cells until settled; it is correct but can add a factor of `m` to each gravity phase.
- **Remove one run immediately:** applying gravity before all current runs are marked violates the required simultaneous-round semantics.
- Runs longer than three are found through overlapping triples and must be removed in full.
- A candy at a horizontal and vertical intersection is removed once while contributing to both runs.
- Zeros never form crushable groups.
- A board with no initial match is returned unchanged after one scan.

</details>
