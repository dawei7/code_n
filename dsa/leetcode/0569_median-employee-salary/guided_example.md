# Guided Example: Median Employee Salary

We trace the step-by-step company partition ranking (`ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary ASC)`), group cardinality aggregation (`COUNT(id) OVER (PARTITION BY company)`), parity-unified median index interval formulation ($rk \ge n/2 \land rk \le n/2 + 1$), and individual median record filtering on representative employee salary tables:

- **Input:**
  - `Employee` table:
    | `id` | `company` | `salary` |
    |:---:|:---:|:---:|
    | $1$ | `A` | $2341$ |
    | $2$ | `A` | $341$ |
    | $3$ | `A` | $15$ |
    | $4$ | `A` | $15314$ |
    | $5$ | `A` | $451$ |
    | $6$ | `A` | $513$ |
    | $7$ | `B` | $15$ |
    | $8$ | `B` | $13$ |
    | $9$ | `B` | $1154$ |
    | $10$ | `B` | $1345$ |
    | $11$ | `B` | $1221$ |
    | $12$ | `B` | $234$ |
    | $13$ | `C` | $2345$ |
    | $14$ | `C` | $2645$ |
    | $15$ | `C` | $2645$ |
    | $16$ | `C` | $2652$ |
    | $17$ | `C` | $65$ |
- **Required output:**
  - All employee rows whose salaries represent the median within their respective company:
    - For even group size $n$: Exactly two median rows (ranks $n/2$ and $n/2 + 1$).
    - For odd group size $n$: Exactly one median row (rank $(n + 1)/2$).
- **Relational Partition & Parity Trace:**
  - **Company A ($n = 6$ employees, Even size):**
    - Sort employees of Company A in ascending order of salary:
      1. `id = 3`: salary $15$ $\to rank = 1$
      2. `id = 2`: salary $341$ $\to rank = 2$
      3. `id = 5`: salary $451$ $\to rank = \mathbf{3}$
      4. `id = 6`: salary $513$ $\to rank = \mathbf{4}$
      5. `id = 1`: salary $2341$ $\to rank = 5$
      6. `id = 4`: salary $15314$ $\to rank = 6$
    - Group size: $n = 6$.
    - Parity median condition:
      $$
      rk \ge \frac{6}{2} = 3 \quad \land \quad rk \le \frac{6}{2} + 1 = 4
      $$
    - Qualifies ranks $3$ and $4$:
      - `(5, 'A', 451)`
      - `(6, 'A', 513)`
  - **Company B ($n = 6$ employees, Even size):**
    - Sorted salaries: $13$ ($rk=1$), $15$ ($rk=2$), $234$ ($rk=\mathbf{3}$), $1154$ ($rk=\mathbf{4}$), $1221$ ($rk=5$), $1345$ ($rk=6$).
    - Median ranks $3$ and $4$:
      - `id = 12`: salary $234$
      - `id = 9`: salary $1154$
  - **Company C ($n = 5$ employees, Odd size):**
    - Sorted salaries:
      1. `id = 17`: salary $65$ $\to rank = 1$
      2. `id = 13`: salary $2345$ $\to rank = 2$
      3. `id = 14`: salary $2645$ $\to rank = \mathbf{3}$
      4. `id = 15`: salary $2645$ $\to rank = 4$
      5. `id = 16`: salary $2652$ $\to rank = 5$
    - Group size: $n = 5$.
    - Parity median condition:
      $$
      rk \ge \frac{5}{2} = 2.5 \quad \land \quad rk \le \frac{5}{2} + 1 = 3.5
      $$
    - The only integer rank in range $[2.5, 3.5]$ is $rk = \mathbf{3}$!
    - Qualifies rank $3$:
      - `(14, 'C', 2645)`
  - **Consolidated Output Table:**
    | `id` | `company` | `salary` |
    |:---:|:---:|:---:|
    | $5$ | `A` | $451$ |
    | $6$ | `A` | $513$ |
    | $12$ | `B` | $234$ |
    | $9$ | `B` | $1154$ |
    | $14$ | `C` | $2645$ |
- **Single Employee Company ($n = 1$):**
  - $rk \in [0.5, 1.5] \implies rk = 1$ (the single employee).
- **Two Employee Company ($n = 2$):**
  - $rk \in [1, 2] \implies$ both employees are returned.

This instance demonstrates partitioned window ranking in relational databases, mathematically proves why the unified interval condition $rk \in [n/2, n/2 + 1]$ cleanly resolves both odd and even parity medians, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the `Employee` table with `id`, `company`, and `salary`:
Find the **median salary** for each company.
If a company has an odd number of employees, return the single middle employee.
If a company has an even number of employees, return the two middle employees.

