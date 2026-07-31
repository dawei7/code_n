## General

Let $m$ and $n$ denote the matrix dimensions.

**Fix the rook that is middle by row**

Sort any legal placement conceptually by row. If the middle rook occupies \`(r, c)\`, the upper rook comes from rows \`0..r-1\` and the lower rook from rows \`r+1..m-1\`. Those disjoint regions guarantee three different rows. Only column conflicts remain.

For each row prefix, compute the largest value attainable in every column over that prefix, then retain the three best values from distinct columns. Scan from the bottom to create the equivalent suffix summaries.

**Why exactly three summarized columns suffice**

After the other two rooks are fixed, a side region is forbidden from using at most two columns. Its three best distinct columns cannot all be forbidden, so at least one remains. The best surviving summarized value is at least as large as every candidate outside the summary. Thus a globally optimal placement has an equally valuable representative using these summaries.

Enumerate every cell as the middle rook. Combine it with the three candidates from the preceding prefix and the three from the following suffix, retaining only triples of distinct columns. Each middle cell performs at most nine combinations.

Every enumerated triple is legal because its rows lie in three disjoint parts and its columns are checked. For an arbitrary optimum, apply the top-three replacement argument first to one side and then to the other while holding the remaining two columns fixed. This produces an optimum included in the enumeration, proving the maximum is found.

**Scaling to the II limits**

With up to 250,000 cells, enumerating row triples or cell triples is infeasible. The summaries reduce all choices outside the middle row to constant size without losing an optimal placement.

## Complexity detail

Both directional scans update $n$ column maxima for each of $m$ rows and select only three columns, taking $O(mn)$ time. The middle-rook enumeration also costs $O(mn)$ because it checks a constant nine pairs per cell. Three-item summaries for all rows plus one $n$-entry column array use $O(m+n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate row triples:** Restricting each selected row to its top three cells is correct but still takes $O(m^3)$ time.
- **Assignment or min-cost flow:** General matching machinery solves a broader problem but adds substantial overhead for exactly three rooks.
- **One or two regional candidates:** The other rooks can forbid all retained columns; three is the smallest safe number.
- **Select the three largest cells:** They may collide in a row or column.
- Exactly three rooks are mandatory even on an all-negative board.
- A legal sum can exceed signed 32-bit range.
- Equal values and multiple optimal placements do not change the returned sum.
- Wide and tall rectangular boards use the same row-ordered argument.
- Regional summaries must keep distinct columns, not merely three distinct cells.
