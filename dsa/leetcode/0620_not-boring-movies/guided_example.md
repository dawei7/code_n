# Guided Example: Not Boring Movies

We trace the step-by-step modular parity testing ($id \pmod 2 = 1$ or bitwise $id \ \& \ 1 = 1$), textual exclusion filtering ($description \ne \text{'boring'}$), composite predicate conjunction ($\text{odd} \land \text{not boring}$), descending rating sorting (`ORDER BY rating DESC`), and relational projection on representative cinema catalog databases:

- **Input:**
  - `Cinema` table:
    | `id` | `movie` | `description` | `rating` |
    |:---:|:---:|:---:|:---:|
    | $1$ | `War` | `great 3D` | $8.9$ |
    | $2$ | `Science` | `fiction` | $8.5$ |
    | $3$ | `irish` | `boring` | $6.2$ |
    | $4$ | `Ice song` | `Fantacy` | $8.6$ |
    | $5$ | `House card` | `Interesting` | $9.1$ |
- **Required output:**
  | `id` | `movie` | `description` | `rating` |
  |:---:|:---:|:---:|:---:|
  | $5$ | `House card` | `Interesting` | $9.1$ |
  | $1$ | `War` | `great 3D` | $8.9$ |
  - Business qualification rules: A film record qualifies if and only if it satisfies **both** of the following criteria:
    1. Parity constraint: `id` is an **odd number** ($id \pmod 2 = 1$).
    2. Quality constraint: `description` is **not equal to "boring"** ($description \ne \text{'boring'}$).
  - Ordering: Output must be sorted by `rating DESC` (highest rated movie first).
- **Conjunctive Filtering Trace:**
  - Composite predicate:
    $$
    P(\text{row}) = (id \pmod 2 = 1) \quad \land \quad (description \ne \text{'boring'})
    $$
  - **Row 1 (`id = 1, movie = 'War'`):**
    - Parity check: $1 \pmod 2 = 1 \implies \mathbf{True}$ (Odd).
    - Description check: `'great 3D' \ne 'boring'` $\implies \mathbf{True}$ (Not boring).
    - Conjunction: $True \land True = \mathbf{True}$ (Qualifies!).
  - **Row 2 (`id = 2, movie = 'Science'`):**
    - Parity check: $2 \pmod 2 = 0 \ne 1 \implies \mathbf{False}$ (Even).
    - Disqualified immediately by parity!
  - **Row 3 (`id = 3, movie = 'irish'`):**
    - Parity check: $3 \pmod 2 = 1 \implies \mathbf{True}$ (Odd).
    - Description check: `'boring' \ne 'boring'` $\implies \mathbf{False}$ (Boring!).
    - Conjunction: $True \land False = \mathbf{False}$ (Disqualified!).
  - **Row 4 (`id = 4, movie = 'Ice song'`):**
    - Parity check: $4 \pmod 2 = 0 \implies \mathbf{False}$ (Even).
    - Disqualified!
  - **Row 5 (`id = 5, movie = 'House card'`):**
    - Parity check: $5 \pmod 2 = 1 \implies \mathbf{True}$ (Odd).
    - Description check: `'Interesting' \ne 'boring'` $\implies \mathbf{True}$ (Not boring).
    - Conjunction: $True \land True = \mathbf{True}$ (Qualifies!).
  - **Step 2: Sort Surviving Records by Rating Descending:**
    - Surviving movies:
      - `House card` with rating $9.1$
      - `War` with rating $8.9$
    - Since $9.1 > 8.9$:
      1. First: `(5, 'House card', 'Interesting', 9.1)`
      2. Second: `(1, 'War', 'great 3D', 8.9)`
- **All Movies Even Instance:**
  - If all IDs are even ($2, 4, 6$), 0 rows satisfy the condition $\implies$ empty table.
- **Tied Ratings:**
  - If two qualified movies share the same rating, their relative order is stable or determined by engine defaults.

