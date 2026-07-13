# Battleships in a Board

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 419 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/battleships-in-a-board/) |

## Problem Description
### Goal
Given a nonempty rectangular board containing ship cells `"X"` and empty cells `"."`, each battleship is one straight horizontal or vertical run of one or more ship cells. Ships never bend, and distinct ships do not touch through a horizontal or vertical edge.

Return the number of battleships in one pass, without modifying the board and using only $O(1)$ extra memory. A single isolated `"X"` is a one-cell ship, and diagonally touching ships remain distinct. Count each run once rather than once per occupied cell. The task returns only the number of ships, not their coordinates, lengths, or orientations.

### Function Contract
**Inputs**

- `board`: a nonempty rectangular character matrix containing only `"X"` and `"."`

**Return value**

- Return the number of distinct battleships without modifying the board.

### Examples
**Example 1**

- Input: `board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]`
- Output: `2`

**Example 2**

- Input: `board = [["."]]`
- Output: `0`

**Example 3**

- Input: `board = [["X"]]`
- Output: `1`

### Required Complexity

- **Time:** $O(rc)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Give every ship one canonical cell**

The leftmost cell of a horizontal ship and the topmost cell of a vertical ship have no ship cell immediately above or immediately left. Every other cell in either orientation has one of those predecessors.

**Count only canonical starts**

Scan every board position. Ignore empty cells. For an `"X"`, also ignore it when the cell above exists and is `"X"`, or when the cell to the left exists and is `"X"`. Count it only when both predecessor checks are absent or empty.

**Why no start is shared by two ships**

Ships are straight and distinct ships do not touch orthogonally. Therefore an `"X"` cannot be the intersection of horizontal and vertical ships, and no neighboring ship can masquerade as its predecessor. Each ship contributes exactly one accepted start cell.

**Avoid mutation and visited storage**

The local predecessor test derives membership from the valid board structure itself. There is no need to erase cells, flood-fill a component, or remember previously visited coordinates.

#### Complexity detail

Every one of the $r \cdot c$ cells receives a constant number of neighbor checks, giving $O(rc)$ time. Counters and indices use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Depth-first or breadth-first component counting:** is linear but uses $O(rc)$ visited storage or modifies the board.
- **Walk back to a canonical head for every ship cell:** is correct but can rescan a long ship and take quadratic time.
- **Count all X cells and divide by a length:** fails because ships can have different lengths.
- An all-empty board contains zero ships.
- A one-cell ship is its own canonical start.
- A ship may occupy an entire row or column.
- Boundary checks must not read above the first row or left of the first column.

</details>
