# Guided Example: Find Median Given Frequency of Numbers

We trace the step-by-step forward cumulative frequency aggregation ($rk_1 = \sum_{x \le num} freq$), reverse cumulative frequency aggregation ($rk_2 = \sum_{x \ge num} freq$), total sample mass normalization ($s = \sum freq$), bidirectional half-mass median intersection predicate ($rk_1 \ge s/2 \land rk_2 \ge s/2$), and 1-decimal rounded mean projection on representative frequency tables:

- **Input:**
  - `Numbers` table:
    | `num` | `frequency` |
    |:---:|:---:|
    | $0$ | $7$ |
    | $1$ | $1$ |
    | $2$ | $3$ |
    | $3$ | $1$ |
- **Required output:**
  | `median` |
  |:---:|
  | $0.0$ |
  - Problem contract:
    - The table represents a compressed multiset of integers where each number `num` appears `frequency` times.
    - Total expanded dataset: $[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3]$ ($12$ total numbers).
    - Objective: Compute the median of this expanded multiset, rounded to $1$ decimal place.
- **Bidirectional Cumulative Frequency Window Trace:**
  - Total mass of all numbers:
    $$
    s = \sum frequency = 7 + 1 + 3 + 1 = \mathbf{12}
    $$
  - Half-mass threshold:
    $$
    \frac{s}{2} = \frac{12}{2} = \mathbf{6}
    $$
  - **The Symmetrical Median Criterion:**
    - In any sorted frequency distribution, the median elements are those that overlap the exact center.
    - An element `num` covers the center if and only if:
      1. Cumulative count from the left up to and including `num` is $\ge s/2$ ($rk_1 \ge s/2$).
      2. Cumulative count from the right down to and including `num` is $\ge s/2$ ($rk_2 \ge s/2$).
    - If a single number contains both middle indices (e.g. 6th and 7th), it alone satisfies both inequalities.
    - If two distinct numbers contain the 6th and 7th elements, both numbers satisfy the inequalities, and `AVG(num)` averages them!
  - **Step 1: Compute Forward and Reverse Running Totals:**
    - **Row 1 (`num = 0, frequency = 7`):**
      - Ascending prefix ($rk_1$): $7$
      - Descending suffix ($rk_2$): $7 + 1 + 3 + 1 = \mathbf{12}$
      - Test:
        $$
        rk_1 = 7 \ge 6 \quad \land \quad rk_2 = 12 \ge 6 \implies \mathbf{True} \quad (\text{Satisfies Median!})
        $$
    - **Row 2 (`num = 1, frequency = 1`):**
      - Ascending prefix ($rk_1$): $7 + 1 = 8 \ge 6$ (True)
      - Descending suffix ($rk_2$): $1 + 3 + 1 = \mathbf{5} < 6$ (**Fails!**)
      - Condition fails.
    - **Row 3 (`num = 2, frequency = 3`):**
      - Ascending prefix ($rk_1$): $7 + 1 + 3 = 11 \ge 6$ (True)
      - Descending suffix ($rk_2$): $3 + 1 = \mathbf{4} < 6$ (**Fails!**)
      - Condition fails.
    - **Row 4 (`num = 3, frequency = 1`):**
      - Ascending prefix ($rk_1$): $12 \ge 6$ (True)
      - Descending suffix ($rk_2$): $1 < 6$ (**Fails!**)
      - Condition fails.
  - **Step 2: Collect Qualifying Median Numbers:**
    - The only number satisfying $rk_1 \ge 6 \land rk_2 \ge 6$ is:
      $$
      \text{Numbers} = \{0\}
      $$
  - **Step 3: Average and Round:**
    $$
    \text{median} = \text{ROUND}(\text{AVG}(0), \; 1) = \mathbf{0.0}
    $$
- **Split Median Example (Two Distinct Middle Elements):**
  - Suppose expanded set is $[1, 2, 3, 4]$ ($s = 4, s/2 = 2$).
  - For $2$: $rk_1 = 2 \ge 2, \; rk_2 = 3 \ge 2 \implies$ Qualifies!
  - For $3$: $rk_1 = 3 \ge 2, \; rk_2 = 2 \ge 2 \implies$ Qualifies!
  - Qualified: $\{2, 3\}$.
  - $\text{AVG}(2, 3) = \frac{2 + 3}{2} = \mathbf{2.5}$.
  - Correctly averages the two middle values without procedural logic!

This instance demonstrates cumulative mass balancing over discrete frequency measures, mathematically proves why the intersection of forward and reverse half-mass sets yields the exact median, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Numbers` table containing `num` and its `frequency`:
Calculate the **median** of the decompressed dataset, rounded to 1 decimal place.

```text
Table:
  num: 0, frequency: 7
  num: 1, frequency: 1
  num: 2, frequency: 3
  num: 3, frequency: 1

Decompressed:
  [ 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3 ]   (Total 12 numbers)
              ^  ^
         Indices 5 and 6 (6th and 7th numbers) are both 0.

