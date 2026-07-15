# Minimum Moves to Move a Box to Their Target Location

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1263 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/) |

## Problem Description

### Goal

A grid contains walls `"#"`, open cells `"."`, one player `"S"`, one movable box `"B"`, and one target `"T"`. The player may walk one cell horizontally or vertically through open cells, but cannot walk through walls or through the box.

When the player stands next to the box, the player may push it into the adjacent cell on the opposite side if that destination is open. The player cannot pull the box. Only pushes count as moves; ordinary player steps have zero cost. Return the minimum pushes needed to place the box on the target, or `-1` when this is impossible.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ character matrix, where $6 \le m,n \le 20$, with exactly one `"S"`, `"B"`, and `"T"`.
- Let $V=mn$ be the total number of grid cells.

**Return value**

- Return the minimum number of box pushes required to reach `"T"`, or `-1` if no valid sequence exists.

### Examples

**Example 1**

- Input: `grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `3`

**Example 2**

- Input: the same layout with row three replaced by all walls except its final open corridor cell.
- Output: `-1`

**Example 3**

- Input: `grid = [["#","#","#","#","#","#"],["#","T",".",".","#","#"],["#",".","#","B",".","#"],["#",".",".",".",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `5`

### Required Complexity

- **Time:** $O(V^2)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

Run breadth-first search by number of box pushes. A queue state stores the box position and the player's position immediately after the most recent push. At that moment the player occupies the box's former cell, so there are only a constant number of meaningful player-side states for each box cell.

**Test whether a proposed push is available**

For each direction, the box destination must be open, and the cell on the opposite side is where the player must stand. With the current box treated as a temporary wall, run a player flood fill to determine whether the player can reach that standing cell without pushing. Walking distance does not affect the objective, so only reachability matters.

**Breadth-first search preserves push optimality**

If the standing cell is reachable, pushing moves the box to the destination and leaves the player at the old box cell. Enqueue that new state with one additional push unless the same box/player-side state was already visited. Because every queue edge represents exactly one push, the first state whose box is on the target has the minimum push count.

The visited key must include both the new box cell and the player's resulting side. Reaching the same box position from different sides can enable different future pushes, so merging those states would be incorrect.

#### Complexity detail

There are $O(V)$ reachable box-and-side states. Each state considers four pushes, and a player reachability search may inspect $O(V)$ cells, giving $O(V^2)$ time. The outer queue, visited states, and one reachability search each use $O(V)$ space.

#### Alternatives and edge cases

- **Zero-one BFS over box and player cells:** Model player steps with cost zero and pushes with cost one; it is correct but can retain $O(V^2)$ explicit states.
- **Count player steps as moves:** Ordinary walking must not increase the objective, so a standard unweighted BFS over every player step gives the wrong metric.
- **Track only the box position:** It loses which side the player can occupy after a push and may discard necessary states.
- **Box in a non-target corner:** With no room to stand behind it, the box may be permanently stuck.
- **Player path blocked by the box:** Reachability must treat the current box cell as impassable.
- **Box initially adjacent to target:** One push is sufficient only when the player can reach the required opposite side.

</details>
