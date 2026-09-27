# Guided Example: Students Report By Geography

We trace the step-by-step partitioned window ranking (`ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name)`), relational cross-tabulation pivot matrix alignment, conditional case aggregation (`MAX(CASE WHEN ...)`), ragged column null-padding, and alphabetical geography report generation on representative student rosters:

- **Input:**
  - `Student` table:
    | `name` | `continent` |
    |:---:|:---:|
    | `Jane` | `America` |
    | `Pascal` | `Europe` |
    | `Xi` | `Asia` |
    | `Jack` | `America` |
- **Required output:**
  | `America` | `Asia` | `Europe` |
  |:---:|:---:|:---:|
  | `Jack` | `Xi` | `Pascal` |
  | `Jane` | `null` | `null` |
  - Problem objective: Pivot the table horizontally so each continent becomes a column header (`America`, `Asia`, `Europe`).
  - Within each continent column, names must appear in **alphabetical ascending order**.
  - Unequal list length policy: If a continent has fewer students than the maximum, pad its trailing rows with `null`.
- **Relational Pivot & Partitioned Rank Alignment Trace:**
  - Standard SQL does not allow joining ragged lists of arbitrary sizes without a shared join key.
  - **The Shared Row Key Technique ($rk$):**
    - Within each continent partition, sort students alphabetically by `name` and assign an integer rank:
      $$
      rk = \text{ROW\_NUMBER}() \text{ OVER (PARTITION BY } continent \text{ ORDER BY } name)
      $$
    - The 1st student of America, the 1st student of Asia, and the 1st student of Europe all receive $rk = 1$.
    - The 2nd student of America receives $rk = 2$.
    - This creates a **synthetic horizontal row identifier** across the disjoint geographic partitions!
  - **The Conditional Pivot Matrix (`GROUP BY rk`):**
    - Group by $rk$.
    - For each column, extract the student matching that continent via `MAX(CASE WHEN continent = 'X' THEN name END)`.
    - If no student from that continent achieved rank $rk$, the expression evaluates to `null`.
- **Step-by-Step Worked Trace:**
  - **Step 1: Compute Partitioned Rank in CTE $T$:**
    - **Partition `continent = 'America'`:**
      - Alphabetical sort: `['Jack', 'Jane']`
      - `Jack` $\to rk = \mathbf{1}$
      - `Jane` $\to rk = \mathbf{2}$
    - **Partition `continent = 'Asia'`:**
      - Alphabetical sort: `['Xi']`
      - `Xi` $\to rk = \mathbf{1}$
    - **Partition `continent = 'Europe'`:**
      - Alphabetical sort: `['Pascal']`
      - `Pascal` $\to rk = \mathbf{1}$
    - Formatted intermediate rows:
      | `name` | `continent` | `rk` |
      |:---:|:---:|:---:|
      | `Jack` | `America` | $1$ |
      | `Jane` | `America` | $2$ |
      | `Xi` | `Asia` | $1$ |
      | `Pascal` | `Europe` | $1$ |
  - **Step 2: Group by Rank $rk$ and Pivot:**
    - **Row Group $rk = 1$:**
      - America: `Jack`
      - Asia: `Xi`
      - Europe: `Pascal`
      - Emits:
        $$
        (\text{'Jack'}, \; \text{'Xi'}, \; \text{'Pascal'})
        $$
    - **Row Group $rk = 2$:**
      - America: `Jane`
      - Asia: None $\implies \mathbf{null}$
      - Europe: None $\implies \mathbf{null}$
      - Emits:
        $$
        (\text{'Jane'}, \; \mathbf{null}, \; \mathbf{null})
        $$
  - **Step 3: Final Matrix Assembly:**
    | `America` | `Asia` | `Europe` |
    |:---:|:---:|:---:|
    | `Jack` | `Xi` | `Pascal` |
    | `Jane` | `null` | `null` |
- **Equal Length Continents:**
  - If America, Asia, and Europe each have 3 students, all cells are filled with zero `null` entries across 3 rows.
