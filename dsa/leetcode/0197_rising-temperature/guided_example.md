# Guided Example: Rising Temperature

We trace the step-by-step SQL calendar-day self-join, date gap validation via `DATEDIFF`, and strict temperature comparison on representative meteorological tables:

- **Input Table `Weather`:**
  $$
  \begin{array}{|c|c|c|}
  \hline
  \textbf{id} & \textbf{recordDate} & \textbf{temperature} \\
  \hline
  1 & \text{"2015-01-01"} & 10 \\
  2 & \text{"2015-01-02"} & 25 \\
  3 & \text{"2015-01-03"} & 20 \\
  4 & \text{"2015-01-04"} & 30 \\
  \hline
  \end{array}
  $$
- **Required output:** `{"columns": ["id"], "rows": [[2], [4]]}` (Jan 2 rose from Jan 1; Jan 4 rose from Jan 3)
- **Date Gap Trap Instance:** `[(1, "2015-01-01", 10), (2, "2015-01-03", 25)] \implies []` (Jan 3 is not yesterday to Jan 1; omitted)
- **Unordered Rows Instance:** Table rows inserted in non-chronological order $\implies$ Relational date math matches records independent of physical table order.

This instance demonstrates SQL date arithmetic (`DATEDIFF(today, yesterday) = 1`), exposes the trap of assuming consecutive row indices or physical table sorting, enforces strict inequality ($T_1 > T_0$), and executes in $O(N)$ time with an index on `recordDate`.

---

## 1. Instance & Teaching Goal

Given a relational table `Weather`:
$$
\begin{array}{|c|c|c|}
\hline
\textbf{id} & \textbf{recordDate} & \textbf{temperature} \\
\hline
1 & \text{"2015-01-01"} & 10 \\
2 & \text{"2015-01-02"} & 25 \\
3 & \text{"2015-01-03"} & 20 \\
4 & \text{"2015-01-04"} & 30 \\
\hline
\end{array}
$$
Find all dates' `id` that had a higher temperature compared to its **previous date (yesterday)**.

Chronological comparison:
- **Jan 1 ($10^\circ$):** No preceding record in table $\implies$ Disqualified.
- **Jan 2 ($25^\circ$):** Preceded by Jan 1 ($10^\circ$). Difference: $25 - 10 = +15 > 0$. **Selected (ID 2).**
- **Jan 3 ($20^\circ$):** Preceded by Jan 2 ($25^\circ$). Difference: $20 - 25 = -5 \le 0$. Disqualified.
- **Jan 4 ($30^\circ$):** Preceded by Jan 3 ($20^\circ$). Difference: $30 - 20 = +10 > 0$. **Selected (ID 4).**
Result: IDs `2` and `4`.

A critical trap in database design:
- Rows are not guaranteed to be ordered by date.
- Dates are not guaranteed to be consecutive (days may be skipped).
- Primary keys (`id`) do not necessarily correlate with date sequence.
Therefore, solutions must bind records strictly using true calendar date arithmetic, not physical row offset or row ID subtraction.

---

## 2. Conceptual Foundation & Invariants

### Method A: Self-Join with `DATEDIFF` (Recommended)
```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2 
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```

#### Why `DATEDIFF` Establishes True Calendar Adjacency:
1. `w1` represents the candidate target day ("today").
2. `w2` represents the reference day ("yesterday").
3. `DATEDIFF(w1.recordDate, w2.recordDate) = 1`:
   Evaluates to $+1$ if and only if `w1.recordDate` is **exactly one calendar day after** `w2.recordDate`.
   - If a day is skipped (e.g. Jan 1 to Jan 3), `DATEDIFF = 2 \ne 1`, correctly preventing invalid comparisons.
4. `WHERE w1.temperature > w2.temperature`:
   Enforces strict temperature increase ($>$).

### Method B: Window Function `LAG()` with Date Validation
```sql
SELECT id
FROM (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
) t
WHERE temperature > prev_temp 
  AND DATEDIFF(recordDate, prev_date) = 1;
```

> **Invariant.** A weather record $w_1$ is selected if and only if there exists another record $w_2$ in `Weather` such that $w_1.\text{recordDate} - w_2.\text{recordDate} = 1\text{ day}$ and $w_1.\text{temperature} > w_2.\text{temperature}$.

---

## 3. Step-by-Step Worked Execution

We trace the self-join matching across all rows of `Weather`:

### Candidate 1: $w_1 = \text{Row 1}$ (Jan 1, $10^\circ$, ID 1)
- Search for $w_2$ where $\text{DATEDIFF} = 1 \implies w_2.\text{recordDate} = \text{"2014-12-31"}$.
- No matching record exists in `Weather`.
- Join condition fails $\implies$ Omitted.

