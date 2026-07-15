# Minimum Moves to Reach Target with Rotations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1210 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) |

## Problem Description

### Goal

An $n\times n$ grid contains empty cells marked `0` and blocked cells marked `1`. A snake spans two adjacent cells. It begins horizontally across `(0, 0)` and `(0, 1)` and must finish horizontally across `(n - 1, n - 2)` and `(n - 1, n - 1)`.

In one move, the snake may translate one cell right or one cell down while preserving its orientation, provided both destination cells are empty. A horizontal snake at `(r, c)` and `(r, c + 1)` may rotate clockwise around `(r, c)` when both cells directly below it are empty, becoming vertical at `(r, c)` and `(r + 1, c)`. A vertical snake at `(r, c)` and `(r + 1, c)` may rotate counterclockwise around `(r, c)` when both cells directly to its right are empty, becoming horizontal at `(r, c)` and `(r, c + 1)`.

Return the minimum number of moves needed to reach the target. If no valid sequence reaches it, return `-1`.

### Function Contract

**Inputs**

- `grid`: An $n\times n$ binary matrix, where $2\le n\le100$; zero cells are empty and one cells are blocked.
- The two starting cells are guaranteed to be empty.

**Return value**

- The fewest translations and rotations required to reach the bottom-right horizontal target, or `-1` when it is unreachable.

### Examples

**Example 1**

- Input: `grid = [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]`
- Output: `11`

One shortest sequence uses translations in both directions and both allowed rotations.

**Example 2**

- Input: `grid = [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]]`
- Output: `9`

**Example 3**

- Input: `grid = [[0,0],[0,0]]`
- Output: `1`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Encode position and orientation together.** Represent a state as `(r, c, orientation)`, where `(r, c)` is the snake's upper or left pivot cell and `orientation` is horizontal or vertical. This identifies both occupied cells; coordinates alone would confuse configurations with different legal next moves.

**Generate only geometrically legal neighbors.** From a horizontal state, moving right checks the new rightmost cell. Moving down and rotating clockwise both require the two cells below the snake to be empty. From a vertical state, moving down checks the new bottom cell. Moving right and rotating counterclockwise both require the two cells to its right to be empty. Bounds are checked before grid access.

**Use breadth-first search for the minimum.** Begin with the horizontal state at `(0, 0)` in a queue and visited set. Every edge is exactly one move, so BFS removes every state at distance $d$ before any state at distance $d+1$. The first removal of the horizontal target therefore has minimum distance. Marking states when enqueued prevents cycles caused by reversing translations or rotations.

There are at most two orientations for each pivot cell. If the queue empties without the target, every reachable configuration has been explored and no valid sequence exists.

#### Complexity detail

At most $2n^2$ states exist, and each produces at most three constant-time transition checks. Hash-set membership is expected $O(1)$, so total time is $O(n^2)$. The queue and visited set each hold at most $O(n^2)$ states.

#### Alternatives and edge cases

- **Depth-first search over paths:** DFS can establish reachability but does not produce the minimum without exploring and comparing many paths.
- **BFS with a list for visited states:** It remains correct, but linear membership checks can raise total time to $O(n^4)$.
- **Dijkstra's algorithm:** It gives the same distances, but all moves have unit cost, so a priority queue adds unnecessary overhead.
- **Track occupied cells without orientation:** Normalizing cell pairs works, but explicit orientation makes rotations and target comparison clearer.
- **Blocked target cell:** The target configuration is unreachable and the search returns `-1`.
- **Open grid:** Translations alone can reach the target, although rotations create extra states.
- **Rotation clearance:** Both cells in the swept $2\times2$ area must be empty, not only the new endpoint.
- **Two-by-two grid:** One downward move reaches the target without a special case.

</details>
