## General

**Choose the right-angle vertex first**

A valid triangle has three cells containing 1. One cell is special: it shares its row with one of the other cells and its column with the remaining cell. That special cell is the right-angle vertex.

Fix a 1-cell at coordinates `(i, j)`. To complete a triangle with this cell as the vertex, we independently choose:

1. another 1 somewhere else in row $i$;
2. another 1 somewhere else in column $j$.

If row $i$ contains `rows[i]` ones in total, there are `rows[i] - 1` possible horizontal partners because the vertex itself must be excluded. Similarly, there are `cols[j] - 1` possible vertical partners.

Every horizontal choice can be combined with every vertical choice, so the number of triangles whose right angle is at `(i, j)` is

$$
(\texttt{rows[i]} - 1)(\texttt{cols[j]} - 1).
$$

The other two cells cannot accidentally be the same cell: a horizontal partner differs from the vertex's column, while a vertical partner differs from its row. Their coordinates therefore differ in both roles. They also do not have to be adjacent to the vertex; the definition permits any distance in the same row or column.

**Precompute row and column counts**

Computing the row and column totals separately for every possible vertex would repeatedly scan the same cells. The first nested loop avoids that repetition.

The array `rows` has one entry for each row, and `cols` has one entry for each column. When the loop sees `grid[i][j]`:

- it adds that 0 or 1 to `rows[i]`;
- it adds the same value to `cols[j]`.

After this full pass, every row and column count is available in constant time.

The second nested loop visits all cells again. A zero cell cannot be part of a requested triangle, much less serve as its vertex, so `if x` skips it. For each 1-cell, the code adds the product of the two partner counts to `ans`.

**Why this counts every triangle exactly once**

First, every contribution created by the formula is valid. The current cell contains 1, the chosen horizontal partner contains 1 in the same row, and the chosen vertical partner contains 1 in the same column. These are three distinct cells and meet the definition.

Second, every valid triangle is included. By definition, it has a cell that shares a row with one selected cell and a column with the third. When the second pass reaches that right-angle cell, its horizontal partner is among the `rows[i] - 1` choices and its vertical partner is among the `cols[j] - 1` choices. Their pair contributes exactly one to the product.

Third, the same geometric triangle is not counted from another vertex. Of its three cells, only the right-angle cell shares a row with one other selected cell and a column with the other. Each of the two endpoint cells shares only one required axis relation within that triple. Therefore, the triangle appears under one and only one vertex.

**Concrete trace**

For

`[[0,1,0],[0,1,1],[0,1,0]]`,

the row counts are `[1,2,1]` and the column counts are `[0,3,1]`.

- At `(0,1)`, the row has no other 1, so the contribution is $(1-1)(3-1)=0$.
- At `(1,1)`, there is one horizontal choice and two vertical choices, so the contribution is $(2-1)(3-1)=2$.
- At `(1,2)`, its column has no other 1, so the contribution is $(2-1)(1-1)=0$.
- At `(2,1)`, the row has no other 1, so the contribution is 0.

The final answer is 2. This also shows why three collinear 1-cells alone do not form a right triangle: every possible vertex among them lacks a horizontal partner, causing one factor to be zero.

**Why multiplication, not addition**

The row and column partners are two independent decisions. If a vertex has three horizontal choices and four vertical choices, each of the three can be paired with each of the four, producing $3 \cdot 4 = 12$ distinct triangles. Adding the counts would give 7 and miss combinations. This product rule is the heart of the solution.

## Complexity detail

Let $m$ be the number of rows and $n$ be the number of columns.

The first pass reads all $mn$ cells to build the counts. The second pass reads all $mn$ cells again and performs constant work for each one. Thus total time is

$$
O(mn) + O(mn) = O(mn).
$$

The `rows` array has $m$ integers and the `cols` array has $n$ integers, so auxiliary space is $O(m+n)$. The scalar answer and loop variables use $O(1)$ additional space. The input grid is not modified and is not counted as auxiliary storage.

The answer can be much larger than the number of cells because one dense vertex may participate in many combinations. In an all-one $m \times n$ grid, each of the $mn$ vertices contributes $(n-1)(m-1)$. Python integers grow automatically, so the exact implementation does not overflow a fixed-width accumulator.

The asymptotic time is optimal for an explicitly supplied arbitrary grid: every cell may affect a row count, a column count, and therefore the answer, so an algorithm must inspect all $mn$ values in the worst case.

## Alternatives and edge cases

- **Recount for each vertex:** Scan the vertex's row and column whenever a 1 is found. This uses little extra storage but can take $O(mn(m+n))$ time on a dense grid.
- **Store coordinates of ones:** Group 1-cell coordinates by row and column, then apply the same product formula. This can be attractive for a sparse representation, but the given dense matrix still takes $O(mn)$ time to read and the groups can use $O(mn)$ space.
- **Count triples directly:** Enumerating every triple of 1-cells is far more expensive and then requires testing row/column relationships. Choosing the unique right-angle vertex exposes independent choices immediately.
- **Single row or single column:** One of `rows[i] - 1` or `cols[j] - 1` is always zero, so the answer is correctly zero.
- **Isolated 1-cell:** Both partner counts are zero and it contributes nothing.
- **Several collinear ones:** They still contribute nothing unless some cell also has a partner on the perpendicular axis.
- **All-zero grid:** The second pass never enters the contribution branch, leaving `ans` equal to zero.
- **All-one grid:** Every cell is a possible right-angle vertex and contributes $(n-1)(m-1)$; no triangle is duplicated because its right-angle vertex is unique.
- **Non-adjacent cells:** Distance is irrelevant. Row and column totals deliberately include partners anywhere on the corresponding axis.
- **Subtracting the vertex:** Both counts include the current 1, so subtracting one from each is mandatory. Omitting either subtraction would allow the vertex to be selected as its own partner.
- **Boolean matrix representation:** The code relies on entries being numeric 0 or 1 so that adding `x` directly counts ones.