- **Single Continent Dataset:**
  - If all students are in America, the `America` column contains all names while `Asia` and `Europe` contain `null` in every row.

This instance demonstrates ragged-array relational pivoting via synthetic partitioned ordinal keys, mathematically proves why grouped conditional maximization transposes sparse attributes into aligned tabular schemas, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Student` table with `name` and `continent`:
Pivot the table into 3 columns (`America`, `Asia`, `Europe`).
Each column must list students sorted alphabetically, padded with `null` if counts differ.

```text
Students:
  America: Jack, Jane
  Asia:    Xi
  Europe:  Pascal

Row 1 (Rank 1): Jack    | Xi   | Pascal
Row 2 (Rank 2): Jane    | null | null
```

### The Ragged Pivot Challenge
- In relational databases, pivoting requires a common key to align columns horizontally.
- Because students in different continents have no natural relationship, we generate an artificial row index $rk = \text{ROW\_NUMBER}()$ for each continent independently.
- Grouping on $rk$ stitches the $k$-th student of each continent into row $k$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Partitioned Rank Expression:
$$
rk = \text{ROW\_NUMBER}() \text{ OVER (PARTITION BY } continent \text{ ORDER BY } name)
$$

### 2. The Conditional Max Pivot:
```sql
SELECT
    MAX(CASE WHEN continent = 'America' THEN name END) AS "America",
    MAX(CASE WHEN continent = 'Asia' THEN name END) AS "Asia",
    MAX(CASE WHEN continent = 'Europe' THEN name END) AS "Europe"
FROM T
GROUP BY rk;
```
- For a given $rk$, each continent has at most one student.
- `MAX()` extracts that unique student name or returns `NULL`.

> **Ordinal Stitching Invariant.** Assigning independent dense ordinal ranks within categorical partitions enables bijective horizontal mapping across unequal set cardinalities.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Assign Local Alphabetical Ranks
- `America`: `Jack` (1), `Jane` (2).
- `Asia`: `Xi` (1).
- `Europe`: `Pascal` (1).

---

### Step 2: Aggregate by $rk = 1$
- America student: `Jack`.
- Asia student: `Xi`.
- Europe student: `Pascal`.
- Row 1: `('Jack', 'Xi', 'Pascal')`.

---

### Step 3: Aggregate by $rk = 2$
- America student: `Jane`.
- Asia student: `null`.
- Europe student: `null`.
- Row 2: `('Jane', null, null)`.

---

## 4. Complete Execution Trace

| Rank $rk$ | `America` Candidate | `Asia` Candidate | `Europe` Candidate | Resulting Row |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | `Jack` | `Xi` | `Pascal` | `('Jack', 'Xi', 'Pascal')` |
| $2$ | `Jane` | None (`null`) | None (`null`) | `('Jane', null, null)` |

---

## 5. Boundary Cases & Failure Modes

- **Continent With No Students:** That column contains exclusively `null` values for all rows.
- **Large Dataset with Unequal Counts (100 in America, 2 in Asia):** 100 rows returned; Asia has 2 names and 98 `null` values.
- **Duplicate Names in Same Continent:** Handled gracefully by `ROW_NUMBER()` generating distinct consecutive ranks.
- **All Counts Equal:** Clean rectangular matrix with 0 nulls.

---

## 6. Traps & Common Anti-Patterns

- **Using `COUNT()` Instead of `ROW_NUMBER()`:** `COUNT()` returns the total size of the group rather than an increasing sequence of row indexes.
- **Ordering by Original Insertion Order:** The problem strictly requires sorting alphabetically within each continent (`ORDER BY name`).
- **Forgetting Double Quotes Around Headers in PostgreSQL:** Column headers with mixed case (e.g. `"America"`) must be quoted in PostgreSQL so case is preserved.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Partitioned sort and ranking: $\mathcal{O}(N \log N)$ where $N$ is total student count.
  - Grouping by $rk$ and projecting 3 columns: $\mathcal{O}(N)$ time.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store ranked intermediate tuples in CTE $T$.
