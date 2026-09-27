# Guided Example: Range Sum Query 2D - Mutable

We trace the step-by-step row-wise Binary Indexed Tree (Fenwick tree) decomposition, isolated point update delta computation ($\Delta = val - \text{prev}$), row-by-row horizontal prefix interval querying, and subgrid aggregation on representative 2D mutable matrix instances:

- **Input:**
  $$
  \text{matrix} = \begin{bmatrix}
  3 & 0 & 1 & 4 & 2 \\
  5 & 6 & 3 & 2 & 1 \\
  1 & 2 & 0 & 1 & 5 \\
  4 & 1 & 0 & 1 & 7 \\
  1 & 0 & 3 & 0 & 5
  \end{bmatrix}
  $$
  $$
  \text{operations} = [\text{sumRegion}(2, 1, 4, 3), \; \text{update}(3, 2, 2), \; \text{sumRegion}(2, 1, 4, 3)]
  $$
- **Required outputs:** $[8, 10]$
  - Initial $\text{sumRegion}(2, 1, 4, 3) = (2 + 0 + 1) + (1 + 0 + 1) + (0 + 3 + 0) = 3 + 2 + 3 = 8$
  - $\text{update}(3, 2, 2)$ sets cell $(3, 2)$ from $0$ to $2$ ($\Delta = +2$)
  - Subsequent $\text{sumRegion}(2, 1, 4, 3) = 3 + (1 + 2 + 1) + 3 = 3 + 4 + 3 = 10$
- **Single Cell Region Query:** $\text{sumRegion}(r, c, r, c)$ isolates exactly $\text{matrix}[r][c]$ via row Fenwick tree
- **Zero Delta Update:** Re-assigning an identical value yields $\Delta = 0$, leaving all prefix sums unchanged

This instance demonstrates row-partitioned Fenwick tree data structures, explains why each row maintains an independent 1D Binary Indexed Tree to achieve $O(\log N)$ point updates without complex 2D tree rebalancing, details row-by-row prefix accumulation across $[row_1, row_2]$, and analyzes time complexity ($O(H \log N)$ query time, $O(M N)$ space).

---

## 1. Instance & Teaching Goal

Given a 2D integer matrix of size $M \times N$ ($5 \times 5$):
We need to support two dynamic operations:
1. `update(row, col, val)`: Update the cell at $(row, col)$ to $val$.
2. `sumRegion(row1, col1, row2, col2)`: Calculate the sum of elements inside the subgrid $[row_1, row_2] \times [col_1, col_2]$.

```text
Query Subgrid: Rows 2 to 4, Columns 1 to 3
Row 2: [., 2, 0, 1, .] -> Sum = 3
Row 3: [., 1, 0, 1, .] -> Sum = 2
Row 4: [., 0, 3, 0, .] -> Sum = 3
Initial Total = 3 + 2 + 3 = 8

Update(row=3, col=2, val=2): Modifies cell (3, 2) from 0 to 2
Row 3 becomes: [., 1, 2, 1, .] -> Sum = 4
New Total = 3 + 4 + 3 = 10
```

### The Design Tradeoff
- A 2D static prefix table achieves $O(1)$ query, but point updates cost $O(M N)$ to propagate across all lower-right cells.
- A naive 2D matrix gives $O(1)$ updates, but queries cost $O(H \cdot W)$.
- The **Row-Wise Fenwick Tree** architecture:
  Each of the $M$ rows contains an independent 1D Binary Indexed Tree of length $N$:
  - `update` touches only row $r$, taking strictly **$O(\log N)$ time**.
  - `sumRegion` queries $(row_2 - row_1 + 1)$ row trees, taking **$O(H \log N)$ time**.

---

## 2. Conceptual Foundation & Invariants

### 1D Row Fenwick Tree Inside Each Row
For each row $i \in [0, M - 1]$:
Maintain $\text{tree}[i] = \text{BinaryIndexedTree}(N)$ where array $c$ of size $N + 1$ stores column prefix chunks:
$$
\operatorname{lowbit}(x) = x \ \& \ (-x)
$$
- `query(x)` returns the sum of columns $0$ to $x - 1$ in row $i$ in $O(\log N)$ time.
- `update(x, delta)` adds $\Delta$ to 1-based column $x$ and its ancestors in $O(\log N)$ time.

