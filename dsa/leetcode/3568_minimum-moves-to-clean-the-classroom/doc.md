# Minimum Moves to Clean the Classroom

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3568 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/) |

## Problem Description

### Goal

A student starts in a classroom grid with a fixed maximum energy capacity and must collect every piece of litter. The grid contains exactly one start cell `S`, litter cells `L`, reusable reset cells `R`, blocked cells `X`, and ordinary empty cells `.`.

One move travels up, down, left, or right and consumes one energy unit. Obstacles cannot be entered. Entering a litter cell collects that item permanently. Entering a reset cell restores energy to the original maximum, even when the move onto it used the last available unit. A student whose energy is zero cannot make another move unless the current cell has already reset that energy.

Find the minimum number of moves needed to collect every litter item. The route may revisit traversable cells and reset cells any number of times. Return `-1` when no valid route exists.

### Function Contract

**Inputs**

- `classroom`: An $m\times n$ array of equal-length strings over `S`, `L`, `R`, `X`, and `.`, where $1\le m,n\le20$. It contains exactly one `S` and at most ten `L` cells.
- `energy`: The maximum and initial energy capacity $E$, where $1\le E\le50$.

Let $V=mn$ and let $L$ also denote the number of litter cells when used in complexity expressions.

**Return value**

Return the minimum number of orthogonal moves required to collect all litter, or `-1` if it is impossible. If the classroom contains no litter, return zero.

### Examples

**Example 1**

- Input: `classroom = ["S.","XL"], energy = 2`
- Output: `2`
- Explanation: Moving right and then down reaches the litter exactly as the energy is exhausted.

**Example 2**

- Input: `classroom = ["LS","RL"], energy = 4`
- Output: `3`
- Explanation: Collect the upper-left litter, step onto the reset, and then collect the lower-right litter.

**Example 3**

- Input: `classroom = ["L.S","RXL"], energy = 3`
- Output: `-1`
- Explanation: Obstacles and the energy limit prevent any route from collecting both litter cells.

---
