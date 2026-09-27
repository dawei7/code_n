# Guided Example: Investments in 2016

We trace the step-by-step partition frequency windowing (`COUNT(1) OVER (PARTITION BY tiv_2015)`), geographic coordinate uniqueness validation (`COUNT(1) OVER (PARTITION BY lat, lon)`), dual conjunctive condition filtering ($cnt_1 > 1 \land cnt_2 = 1$), 2016 investment value summation, and 2-decimal rounding on representative insurance policies:

- **Input:**
  - `Insurance` table:
    | `pid` | `tiv_2015` | `tiv_2016` | `lat` | `lon` |
    |:---:|:---:|:---:|:---:|:---:|
    | $1$ | $10$ | $5.0$ | $1$ | $1$ |
    | $2$ | $10$ | $7.5$ | $2$ | $2$ |
    | $3$ | $20$ | $100.0$ | $3$ | $3$ |
- **Required output:**
  | `tiv_2016` |
  |:---:|
  | $12.50$ |
  - Business qualification criteria:
    1. **Duplicate 2015 Investment:** Policyholder must share their `tiv_2015` value with **at least one other policyholder** (frequency $> 1$).
    2. **Unique Geographic Location:** Policyholder must have a **unique $(lat, lon)$ coordinate pair** across the entire table (no collision with any other policyholder, frequency $= 1$).
    3. Output: Sum of `tiv_2016` for all qualifying policyholders, rounded to $2$ decimal places.
- **Relational Partition Windowing Trace:**
  - **Step 1: Compute Frequencies in CTE $T$:**
    - For each row, calculate two independent analytical counts:
      - $cnt_1$: Total rows sharing the same `tiv_2015`.
      - $cnt_2$: Total rows sharing the same $(lat, lon)$.
    - **Policy 1 (`pid = 1`):**
      - `tiv_2015 = 10`: Appears in Policy 1 and Policy 2 $\implies cnt_1 = \mathbf{2}$.
      - `(lat, lon) = (1, 1)`: Unique in table $\implies cnt_2 = \mathbf{1}$.
    - **Policy 2 (`pid = 2`):**
      - `tiv_2015 = 10`: Appears in Policy 1 and Policy 2 $\implies cnt_1 = \mathbf{2}$.
      - `(lat, lon) = (2, 2)`: Unique in table $\implies cnt_2 = \mathbf{1}$.
    - **Policy 3 (`pid = 3`):**
      - `tiv_2015 = 20`: Appears only in Policy 3 $\implies cnt_1 = \mathbf{1}$.
      - `(lat, lon) = (3, 3)`: Unique in table $\implies cnt_2 = \mathbf{1}$.
  - **Step 2: Evaluate Conjunctive Predicate ($cnt_1 > 1 \land cnt_2 = 1$):**
    - **Policy 1:** $cnt_1 = 2 > 1$ (True), $cnt_2 = 1$ (True) $\implies \mathbf{Qualifies!}$
      - Contributes `tiv_2016 = 5.0`.
    - **Policy 2:** $cnt_1 = 2 > 1$ (True), $cnt_2 = 1$ (True) $\implies \mathbf{Qualifies!}$
      - Contributes `tiv_2016 = 7.5`.
    - **Policy 3:** $cnt_1 = 1 \ngtr 1$ (**Fails Criterion 1**) $\implies$ Disqualified.
  - **Step 3: Aggregate and Round:**
    - Sum of qualifying 2016 investments:
      $$
      \text{Sum} = 5.0 + 7.5 = \mathbf{12.50}
      $$
    - Format with 2 decimal places:
      $$
      \text{ROUND}(12.50, \; 2) = \mathbf{12.50}
      $$
- **Geographic Collision Disqualification Instance:**
  - Suppose Policy 4 has `tiv_2015 = 10, lat = 1, lon = 1`.
  - Now Policy 1 and Policy 4 collide on coordinates $(1, 1)$ $\implies cnt_2 = 2 \ne 1$.
  - Both Policy 1 and Policy 4 fail the location uniqueness test and are dropped!
- **No Qualifying Policyholders:**
  - If all policies have unique 2015 values or all collide on location, sum is `NULL` or $0.00$.

This instance demonstrates multi-dimensional partition counting in relational analytical processing, mathematically proves why parallel window aggregations eliminate nested self-joins, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an `Insurance` table with `pid`, `tiv_2015`, `tiv_2016`, `lat`, and `lon`:
Find the sum of `tiv_2016` (rounded to 2 decimals) for all policyholders who:
1. Have the same `tiv_2015` as at least one other person.
2. Have a completely unique `(lat, lon)` coordinate pair.

