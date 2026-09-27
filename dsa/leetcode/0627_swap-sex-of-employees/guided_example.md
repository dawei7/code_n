# Guided Example: Swap Salary (Swap Sex of Employees)

We trace the step-by-step single-pass atomic mutation (`UPDATE`), conditional bit-flip assignment (`CASE WHEN sex = 'f' THEN 'm' ELSE 'f' END`), intermediate table avoidance, row-level transaction isolation, and binary attribute inversion on representative corporate payroll tables:

- **Input:**
  - `Salary` table before update:
    | `id` | `name` | `sex` | `salary` |
    |:---:|:---:|:---:|:---:|
    | $1$ | `A` | `m` | $2500$ |
    | $2$ | `B` | `f` | $1500$ |
    | $3$ | `C` | `m` | $5500$ |
    | $4$ | `D` | `f` | $500$ |
- **Required output:**
  - `Salary` table after update:
    | `id` | `name` | `sex` | `salary` |
    |:---:|:---:|:---:|:---:|
    | $1$ | `A` | `f` | $2500$ |
    | $2$ | `B` | `m` | $1500$ |
    | $3$ | `C` | `f` | $5500$ |
    | $4$ | `D` | `m` | $500$ |
  - Problem constraints:
    1. Invert every `'m'` to `'f'`, and every `'f'` to `'m'`.
    2. Must be accomplished using a **single `UPDATE` statement**.
    3. Do not use intermediate temporary tables or secondary `SELECT` statements.
- **The Binary Inversion Dilemma & Atomic Conditional Updates:**
  - If we ran two naive sequential updates:
    ```sql
    -- DANGEROUS / INCORRECT NAIVE APPROACH:
    UPDATE Salary SET sex = 'm' WHERE sex = 'f';
    UPDATE Salary SET sex = 'f' WHERE sex = 'm';
    ```
    - The first statement converts all `'f'`s to `'m'`s.
    - The second statement immediately converts **all** records (including the newly created `'m'`s) to `'f'`, destroying the original data!
  - **The Atomic Conditional Expression Solution:**
    - SQL's `UPDATE ... SET sex = CASE ... END` evaluates the target expression row-by-row on the **current pre-update snapshot** of each row:
      $$
      sex_{new} = \begin{cases} \text{'m'} & \text{if } sex_{old} = \text{'f'} \\ \text{'f'} & \text{if } sex_{old} = \text{'m'} \end{cases}
      $$
    - Because the assignment is evaluated in a single atomic database statement, neither value overwrites the other during the transition.
- **Step-by-Step Row Mutation Trace:**
  - **Row 1 (`id = 1, sex = 'm'`):**
    - Evaluate `CASE WHEN sex = 'f' THEN 'm' ELSE 'f' END`.
    - $sex = \text{'m'} \ne \text{'f'} \implies$ Branch falls to `ELSE`.
    - New value assigned:
      $$
      sex \leftarrow \mathbf{\text{'f'}}
      $$
  - **Row 2 (`id = 2, sex = 'f'`):**
    - Evaluate conditional test: $sex == \text{'f'} \implies \mathbf{True}$.
    - Branch returns `'m'`.
    - New value assigned:
      $$
      sex \leftarrow \mathbf{\text{'m'}}
      $$
  - **Row 3 (`id = 3, sex = 'm'`):**
    - $sex == \text{'m'} \implies$ Falls to `ELSE`.
    - New value assigned:
      $$
      sex \leftarrow \mathbf{\text{'f'}}
      $$
  - **Row 4 (`id = 4, sex = 'f'`):**
    - $sex == \text{'f'} \implies$ Returns `'m'`.
    - New value assigned:
      $$
      sex \leftarrow \mathbf{\text{'m'}}
      $$
  - Transaction commits!
  - All values are perfectly inverted in place without intermediate storage.
- **ASCII Arithmetic Alternative:**
  - In ASCII, the characters `'f'` (102) and `'m'` (109) sum to $102 + 109 = 211$.
  - Assigning `CHR(211 - ASCII(sex))` algebraically maps $102 \leftrightarrow 109$.
  - The `CASE` statement is standard, portable, and self-documenting.

This instance demonstrates atomic in-place record mutation via conditional relational assignments, mathematically proves why single-statement evaluation avoids destructive cascading overwrites, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a `Salary` table with a column `sex` containing `'m'` or `'f'`:
Invert all `'m'` values to `'f'`, and all `'f'` values to `'m'`.
Perform the change in a **single `UPDATE` statement** without temporary tables.

```text
Before:
  id 1: m
  id 2: f
  id 3: m
  id 4: f

After single UPDATE:
  id 1: f
  id 2: m
  id 3: f
  id 4: m
```

### The Invariant of Atomic Conditional Assignment
- You cannot perform two sequential updates without an intermediate holding state, because the second update will overwrite the results of the first update.
- The `CASE` expression allows the database engine to assign the complementary value row by row in a single atomic transition.

---

## 2. Conceptual Foundation & Invariants

### 1. The Single Update Statement:
```sql
UPDATE Salary
SET sex = (CASE WHEN sex = 'f' THEN 'm' ELSE 'f' END);
```

### 2. Idempotent Double-Inversion Property:
Applying this operation twice returns the table to its exact initial state:
$$
f(f(x)) = x \quad \forall x \in \{\text{'m'}, \text{'f'}\}
$$

> **Atomic Substitution Invariant.** In SQL transactions, update expressions evaluate against the pre-image state of the row, preventing concurrent intra-statement interference.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Execute UPDATE on Row 1
- Initial: `sex = 'm'`.
- `sex = 'f'` is False $\implies$ assigned `'f'`.

---

### Step 2: Execute UPDATE on Row 2
- Initial: `sex = 'f'`.
- `sex = 'f'` is True $\implies$ assigned `'m'`.

---

### Step 3: Execute UPDATE on Row 3
- Initial: `sex = 'm'`.
- Assigned `'f'`.

---

### Step 4: Execute UPDATE on Row 4
- Initial: `sex = 'f'`.
- Assigned `'m'`.

---

## 4. Complete Execution Trace

| Row `id` | Original `sex` | `sex = 'f'` Test | Selected Branch | Final Mutated `sex` |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | `'m'` | False | `ELSE 'f'` | **`'f'`** |
| $2$ | `'f'` | **True** | `THEN 'm'` | **`'m'`** |
| $3$ | `'m'` | False | `ELSE 'f'` | **`'f'`** |
| $4$ | `'f'` | **True** | `THEN 'm'` | **`'m'`** |

---

## 5. Boundary Cases & Failure Modes

- **All Records are `'m'`:** All become `'f'`.
- **All Records are `'f'`:** All become `'m'`.
- **Single Row in Table:** Inverts cleanly.
- **Large Dataset ($10^6$ rows):** Updated via a single clustered index sweep without locking deadlocks.

---

## 6. Traps & Common Anti-Patterns

- **Writing a `SELECT` Statement:** The problem explicitly demands an `UPDATE` statement; returning a `SELECT` fails automated validation.
- **Using Two Sequential UPDATE Queries:** Running two statements (`UPDATE ... SET sex = 'm' WHERE sex = 'f'` followed by `UPDATE ... SET sex = 'f' WHERE sex = 'm'`) overwrites everything with `'f'`.
- **Using Temporary Values (e.g. `'x'`):** Using a 3-step temporary transition (`'f' -> 'x', 'm' -> 'f', 'x' -> 'm'`) violates the single update statement rule.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single sequential table scan over $N$ rows: $\mathcal{O}(N)$ operations.
  - Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary memory (in-place modification).
