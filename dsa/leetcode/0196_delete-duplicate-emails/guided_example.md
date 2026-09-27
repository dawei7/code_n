# Guided Example: Delete Duplicate Emails

We trace the step-by-step SQL destructive record deletion, relational self-join cross-comparison, and MySQL Error 1093 subquery materialization on representative user tables:

- **Input Table `Person`:**
  ```text
  +----+------------------+
  | id | email            |
  +----+------------------+
  | 1  | john@example.com |
  | 2  | bob@example.com  |
  | 3  | john@example.com |
  +----+------------------+
  ```
- **Required Post-Deletion Table State:**
  ```text
  +----+------------------+
  | id | email            |
  +----+------------------+
  | 1  | john@example.com |
  | 2  | bob@example.com  |
  +----+------------------+
  ```
- **Three Duplicates Instance:** `[(1, "a@x.com"), (2, "a@x.com"), (3, "a@x.com")] \implies` Deletes rows 2 and 3, preserving row 1.
- **No Duplicates Instance:** `[(1, "a@x.com"), (2, "b@x.com")] \implies` Deletes 0 rows.

This instance demonstrates destructive data manipulation (`DELETE`), contrasts multi-table self-joins (`p1.id > p2.id`) with keeper subqueries (`id NOT IN (SELECT MIN(id) ...)`), explains MySQL Error 1093 target-table locking rules, and executes in $O(N)$ expected time.

---

## 1. Instance & Teaching Goal

Given a database table `Person`:
$$
\begin{array}{|c|c|}
\hline
\textbf{id} & \textbf{email} \\
\hline
1 & \text{john@example.com} \\
2 & \text{bob@example.com} \\
3 & \text{john@example.com} \\
\hline
\end{array}
$$
Write an in-place **`DELETE` statement** that removes all duplicate email entries, preserving strictly the single row with the **smallest `id`** for each unique email address.

Analyzing the table rows:
- `john@example.com` appears in row $1$ and row $3$. Since $\min(1, 3) = 1$, row $3$ must be deleted and row $1$ retained.
- `bob@example.com` appears only in row $2$. Since it has no duplicates, row $2$ is retained.

The query must execute a destructive modification (`DELETE`), not a read-only projection (`SELECT`).

---

## 2. Conceptual Foundation & Invariants

### Method A: Relational Self-Join `DELETE` (Idiomatic MySQL)
```sql
DELETE p1 
FROM Person p1, Person p2
WHERE p1.email = p2.email 
  AND p1.id > p2.id;
```

#### How the Self-Join Identifies Removable Rows:
1. Join relation `Person p1` with `Person p2` on equal email addresses: $p_1.\text{email} = p_2.\text{email}$.
2. If there exists any other record $p_2$ sharing the same email such that $p_1.\text{id} > p_2.\text{id}$, then $p_1$ is **not** the record with the minimum ID for that email.
3. Therefore, deleting $p_1$ removes all rows with duplicate emails except the single record with the strictly smallest `id`!

### Method B: Grouped Minimum Subquery with Derived Table
```sql
DELETE FROM Person
WHERE id NOT IN (
    SELECT min_id FROM (
        SELECT MIN(id) AS min_id
        FROM Person
        GROUP BY email
    ) temp
);
```

#### The MySQL Error 1093 Workaround:
In standard MySQL, executing:
```sql
DELETE FROM Person WHERE id NOT IN (SELECT MIN(id) FROM Person GROUP BY email);
```
triggers `ERROR 1093 (HY000): You can't specify target table 'Person' for update in FROM clause`.
MySQL prohibits modifying a table while simultaneously reading from it in an un-materialized subquery. Wrapping the subquery in `(SELECT MIN(id) ... ) temp` forces MySQL to materialize the results into an in-memory temporary table before executing the delete.

> **Invariant.** A row $p_1$ is deleted if and only if there exists another row $p_2$ in `Person` such that $p_1.\text{email} = p_2.\text{email}$ and $p_1.\text{id} > p_2.\text{id}$.

---

## 3. Step-by-Step Worked Execution

We trace the Self-Join `DELETE` evaluation across `Person`:

