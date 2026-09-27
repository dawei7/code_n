# Guided Example: Big Countries

We trace the step-by-step disjunctive predicate evaluation (`area >= 3000000 OR population >= 25000000`), inclusive boundary threshold validation, relational projection (`name`, `population`, `area`), index union filtering, and qualification classification on representative geographical demographic tables:

- **Input:**
  - `World` table:
    | `name` | `continent` | `area` | `population` | `gdp` |
    |:---:|:---:|:---:|:---:|:---:|
    | `Afghanistan` | `Asia` | $652230$ | $25500100$ | $20343000000$ |
    | `Albania` | `Europe` | $28748$ | $2831741$ | $12960000000$ |
    | `Algeria` | `Africa` | $2381741$ | $37100000$ | $188681000000$ |
    | `Andorra` | `Europe` | $468$ | $78115$ | $3712000000$ |
    | `Angola` | `Africa` | $1246700$ | $20609294$ | $100990000000$ |
- **Required output:**
  | `name` | `population` | `area` |
  |:---:|:---:|:---:|
  | `Afghanistan` | $25500100$ | $652230$ |
  | `Algeria` | $37100000$ | $2381741$ |
  - Business qualification rules: A country is classified as **big** if and only if it satisfies **at least one** of the following two thresholds:
    1. Geographic threshold: $\text{area} \ge 3{,}000{,}000$
    2. Demographic threshold: $\text{population} \ge 25{,}000{,}000$
- **Disjunctive Predicate Evaluation Trace:**
  - Filter predicate:
    $$
    P(\text{row}) = (\text{area} \ge 3{,}000{,}000) \lor (\text{population} \ge 25{,}000{,}000)
    $$
  - **Row 1 (`Afghanistan`):**
    - Area test: $652230 \ge 3000000 \implies \mathbf{False}$
    - Population test: $25500100 \ge 25000000 \implies \mathbf{True}$
    - Combined test: $False \lor True = \mathbf{True}$
    - **Qualified!** Project `('Afghanistan', 25500100, 652230)`.
  - **Row 2 (`Albania`):**
    - Area test: $28748 \ge 3000000 \implies \mathbf{False}$
    - Population test: $2831741 \ge 25000000 \implies \mathbf{False}$
    - Combined test: $False \lor False = \mathbf{False}$
    - Disqualified.
  - **Row 3 (`Algeria`):**
    - Area test: $2381741 \ge 3000000 \implies \mathbf{False}$
    - Population test: $37100000 \ge 25000000 \implies \mathbf{True}$
    - Combined test: $False \lor True = \mathbf{True}$
    - **Qualified!** Project `('Algeria', 37100000, 2381741)`.
  - **Row 4 (`Andorra`):**
    - Area: $468 < 3000000$, Pop: $78115 < 25000000 \implies \mathbf{False}$.
    - Disqualified.
  - **Row 5 (`Angola`):**
    - Area: $1246700 < 3000000$, Pop: $20609294 < 25000000 \implies \mathbf{False}$.
    - Disqualified.
- **Exact Boundary Inclusion Instance:**
  - Suppose a country has $\text{area} = 3{,}000{,}000$ and $\text{population} = 1$.
  - The inequality is inclusive ($\ge$): $3000000 \ge 3000000 \implies \mathbf{True}$ (Qualifies).
  - A country with $\text{area} = 2{,}999{,}999$ and $\text{population} = 24{,}999{,}999$ is strictly below both thresholds $\implies \mathbf{False}$ (Disqualified).
- **Dual Qualification:**
  - A country exceeding both thresholds (e.g. Russia, USA) satisfies $True \lor True = \mathbf{True}$ without row duplication.

This instance demonstrates relational selection via disjunctive Boolean predicates, mathematically proves why inclusive inequalities enforce boundary retention, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a `World` table with country statistics:
Identify all **big countries** that satisfy either:
1. `area >= 3,000,000` km$^2$, OR
2. `population >= 25,000,000`.
Return their `name`, `population`, and `area` in any order.

