## Function Contract

**Inputs**

- `grid`: A rectangular matrix of cell values whose dimensions are $m$ rows by $n$ columns.
- `k`: The maximum total path cost allowed.

Both the starting and ending cells belong to the path and contribute according to the same score-and-cost rules. The source guarantees `grid[0][0] == 0`.

For complexity notation, define

$$
L = \min(k,m+n-2),
$$

the useful cost-state limit because a right/down path visits $m+n-1$ cells and its guaranteed-zero starting cell costs nothing.

**Return value**

Return the maximum score among paths of cost at most `k`, or `-1` when every path exceeds the budget.