Median = (0 + 0) / 2 = 0.0
```

### The Dual-Cumulative Frequency Theorem
- Decompressing the table into individual rows is extremely slow and memory-intensive if frequencies are large (e.g. frequency $= 10^6$).
- Instead, we work directly on the compressed frequency table using **window functions**:
  - $rk_1$: Cumulative sum of frequencies ordered ascending by `num`.
  - $rk_2$: Cumulative sum of frequencies ordered descending by `num`.
  - $s$: Total sum of all frequencies.
- A number contains a median point if and only if:
  $$
  rk_1 \ge \frac{s}{2} \quad \text{AND} \quad rk_2 \ge \frac{s}{2}
  $$
- Taking `AVG(num)` across the qualifying rows automatically handles both odd lengths and even lengths!

---

## 2. Conceptual Foundation & Invariants

### 1. Cumulative Frequency Window Functions:
In CTE `t`:
```sql
SELECT
    *,
    SUM(frequency) OVER (ORDER BY num ASC) AS rk1,
    SUM(frequency) OVER (ORDER BY num DESC) AS rk2,
    SUM(frequency) OVER () AS s
FROM Numbers
```

### 2. Median Filter Condition:
$$
\text{WHERE } rk_1 \ge \frac{s}{2} \quad \text{AND} \quad rk_2 \ge \frac{s}{2}
$$

### 3. Aggregation:
$$
\text{SELECT ROUND(AVG(num), 1) AS median FROM t}
$$

> **Mass Centroid Invariant.** The conditions $rk_1 \ge s/2$ and $rk_2 \ge s/2$ define the central interval containing the 50th percentile mass of the cumulative distribution function.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Compute Window Values
Total sum of frequencies:
$$
s = 7 + 1 + 3 + 1 = 12 \implies \frac{s}{2} = 6
$$

| `num` | `frequency` | Ascending Prefix $rk_1$ | Descending Suffix $rk_2$ |
|:---:|:---:|:---:|:---:|
| $0$ | $7$ | $7$ | $12$ |
| $1$ | $1$ | $8$ | $5$ |
| $2$ | $3$ | $11$ | $4$ |
| $3$ | $1$ | $12$ | $1$ |

---

### Step 2: Evaluate Filter ($rk_1 \ge 6 \land rk_2 \ge 6$)
- `num = 0`: $7 \ge 6$ and $12 \ge 6 \implies \mathbf{True}$.
- `num = 1`: $8 \ge 6$ but $5 < 6 \implies \mathbf{False}$.
- `num = 2`: $11 \ge 6$ but $4 < 6 \implies \mathbf{False}$.
- `num = 3`: $12 \ge 6$ but $1 < 6 \implies \mathbf{False}$.

---

### Step 3: Compute Median
Only row `num = 0` survives.
$$
\text{median} = \text{ROUND}(\text{AVG}(0), 1) = \mathbf{0.0}
$$

---

## 4. Complete Execution Trace

| `num` | `frequency` | $rk_1 \ge 6$? | $rk_2 \ge 6$? | Both Satisfied? | Contribution to Median |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $7$ | **Yes** ($7$) | **Yes** ($12$) | **Yes** | $0$ |
| $1$ | $1$ | **Yes** ($8$) | No ($5$) | No | — |
| $2$ | $3$ | **Yes** ($11$) | No ($4$) | No | — |
| $3$ | $1$ | **Yes** ($12$) | No ($1$) | No | — |
| **Result** | — | — | — | — | **$\text{ROUND}(0, 1) = \mathbf{0.0}$** |

---

## 5. Boundary Cases & Failure Modes

- **Even Count with Two Distinct Medians ($nums = [1, 2], freqs = [1, 1]$):** $s=2, s/2=1$. Both 1 and 2 qualify $\implies \text{AVG}(1, 2) = \mathbf{1.5}$.
- **Single Row ($num = 5, frequency = 10$):** $rk_1 = 10, rk_2 = 10 \ge 5 \implies \mathbf{5.0}$.
- **Massive Frequencies ($frequency = 10^9$):** Window sums avoid table row duplication, running in $O(N \log N)$ where $N$ is the number of distinct values.

---

## 6. Traps & Common Anti-Patterns

- **Generating Row Numbers via Recursive CTEs:** Generating $10^6$ physical rows from frequencies exhausts database memory. Analytical window functions process cumulative frequencies directly without generating rows.
- **Using Integer Division on `AVG()`:** Averaging integers $1$ and $2$ in SQL might truncate to $1$ instead of $1.5$. Casting to numeric or using decimal rounding preserves decimal fractions.
- **Ordering by Frequency Instead of `num`:** Cumulative sums must be ordered by the numerical value `num ASC` / `num DESC`, not by frequency!

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting by `num` for window functions: $\mathcal{O}(K \log K)$ where $K$ is the number of distinct numbers in the table.
  - Linear scan and filtering: $\mathcal{O}(K)$.
  - Total Time: $\mathcal{O}(K \log K)$. For $K = 10^4$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space to store cumulative sums in CTE $t$.
