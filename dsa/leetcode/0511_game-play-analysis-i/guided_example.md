# Guided Example: Game Play Analysis I

We trace the step-by-step relational group partitioning by entity identifier (`player_id`), date-column ordering and chronologically earliest timestamp selection ($\min(event\_date)$), alias projection (`first_login`), and deterministic aggregation on representative player activity logs:

- **Input Table (`Activity`):**
  | `player_id` | `device_id` | `event_date` | `games_played` |
  |:---:|:---:|:---:|:---:|
  | $1$ | $2$ | `2016-03-01` | $5$ |
  | $1$ | $2$ | `2016-05-02` | $6$ |
  | $2$ | $3$ | `2017-06-25` | $1$ |
  | $3$ | $1$ | `2016-03-02` | $0$ |
  | $3$ | $4$ | `2018-07-03` | $5$ |
- **Required output:**
  | `player_id` | `first_login` |
  |:---:|:---:|
  | $1$ | `2016-03-01` |
  | $2$ | `2017-06-25` |
  | $3$ | `2016-03-02` |
  - Composite primary key: `(player_id, event_date)`
  - Objective: For each distinct player, find their very first login date.
- **Relational aggregation execution trace:**
  - **Phase 1: Group By Partitioning:**
    - Partition all activity records by unique `player_id`:
      - **Group $player\_id = 1$:**
        - Row 1: `event_date` = `2016-03-01`
        - Row 2: `event_date` = `2016-05-02`
      - **Group $player\_id = 2$:**
        - Row 3: `event_date` = `2017-06-25`
      - **Group $player\_id = 3$:**
        - Row 4: `event_date` = `2016-03-02`
        - Row 5: `event_date` = `2018-07-03`
  - **Phase 2: Aggregate Function Evaluation ($\min$):**
    - **For Group 1:**
      - Dates: `{"2016-03-01", "2016-05-02"}`
      - Earliest chronological date:
        $$
        \min(\text{"2016-03-01"}, \; \text{"2016-05-02"}) = \mathbf{\text{"2016-03-01"}}
        $$
    - **For Group 2:**
      - Dates: `{"2017-06-25"}`
      - Earliest date:
        $$
        \min(\text{"2017-06-25"}) = \mathbf{\text{"2017-06-25"}}
        $$
    - **For Group 3:**
      - Dates: `{"2016-03-02", "2018-07-03"}`
      - Earliest chronological date:
        $$
        \min(\text{"2016-03-02"}, \; \text{"2018-07-03"}) = \mathbf{\text{"2016-03-02"}}
        $$
  - **Phase 3: Projection & Renaming:**
    - Output schema: `(player_id, first_login)`
    - Record pairs:
      $$
      (1, \text{"2016-03-01"}), \quad (2, \text{"2017-06-25"}), \quad (3, \text{"2016-03-02"})
      $$
- **Single Login Player Instance:**
  - If a player only logged in once, $\min$ over a single element returns that date directly.
- **Multiple Disordered Date Entries:**
  - Standard ISO-8601 date format (`YYYY-MM-DD`) enables direct lexicographical and chronological minimum evaluation.

This instance demonstrates relational grouping and extreme value aggregation, mathematically proves why $\min()$ across partitioned entity sets selects the earliest timestamp in linear time, and derives $O(N)$ runtime and $O(P)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the `Activity` table with schema `(player_id, device_id, event_date, games_played)`:
The table's primary key is `(player_id, event_date)`.
Each row records a day on which a player logged in and played some number of games.
Find the **first login date** for each player.

```text
Table Activity:
  Player 1 -> Logs in on 2016-03-01 and 2016-05-02
  Player 2 -> Logs in on 2017-06-25
  Player 3 -> Logs in on 2016-03-02 and 2018-07-03

Group by player_id and select MIN(event_date):
  Player 1 -> First Login = 2016-03-01
  Player 2 -> First Login = 2017-06-25
  Player 3 -> First Login = 2016-03-02
```

### The Relational Aggregation Pattern
- We want one summary row per player.
- In relational algebra, grouping rows by `player_id` partitions the dataset into independent buckets $\mathcal{B}_p$.
- Applying the aggregate function $\min(event\_date)$ over each bucket extracts the earliest chronological entry.
- Renaming the aggregate result to `first_login` matches the expected output schema.