```text
Company A Salaries (Sorted):
  Rank 1: 15
  Rank 2: 341
  Rank 3: 451   <-- Median (1st of 2)
  Rank 4: 513   <-- Median (2nd of 2)
  Rank 5: 2341
  Rank 6: 15314

Company C Salaries (Sorted):
  Rank 1: 65
  Rank 2: 2345
  Rank 3: 2645  <-- Single Median
  Rank 4: 2645
  Rank 5: 2652
```

### The Parity-Unified Rank Inequality
- For group size $n$:
  - When $n$ is even (e.g. $n = 6$):
    - Middle ranks are $n / 2 = 3$ and $n / 2 + 1 = 4$.
  - When $n$ is odd (e.g. $n = 5$):
    - Exact middle rank is $(n + 1) / 2 = 3$.
- In continuous arithmetic:
  $$
  rk \in \left[ \frac{n}{2}, \; \frac{n}{2} + 1 \right]
  $$
  - If $n = 6$: interval is $[3, 4]$, capturing integers $\{3, 4\}$.
  - If $n = 5$: interval is $[2.5, 3.5]$, capturing only integer $\{3\}$.
- A single inequality handles both odd and even cases simultaneously!

---

## 2. Conceptual Foundation & Invariants

### 1. Window Functions:
In Common Table Expression (CTE) `t`:
1. `ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary ASC) AS rk`
   Assigns a unique 1-based sequential rank to each employee within their company.
2. `COUNT(id) OVER (PARTITION BY company) AS n`
   Computes the total number of employees in that company.

### 2. Filter Predicate:
$$
\text{WHERE } rk \ge \frac{n}{2} \quad \text{AND} \quad rk \le \frac{n}{2} + 1
$$

> **Distribution Invariant.** Sorting by salary within each company partition ensures that the elements at median ranks divide the lower and upper halves of the company's salary distribution symmetrically.

---

## 3. Step-by-Step Worked Execution

We trace Company A ($n = 6$) and Company C ($n = 5$):

---

### Step 1: Assign Ranks in Company A
- Salaries: $15, 341, 451, 513, 2341, 15314$.
- Ranks: $1, 2, 3, 4, 5, 6$. Total $n = 6$.
- Filter range: $[6 / 2, 6 / 2 + 1] = [3, 4]$.
- Selected ranks:
  - Rank 3: id 5, salary $451$.
  - Rank 4: id 6, salary $513$.

---

### Step 2: Assign Ranks in Company C
- Salaries: $65, 2345, 2645, 2645, 2652$.
- Ranks: $1, 2, 3, 4, 5$. Total $n = 5$.
- Filter range: $[5 / 2, 5 / 2 + 1] = [2.5, 3.5]$.
- Selected rank:
  - Rank 3: id 14, salary $2645$.

---

### Step 3: Combine Results
The query projects `id`, `company`, `salary` for all qualified rows across all companies.

---

## 4. Complete Execution Trace

| `company` | Count $n$ | Target Rank Range $[n/2, n/2 + 1]$ | Qualified Ranks | Output Rows |
|:---:|:---:|:---:|:---:|:---:|
| **`A`** | $6$ | $[3, 4]$ | $3, 4$ | `(5, 'A', 451)`, `(6, 'A', 513)` |
| **`B`** | $6$ | $[3, 4]$ | $3, 4$ | `(12, 'B', 234)`, `(9, 'B', 1154)` |
| **`C`** | $5$ | $[2.5, 3.5]$ | $3$ | `(14, 'C', 2645)` |

---

## 5. Boundary Cases & Failure Modes

- **Tied Salaries:** `ROW_NUMBER()` assigns distinct consecutive integers (e.g. ranks 3 and 4) even if two employees have the exact same salary, guaranteeing the median count is strictly preserved.
- **$n = 1$:** $[0.5, 1.5] \implies$ rank 1 chosen.
- **$n = 2$:** $[1, 2] \implies$ ranks 1 and 2 chosen.
- **Multiple Companies with Variable Sizes:** The `PARTITION BY company` clause isolates each company's calculation independently.

---

## 6. Traps & Common Anti-Patterns

- **Using `DENSE_RANK()` or `RANK()` Instead of `ROW_NUMBER()`:** Tied salaries with `RANK()` skip numbers (e.g. $1, 2, 2, 4$), which causes the filter to miss median ranks or return too many rows. `ROW_NUMBER()` guarantees contiguous integer ranks.
- **Averaging Median Values in SQL:** The problem requires returning the **original employee records** that form the median, not computing a single averaged scalar number.
- **Using Cross Joins for Counting:** Running subquery self-joins to count smaller elements takes $O(N^2)$ time. Window functions `ROW_NUMBER()` and `COUNT()` run in $O(N \log N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Partitioning and sorting by `company` and `salary`: $\mathcal{O}(N \log N)$.
  - Assigning window ranks and filtering takes $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to materialize the CTE intermediate table.
