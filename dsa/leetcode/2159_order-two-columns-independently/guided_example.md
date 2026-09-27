# Guided Example: Order Two Columns Independently

We analyze and execute the decoupled ordinal ranking and equi-join alignment algorithm on a representative database instance, demonstrating how independent window row numbering restructures tabular columns into opposing sorted sequences.

- **Input:** `Data` table:
  - `first_col`: `[4, 2, 3, 1]`
  - `second_col`: `[2, 3, 1, 4]`
- **Output:**
  - `first_col`: `[1, 2, 3, 4]` (ascending)
  - `second_col`: `[4, 3, 2, 1]` (descending)

This instance illustrates decoupling row correlations, independent window sorting, ordinal index generation, and positional equi-join pairing.

---

## 1. Problem Overview & Representative Instance

We are given a database table `Data` containing two integer columns, `first_col` and `second_col`. In standard relational operations, columns within a row remain bound together. Here, the problem requires completely **decoupling** the two columns:
1. All values of `first_col` must be reordered in **ascending order** ($1 \le 2 \le 3 \le \dots$).
2. All values of `second_col` must be reordered in **descending order** ($4 \ge 3 \ge 2 \ge \dots$).
3. The $k$-th value of the sorted `first_col` must be paired horizontally with the $k$-th value of the sorted `second_col`.
4. All occurrences, including duplicate values, must be preserved.

In our representative instance:
- `Data` contains $4$ rows:
  - Row 0: `(4, 2)`
  - Row 1: `(2, 3)`
  - Row 2: `(3, 1)`
  - Row 3: `(1, 4)`

The original pairings (such as $4$ with $2$) must be dissolved, reordering `first_col` as $[1, 2, 3, 4]$ and `second_col` as $[4, 3, 2, 1]$, then outputting the newly aligned pairs.

---

## 2. Mathematical & Algorithmic Principles

### Decoupling Tabular Attributes

Let the input multiset of rows be:
$$\mathcal{D} = \{(x_i, y_i) \mid 1 \le i \le N\}$$

Rather than preserving the pair $(x_i, y_i)$, we extract two independent multisets:
$$\mathcal{X} = \{x_1, x_2, \dots, x_N\} \quad \text{and} \quad \mathcal{Y} = \{y_1, y_2, \dots, y_N\}$$

We then construct two ordered sequences of length $N$:
- $X^*$: elements of $\mathcal{X}$ sorted such that $X^*_1 \le X^*_2 \le \dots \le X^*_N$.
- $Y^*$: elements of $\mathcal{Y}$ sorted such that $Y^*_1 \ge Y^*_2 \ge \dots \ge Y^*_N$.

The final output is the set of ordered pairs:
$$\mathcal{R} = \{(X^*_k, Y^*_k) \mid 1 \le k \le N\}$$

### Positional Alignment via Ordinal Row Numbers

In relational SQL, independent reordering is achieved using the `ROW_NUMBER()` analytic window function:
1. **First Column CTE:**
   Assign a 1-based sequential rank to each element of `first_col` ordered ascending:
   $$\text{rn}_1 = \text{ROW\_NUMBER}() \text{ OVER (ORDER BY } \text{first\_col ASC)}$$
2. **Second Column CTE:**
   Assign a 1-based sequential rank to each element of `second_col` ordered descending:
   $$\text{rn}_2 = \text{ROW\_NUMBER}() \text{ OVER (ORDER BY } \text{second\_col DESC)}$$
3. **Positional Equi-Join:**
   Join the two ranked streams on equality of their generated ordinal ranks:
   $$\text{rn}_1 = \text{rn}_2$$

| Step / Column | Sorting Direction | Window Function | Relational Role |
|---|---|---|---|
| `first_col` | Ascending (`ASC`) | `ROW_NUMBER() OVER (ORDER BY first_col ASC)` | Generates rank $\text{rn}_1$ from smallest to largest |
| `second_col` | Descending (`DESC`) | `ROW_NUMBER() OVER (ORDER BY second_col DESC)` | Generates rank $\text{rn}_2$ from largest to smallest |
| Join Condition | $\text{rn}_1 = \text{rn}_2$ | Inner Join on rank | Fuses independent sorted values at identical ordinal ranks |
| Duplicate Handling | Arbitrary tie-breaking | `ROW_NUMBER()` ensures strict $1 \dots N$ bijection | Preserves duplicate frequencies across both columns |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the relational execution on the 4-row input:

```
Original Table Data:
Row 1: (4, 2)
Row 2: (2, 3)
Row 3: (3, 1)
Row 4: (1, 4)

Sorted Stream 1 (first_col ASC):
rn = 1: 1
rn = 2: 2
rn = 3: 3
rn = 4: 4

Sorted Stream 2 (second_col DESC):
rn = 1: 4
rn = 2: 3
rn = 3: 2
rn = 4: 1

Equi-joined pairs by rn:
(1, 4), (2, 3), (3, 2), (4, 1)
```

### Step 1: Project and Rank `first_col` Ascending
Extract all values of `first_col`: $\{4, 2, 3, 1\}$.
Sort in ascending order and assign row numbers:
- Value $1 \to \text{rn}_1 = 1$
- Value $2 \to \text{rn}_1 = 2$
- Value $3 \to \text{rn}_1 = 3$
- Value $4 \to \text{rn}_1 = 4$

Resulting intermediate table $T_1$:
$$[(1, 1), (2, 2), (3, 3), (4, 4)] \quad (\text{columns: } \text{first\_col}, \text{rn}_1)$$

