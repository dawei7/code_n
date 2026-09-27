# Guided Example: Consecutive Numbers

We trace the step-by-step SQL window consecutive evaluation via `LEAD()` lookahead and three-way self-join matching on representative database log tables:

- **Input Table `Logs`:**
  - `[(1, "1"), (2, "1"), (3, "1"), (4, "2"), (5, "1"), (6, "2"), (7, "2")]`
- **Required output:**
  - `{"columns": ["ConsecutiveNums"], "rows": [["1"]]}`
- **Insufficient Length Instance:** `Logs = [(1, "5"), (2, "5")] \implies \text{Empty Set}` (Only 2 occurrences, minimum required is 3)
- **Overlapping Triples Instance:** `Logs = [(1, "1"), (2, "1"), (3, "1"), (4, "1")] \implies [["1"]]` (`DISTINCT` collapses multiple overlapping windows)

This instance demonstrates identifying consecutive sequences using SQL window lookahead functions (`LEAD`), explains why `DISTINCT` is required to prevent duplicate emissions from extended runs ($\ge 4$ rows), handles non-adjacent recurrences of the same value, and analyzes query performance in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the `Logs` table:
$$
\begin{array}{|c|c|}
\hline
\textbf{id} & \textbf{num} \\
\hline
1 & \text{"1"} \\
2 & \text{"1"} \\
3 & \text{"1"} \\
4 & \text{"2"} \\
5 & \text{"1"} \\
6 & \text{"2"} \\
7 & \text{"2"} \\
\hline
\end{array}
$$
Find all numbers that appear **at least three times consecutively** in order of `id`.

In this table:
- Value `"1"` appears at IDs $1, 2, 3$ $\implies$ consecutive count is $3 \ge 3$. Valid!
- Value `"2"` appears at ID $4$ (count 1), and then at IDs $6, 7$ (count 2). Neither run reaches 3.
- Value `"1"` reappears at ID $5$, but it is isolated from the previous run by ID $4$.
The query must return a single unique column `ConsecutiveNums` containing `"1"`.

---

## 2. Conceptual Foundation & Invariants

### Method A: Window Lookahead `LEAD()` (Recommended & Gap-Tolerant)
```sql
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_1,
        LEAD(num, 2) OVER (ORDER BY id) AS next_2
    FROM Logs
) sub
WHERE num = next_1 AND num = next_2;
```

#### Why `LEAD()` Is Structurally Sound:
1. `ORDER BY id`: Orders log records chronologically.
2. `LEAD(num, 1)`: Peeks at the immediately following row's value.
3. `LEAD(num, 2)`: Peeks at the row two steps ahead.
4. Filter `num = next_1 AND num = next_2`: Identifies any row that initiates a consecutive run of length $\ge 3$.
5. Handles ID Gaps: Unlike arithmetic `id + 1 = next_id`, `LEAD` evaluates row ordering directly, remaining correct even if historical rows were deleted.

### Method B: Three-Way Self Join
```sql
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num
JOIN Logs l3 ON l2.id = l3.id - 1 AND l2.num = l3.num;
```
Matches contiguous ID triples $(i, i+1, i+2)$ where values are identical.

> **Invariant.** A row qualifies if and only if $\text{num}_{i} = \text{num}_{i+1} = \text{num}_{i+2}$. Wrapping with `DISTINCT` guarantees that runs of length $\ge 3$ emit each qualifying number exactly once.

---

## 3. Step-by-Step Worked Execution

We trace the rows in `Logs` using the lookahead window evaluation:

### Row 1: ID 1, `num = "1"`
- Next row (ID 2): $\text{next\_1} = \text{"1"}$.
- Next-next row (ID 3): $\text{next\_2} = \text{"1"}$.
- Evaluate condition:
  $$
  \text{"1"} == \text{"1"} \land \text{"1"} == \text{"1"} \implies \mathbf{True}
  $$
- Value `"1"` qualifies! Added to candidate set: `{"1"}`.

---

### Row 2: ID 2, `num = "1"`
- Next row (ID 3): $\text{next\_1} = \text{"1"}$.
- Next-next row (ID 4): $\text{next\_2} = \text{"2"}$.
- Evaluate condition:
  $$
  \text{"1"} == \text{"1"} \land \text{"1"} == \text{"2"} \implies \mathbf{False}
  $$

