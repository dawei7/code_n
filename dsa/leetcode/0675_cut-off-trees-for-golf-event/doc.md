# Cut Off Trees for Golf Event

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 675 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/cut-off-trees-for-golf-event/) |

## Problem Description
### Goal
A forest is represented by an $m \times n$ matrix: `0` is a cell that cannot be walked through, `1` is empty walkable ground, and a value greater than `1` is a walkable tree whose value is its height. Begin at `(0, 0)` and move one step north, east, south, or west at a time.

Cut every tree in order from shortest to tallest; all tree heights are distinct, and a cut tree's cell becomes `1`. Return the minimum total number of steps required to cut them all. If any required tree cannot be reached in that order, return `-1`. Cutting while standing on a tree costs no additional walking step.

### Function Contract
**Inputs**

- `forest`: a nonempty rectangular integer grid containing obstacles, ground, and uniquely ranked trees

**Return value**

- The minimum number of steps needed to visit and cut every tree in ascending height order, or `-1` when the required route is impossible

### Examples
**Example 1**

- Input: `forest = [[1,2,3],[0,0,4],[7,6,5]]`
- Output: `6`

**Example 2**

- Input: `forest = [[1,2,3],[0,0,0],[7,6,5]]`
- Output: `-1`

**Example 3**

- Input: `forest = [[2,3,4],[0,0,5],[8,7,6]]`
- Output: `6`