### Operations Protocol:

#### 1. Point Update `update(row, col, val)`:
1. Isolate the existing value at $(row, col)$ using two 1-based column queries on row `row`:
   $$
   \text{prev} = \text{tree}[row].\text{query}(col + 1) - \text{tree}[row].\text{query}(col)
   $$
2. Compute the delta:
   $$
   \Delta = val - \text{prev}
   $$
3. Update the 1D tree for row `row`:
   $$
   \text{tree}[row].\text{update}(col + 1, \; \Delta)
   $$

#### 2. Region Query `sumRegion(row1, col1, row2, col2)`:
Iterate across all rows $r \in [row_1, row_2]$:
In each row, the horizontal slice $[col_1, col_2]$ is computed via prefix subtraction:
$$
\text{row\_sum}(r) = \text{tree}[r].\text{query}(col_2 + 1) - \text{tree}[r].\text{query}(col_1)
$$
Sum all row results:
$$
\text{sumRegion} = \sum_{r=row_1}^{row_2} \left( \text{tree}[r].\text{query}(col_2 + 1) - \text{tree}[r].\text{query}(col_1) \right)
$$

> **Invariant.** For each row $r$, `tree[r]` correctly reflects all point updates made to row $r$. The summation across rows $r \in [row_1, row_2]$ equals the exact subgrid area sum.

Row $3$ is the only row the trace modifies, so its tree is worth writing out in
full. Each node owns a fixed column interval; the last two columns show how the
single replacement of cell $(3, 2)$ moves exactly the nodes whose interval
contains column $2$ and nothing else.

| Node $x$ | Binary | $\operatorname{lowbit}(x)$ | Columns covered (1-based) | Cells held | $c[x]$ before | $c[x]$ after `update(3, 2, 2)` |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | 001 | 1 | $[1, 1]$ | matrix[3][0] = 4 | 4 | 4 |
| 2 | 010 | 2 | $[1, 2]$ | matrix[3][0] + matrix[3][1] = 5 | 5 | 5 |
| 3 | 011 | 1 | $[3, 3]$ | matrix[3][2] = 0 | 0 | **2** |
| 4 | 100 | 4 | $[1, 4]$ | matrix[3][0..3] = 6 | 6 | **8** |
| 5 | 101 | 1 | $[5, 5]$ | matrix[3][4] = 7 | 7 | 7 |

The propagation path is read straight off the table: node $3$ holds the changed
column, and its single ancestor is $3 + \operatorname{lowbit}(3) = 4$, whose
interval $[1, 4]$ contains column $2$. Nodes $1$, $2$ and $5$ hold intervals that
exclude column $2$, so their stored sums must not move — and they do not.

---

## 3. Step-by-Step Worked Execution

We trace the operations on the $5 \times 5$ matrix:

---

### Step 1: Initial State & Query 1 — $\text{sumRegion}(2, 1, 4, 3)$
Target rows: $r \in [2, 4]$. Target columns: $col \in [1, 3]$.
Queried column boundaries: $\text{query}(3 + 1 = 4) - \text{query}(1)$.

1. **Row $r = 2$:**
   Row 2 values: $[1, 2, 0, 1, 5]$.
   - $\text{query}(4) = 1 + 2 + 0 + 1 = 4$.
   - $\text{query}(1) = 1$.
   - Horizontal slice sum: $4 - 1 = \mathbf{3}$ (Cells: $2 + 0 + 1$).
2. **Row $r = 3$:**
   Row 3 values: $[4, 1, 0, 1, 7]$.
   - $\text{query}(4) = 4 + 1 + 0 + 1 = 6$.
   - $\text{query}(1) = 4$.
   - Horizontal slice sum: $6 - 4 = \mathbf{2}$ (Cells: $1 + 0 + 1$).
3. **Row $r = 4$:**
   Row 4 values: $[1, 0, 3, 0, 5]$.
   - $\text{query}(4) = 1 + 0 + 3 + 0 = 4$.
   - $\text{query}(1) = 1$.
   - Horizontal slice sum: $4 - 1 = \mathbf{3}$ (Cells: $0 + 3 + 0$).

Total sum:
$$
\text{Sum} = 3 + 2 + 3 = \mathbf{8}
$$

