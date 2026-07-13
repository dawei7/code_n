# Bricks Falling When Hit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 803 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bricks-falling-when-hit/) |

## Problem Description

### Goal

Given an $m \times n$ binary grid, `1` represents a brick and `0` empty space. A brick is stable when it is in the top row or is connected horizontally or vertically through other stable bricks to the top.

Apply each hit in order by erasing the brick at its coordinate if one exists. Any other bricks that become unstable then fall and are immediately removed rather than landing elsewhere. Return, for every hit, the number of bricks that fall because of it, excluding the brick directly erased by that hit.

### Function Contract

**Inputs**

- `grid`: a rectangular binary matrix, where `1` is a brick and `0` is empty.
- `hits`: a list of `[row, column]` positions struck in order.

**Return value**

- One integer per hit: the number of bricks that fall because of that hit, excluding the brick directly removed by the hit.

### Examples

**Example 1**

- Input: `grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]`
- Output: `[2]`
- Explanation: Removing the lower-left support disconnects the other two bricks in its row from the top.

**Example 2**

- Input: `grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]`
- Output: `[0,0]`
- Explanation: The first removed brick supports nothing, and the second hit does not count the brick it directly removes.

**Example 3**

- Input: `grid = [[1],[1],[1]], hits = [[1,0],[2,0],[0,0]]`
- Output: `[1,0,0]`
- Explanation: The first hit makes the bottom brick fall; later hits strike an empty cell and then the remaining top brick.

### Required Complexity

- **Time:** $O((r \cdot c + h) \cdot \alpha(r \cdot c))$
- **Space:** $O(r \cdot c)$

<details>
<summary>Approach</summary>

#### General

**Reverse removals into additions**

Connectivity is difficult to maintain while vertices are deleted, but union-find handles additions efficiently. Copy the grid, apply all hits, and build connected components among the bricks that remain. Add one virtual roof node and join every brick in the top row to it; a brick is stable exactly when it belongs to the roof component.

**Restore each hit backward**

Process hits in reverse order. A hit that originally struck empty space changes nothing. Otherwise, record the roof component size, restore that brick, and union it with the roof when it is in row zero and with every present orthogonal neighbor.

The increase in roof-component size counts all bricks that become stable when this brick is restored. Subtract one for the restored brick itself, and clamp at zero. Reversing the event again means those other newly connected bricks are exactly the ones that fell after the corresponding forward hit.

The union-find state initially represents the grid after every hit. By backward induction, before restoring a hit it represents the grid immediately after that forward hit, and afterward it represents the grid immediately before it. Roof membership therefore matches stability at both times, making the component-size difference the exact answer.

#### Complexity detail

Let the grid have $r \cdot c$ cells and let `h` be the number of hits. Building the final-state components and restoring all hits performs $O(r \cdot c + h)$ union-find operations, each amortized $O(\alpha(r \cdot c))$. The copied grid and union-find arrays use $O(r \cdot c)$ space; the output uses $O(h)$ additional required space.

#### Alternatives and edge cases

- **Reverse flood fill:** After all hits, mark roof-connected bricks; when restoring a brick adjacent to stability, flood only newly stable bricks. Each brick is marked once, giving linear total traversal without union-find.
- **Forward rescan after every hit:** Recompute roof reachability and remove unstable bricks after each strike; it is direct but can take $O(h \cdot r \cdot c)$ time.
- **Offline dynamic connectivity:** More general deletion structures are possible, but reversing the fixed hit sequence is simpler.
- **Hit on empty space:** Record zero and do not add a brick during reversal.
- **Removed brick:** The directly hit brick is never included in the fallen count, which is why the restored brick is subtracted.
- **Multiple roof connections:** Unions within an already stable component do not increase its size and correctly contribute zero.
- **Top-row brick:** Restoring it connects directly to the virtual roof before neighboring components are measured.

</details>