---

### Row 3: ID 3, `num = "1"`
- Next row (ID 4): $\text{next\_1} = \text{"2"}$.
- Next-next row (ID 5): $\text{next\_2} = \text{"1"}$.
- Condition: $\text{"1"} == \text{"2"} \implies \mathbf{False}$.

---

### Row 4: ID 4, `num = "2"`
- Next row (ID 5): $\text{next\_1} = \text{"1"}$.
- Condition: $\text{"2"} == \text{"1"} \implies \mathbf{False}$.

---

### Row 5: ID 5, `num = "1"`
- Next row (ID 6): $\text{next\_1} = \text{"2"}$.
- Condition: $\text{"1"} == \text{"2"} \implies \mathbf{False}$.

---

### Row 6: ID 6, `num = "2"`
- Next row (ID 7): $\text{next\_1} = \text{"2"}$.
- Next-next row: End of table $\implies \text{next\_2} = \text{NULL}$.
- Condition: $\text{"2"} == \text{NULL} \implies \mathbf{False}$.

---

### Row 7: ID 7, `num = "2"`
- No subsequent rows $\implies \text{next\_1} = \text{NULL}, \text{next\_2} = \text{NULL} \implies \mathbf{False}$.

---

### Finalization
- Candidate set: `{"1"}`.
- Emitted output table: `[["1"]]`.

---

## 4. Complete Execution Trace

```text
Table: Logs
id:   1    2    3    4    5    6    7
num: "1"  "1"  "1"  "2"  "1"  "2"  "2"

Window Evaluation:
Row 1: num="1", next_1="1", next_2="1" -> MATCH! (Value "1")
Row 2: num="1", next_1="1", next_2="2" -> No match
Row 3: num="1", next_1="2", next_2="1" -> No match
Row 4: num="2", next_1="1", next_2="2" -> No match
Row 5: num="1", next_1="2", next_2="2" -> No match
Row 6: num="2", next_1="2", next_2=NULL-> No match
Row 7: num="2", next_1=NULL,next_2=NULL-> No match

Deduplicated Output: "1"
```

| ID | `num` | `next_1` (LEAD 1) | `next_2` (LEAD 2) | Match Condition ($\text{num} = \text{next\_1} = \text{next\_2}$) | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **`"1"`** | **`"1"`** | **`"1"`** | **`True`** | **Emit `"1"`** |
| 2 | `"1"` | `"1"` | `"2"` | `False` | Discard |
| 3 | `"1"` | `"2"` | `"1"` | `False` | Discard |
| 4 | `"2"` | `"1"` | `"2"` | `False` | Discard |
| 5 | `"1"` | `"2"` | `"2"` | `False` | Discard |
| 6 | `"2"` | `"2"` | `NULL` | `False` | Discard |
| 7 | `"2"` | `NULL` | `NULL` | `False` | Discard |

---

## 5. Algorithmic Correctness

**Soundness.** A value qualifies if and only if there exists an anchor index $i$ such that $\text{num}_i = \text{num}_{i+1} = \text{num}_{i+2}$. By checking each row against its immediate two successors in ID order, any sequence of length 3 or greater is detected at its starting position.

**Completeness.** Applying `DISTINCT` eliminates duplicates caused by runs longer than 3 (e.g., a run of 5 consecutive values produces 3 overlapping windows) or runs occurring at separate intervals, ensuring each qualifying number appears exactly once.

---

## 6. Traps This Instance Exposes

- **Missing `DISTINCT`:** If a number appears four times in a row, rows 1 and 2 both satisfy the condition, causing the number to be emitted twice if `DISTINCT` is omitted.
- **ID Gaps in Table:** A self-join on `l1.id = l2.id - 1` assumes IDs are strictly sequential integers without gaps. If records were deleted (e.g. IDs $1, 3, 4$), the self-join fails to detect consecutive rows. Window functions like `LEAD()` solve this cleanly.
- **Null Safety:** `LEAD` at the boundary returns `NULL`. In SQL, `num = NULL` evaluates to `UNKNOWN` (falsy), correctly disqualifying trailing rows.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$ or $O(N)$ with an index on `id`. Ordering the rows takes $O(N \log N)$, and computing `LEAD()` takes a single linear sweep $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ working memory to buffer the window frame.