---

### Step 2: Execute $\text{update}(3, 2, 2)$
Modify cell at $(row=3, col=2)$ from $0$ to $2$:
- Target row: `tree[3]`.
- 1-based column position: $col + 1 = 3$.
- Find current value:
  $$
  \text{prev} = \text{tree}[3].\text{query}(3) - \text{tree}[3].\text{query}(2) = (4 + 1 + 0) - (4 + 1) = 5 - 5 = \mathbf{0}
  $$
- Compute delta:
  $$
  \Delta = val - \text{prev} = 2 - 0 = \mathbf{+2}
  $$
- Call $\text{tree}[3].\text{update}(3, +2)$:
  - Position 3 updated by $+2$.
  - Position $3 + \operatorname{lowbit}(3) = 3 + 1 = 4$ updated by $+2$.
- Row 3 logically becomes: $[4, 1, \mathbf{2}, 1, 7]$.

---

### Step 3: Evaluate Query 2 — $\text{sumRegion}(2, 1, 4, 3)$ After Update
Re-evaluate the same region $[2, 4] \times [1, 3]$:
1. **Row $r = 2$:** Slice sum $= \mathbf{3}$ (Unchanged).
2. **Row $r = 3$:**
   - $\text{query}(4) = 4 + 1 + 2 + 1 = 8$.
   - $\text{query}(1) = 4$.
   - Horizontal slice sum: $8 - 4 = \mathbf{4}$ (Cells: $1 + 2 + 1$).
3. **Row $r = 4$:** Slice sum $= \mathbf{3}$ (Unchanged).

New total sum:
$$
\text{Sum} = 3 + 4 + 3 = \mathbf{10}
$$

---

## 4. Complete Execution Trace

```text
Matrix (5x5)

Query 1: sumRegion(2, 1, 4, 3):
  Row 2: query(4) - query(1) = 4 - 1 = 3
  Row 3: query(4) - query(1) = 6 - 4 = 2
  Row 4: query(4) - query(1) = 4 - 1 = 3
  Total = 3 + 2 + 3 = 8

Update: update(row=3, col=2, val=2):
  prev = tree[3].query(3) - tree[3].query(2) = 0
  delta = 2 - 0 = +2
  tree[3].update(col=3, delta=+2)

Query 2: sumRegion(2, 1, 4, 3):
  Row 2: slice sum = 3
  Row 3: query(4) - query(1) = 8 - 4 = 4
  Row 4: slice sum = 3
  Total = 3 + 4 + 3 = 10

Results: [8, 10]
```

| Operation | Target / Coordinates | Row Evaluated | Prefix Difference Formula | Slice Sum | Total Output |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Query 1** | Rows $2..4$, Cols $1..3$ | Row 2 | $\text{query}(4) - \text{query}(1) = 4 - 1$ | 3 | - |
| | | Row 3 | $\text{query}(4) - \text{query}(1) = 6 - 4$ | 2 | - |
| | | Row 4 | $\text{query}(4) - \text{query}(1) = 4 - 1$ | 3 | **8** |
| **Update** | $(3, 2) \leftarrow 2$ | Row 3 | $\Delta = 2 - 0 = +2$; update col 3 | - | - |
| **Query 2** | Rows $2..4$, Cols $1..3$ | Row 2 | $\text{query}(4) - \text{query}(1) = 4 - 1$ | 3 | - |
| | | Row 3 | $\text{query}(4) - \text{query}(1) = 8 - 4$ | 4 | - |
| | | Row 4 | $\text{query}(4) - \text{query}(1) = 4 - 1$ | 3 | **10** |

---

## 5. Algorithmic Correctness

**Soundness.** Each row tree operates independently on column indices. In row $r$, $\text{query}(col_2 + 1) - \text{query}(col_1)$ cancels all column values outside $[col_1, col_2]$, returning the exact sum of elements in that row segment. Summing across all rows from $row_1$ to $row_2$ aggregates all disjoint horizontal slices, producing the exact 2D subgrid sum.

**Completeness.** Every cell update in row $r$ modifies only `tree[r]` in $O(\log N)$ steps. Because each row tree is independent, no cross-row side effects occur. The query sums all rows in $[row_1, row_2]$ without skipping, guaranteeing the result is complete and up-to-date.

