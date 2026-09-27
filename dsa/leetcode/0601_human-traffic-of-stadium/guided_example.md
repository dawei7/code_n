# Guided Example: Human Traffic of Stadium

We trace the step-by-step traffic threshold filtering ($people \ge 100$), islands-and-gaps consecutive grouping ($rk = id - \text{ROW\_NUMBER}()$), run-length island frequency partition windowing ($\text{COUNT}(1) \text{ OVER (PARTITION BY } rk)$), minimum streak length validation ($cnt \ge 3$), and temporal ordering projection on representative attendance logs:

- **Input:**
  - `Stadium` table:
    | `id` | `visit_date` | `people` |
    |:---:|:---:|:---:|
    | $1$ | `2017-01-01` | $10$ |
    | $2$ | `2017-01-02` | $109$ |
    | $3$ | `2017-01-03` | $150$ |
    | $4$ | `2017-01-04` | $99$ |
    | $5$ | `2017-01-05` | $145$ |
    | $6$ | `2017-01-06` | $1455$ |
    | $7$ | `2017-01-07` | $1999$ |
    | $8$ | `2017-01-08` | $188$ |
- **Required output:**
  | `id` | `visit_date` | `people` |
  |:---:|:---:|:---:|
  | $5$ | `2017-01-05` | $145$ |
  | $6$ | `2017-01-06` | $1455$ |
  | $7$ | `2017-01-07` | $1999$ |
  | $8$ | `2017-01-08` | $188$ |
  - Business objective: Identify all records belonging to streaks of **three or more consecutive days** where attendance was at least $100$ ($people \ge 100$).
  - Ordering: Output must be sorted by `visit_date ASC` (or `id ASC`).
- **The "Islands and Gaps" Difference Invariant:**
  - When filtering a table for rows where $people \ge 100$, consecutive rows will form contiguous clusters ("islands"), separated by non-qualifying days ("gaps").
  - Consider a contiguous streak of IDs: $k, \; k+1, \; k+2, \; \dots, \; k+m$.
  - In CTE $S$, assign each filtered row a sequential rank:
    $$
    rn = \text{ROW\_NUMBER}() \text{ OVER (ORDER BY } id)
    $$
  - Within any contiguous island, both $id$ and $rn$ advance by exactly $+1$ for each step.
  - Therefore, their arithmetic difference is **strictly constant throughout the entire island**:
    $$
    rk = id - rn
    $$
  - When a gap occurs, $id$ jumps forward while $rn$ increments by only $1$, causing $rk$ to shift to a different value.
  - Thus, $rk$ acts as a **unique identifier for each contiguous streak**!
- **Step-by-Step Worked Trace:**
  - **Step 1: Filter $people \ge 100$ and Compute $rk = id - rn$ (CTE $S$):**
    - Row with $id = 1$ ($10 < 100$): Filtered out.
    - Row with $id = 2$ ($109 \ge 100$): $rn = 1 \implies rk = 2 - 1 = \mathbf{1}$.
    - Row with $id = 3$ ($150 \ge 100$): $rn = 2 \implies rk = 3 - 2 = \mathbf{1}$.
    - Row with $id = 4$ ($99 < 100$): Filtered out (Gap!).
    - Row with $id = 5$ ($145 \ge 100$): $rn = 3 \implies rk = 5 - 3 = \mathbf{2}$.
    - Row with $id = 6$ ($1455 \ge 100$): $rn = 4 \implies rk = 6 - 4 = \mathbf{2}$.
    - Row with $id = 7$ ($1999 \ge 100$): $rn = 5 \implies rk = 7 - 5 = \mathbf{2}$.
    - Row with $id = 8$ ($188 \ge 100$): $rn = 6 \implies rk = 8 - 6 = \mathbf{2}$.
    - Table $S$ contents:
      | `id` | `visit_date` | `people` | `rn` | `rk` ($id - rn$) |
      |:---:|:---:|:---:|:---:|:---:|
      | $2$ | `2017-01-02` | $109$ | $1$ | **$1$** |
      | $3$ | `2017-01-03` | $150$ | $2$ | **$1$** |
      | $5$ | `2017-01-05` | $145$ | $3$ | **$2$** |
      | $6$ | `2017-01-06` | $1455$ | $4$ | **$2$** |
      | $7$ | `2017-01-07` | $1999$ | $5$ | **$2$** |
      | $8$ | `2017-01-08` | $188$ | $6$ | **$2$** |
  - **Step 2: Partition by Island Key $rk$ and Count Island Size (CTE $T$):**
    - Group $rk = 1$: contains IDs $\{2, 3\}$.
      $$
      cnt(rk = 1) = \mathbf{2}
      $$
    - Group $rk = 2$: contains IDs $\{5, 6, 7, 8\}$.
      $$
      cnt(rk = 2) = \mathbf{4}
      $$
  - **Step 3: Filter for Streaks of Size $\ge 3$:**
    - Group $rk = 1$: $cnt = 2 < 3 \implies \mathbf{Disqualified}$ (only 2 consecutive days).
    - Group $rk = 2$: $cnt = 4 \ge 3 \implies \mathbf{Qualified!}$
  - **Step 4: Project Final Attributes:**
    - Extract records with $rk = 2$ in ascending order of `id`:
      - `(5, '2017-01-05', 145)`
      - `(6, '2017-01-06', 1455)`
      - `(7, '2017-01-07', 1999)`
      - `(8, '2017-01-08', 188)`
