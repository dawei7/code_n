# Largest Plus Sign

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 764 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-plus-sign/) |

## Problem Description

### Goal

Begin with an $n \times n$ grid filled with `1`s, then place `0` at every coordinate listed in `mines`. An axis-aligned plus sign of order `k` has one center cell and four arms extending up, down, left, and right by $k - 1$ cells each, with every covered cell equal to `1`.

Return the largest order of any plus sign in the grid. An order-`1` plus consists only of its center, and if no `1` cell remains the answer is `0`; diagonal cells do not form part of an axis-aligned arm.

### Function Contract

**Inputs**

- `n`: the side length of the square grid.
- `mines`: distinct coordinate pairs `[row, column]` whose cells contain zero.

**Return value**

- The maximum plus order, or `0` when the grid contains no one-cell.

### Examples

**Example 1**

- Input: `n = 5`, `mines = [[4,2]]`
- Output: `2`
- Explanation: Several centers support one one-cell in all four directions, but no order-three plus survives the mine and boundaries.

**Example 2**

- Input: `n = 1`, `mines = [[0,0]]`
- Output: `0`
- Explanation: The only cell is a mine.

**Example 3**

- Input: `n = 3`, `mines = []`
- Output: `2`
- Explanation: The center and its four adjacent cells form an order-two plus.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Measure the four arm capacities**

For each non-mine cell, determine how many consecutive ones extend through it from each direction. A left-to-right row sweep keeps the current run length since the last mine; write that length into the cell. Repeat right-to-left, top-to-bottom, and bottom-to-top, retaining the minimum value seen at each cell.

**Why the minimum is the plus order**

If a cell's four directional run lengths are `left`, `right`, `up`, and `down`, an order-`k` plus centered there exists exactly when every run is at least `k`. Therefore its largest possible order is `min(left, right, up, down)`. A mine resets every relevant directional run to zero.

After all four sweeps, each table entry is precisely the maximum order for a plus with that center. Taking the maximum entry considers every possible center, so it returns the largest plus anywhere in the grid.

#### Complexity detail

Each of four sweeps visits all $n^{2}$ cells once, for $O(n^2)$ time. The directional-minimum table and mine lookup use $O(n^2)$ space in the worst case.

#### Alternatives and edge cases

- **Expand from every center:** Checking successively longer arms is straightforward but takes $O(n^3)$ time on a mine-free grid.
- **Four separate directional tables:** This is equally correct but uses four times the dynamic-programming storage instead of updating one minimum table.
- **Row and column prefix sums:** They can test a proposed arm in constant time, but finding the best arm for every center still needs careful searching.
- **All cells are mines:** Every directional minimum is zero, so return `0`.
- **No mines:** The best center reaches the nearest boundary and has order $\lfloor (n+1)/2 \rfloor$.
- **Boundary centers:** They can support only order one because at least one arm cannot extend.
- **A mine at a candidate center:** Its order is zero regardless of neighboring ones.

</details>
