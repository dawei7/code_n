# Moving Stones Until Consecutive

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1033 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/moving-stones-until-consecutive/) |

## Problem Description

### Goal

Three stones occupy different integer positions `a`, `b`, and `c` on the x-axis.

In one move, sort the current positions as `x < y < z`, pick up an endpoint stone at `x` or `z`, and place it at an unoccupied integer position `k` satisfying `x < k < z` and `k != y`. The game ends when no move is possible, which occurs when the stones occupy three consecutive positions.

Return `[minimum_moves, maximum_moves]`, where the two values are respectively the fewest and greatest numbers of legal moves that can be played before the game ends.

### Function Contract

**Inputs**

- `a`, `b`, and `c`: three distinct stone positions, each between $1$ and $100$, inclusive.

**Return value**

- A two-element array containing the minimum and maximum possible move counts.

### Examples

**Example 1**

- Input: `a = 1, b = 2, c = 5`
- Output: `[1,2]`
- Explanation: Move `5` directly to `3` for the minimum, or move it first to `4` and then to `3` for the maximum.

**Example 2**

- Input: `a = 4, b = 3, c = 2`
- Output: `[0,0]`
- Explanation: The sorted positions are already consecutive.

**Example 3**

- Input: `a = 3, b = 5, c = 1`
- Output: `[1,2]`
- Explanation: Move `1` directly to `4`, or move it through `2` before reaching `4`.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Normalize the positions:** Sort the three fixed inputs as `x < y < z`. Let the adjacent gaps be `left_gap = y - x` and `right_gap = z - y`.

**Derive the minimum:** If both gaps equal one, the stones are consecutive and zero moves are needed. If either gap is at most two, one endpoint can be placed into the single missing position next to the other two stones, finishing in one move. When both gaps exceed two, no single endpoint move can create three consecutive positions, but two moves always suffice.

**Count the maximum:** The interval from `x` through `z` contains `z - x + 1` positions, three of which are occupied. Every maximum-length strategy can consume one interior empty position per move while keeping a legal endpoint move available. Therefore the greatest number of moves is `z - x - 2`.

The minimum cases exhaust all possible adjacent-gap patterns. For the maximum, each move must eliminate at least one empty position inside the outer span, so more than `z - x - 2` moves are impossible; moving an endpoint inward one position at a time attains that bound.

#### Complexity detail

Sorting exactly three values and evaluating a fixed number of arithmetic comparisons takes $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **State-space search:** Explore every legal move until consecutive states are reached. The bounded domain makes this finite, but it obscures the direct gap formulas.
- **Count empty positions explicitly:** Iterate through every integer strictly between `x` and `z` except `y`. This computes the maximum correctly but takes time proportional to the coordinate span.
- **Already consecutive:** Both answers are zero even if the inputs arrive in a different order.
- **One gap of two:** The minimum is one because the far endpoint can fill the missing position.
- **Both gaps larger than two:** The minimum is exactly two, not the size of either gap.
- **Maximum coordinate span:** Positions `1` and `100` still obey the same empty-position count.

</details>
