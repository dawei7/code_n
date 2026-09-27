# Guided Example: Duplicate Emails

We trace the step-by-step SQL aggregation, hash grouping, and `HAVING` group-cardinality filtering on representative user registration tables:

- **Input Table `Person`:**
  - `[(1, "a@b.com"), (2, "c@d.com"), (3, "a@b.com")]`
- **Required output:**
  - `{"columns": ["Email"], "rows": [["a@b.com"]]}` (`"a@b.com"` appears twice, exceeding the duplicate threshold count $> 1$)
- **All-Unique Emails Instance:** `Person = [(1, "a@x"), (2, "b@x")] \implies \text{Empty Set}` (All group counts $= 1$, rejected by `HAVING`)
- **Triplicate Email Instance:** `Person = [(1, "x@y"), (2, "x@y"), (3, "x@y")] \implies [["x@y"]]` (Emits exactly one row per duplicate email)

This instance demonstrates relational grouping semantics, clarifies the execution difference between row-filtering (`WHERE`) and post-aggregation filtering (`HAVING COUNT(email) > 1`), and runs in $O(N)$ linear time via hash-based aggregation.

---

## 1. Instance & Teaching Goal

Given the `Person` table:
$$
\begin{array}{|c|c|}
\hline
\textbf{id} & \textbf{email} \\
\hline
1 & \text{"a@b.com"} \\
2 & \text{"c@d.com"} \\
3 & \text{"a@b.com"} \\
\hline
\end{array}
$$
Find all email addresses that appear more than once in the table.

Counting occurrences:
- `"a@b.com"`: appears at ID 1 and ID 3 (count $= 2$).
- `"c@d.com"`: appears at ID 2 (count $= 1$).
Because $2 > 1$, `"a@b.com"` is a duplicate.
The output table must report a single column named `Email` containing `["a@b.com"]`.

---

## 2. Conceptual Foundation & Invariants

### Grouping and Cardinality Filtering
Relational aggregation partitions rows into equivalence classes based on attribute equality:
1. **Partitioning:** Group rows by the distinct value of `email`.
2. **Aggregation:** Compute the aggregate size $|\mathcal{G}|$ of each group using `COUNT(email)`.
3. **Filtering:** Retain only groups where $|\mathcal{G}| > 1$.

```sql
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
```

### Why `HAVING` Instead of `WHERE`
- The `WHERE` clause filters individual tuples **before** groups are formed. It cannot evaluate summary properties like `COUNT()`.
- The `HAVING` clause filters aggregated groups **after** the group partitions are formed.

### Alternative: Self-Join Formulation
```sql
SELECT DISTINCT p1.email AS Email
FROM Person p1
JOIN Person p2 
    ON p1.email = p2.email AND p1.id != p2.id;
```
While functional, the self-join approach generates $O(k^2)$ intermediate pairs for an email occurring $k$ times and requires an extra `DISTINCT` pass. `GROUP BY ... HAVING` performs the count in a single pass.

> **Invariant.** An email $e$ is emitted if and only if $|\{ p \in \text{Person} \mid p.\text{email} = e \}| \ge 2$. Each qualifying email is emitted exactly once.

---

## 3. Step-by-Step Worked Execution

We trace the relational group evaluation across `Person`:

### Step 1: Scan and Group by `email`
Partition rows by attribute `email`:
- **Group 1 (`email = "a@b.com"`):**
  - Row 1: `(id: 1, email: "a@b.com")`
  - Row 3: `(id: 3, email: "a@b.com")`
  - Members: $\{1, 3\}$.
- **Group 2 (`email = "c@d.com"`):**
  - Row 2: `(id: 2, email: "c@d.com")`
  - Members: $\{2\}$.

---

### Step 2: Compute Group Counts (`COUNT(email)`)
- For Group `"a@b.com"`:
  $$
  \text{count} = 2
  $$
- For Group `"c@d.com"`:
  $$
  \text{count} = 1
  $$

---

### Step 3: Evaluate `HAVING COUNT(email) > 1`
- **Group `"a@b.com"`:**
  $$
  2 > 1 \implies \mathbf{True} \quad (\text{Retained})
  $$
- **Group `"c@d.com"`:**
  $$
  1 > 1 \implies \mathbf{False} \quad (\text{Discarded})
  $$

---

### Step 4: Projection
- Project `email` as `Email`.
- Emitted output table: `[["a@b.com"]]`.

---

## 4. Complete Execution Trace

```text
Person Table:
id=1: a@b.com
id=2: c@d.com
id=3: a@b.com

Hash Grouping by email:
  Key "a@b.com" -> count = 2
  Key "c@d.com" -> count = 1

HAVING count > 1:
  "a@b.com": 2 > 1 -> TRUE  -> Emit "a@b.com"
  "c@d.com": 1 > 1 -> FALSE -> Discard

Result:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```

| Group Key (`email`) | Contributing IDs | Group Size $\text{COUNT}(*)$ | Filter Condition ($> 1$) | Emitted Output |
|:---|:---:|:---:|:---:|:---:|
| **`"a@b.com"`** | $\{1, 3\}$ | **2** | **$2 > 1$ (True)** | **`"a@b.com"`** |
| `"c@d.com"` | $\{2\}$ | 1 | $1 > 1$ (False) | Rejected |

---

## 5. Algorithmic Correctness

**Soundness.** Every group formed by `GROUP BY email` contains all rows sharing that specific email address. The condition `COUNT(email) > 1` holds if and only if that email was registered by at least two distinct entries.

**Completeness.** Since grouping partitions the entire table without dropping any row, every email in the dataset is represented by exactly one group. All duplicate emails are evaluated and emitted.

---

## 6. Traps This Instance Exposes

- **Attempting `WHERE COUNT(email) > 1`:** Aggregate functions cannot be used in a `WHERE` clause because grouping has not yet occurred at the time `WHERE` executes. `HAVING` must be used.
- **Missing Alias `Email`:** LeetCode requires the result column header to match `Email` with an uppercase `'E'`.
- **Triplicate Duplication:** If an email occurs 3 or 4 times, `GROUP BY` collapses them into one group and emits the email once. A self-join would emit $k(k-1)$ rows without `DISTINCT`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of rows in `Person`. The query engine builds a hash table on `email` in $O(N)$ time, then filters the groups in $O(U)$ time where $U \le N$ is the number of unique emails.
- **Auxiliary Space Complexity:** $O(U) \le O(N)$ memory to store the hash aggregation map.