### Step 1: Form Cross Pairs on Equal Email
Evaluate all pairs $(p_1, p_2)$ with $p_1.\text{email} = p_2.\text{email}$:
- Pair $(1, 1)$: `email = john@example.com`, $p_1.\text{id} = 1, p_2.\text{id} = 1$.
- Pair $(1, 3)$: `email = john@example.com`, $p_1.\text{id} = 1, p_2.\text{id} = 3$.
- Pair $(2, 2)$: `email = bob@example.com`, $p_1.\text{id} = 2, p_2.\text{id} = 2$.
- Pair $(3, 1)$: `email = john@example.com`, $p_1.\text{id} = 3, p_2.\text{id} = 1$.
- Pair $(3, 3)$: `email = john@example.com`, $p_1.\text{id} = 3, p_2.\text{id} = 3$.

---

### Step 2: Test Condition $p_1.\text{id} > p_2.\text{id}$
- Pair $(1, 1)$: $1 > 1 \implies \text{False}$.
- Pair $(1, 3)$: $1 > 3 \implies \text{False}$.
- Pair $(2, 2)$: $2 > 2 \implies \text{False}$.
- **Pair $(3, 1)$:** $3 > 1 \implies \mathbf{\text{True}!}$
  - Target for deletion: $p_1$ (row $3$ with ID $3$).
- Pair $(3, 3)$: $3 > 3 \implies \text{False}$.

---

### Step 3: Execute Deletion
- Row $3$ matches the condition ($3 > 1$).
- Row $3$ is deleted from `Person`.
- Rows $1$ and $2$ have no matching $p_2$ with a smaller ID; both survive intact.

Final table state:
```text
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```

---

## 4. Complete Execution Trace

```text
Person Table:
Row 1: (id: 1, john@example.com)
Row 2: (id: 2, bob@example.com)
Row 3: (id: 3, john@example.com)

Self-Join Comparison (p1 vs p2):
  p1 = Row 1 (id: 1) vs p2 = Row 3 (id: 3):  1 > 3 is False -> KEEP Row 1
  p1 = Row 2 (id: 2) vs p2 = Row 2 (id: 2):  2 > 2 is False -> KEEP Row 2
  p1 = Row 3 (id: 3) vs p2 = Row 1 (id: 1):  3 > 1 is TRUE  -> DELETE Row 3

Final Person Table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```

| $p_1.\text{id}$ | $p_1.\text{email}$ | Matched $p_2.\text{id}$ | Condition $p_1.\text{id} > p_2.\text{id}$ | Evaluation Result | Mutation Applied |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | `john@example.com` | 1 | $1 > 1$ | `False` | Preserved |
| 1 | `john@example.com` | 3 | $1 > 3$ | `False` | Preserved |
| 2 | `bob@example.com` | 2 | $2 > 2$ | `False` | Preserved |
| **3** | **`john@example.com`** | **1** | **$3 > 1$** | **`True`** | **DELETED** |
| 3 | `john@example.com` | 3 | $3 > 3$ | `False` | Already marked |

---

## 5. Algorithmic Correctness

**Soundness.** In any set of rows sharing an email address, there is exactly one element with the minimum ID: $m = \min \{ \text{id} \}$. For this row, no row exists with the same email and a smaller ID, so $m > p_2.\text{id}$ is never true and row $m$ cannot be deleted. For every other duplicate row $d$ in the group, $d > m$ is strictly true when compared against row $m$, guaranteeing that every duplicate row is deleted.

**Completeness.** Self-joins examine all pairs of records. Every duplicate row with an ID greater than the group minimum is matched and deleted.

---

## 6. Traps This Instance Exposes

- **Writing a `SELECT` Query:** The problem specifically mandates an in-place `DELETE` statement. Returning rows via `SELECT` fails judge validation.
- **MySQL Error 1093:** Subqueries deleting directly with `WHERE id NOT IN (SELECT MIN(id) FROM Person ...)` crash on MySQL unless wrapped in an intermediate derived table `(SELECT ... ) temp`.
- **Direction of Inequality:** Writing `p1.id < p2.id` deletes the row with the *smallest* ID and keeps the largest ID! The required condition is strictly `p1.id > p2.id` to delete the larger IDs.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ with an index on `email`, where $N$ is the number of rows in `Person`. Without an index, the self-join performs an $O(N^2)$ nested loop or an $O(N \log N)$ sort-merge join.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space for in-place self-join deletion; $O(U)$ memory if materializing a keeper table with $U$ unique emails.