### Step 2: Project and Rank `second_col` Descending
Extract all values of `second_col`: $\{2, 3, 1, 4\}$.
Sort in descending order and assign row numbers:
- Value $4 \to \text{rn}_2 = 1$
- Value $3 \to \text{rn}_2 = 2$
- Value $2 \to \text{rn}_2 = 3$
- Value $1 \to \text{rn}_2 = 4$

Resulting intermediate table $T_2$:
$$[(4, 1), (3, 2), (2, 3), (1, 4)] \quad (\text{columns: } \text{second\_col}, \text{rn}_2)$$

### Step 3: Execute Positional Equi-Join on $\text{rn}_1 = \text{rn}_2$
Match rows where $\text{rn}_1 = \text{rn}_2$:
- Rank $1$: $T_1.\text{first\_col} = 1$, $T_2.\text{second\_col} = 4 \implies (1, 4)$
- Rank $2$: $T_1.\text{first\_col} = 2$, $T_2.\text{second\_col} = 3 \implies (2, 3)$
- Rank $3$: $T_1.\text{first\_col} = 3$, $T_2.\text{second\_col} = 2 \implies (3, 2)$
- Rank $4$: $T_1.\text{first\_col} = 4$, $T_2.\text{second\_col} = 1 \implies (4, 1)$

### Step 4: Final Output
The aligned table contains $4$ rows:
- `(1, 4)`
- `(2, 3)`
- `(3, 2)`
- `(4, 1)`

---

## 4. Comprehensive State Trace

The table below catalogs the progression from raw uncoupled data to the final aligned tabular output:

| Input Row | Raw `first_col` | Raw `second_col` | Ascending Rank $\text{rn}_1$ | Sorted `first_col` | Descending Rank $\text{rn}_2$ | Sorted `second_col` | Fused Output Row $(\text{rn}_1 = \text{rn}_2)$ |
|---|---|---|---|---|---|---|---|
| $1$ | $4$ | $2$ | $1$ | $1$ | $1$ | $4$ | `(1, 4)` |
| $2$ | $2$ | $3$ | $2$ | $2$ | $2$ | $3$ | `(2, 3)` |
| $3$ | $3$ | $1$ | $3$ | $3$ | $3$ | $2$ | `(3, 2)` |
| $4$ | $1$ | $4$ | $4$ | $4$ | $4$ | $1$ | `(4, 1)` |

### Verification of Invariants

- **`first_col` Monotonicity:** $1 < 2 < 3 < 4$ (Strictly ascending).
- **`second_col` Monotonicity:** $4 > 3 > 2 > 1$ (Strictly descending).
- **Multiset Conservation:** Both output columns contain the exact multiset of values from the input columns without loss or insertion.

---

## 5. Algorithmic Correctness & Soundness

### Bijective Rank Pairing
Because `ROW_NUMBER()` generates a contiguous sequence of distinct integers $1, 2, \dots, N$ for any input table of $N$ rows:
- The domain of $\text{rn}_1$ is strictly $\{1, 2, \dots, N\}$.
- The domain of $\text{rn}_2$ is strictly $\{1, 2, \dots, N\}$.
- The join condition $\text{rn}_1 = \text{rn}_2$ defines a perfect 1-to-1 bijection between the two sorted streams.
- Every element in `first_col` is matched with exactly one element in `second_col`, and every row is preserved.

### Duplicate Preservation
If identical values exist in either column (e.g., two copies of $2$ in `first_col`), `ROW_NUMBER()` assigns distinct consecutive ranks (e.g., $2$ and $3$) to each occurrence. Neither copy is collapsed or discarded, satisfying multiset preservation.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Duplicate Elements in Columns:** If `first_col = [2, 2, 2]`, `ROW_NUMBER()` assigns ranks $1, 2, 3$. The join pairs all three copies with the corresponding top 3 descending values of `second_col`.
2. **Single Row Table:** $N = 1$. Both streams have rank $1$. The single row is emitted unchanged.
3. **Already Sorted Table:** If `first_col` is already ascending and `second_col` is already descending, the output matches the input row for row.

### Common Anti-Patterns
- **Using `RANK()` or `DENSE_RANK()`:** `RANK()` assigns identical rank numbers to equal values (e.g., $1, 2, 2, 4$), skipping numbers. Joining on non-contiguous ranks produces Cartesian products on duplicate ties and leaves gaps where ranks were skipped. `ROW_NUMBER()` is mandatory to guarantee a contiguous permutation $1 \dots N$.
- **Sorting in Place without Window Functions:** Relational SQL has no inherent row order. One cannot simply write `ORDER BY first_col ASC, second_col DESC` on the original table, because this sorts entire rows together rather than uncoupling the two columns.
- **Cartesian Cross Join with Inequality:** Joining all rows and attempting to filter creates an $O(N^2)$ cross product. Row numbering enables an optimal $O(N \log N)$ sort-merge or hash join.

---

## 7. Complexity Analysis

### Time Complexity
- **Window Sorting of Column 1:** Sorting $N$ elements of `first_col` takes $O(N \log N)$ time.
- **Window Sorting of Column 2:** Sorting $N$ elements of `second_col` takes $O(N \log N)$ time.
- **Equi-Join on Row Number:** Since both streams are sorted by rank $1 \dots N$, a linear merge join executes in $O(N)$ time.
- Total time complexity is $O(N \log N)$, taking less than $10$ milliseconds for typical table sizes.

### Auxiliary Space Complexity
- Intermediate Common Table Expressions store $N$ rows for each ranked stream.
- Total auxiliary space complexity is $O(N)$ query memory.
