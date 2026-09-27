# Guided Example: Rank Scores

We trace the step-by-step SQL window ranking evaluation comparing `DENSE_RANK()`, `RANK()`, and `ROW_NUMBER()` on representative competition score tables:

- **Input Table `Scores`:**
  - `[(1, 3.50), (2, 3.65), (3, 4.00), (4, 3.85), (5, 4.00), (6, 3.65)]`
- **Required output:**
  - `[[4.00, 1], [4.00, 1], [3.85, 2], [3.65, 3], [3.65, 3], [3.50, 4]]`

This instance demonstrates SQL window ranking functions, contrasts dense ranking against sparse ranking and monotonic row numbers, explains why consecutive integer ranks without gaps require `DENSE_RANK()`, and analyzes execution performance in $O(N \log N)$ time.

---

## 1. Instance & Teaching Goal

Given the `Scores` table:
$$
\begin{array}{|c|c|}
\hline
\textbf{id} & \textbf{score} \\
\hline
1 & 3.50 \\
2 & 3.65 \\
3 & 4.00 \\
4 & 3.85 \\
5 & 4.00 \\
6 & 3.65 \\
\hline
\end{array}
$$
Rank all scores from highest to lowest according to the following rules:
1. Higher scores receive lower rank numbers (score $4.00$ gets rank 1).
2. Tied scores share the exact same rank (both rows with $4.00$ get rank 1).
3. The next distinct score must receive the **next consecutive integer** without skipping numbers (score $3.85$ must receive rank 2, NOT rank 3).
4. Return the result table ordered by `score` descending.

### Ranking Function Comparison
Given scores `[4.00, 4.00, 3.85, 3.65, 3.65, 3.50]`:
- `ROW_NUMBER()`: $[1, 2, 3, 4, 5, 6]$ (Arbitrarily breaks ties).
- `RANK()`: $[1, 1, 3, 4, 4, 6]$ (Ties share rank, but leaves gaps proportional to tie counts).
- `DENSE_RANK()`: $[1, 1, 2, 3, 3, 4]$ (**Correct**: ties share rank, and the next rank is consecutive).

---

## 2. Conceptual Foundation & Invariants

### Method A: Window Function `DENSE_RANK()` (Optimal)
```sql
SELECT 
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
```

#### Mechanics of `DENSE_RANK() OVER (...)`:
1. `ORDER BY score DESC`: Sorts the window frame from largest to smallest score.
2. Partitioning: Since there is no `PARTITION BY`, all rows belong to a single global window frame.
3. Peer Groups: Rows with identical `score` values form a peer group and are assigned the identical integer rank.
4. Consecutive Increment: Transitioning to the next peer group increments the rank counter by exactly $+1$.

### Method B: Correlated Subquery (Engine-Agnostic)
```sql
SELECT 
    s1.score,
    (
        SELECT COUNT(DISTINCT s2.score)
        FROM Scores s2
        WHERE s2.score >= s1.score
    ) AS `rank`
FROM Scores s1
ORDER BY s1.score DESC;
```
For each score $s_1$, the rank is precisely the count of distinct scores in the table that are greater than or equal to $s_1$.
- For $4.00$: Distinct scores $\ge 4.00$ is $\{4.00\}$, count $= 1$.
- For $3.85$: Distinct scores $\ge 3.85$ is $\{4.00, 3.85\}$, count $= 2$.
- For $3.65$: Distinct scores $\ge 3.65$ is $\{4.00, 3.85, 3.65\}$, count $= 3$.
- For $3.50$: Distinct scores $\ge 3.50$ is $\{4.00, 3.85, 3.65, 3.50\}$, count $= 4$.

> **Invariant.** For any row with score $v$, its rank equals $1 + |\text{distinct } s \in \text{Scores} \text{ such that } s > v|$.

---

## 3. Step-by-Step Worked Execution

We trace the rows sorted descending by score:
Sorted scores: $[4.00, \, 4.00, \, 3.85, \, 3.65, \, 3.65, \, 3.50]$.

