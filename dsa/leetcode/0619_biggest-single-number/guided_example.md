# Guided Example: Biggest Single Number

We trace the step-by-step element frequency histogram aggregation (`GROUP BY num`), strict singleton filter isolation (`HAVING COUNT(1) = 1`), scalar supremum extraction (`MAX(num)`), empty relation null-fallback propagation, and unique maximum reporting on representative integer multiset tables:

- **Input:**
  - `MyNumbers` table:
    | `num` |
    |:---:|
    | $8$ |
    | $8$ |
    | $3$ |
    | $3$ |
    | $1$ |
    | $4$ |
    | $5$ |
    | $6$ |
- **Required output:**
  | `num` |
  |:---:|
  | $6$ |
  - Problem definitions:
    - A **single number** is an integer that appears **exactly once** in the table ($\text{frequency} = 1$).
    - Any number appearing 2 or more times is disqualified.
    - Objective: Report the **largest** among all single numbers.
    - If no single number exists, return `null`.
- **Relational Aggregation & Null Propagation Architecture:**
  - **Phase 1: Filter for Singletons in Subquery `t`:**
    - Group by the value `num`.
    - Apply `HAVING COUNT(1) = 1` to retain only numbers with multiplicity 1:
      $$
      t = \{x \mid x \in \text{MyNumbers}, \; \text{count}(x) = 1\}
      $$
  - **Phase 2: Extract Scalar Maximum with `MAX(num)`:**
    - By wrapping the subquery in `SELECT MAX(num) FROM (...)`:
      - If $t$ contains values, `MAX(num)` returns the largest value.
      - If $t$ is empty (all numbers were duplicates), `MAX()` on an empty set in SQL naturally evaluates to **`null`** without crashing or returning an empty row!
- **Step-by-Step Worked Execution Trace:**
  - Given multiset: $[8, 8, 3, 3, 1, 4, 5, 6]$.
  - **Step 1: Group and Count Multiplicities:**
    - Value $8$: occurs at indices 0 and 1 $\implies \text{count} = \mathbf{2}$ (Duplicate).
    - Value $3$: occurs at indices 2 and 3 $\implies \text{count} = \mathbf{2}$ (Duplicate).
    - Value $1$: occurs at index 4 $\implies \text{count} = \mathbf{1}$ (Single!).
    - Value $4$: occurs at index 5 $\implies \text{count} = \mathbf{1}$ (Single!).
    - Value $5$: occurs at index 6 $\implies \text{count} = \mathbf{1}$ (Single!).
    - Value $6$: occurs at index 7 $\implies \text{count} = \mathbf{1}$ (Single!).
  - **Step 2: Filter via `HAVING COUNT(1) = 1`:**
    - Intermediate relation $t$ contains:
      $$
      t = [1, \; 4, \; 5, \; 6]
      $$
    - Notice: Although $8$ is the largest number in the raw table, it is completely excluded because its frequency is $2$!
  - **Step 3: Compute Supremum (`MAX`):**
    - Inspect values in $t$:
      $$
      \max(1, 4, 5, 6) = \mathbf{6}
      $$
    - Emit final scalar:
      $$
      num: \mathbf{6}
      $$
- **All Elements Duplicate Instance ($MyNumbers = [8, 8, 7, 7, 3, 3]$):**
  - Counts: $8 \to 2, \; 7 \to 2, \; 3 \to 2$.
  - Subquery $t$ filters out all values $\implies t = \emptyset$.
  - Outer query evaluates `SELECT MAX(num) FROM empty_set`:
    $$
    num: \mathbf{null}
    $$
- **Table with Single Unique Entry ($MyNumbers = [5]$):**
  - Count is $1 \implies t = [5] \implies$ returns $5$.

This instance demonstrates grouped cardinality filtering and aggregation-based null coalescing in relational databases, mathematically proves why singleton set maximization excludes dominant multi-occurrence values, and derives $O(N)$ execution time and $O(U)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `MyNumbers` table of integers with possible duplicates:
Find the **largest single number** (a number that appears exactly once).
If no such number exists, return `null`.