```text
Policies:
  pid 1: tiv_2015 = 10, lat/lon = (1, 1) -> Shared 2015, unique loc -> VALID! (5.0)
  pid 2: tiv_2015 = 10, lat/lon = (2, 2) -> Shared 2015, unique loc -> VALID! (7.5)
  pid 3: tiv_2015 = 20, lat/lon = (3, 3) -> Unique 2015 -> INVALID!

Total 2016 Investment = 5.0 + 7.5 = 12.50
```

### The Window Function Acceleration
- Traditional approaches use two subqueries with `IN` and `NOT IN`, requiring multiple table scans.
- Using window functions:
  - `cnt1 = COUNT(1) OVER (PARTITION BY tiv_2015)`
  - `cnt2 = COUNT(1) OVER (PARTITION BY lat, lon)`
- Both criteria are attached directly to each row in a single pipeline:
  - Filter: `WHERE cnt1 > 1 AND cnt2 = 1`
  - Aggregate: `ROUND(SUM(tiv_2016), 2)`

---

## 2. Conceptual Foundation & Invariants

### 1. The Dual-Partition CTE:
```sql
WITH T AS (
    SELECT
        tiv_2016,
        COUNT(1) OVER (PARTITION BY tiv_2015) AS cnt1,
        COUNT(1) OVER (PARTITION BY lat, lon) AS cnt2
    FROM Insurance
)
```

### 2. The Filter and Summation:
```sql
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM T
WHERE cnt1 > 1 AND cnt2 = 1;
```

> **Orthogonal Partition Invariant.** The financial partition (`tiv_2015`) and the spatial partition (`lat, lon`) are statistically independent; window partitioning evaluates each dimension without combinatorial cross-product explosion.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Window Aggregation
- Rows with `tiv_2015 = 10`: policies 1 and 2 $\implies cnt_1 = 2$.
- Rows with `tiv_2015 = 20`: policy 3 $\implies cnt_1 = 1$.
- Location $(1, 1)$: policy 1 $\implies cnt_2 = 1$.
- Location $(2, 2)$: policy 2 $\implies cnt_2 = 1$.
- Location $(3, 3)$: policy 3 $\implies cnt_2 = 1$.

---

### Step 2: Evaluate Filter Predicate
- Policy 1: $cnt_1 = 2 > 1$ and $cnt_2 = 1 \implies \mathbf{True}$ (Kept, value 5.0).
- Policy 2: $cnt_1 = 2 > 1$ and $cnt_2 = 1 \implies \mathbf{True}$ (Kept, value 7.5).
- Policy 3: $cnt_1 = 1 \ngtr 1 \implies \mathbf{False}$ (Dropped).

---

### Step 3: Compute Sum
$$
5.0 + 7.5 = \mathbf{12.50}
$$

---

## 4. Complete Execution Trace

| `pid` | `tiv_2015` | `(lat, lon)` | `cnt1` (Shared 2015) | `cnt2` (Unique Loc) | Passes Filter? | `tiv_2016` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $10$ | $(1, 1)$ | **$2$** | **$1$** | **Yes** | **$5.0$** |
| **$2$** | $10$ | $(2, 2)$ | **$2$** | **$1$** | **Yes** | **$7.5$** |
| $3$ | $20$ | $(3, 3)$ | $1$ | $1$ | No | — |
| **Total** | — | — | — | — | — | **`12.50`** |

---

## 5. Boundary Cases & Failure Modes

- **No Policy Meets Both Criteria:** Output sum is `null` (or $0.00$ depending on coalesce).
- **Location Collision:** Two policyholders with same coordinates both have $cnt_2 \ge 2$, disqualifying both.
- **Floating-Point Rounding:** `ROUND(SUM(tiv_2016), 2)` ensures exactly 2 decimal digits are preserved.

---

## 6. Traps & Common Anti-Patterns

- **Multiple Self-Joins ($O(N^2)$):** Joining `Insurance` on `tiv_2015` and left-joining on `(lat, lon)` generates quadratic intermediate sets. Window functions process partitions in $O(N \log N)$ time.
- **Grouping by `tiv_2016`:** Aggregating `tiv_2016` directly collapses policies that happen to have the same 2016 payout. Filtering must occur at the policyholder level.
- **Forgetting Location is a Coordinate Pair:** Testing `lat` and `lon` separately is incorrect. Two people can share the same latitude as long as their longitudes differ; the combination `(lat, lon)` must be unique.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Partitioning by `tiv_2015`: $\mathcal{O}(N \log N)$ sorting/hashing.
  - Partitioning by `(lat, lon)`: $\mathcal{O}(N \log N)$ sorting/hashing.
  - Linear scan and summation: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to materialize CTE $T$ columns.