### Row 1: ID 3, Score 4.00
- First distinct score encountered.
- Assigned rank: $\mathbf{1}$.
- Output row: `[4.00, 1]`.

---

### Row 2: ID 5, Score 4.00
- Score is $4.00$, matching previous row (Peer group tie).
- Rank remains unchanged: $\mathbf{1}$.
- Output row: `[4.00, 1]`.

---

### Row 3: ID 4, Score 3.85
- Score drops to a new distinct value ($3.85 < 4.00$).
- Rank increments by 1: $\text{rank} \leftarrow 1 + 1 = \mathbf{2}$.
- *(Note: `RANK()` would have jumped to 3; `DENSE_RANK()` produces consecutive 2)*.
- Output row: `[3.85, 2]`.

---

### Row 4: ID 2, Score 3.65
- Score drops to a new distinct value ($3.65 < 3.85$).
- Rank increments by 1: $\text{rank} \leftarrow 2 + 1 = \mathbf{3}$.
- Output row: `[3.65, 3]`.

---

### Row 5: ID 6, Score 3.65
- Score is $3.65$, matching previous row (Peer group tie).
- Rank remains unchanged: $\mathbf{3}$.
- Output row: `[3.65, 3]`.

---

### Row 6: ID 1, Score 3.50
- Score drops to a new distinct value ($3.50 < 3.65$).
- Rank increments by 1: $\text{rank} \leftarrow 3 + 1 = \mathbf{4}$.
- Output row: `[3.50, 4]`.

---

## 4. Complete Execution Trace

```text
Input Rows (Sorted by Score DESC):
ID 3: 4.00 -> Rank 1
ID 5: 4.00 -> Rank 1 (Tie with ID 3)
ID 4: 3.85 -> Rank 2 (Next consecutive distinct rank)
ID 2: 3.65 -> Rank 3
ID 6: 3.65 -> Rank 3 (Tie with ID 2)
ID 1: 3.50 -> Rank 4

Result Table:
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

| Row Order | Source `id` | `score` | Distinct Score Group | `DENSE_RANK()` | `RANK()` Contrast (Gaps) | `ROW_NUMBER()` Contrast |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 3 | 4.00 | Group 1 | **1** | 1 | 1 |
| 2 | 5 | 4.00 | Group 1 | **1** | 1 | 2 |
| 3 | 4 | 3.85 | Group 2 | **2** | 3 *(gap)* | 3 |
| 4 | 2 | 3.65 | Group 3 | **3** | 4 | 4 |
| 5 | 6 | 3.65 | Group 3 | **3** | 4 | 5 |
| **6** | **1** | **3.50** | **Group 4** | **4** | **6 *(gap)*** | **6** |

---

## 5. Algorithmic Correctness

**Soundness.** `DENSE_RANK()` is defined in ANSI SQL to assign identical ranks to peers within an ordering window and increment by exactly 1 for each distinct subsequent value. This guarantees that all identical scores receive equal rank without generating rank gaps.

**Completeness.** Window functions preserve every original row in the input relation. Unlike `GROUP BY`, which would collapse identical scores into a single aggregate row, the window specification emits all six participant rows.

---

## 6. Traps This Instance Exposes

- **Using `RANK()` Instead of `DENSE_RANK()`:** `RANK()` leaves gaps after ties (e.g. ranks become $1, 1, 3$ instead of $1, 1, 2$).
- **Reserved Keyword Escaping:** In MySQL, `RANK` is a reserved keyword. The output column alias must be quoted with backticks: `` `rank` `` or `'rank'`.
- **Missing Outer `ORDER BY`:** Specifying `OVER (ORDER BY score DESC)` dictates the order within the window calculation, but standard SQL does not guarantee the final output display order without an explicit query-level `ORDER BY score DESC`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of rows in `Scores`. The database engine sorts the table by score once, then assigns ranks in a single linear sweep $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ working memory to buffer the sorted result set.
