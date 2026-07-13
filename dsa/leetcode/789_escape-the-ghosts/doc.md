# Escape The Ghosts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 789 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/escape-the-ghosts/) |

## Problem Description

### Goal

You start at `(0, 0)` on an unbounded integer grid, while each ghost starts at its supplied coordinate. During every turn, you and every ghost may move one unit horizontally or vertically, and all participants may choose their routes.

Return `True` if you can guarantee reaching `target` before every ghost can intercept you there or along the way, and `False` otherwise. A ghost reaching your position at the same time is enough to prevent escape, and ghosts choose their movements adversarially rather than randomly.

### Function Contract

**Inputs**

- `ghosts`: a list of starting coordinates `[x, y]` for the ghosts.
- `target`: the destination coordinate `[x, y]`.

**Return value**

- `True` if you can guarantee reaching the target before every ghost; otherwise `False`.

### Examples

**Example 1**

- Input: `ghosts = [[1,0],[0,3]], target = [0,1]`
- Output: `True`
- Explanation: You need one move, while each ghost needs at least two moves to reach the target.

**Example 2**

- Input: `ghosts = [[1,0]], target = [2,0]`
- Output: `False`
- Explanation: The ghost can reach the target in one move, before your two-move route finishes.

**Example 3**

- Input: `ghosts = [[2,0]], target = [1,0]`
- Output: `False`
- Explanation: Both you and the ghost can arrive after one move, and a tie is not an escape.

### Required Complexity

- **Time:** $O(g)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare shortest arrival times at the target**

Grid movement without obstacles has Manhattan distance $\left\lvert x1 - x2 \right\rvert + \left\lvert y1 - y2 \right\rvert$. Your fastest arrival time is the distance from `(0, 0)` to `target`. Compute each ghost's Manhattan distance to the same target; if any ghost needs no more moves than you, it can wait there and prevent escape.

**Why an earlier interception adds no new condition**

Suppose a ghost could meet you at some point after `t` moves along one of your shortest routes of total length `D`. By the triangle inequality, that ghost could then reach the target in at most $t + (D - t) = D$ moves. Such a ghost already fails the target-distance test. Therefore, when every ghost is farther from the target than you are, following a shortest route cannot be intercepted in time.

The condition is both necessary and sufficient: a ghost with target distance at most yours wins by heading to the target, while strictly larger target distances rule out both waiting at the destination and interception of a shortest path.

#### Complexity detail

The algorithm computes one constant-time Manhattan distance for each of the `g` ghosts, taking $O(g)$ time. It stores only the player's distance and current ghost coordinates, for $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Minimum ghost distance list:** Build all ghost-to-target distances and compare their minimum with the player's distance; this is also $O(g)$ but uses $O(g)$ space.
- **Sort ghost distances:** Sorting before inspecting the nearest ghost is unnecessary and takes $O(g \log g)$ time.
- **Simulate grid movement:** Searching positions turn by turn ignores the direct distance characterization and has an unbounded state space.
- **Tied arrival:** A ghost arriving at the same time blocks escape, so the comparison must be strict.
- **Target at the origin:** Your distance is zero, and any ghost not already there is too late.
- **Negative coordinates:** Manhattan distance handles every quadrant without special cases.
- **One dangerous ghost:** A single ghost at least as close to the target is enough to return false.

</details>