---

## 2. Conceptual Foundation & Invariants

### 1. Partitioning and Reduction:
Let the table be a relation $\mathcal{R}$.
- Partition relation $\mathcal{R}$ into subsets by unique player:
  $$
  \mathcal{B}_p = \{r \in \mathcal{R} \mid r.player\_id = p\}
  $$
- For each group $\mathcal{B}_p$, compute:
  $$
  first\_login(p) = \min_{r \in \mathcal{B}_p} (r.event\_date)
  $$
- Return the relation $\gamma_{player\_id, \min(event\_date) \to first\_login}(\mathcal{R})$.

### 2. ISO-8601 Date Ordering Invariant:
Because dates are formatted as `YYYY-MM-DD`:
- Chronological ordering is identical to lexicographical string ordering:
  $$
  D_1 < D_2 \iff \text{str}(D_1) < \text{str}(D_2)
  $$
- This guarantees that $\min()$ unambiguously selects the earliest date.

> **Grouping Invariant.** Because `(player_id, event_date)` is the primary key, no player has duplicate identical dates, and each group produces exactly one row in the output.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Scan and Group Rows
1. **Player 1 Bucket:**
   - Record 1: date `2016-03-01`
   - Record 2: date `2016-05-02`
2. **Player 2 Bucket:**
   - Record 3: date `2017-06-25`
3. **Player 3 Bucket:**
   - Record 4: date `2016-03-02`
   - Record 5: date `2018-07-03`

---

### Step 2: Compute Minimum Date per Bucket
- Bucket 1:
  $$
  \min(\text{"2016-03-01"}, \; \text{"2016-05-02"}) = \mathbf{\text{"2016-03-01"}}
  $$
- Bucket 2:
  $$
  \min(\text{"2017-06-25"}) = \mathbf{\text{"2017-06-25"}}
  $$
- Bucket 3:
  $$
  \min(\text{"2016-03-02"}, \; \text{"2018-07-03"}) = \mathbf{\text{"2016-03-02"}}
  $$

---

### Step 3: Format Final Result Table
| `player_id` | `first_login` |
|:---:|:---:|
| $1$ | `2016-03-01` |
| $2$ | `2017-06-25` |
| $3$ | `2016-03-02` |

---

## 4. Complete Execution Trace

| Input Row ID | `player_id` | `event_date` | Assigned Partition | Running Minimum in Partition |
|:---:|:---:|:---:|:---:|:---:|
| **1** | $1$ | `2016-03-01` | Group $1$ | `2016-03-01` |
| **2** | $1$ | `2016-05-02` | Group $1$ | `2016-03-01` |
| **3** | $2$ | `2017-06-25` | Group $2$ | `2017-06-25` |
| **4** | $3$ | `2016-03-02` | Group $3$ | `2016-03-02` |
| **5** | $3$ | `2018-07-03` | Group $3$ | `2016-03-02` |

---

## 5. Boundary Cases & Failure Modes

- **Single Record per Player:** Bucket contains only 1 date $\implies$ returns that date directly.
- **Single Player with Many Dates:** 1 group reduced to its single earliest date.
- **Unsorted Input Rows:** Dates arriving out of order (e.g. 2018 before 2016) are correctly resolved by $\min()$.
- **Empty Table:** Returns empty result with correct column headers `(player_id, first_login)`.

---

## 6. Traps & Common Anti-Patterns

- **Selecting Without `GROUP BY`:** Querying `SELECT player_id, MIN(event_date)` without `GROUP BY player_id` causes an SQL syntax error or collapses all players into a single global minimum row.
- **Using Window Functions Unnecessarily:** `ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date)` works, but introduces sorting overhead $O(N \log N)$ compared to the $O(N)$ streaming accumulator of `MIN()`.
- **Misnaming the Output Column:** Failing to alias `MIN(event_date) AS first_login` will cause automated judge assertion failure on column naming.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A hash aggregate or streaming group-by reads each of the $N$ rows once: $\mathcal{O}(N)$.
  - Updating the running minimum for each player takes $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(P)$ memory where $P$ is the number of distinct players, to store the hash aggregate table.