- **Isolated Days Above 100 ($cnt = 1$):**
  - A single day above 100 has $cnt = 1 < 3 \implies$ excluded.
- **Consecutive Streak of Exactly 3 Days:**
  - $cnt = 3 \ge 3 \implies$ all 3 rows qualify.

This instance demonstrates the analytical islands-and-gaps technique in SQL, mathematically proves why index-rank difference invariance partitions contiguous arithmetic progressions, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Stadium` table recording daily attendance:
Find all dates that are part of a streak of **at least 3 consecutive days** where `people >= 100`.
Order by `visit_date ASC`.

```text
Attendance:
  Day 1: 10   (< 100)
  Day 2: 109  (>= 100) \  Streak of 2 days -> Disqualified (< 3)
  Day 3: 150  (>= 100) /
  Day 4: 99   (< 100)
  Day 5: 145  (>= 100) \
  Day 6: 1455 (>= 100)  | Streak of 4 days -> QUALIFIED! (>= 3)
  Day 7: 1999 (>= 100)  |
  Day 8: 188  (>= 100) /

Output: Days 5, 6, 7, 8
```

### The Pitfall of Triple Self-Joins
- A naive approach joins `Stadium` three times: `s1.id = s2.id - 1 AND s2.id = s3.id - 1`.
- This requires three branches (current row as start, middle, or end of streak) followed by a `DISTINCT` union.
- The **Islands and Gaps** window method handles streaks of arbitrary length ($3, 4, 5, \dots, 100$) automatically without self-joins.

---

## 2. Conceptual Foundation & Invariants

### 1. Island Identification Formula:
After filtering for $people \ge 100$:
$$
rk = id - \text{ROW\_NUMBER}() \text{ OVER (ORDER BY } id)
$$
- For consecutive elements: $(id+1) - (rn+1) = id - rn = rk$.
- Thus, every continuous streak of consecutive integers shares the exact same $rk$.

### 2. Group Size Filter:
$$
cnt = \text{COUNT}(1) \text{ OVER (PARTITION BY } rk)
$$
Keep rows where $cnt \ge 3$.

> **Affine Difference Invariant.** Subtracting a contiguous rank sequence from a contiguous identifier sequence yields a zero derivative $\Delta(id - rn) = 0$, forming an equivalence relation over consecutive runs.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Filter `people >= 100`
- Qualified IDs: $[2, 3, 5, 6, 7, 8]$.

---

### Step 2: Compute $rk$
- ID 2: $rn = 1 \implies rk = 2 - 1 = 1$.
- ID 3: $rn = 2 \implies rk = 3 - 2 = 1$.
- ID 5: $rn = 3 \implies rk = 5 - 3 = 2$.
- ID 6: $rn = 4 \implies rk = 6 - 4 = 2$.
- ID 7: $rn = 5 \implies rk = 7 - 5 = 2$.
- ID 8: $rn = 6 \implies rk = 8 - 6 = 2$.

---

### Step 3: Count per $rk$
- $rk = 1$: count = 2.
- $rk = 2$: count = 4.

---

### Step 4: Filter $cnt \ge 3$
- Only $rk = 2$ qualifies ($4 \ge 3$).
- Project IDs $5, 6, 7, 8$.

---

## 4. Complete Execution Trace

| `id` | `visit_date` | `people` | $people \ge 100$ | $rn$ | $rk = id - rn$ | Island Count $cnt$ | Kept? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `2017-01-01` | $10$ | No | — | — | — | No |
| $2$ | `2017-01-02` | $109$ | Yes | $1$ | **$1$** | $2$ | No ($< 3$) |
| $3$ | `2017-01-03` | $150$ | Yes | $2$ | **$1$** | $2$ | No ($< 3$) |
| $4$ | `2017-01-04` | $99$ | No | — | — | — | No |
| **$5$** | `2017-01-05` | $145$ | Yes | $3$ | **$2$** | **$4$** | **Yes** |
| **$6$** | `2017-01-06` | $1455$ | Yes | $4$ | **$2$** | **$4$** | **Yes** |
| **$7$** | `2017-01-07` | $1999$ | Yes | $5$ | **$2$** | **$4$** | **Yes** |
| **$8$** | `2017-01-08` | $188$ | Yes | $6$ | **$2$** | **$4$** | **Yes** |

---

## 5. Boundary Cases & Failure Modes

- **No Streak Reaches 3 Days:** Output table is empty with correct column headers.
- **Multiple Disjoint 3+ Day Streaks:** Each distinct streak gets a different $rk$; all streaks with count $\ge 3$ are returned.
- **Streak Spanning Entire Table:** All rows returned.
- **People Exactly 100:** Boundary value passes $people \ge 100$.

---

## 6. Traps & Common Anti-Patterns

- **Using Date Differences Directly Without ID Assumptions:** In LeetCode 601, `id` is guaranteed to be consecutive and incrementing daily. Using `id - ROW_NUMBER()` is fast and concise.
- **Limiting Self-Joins to Exactly 3 Rows:** Multiple self-joins require complicated `OR` conditions to handle streaks of length 4 or more, often producing duplicate rows.
- **Ordering by Attendance Instead of Date:** The problem requires `ORDER BY visit_date ASC`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Filtering $people \ge 100$: $\mathcal{O}(N)$ sequential scan.
  - Sorting and window ranking: $\mathcal{O}(K \log K)$ where $K \le N$ is the number of qualified days.
  - Partition count and final filter: $\mathcal{O}(K)$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space to store CTE intermediate attributes.