---

### Candidate 2: $w_1 = \text{Row 2}$ (Jan 2, $25^\circ$, ID 2)
- Search for $w_2$ where $\text{DATEDIFF} = 1 \implies w_2.\text{recordDate} = \text{"2015-01-01"}$.
- Match found: Row 1 ($w_2.\text{id} = 1, \text{temp} = 10$).
- Evaluate `w1.temperature > w2.temperature`:
  $$
  25 > 10 \implies \mathbf{True!}
  $$
- Condition satisfied!
- **Emit ID: 2.**

---

### Candidate 3: $w_1 = \text{Row 3}$ (Jan 3, $20^\circ$, ID 3)
- Search for $w_2$ where $\text{DATEDIFF} = 1 \implies w_2.\text{recordDate} = \text{"2015-01-02"}$.
- Match found: Row 2 ($w_2.\text{id} = 2, \text{temp} = 25$).
- Evaluate `w1.temperature > w2.temperature`:
  $$
  20 > 25 \implies \mathbf{False}
  $$
- Discarded.

---

### Candidate 4: $w_1 = \text{Row 4}$ (Jan 4, $30^\circ$, ID 4)
- Search for $w_2$ where $\text{DATEDIFF} = 1 \implies w_2.\text{recordDate} = \text{"2015-01-03"}$.
- Match found: Row 3 ($w_2.\text{id} = 3, \text{temp} = 20$).
- Evaluate `w1.temperature > w2.temperature`:
  $$
  30 > 20 \implies \mathbf{True!}
  $$
- Condition satisfied!
- **Emit ID: 4.**

---

## 4. Complete Execution Trace

```text
Weather Table:
ID 1: 2015-01-01 (10 deg)
ID 2: 2015-01-02 (25 deg)
ID 3: 2015-01-03 (20 deg)
ID 4: 2015-01-04 (30 deg)

Self-Join Evaluation:
  ID 1: No yesterday in table                     -> SKIP
  ID 2: Yesterday is ID 1 (10 deg). 25 > 10 = TRUE -> EMIT ID 2
  ID 3: Yesterday is ID 2 (25 deg). 20 > 25 = FALSE-> SKIP
  ID 4: Yesterday is ID 3 (20 deg). 30 > 20 = TRUE -> EMIT ID 4

Result:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
```

| Candidate ID $w_1$ | Candidate Date | Candidate Temp | Matched Yesterday $w_2$ | Yesterday Temp | $T_{w_1} > T_{w_2}$ | Decision | Emitted ID |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 2015-01-01 | 10 | (None) | - | - | Discarded | - |
| **2** | **2015-01-02** | **25** | **ID 1 (Jan 1)** | **10** | **$25 > 10$** | **Selected** | **`2`** |
| 3 | 2015-01-03 | 20 | ID 2 (Jan 2) | 25 | $20 > 25$ | Discarded | - |
| **4** | **2015-01-04** | **30** | **ID 3 (Jan 3)** | **20** | **$30 > 20$** | **Selected** | **`4`** |

---

## 5. Algorithmic Correctness

**Soundness.** `DATEDIFF(w1.recordDate, w2.recordDate) = 1` enforces that $w_2$ occurred exactly one day prior to $w_1$. The predicate $w_1.\text{temperature} > w_2.\text{temperature}$ guarantees that only days with strict temperature increases are emitted.

**Completeness.** Since `recordDate` values are distinct across all rows, each candidate $w_1$ matches at most one genuine yesterday record $w_2$. Every day with a warmer temperature than its true calendar predecessor is evaluated and returned.

---

## 6. Traps This Instance Exposes

- **The Missing Calendar Day Trap:** In a table with records `[Jan 1 (10 deg), Jan 3 (25 deg)]`, Jan 3 is *not* yesterday to Jan 1. An unconditional `LAG()` or `w1.id = w2.id + 1` would wrongly compare Jan 3 against Jan 1 and output ID 2. `DATEDIFF` prevents this.
- **`DATEDIFF` Argument Order:** In MySQL, `DATEDIFF(d1, d2)` computes $d_1 - d_2$. Swapping arguments to `DATEDIFF(w2.recordDate, w1.recordDate) = 1` would compare today against *tomorrow*, checking for cooling instead of warming!
- **Strict Inequality:** A day with identical temperature ($25^\circ$ vs $25^\circ$) is not rising; `>=` must never be used in place of `>`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ with an index on `recordDate`, where $N$ is the number of rows in `Weather`. Without an index, the optimizer executes a sort-merge join in $O(N \log N)$ or nested loops in $O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$ extra space beyond query engine join buffers.