This instance demonstrates conjunctive relational filtering over arithmetic and string attributes, mathematically proves why parity partitioning and string inequality compose as independent orthogonal constraints, and derives $O(N \log N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Cinema` table with movie ratings:
Find all movies that have:
1. An **odd-numbered ID**, AND
2. A description that is **not "boring"**.
Sort the results by **`rating DESC`**.

```text
Row 1: id = 1 (Odd),  desc = "great 3D"    (Not boring) -> QUALIFIED! (Rating: 8.9)
Row 2: id = 2 (Even)                                    -> Disqualified
Row 3: id = 3 (Odd),  desc = "boring"      (Boring!)    -> Disqualified
Row 4: id = 4 (Even)                                    -> Disqualified
Row 5: id = 5 (Odd),  desc = "Interesting" (Not boring) -> QUALIFIED! (Rating: 9.1)

Sorted by Rating DESC:
  1. id = 5 (Rating: 9.1)
  2. id = 1 (Rating: 8.9)
```

### The Invariant of Simultaneous Conjunction
- Both constraints must be strictly satisfied ($C_1 \land C_2$).
- If either condition fails, the row is discarded.

---

## 2. Conceptual Foundation & Invariants

### 1. The SQL Query:
```sql
SELECT id, movie, description, rating
FROM Cinema
WHERE description != 'boring'
  AND (id % 2 = 1)
ORDER BY rating DESC;
```

### 2. Parity Testing Forms:
- Modulo: `id % 2 = 1` or `MOD(id, 2) = 1`.
- Bitwise: `id & 1 = 1`.
- All forms are semantically equivalent for positive integers.

> **Orthogonal Filter Invariant.** The selection predicate decomposes into two independent projections: $\sigma_{id \pmod 2 = 1}(\sigma_{description \ne 'boring'}(\text{Cinema}))$, each operating on distinct attribute domains.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Scan and Filter Rows
- Row 1: ID 1 odd, description `'great 3D'` $\implies \mathbf{Keep}$ ($rating = 8.9$).
- Row 2: ID 2 even $\implies$ Drop.
- Row 3: ID 3 odd, description `'boring'` $\implies$ Drop.
- Row 4: ID 4 even $\implies$ Drop.
- Row 5: ID 5 odd, description `'Interesting'` $\implies \mathbf{Keep}$ ($rating = 9.1$).

---

### Step 2: Sort by `rating DESC`
- Rank 1: ID 5 ($rating = 9.1$).
- Rank 2: ID 1 ($rating = 8.9$).

---

### Step 3: Project Resulting Table
Emit columns `id, movie, description, rating`.

---

## 4. Complete Execution Trace

| `id` | `movie` | `id` is Odd? | Description $\ne$ `'boring'`? | Qualified? | `rating` | Sort Rank |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `War` | **Yes** | **Yes** | **Yes** | $8.9$ | $2$ |
| $2$ | `Science` | No | Yes | No | $8.5$ | — |
| $3$ | `irish` | **Yes** | No (Boring) | No | $6.2$ | — |
| $4$ | `Ice song` | No | Yes | No | $8.6$ | — |
| **$5$** | **`House card`** | **Yes** | **Yes** | **Yes** | **$9.1$** | **$1$ (Top)** |

---

## 5. Boundary Cases & Failure Modes

- **No Odd IDs with High Quality:** Returns empty result table with all four column headers.
- **All Descriptions "boring":** 0 rows pass $\implies$ empty table.
- **Rating Ties:** Preserves rating order.
- **Single Qualifying Movie:** Returns single row.

---

## 6. Traps & Common Anti-Patterns

- **Using `OR` Instead of `AND`:** Writing `WHERE id % 2 = 1 OR description != 'boring'` includes movies with even IDs as long as they are not boring, producing incorrect results.
- **Ascending Sort by Mistake:** Forgetting `DESC` outputs lowest rated movies first (`ORDER BY rating ASC`).
- **Missing Columns in Output:** Writing `SELECT movie` instead of `SELECT *` fails the required 4-column schema.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Filtering $N$ rows: $\mathcal{O}(N)$ sequential table scan.
  - Sorting $K$ qualified rows by rating: $\mathcal{O}(K \log K)$ where $K \le N$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space for sorting output rows.
