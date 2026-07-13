# Robot Return to Origin

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 657 |
| Difficulty | Easy |
| Topics | String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/robot-return-to-origin/) |

## Problem Description
### Goal
A robot starts at `(0, 0)`, the origin of a two-dimensional plane. The string `moves` gives its sequence of unit movements: `R` moves right, `L` left, `U` up, and `D` down.

Return `True` if the robot is back at `(0, 0)` after completing every move, and `False` otherwise. The robot's facing direction is irrelevant: each character always moves in its named absolute direction, and every move has the same magnitude. Visiting the origin before the sequence ends is insufficient unless the final position is also the origin.

### Function Contract
**Inputs**

- `moves`: a nonempty string containing only `U`, `D`, `L`, and `R`

**Return value**

- `True` when the final position is the origin; otherwise `False`

### Examples
**Example 1**

- Input: `moves = "UD"`
- Output: `True`

**Example 2**

- Input: `moves = "LL"`
- Output: `False`

**Example 3**

- Input: `moves = "URDL"`
- Output: `True`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the two independent displacements**

Maintain horizontal and vertical coordinates, both initially zero. `R` and `L` add one and subtract one from the horizontal coordinate; `U` and `D` do the same for the vertical coordinate. Process every command exactly once.

**Why the final coordinates are sufficient**

Each command contributes a fixed displacement vector, and vector addition is associative and commutative. The accumulated coordinates therefore equal the sum of all move vectors regardless of the route's intermediate shape. The robot returns precisely when both accumulated components are zero, which is equivalent to equal counts of opposing horizontal moves and equal counts of opposing vertical moves.

#### Complexity detail

The algorithm scans all `N` commands once, taking $O(N)$ time. It stores only two integer coordinates, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Compare opposing character counts:** is also $O(N)$ time and $O(1)$ auxiliary space, though it performs several full string scans instead of one explicit simulation.
- **Store every visited coordinate:** can visualize the route but uses $O(N)$ space that the final-position question does not require.
- **Recompute every prefix position from the beginning:** eventually obtains the same final coordinate but repeats work and takes $O(N^2)$ time.
- Immediate reversals are not required; moves may cancel anywhere in the sequence.
- Returning on one axis is insufficient when displacement remains on the other axis.
- The route may revisit the origin before its final command and still finish elsewhere.

</details>