---

## 6. Traps This Instance Exposes

- **Overwriting Instead of Delta:** Fenwick tree `update` performs an addition. An assignment operation must calculate $\Delta = val - \text{prev}$.
- **Full 2D Static Prefix Sums:** Rebuilding a 2D static prefix table after each point update takes $O(M N)$, causing Time Limit Exceeded when updates are frequent. Row-wise Fenwick trees restrict update time to $O(\log N)$.
- **1-Based Slicing:** When querying columns $col_1$ to $col_2$, the 1-based bounds are $col_2 + 1$ and $col_1$. Using $col_2$ omits the rightmost column.

### Column bounds, translated exactly

The row slice $[col_1, col_2]$ becomes the difference of two 1-based prefix
queries. Every value below is taken from row $2$, whose entries are
$[1, 2, 0, 1, 5]$, so the arithmetic can be checked cell by cell.

| What is wanted | Prefix expression | Row 2 evaluation | Meaning |
|:---|:---|:---:|:---|
| Prefix of the first column only | $\text{query}(1)$ | 1 | columns $[0, 0]$ |
| Prefix through the left edge of the slice | $\text{query}(col_1) = \text{query}(1)$ | 1 | the part that must be cancelled |
| Prefix through the right edge, inclusive | $\text{query}(col_2 + 1) = \text{query}(4)$ | 4 | columns $[0, 3]$ |
| The slice itself | $\text{query}(4) - \text{query}(1)$ | $4 - 1 = 3$ | columns $[1, 3]$: cells $2, 0, 1$ |
| Dropping the $+1$ by mistake | $\text{query}(3) - \text{query}(1)$ | $3 - 1 = 2$ | silently loses the rightmost column, whose value is $1$ |
| A slice starting at column $0$ | $\text{query}(col_2 + 1) - \text{query}(0)$ | $\text{query}(4) - 0 = 4$ | the empty prefix makes the cancellation vanish harmlessly |
| A slice ending at the last column | $\text{query}(n) = \text{query}(5)$ | 9 | all five columns of row 2 |
| A single cell $(r, c)$ | $\text{query}(c + 1) - \text{query}(c)$ | $(2, 2) \to 3 - 3 = 0$ | the cell's current value, which is the $\text{prev}$ used by `update` |

### Structures this instance rules out

| Structure | `update(row, col, val)` | `sumRegion(...)` | Auxiliary space | Consequence here |
|:---|:---:|:---:|:---:|:---|
| Naive matrix | $O(1)$: overwrite the cell | $O(H W)$ | $O(M N)$ | A full $200 \times 200$ region costs $40{,}000$ additions per query, and up to $5000$ calls are allowed |
| 2D prefix table rebuilt after each update | $O(M N)$: every cell below and right is invalidated | $O(1)$ | $O(M N)$ | The mirror image; with frequent updates it degenerates to rebuilding the table $5000$ times |
| Row-wise Fenwick trees (the structure used here) | $O(\log N)$, touching one row | $O(H \log N)$ | $O(M N)$: $M$ trees of $N + 1$ nodes | Updates never leave row $r$; a query pays about 8 bit steps per row at $n = 200$, and at most $200 \times 8 = 1600$ steps for a full-height region |
| Full 2D Fenwick tree | $O(\log M \log N)$ | $O(\log M \log N)$ | $O(M N)$ | Strictly better query asymptotics for tall regions, but the index climb happens in two dimensions at once, which is exactly the rebalancing complexity this row-wise design avoids |
| Column-wise Fenwick trees | $O(\log M)$: one column of trees | $O(W \log M)$ | $O(M N)$ | The transpose of the chosen design; it wins only when regions are wide and short, and loses on the tall region traced here |

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization: $O(M N \log N)$ to insert all cells into the $M$ row trees.
  - `update(row, col, val)`: $O(\log N)$ logarithmic time, updating only the tree corresponding to `row`.
  - `sumRegion(row1, col1, row2, col2)`: $O(H \log N)$, where $H = row_2 - row_1 + 1$ is the query height. In the worst case $H = M$, costing $O(M \log N)$.
- **Auxiliary Space Complexity:** $O(M N)$ auxiliary memory to store $M$ Fenwick trees, each of size $N + 1$.
