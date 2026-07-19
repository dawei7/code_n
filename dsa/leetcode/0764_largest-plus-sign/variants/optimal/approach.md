## General
**Measure the four arm capacities**

For each non-mine cell, determine how many consecutive ones extend through it from each direction. A left-to-right row sweep keeps the current run length since the last mine; write that length into the cell. Repeat right-to-left, top-to-bottom, and bottom-to-top, retaining the minimum value seen at each cell.

**Why the minimum is the plus order**

If a cell's four directional run lengths are `left`, `right`, `up`, and `down`, an order-`k` plus centered there exists exactly when every run is at least `k`. Therefore its largest possible order is `min(left, right, up, down)`. A mine resets every relevant directional run to zero.

After all four sweeps, each table entry is precisely the maximum order for a plus with that center. Taking the maximum entry considers every possible center, so it returns the largest plus anywhere in the grid.

## Complexity detail
Each of four sweeps visits all $n^{2}$ cells once, for $O(n^2)$ time. The directional-minimum table and mine lookup use $O(n^2)$ space in the worst case.

## Alternatives and edge cases
- **Expand from every center:** Checking successively longer arms is straightforward but takes $O(n^3)$ time on a mine-free grid.
- **Four separate directional tables:** This is equally correct but uses four times the dynamic-programming storage instead of updating one minimum table.
- **Row and column prefix sums:** They can test a proposed arm in constant time, but finding the best arm for every center still needs careful searching.
- **All cells are mines:** Every directional minimum is zero, so return `0`.
- **No mines:** The best center reaches the nearest boundary and has order $\lfloor (n+1)/2 \rfloor$.
- **Boundary centers:** They can support only order one because at least one arm cannot extend.
- **A mine at a candidate center:** Its order is zero regardless of neighboring ones.