```text
Conditions:
  Area >= 3,000,000  OR  Population >= 25,000,000

Evaluations:
  Afghanistan: Pop = 25,500,100 (>= 25M) -> BIG!
  Albania:     Area < 3M, Pop < 25M       -> Small
  Algeria:     Pop = 37,100,000 (>= 25M) -> BIG!
  Andorra:     Area < 3M, Pop < 25M       -> Small
  Angola:      Area < 3M, Pop < 25M       -> Small
```

### Relational Selection Logic
- The operation is a pure horizontal selection $\sigma_{P}(\text{World})$ followed by vertical projection $\pi_{name, population, area}$.
- The disjunctive condition $C_1 \lor C_2$ evaluates each tuple independently:
  - If $C_1$ is true, the tuple is accepted immediately (short-circuit).
  - Otherwise, $C_2$ is evaluated.

---

## 2. Conceptual Foundation & Invariants

### 1. The SQL Query:
```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
```

### 2. Alternative Union Form (Index-Friendly):
```sql
SELECT name, population, area FROM World WHERE area >= 3000000
UNION
SELECT name, population, area FROM World WHERE population >= 25000000;
```
- In database engines where separate B-tree indexes exist on `area` and `population`, a `UNION` query can utilize both indexes efficiently.

> **Inclusive Boundary Invariant.** Both criteria require $\ge$, meaning an area of exactly $3{,}000{,}000$ or a population of exactly $25{,}000{,}000$ qualifies as big.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Scan Table Rows
1. `Afghanistan`:
   - $area = 652230 < 3000000$
   - $pop = 25500100 \ge 25000000 \implies \mathbf{True}$.
2. `Albania`:
   - $area = 28748 < 3000000$
   - $pop = 2831741 < 25000000 \implies \mathbf{False}$.
3. `Algeria`:
   - $area = 2381741 < 3000000$
   - $pop = 37100000 \ge 25000000 \implies \mathbf{True}$.

---

### Step 2: Project Required Columns
- Include `name`, `population`, `area`:
  - `('Afghanistan', 25500100, 652230)`
  - `('Algeria', 37100000, 2381741)`

---

## 4. Complete Execution Trace

| `name` | `area` | `area >= 3M` | `population` | `pop >= 25M` | Big Country? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **`Afghanistan`** | $652230$ | No | $25500100$ | **Yes** | **Yes** |
| `Albania` | $28748$ | No | $2831741$ | No | No |
| **`Algeria`** | $2381741$ | No | $37100000$ | **Yes** | **Yes** |
| `Andorra` | $468$ | No | $78115$ | No | No |
| `Angola` | $1246700$ | No | $20609294$ | No | No |

---

## 5. Boundary Cases & Failure Modes

- **Exactly 3,000,000 Area:** Passes because the condition is inclusive $\ge$.
- **Exactly 25,000,000 Population:** Passes because the condition is inclusive $\ge$.
- **No Big Countries in Table:** Returns an empty table with columns `name, population, area`.
- **All Countries Big:** Returns all rows from the table.

---

## 6. Traps & Common Anti-Patterns

- **Using `AND` Instead of `OR`:** The problem requires meeting *either* the area condition *or* the population condition. Using `AND` checks for both, incorrectly excluding countries like Algeria.
- **Using Strict Greater-Than (`>`):** Using `area > 3000000` drops boundary countries with area exactly 3 million.
- **Projecting `*` (All Columns):** Returning extra columns (like `continent` or `gdp`) fails the schema requirement. Only project `name, population, area`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single sequential table scan evaluates the predicate in $\mathcal{O}(N)$ time.
  - Or with B-tree indexes on `area` and `population`, $\mathcal{O}(\log N + K)$ index range scan where $K$ is the number of big countries.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (streaming output pipeline).