```text
Numbers: [ 8, 8, 3, 3, 1, 4, 5, 6 ]

Frequencies:
  8: 2 (Duplicate, Disqualified!)
  3: 2 (Duplicate, Disqualified!)
  1: 1 (Single)
  4: 1 (Single)
  5: 1 (Single)
  6: 1 (Single)

Single Numbers: [ 1, 4, 5, 6 ]
Largest Single Number = 6
```

### The Null Propagation Pattern
- If you use `ORDER BY num DESC LIMIT 1` on the filtered subquery, an empty result set returns **zero rows** instead of a single row containing `null`.
- Applying the aggregate function `MAX(num)` on the subquery guarantees that an empty input produces a valid single-cell row with value `null`.

---

## 2. Conceptual Foundation & Invariants

### 1. The Two-Stage Query:
```sql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(1) = 1
) AS t;
```

### 2. Multiplicity Invariant:
$$
t = \{x \in \text{MyNumbers} \mid \text{multiplicity}(x) = 1\}
$$
$$
\text{Answer} = \sup(t) \quad (\text{with } \sup(\emptyset) = \text{null})
$$

> **Aggregate Null Invariant.** In SQL standard semantics, the scalar aggregation of an empty relation $\text{MAX}(\emptyset)$ evaluates to `NULL`, providing automatic fallback without conditional branching.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Group and Filter Singletons
- Value 8: count 2 $\implies$ drop.
- Value 3: count 2 $\implies$ drop.
- Value 1: count 1 $\implies$ keep.
- Value 4: count 1 $\implies$ keep.
- Value 5: count 1 $\implies$ keep.
- Value 6: count 1 $\implies$ keep.
- Singleton set: $\{1, 4, 5, 6\}$.

---

### Step 2: Extract Maximum
$$
\max(1, 4, 5, 6) = \mathbf{6}
$$

---

### Step 3: Emit Output
$$
\mathbf{6}
$$

---

## 4. Complete Execution Trace

| Number $x$ | Total Multiplicity | $\text{count} = 1$? | In Subquery $t$? | Evaluated in `MAX()`? |
|:---:|:---:|:---:|:---:|:---:|
| $8$ | $2$ | No | No | No |
| $3$ | $2$ | No | No | No |
| $1$ | $1$ | **Yes** | **Yes** | Yes |
| $4$ | $1$ | **Yes** | **Yes** | Yes |
| $5$ | $1$ | **Yes** | **Yes** | Yes |
| **$6$** | **$1$** | **Yes** | **Yes** | **Yes (Max)** |
| **Output** | — | — | — | **`num: 6`** |

---

## 5. Boundary Cases & Failure Modes

- **No Single Numbers Present:** Evaluates `MAX(empty)` $\implies$ returns `null`.
- **Empty Table:** Evaluates `MAX(empty)` $\implies$ returns `null`.
- **Negative Numbers ($-5, -5, -2, -1$):** $-2$ and $-1$ are singles $\implies \max(-2, -1) = -1$.
- **Zero ($0$):** Zero is a valid number and returns `0` if single.

---

## 6. Traps & Common Anti-Patterns

- **Using `LIMIT 1` Without Outer `MAX()`:** Writing `SELECT num FROM ... HAVING count(1) = 1 ORDER BY num DESC LIMIT 1` returns an empty table (0 rows) when there are no singles. The problem requires returning a row with `null`.
- **Allowing Multiplicity > 1:** Filtering with `HAVING COUNT(1) >= 1` includes duplicates, erroneously returning the global maximum (8 in our sample).
- **Misnaming Output Column:** Must be named `num`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Hash aggregation on $N$ rows in `MyNumbers`: $\mathcal{O}(N)$ time.
  - Sifting $U$ unique values with `HAVING`: $\mathcal{O}(U)$ where $U \le N$.
  - Outer `MAX()` over singletons: $\mathcal{O}(S)$ where $S \le U$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U)$ space to store the hash group counters.
