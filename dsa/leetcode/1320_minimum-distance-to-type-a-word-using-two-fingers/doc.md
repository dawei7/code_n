# Minimum Distance to Type a Word Using Two Fingers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1320 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/) |

## Problem Description
### Goal
The uppercase English letters occupy a keyboard grid with six columns: `A` through `F` form the first row, `G` through `L` the second, and so on, with `Y` and `Z` in the final partial row. Thus `A` is at $(0,0)$, `B` at $(0,1)$, `P` at $(2,3)$, and `Z` at $(4,1)$.

Moving a finger between $(r_1,c_1)$ and $(r_2,c_2)$ costs the Manhattan distance $\lvert r_1-r_2\rvert+\lvert c_1-c_2\rvert$. Given an uppercase `word`, type its letters in order using exactly two available fingers and minimize their total movement.

Both initial finger positions are free: placing either finger on the first key it types costs 0. The fingers need not begin on the word's first two letters, and either finger may type any next character.

### Function Contract
**Inputs**

- `word`: an uppercase English string of length $n$, where $2\le n\le300$.

**Return value**

The minimum total Manhattan distance traveled by the two fingers while typing every character of `word` in order.

### Examples
**Example 1**

- Input: `word = "CAKE"`
- Output: `3`
- Explanation: One finger types `C` then `A` for cost 2, while the other types `K` then `E` for cost 1.

**Example 2**

- Input: `word = "HAPPY"`
- Output: `6`
- Explanation: An optimal assignment pays 2 to move from `H` to `A` and 4 to move from `A` to `Y`; the other required placements and moves cost 0.

**Example 3**

- Input: `word = "AZ"`
- Output: `0`
- Explanation: Each finger may start for free on one of the two required keys.
