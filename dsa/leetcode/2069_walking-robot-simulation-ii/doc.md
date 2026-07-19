# Walking Robot Simulation II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2069 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Design, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/walking-robot-simulation-ii/) |

## Problem Description

### Goal

A `width` by `height` grid lies on an XY-plane, from `(0,0)` at the bottom-left through `(width - 1, height - 1)` at the top-right. A robot begins at `(0,0)` facing `East`.

For each requested step, the robot tries to move one cell forward. If that cell would be outside the grid, it first turns $90^\circ$ counterclockwise and retries the same step. After completing an instruction, its position and current direction persist for later calls.

Implement the stateful `Robot` class. It must accept movement instructions and report the current position or one of `East`, `North`, `West`, and `South` as the direction.

### Function Contract

**Inputs**

- `Robot(width, height)`: initialize a grid with $2 \le \texttt{width},\texttt{height}\le100$.
- `step(num)`: move the robot by exactly `num` successful cell steps, where $1 \le \texttt{num}\le10^5$.
- `getPos()`: request the current `[x,y]` position.
- `getDir()`: request the current cardinal direction.

At most $Q=10^4$ method calls are made after construction.

**Return value**

- `step` returns no value.
- `getPos` returns `[x,y]`.
- `getDir` returns the current direction string.
- In the app adapter, return the result of every operation in order, using `null` for construction and `step`.

### Examples

**Example 1**

- Input: `operations = ["Robot","step","step","getPos","getDir","step","step","step","getPos","getDir"]`, `arguments = [[6,3],[2],[2],[],[],[2],[1],[4],[],[]]`
- Output: `[null,null,null,[4,0],"East",null,null,null,[1,2],"West"]`
- Explanation: The robot crosses the bottom edge, turns north at the right boundary, and later turns west across the top edge.

### Required Complexity

- **Time:** $O(Q)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Flatten the boundary into one cycle**

The robot never enters an interior cell: starting on the boundary and turning counterclockwise at each corner makes it follow the perimeter in the order bottom, right, top, left. Its cycle length is

$$
P=2(\texttt{width}+\texttt{height})-4.
$$

Store one perimeter index, initially zero. A `step(num)` call replaces it with `(position + num) % P`, making the operation independent of `num`.

**Decode position and direction by segment**

Use the lengths `width - 1` and `height - 1` to determine which of the four boundary segments contains the index, then convert its offset to `[x,y]`. Direction is the direction of the most recently completed movement along that segment. The index zero needs one extra flag: before any movement the robot faces `East`, but after a positive whole number of cycles it has just moved south into `(0,0)` and faces `South`.

Each successful unit step advances to the next point of the same perimeter cycle, including the counterclockwise corner turn. Modular addition therefore reaches exactly the state produced by literal simulation. The segment formulas invert the flattened index, and the movement flag resolves the only index whose initial and post-cycle directions differ.

#### Complexity detail

Construction and every method call take $O(1)$ time, so $Q$ calls take $O(Q)$ total time regardless of the numeric step counts. The class stores a fixed number of integers and one Boolean, requiring $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Move one cell at a time:** This directly follows the statement but takes time proportional to the sum of all requested steps, which can be much larger than $Q$.
- **Precompute every perimeter state:** Indexing a boundary array also gives constant-time calls, but uses $O(\texttt{width}+\texttt{height})$ space.
- Reaching a corner does not turn immediately; the robot retains its incoming direction until the next attempted step is blocked.
- Returning to `(0,0)` after a complete cycle leaves the robot facing `South`, unlike its initial `East` direction.
- Step counts larger than the perimeter must wrap using modulo without losing the post-movement direction.
- Consecutive `step` calls are equivalent to one call with their sum because state persists.

</details>
