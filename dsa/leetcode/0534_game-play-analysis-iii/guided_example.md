# Guided Example: Game Play Analysis III

We trace the step-by-step partition grouping by player entity (`PARTITION BY player_id`), temporal ordering (`ORDER BY event_date`), cumulative running sum window aggregation (`SUM(games_played) OVER`), and running total progression (`games_played_so_far`) on representative activity logs:

- **Input:**
  - `Activity` table:
    | `player_id` | `device_id` | `event_date` | `games_played` |
    |:---:|:---:|:---:|:---:|
    | $1$ | $2$ | `2016-03-01` | $5$ |
    | $1$ | $2$ | `2016-05-02` | $6$ |
    | $1$ | $3$ | `2017-06-25` | $1$ |
    | $3$ | $1$ | `2016-03-02` | $0$ |
    | $3$ | $4$ | `2018-07-03` | $5$ |
  - Primary key: `(player_id, event_date)`.
- **Required output:**
  | `player_id` | `event_date` | `games_played_so_far` |
  |:---:|:---:|:---:|
  | $1$ | `2016-03-01` | $5$ |
  | $1$ | `2016-05-02` | $11$ |
  | $1$ | `2017-06-25` | $12$ |
  | $3$ | `2016-03-02` | $0$ |
  | $3$ | `2018-07-03` | $5$ |
  - Objective: Calculate the cumulative sum of games played by each player up to and including each logged event date.
- **Relational Window Frame Execution Trace:**
  - **Group 1: Partition for `player_id = 1`:**
    - Sort rows chronologically by `event_date`:
      - Row 1: `event_date = '2016-03-01'`, $games\_played = 5$
        - Running cumulative sum:
          $$
          \text{so\_far} = 5
          $$
        - Result row: `(1, '2016-03-01', 5)`
      - Row 2: `event_date = '2016-05-02'`, $games\_played = 6$
        - Running cumulative sum:
          $$
          \text{so\_far} = 5 + 6 = \mathbf{11}
          $$
        - Result row: `(1, '2016-05-02', 11)`
      - Row 3: `event_date = '2017-06-25'`, $games\_played = 1$
        - Running cumulative sum:
          $$
          \text{so\_far} = 11 + 1 = \mathbf{12}
          $$
        - Result row: `(1, '2017-06-25', 12)`
  - **Group 2: Partition for `player_id = 3`:**
    - Sort rows chronologically:
      - Row 1: `event_date = '2016-03-02'`, $games\_played = 0$
        - Running cumulative sum:
          $$
          \text{so\_far} = \mathbf{0}
          $$
        - Result row: `(3, '2016-03-02', 0)`
      - Row 2: `event_date = '2018-07-03'`, $games\_played = 5$
        - Running cumulative sum:
          $$
          \text{so\_far} = 0 + 5 = \mathbf{5}
          $$
        - Result row: `(3, '2018-07-03', 5)`
  - Final relation preserves player ID, event date, and the running cumulative total.
- **Single Activity Event Instance:**
  - A player with only one login event on date $D$ with $G$ games played outputs $G$ as `games_played_so_far`.
- **Zero-Score Session Instance:**
  - Adding a session with $0$ games preserves the existing cumulative sum without altering the progression.

This instance demonstrates relational analytical window functions over partitioned ordered sets, mathematically proves why window accumulation preserves row cardinality while computing prefix sums, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the `Activity` table:
Each record details the `games_played` by a `player_id` on a specific `event_date`.
Compute the **cumulative games played so far** by each player up to each recorded date.

```text
Player 1 History:
  2016-03-01: played 5 -> Total so far = 5
  2016-05-02: played 6 -> Total so far = 5 + 6 = 11
  2017-06-25: played 1 -> Total so far = 11 + 1 = 12

Player 3 History:
  2016-03-02: played 0 -> Total so far = 0
  2018-07-03: played 5 -> Total so far = 0 + 5 = 5
```

### Window Functions vs Self-Joins
- In traditional relational algebra, cumulative sums can be written using a self-join:
  `JOIN Activity a2 ON a1.player_id = a2.player_id AND a2.event_date <= a1.event_date`
  This quadratic self-join takes $O(K^2)$ comparisons per player.
- SQL **Window Functions** (`OVER (...)`) perform running aggregations in a single sorted pass per partition in $O(K \log K)$ time:
  - `PARTITION BY player_id` isolates each player's history independently.
  - `ORDER BY event_date` ensures earlier events precede later events.
  - The default window frame `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` computes the exact cumulative prefix sum.

---

## 2. Conceptual Foundation & Invariants

### 1. The Cumulative Sum Formula:
For a player $p$ on date $t$:
$$
\text{games\_played\_so\_far}(p, t) = \sum_{\substack{r \in Activity \\ r.player\_id = p \\ r.event\_date \le t}} r.games\_played
$$

### 2. Window Execution Semantics:
1. Divide rows into independent partitions by `player_id`.
2. Within each partition, sort records chronologically by `event_date` ascending.
3. For each row, compute the aggregate sum across all rows from the start of the partition up to the current row.

> **Temporal Prefix Invariant.** The cumulative total on date $t$ is strictly monotonic non-decreasing ($S_t \ge S_{t-1}$ since $games\_played \ge 0$) and encapsulates all historical play sessions up to that moment.

---

## 3. Step-by-Step Worked Execution

We trace Player 1 and Player 3:

---

### Step 1: Group by Player
- Partition 1: `player_id = 1` (3 rows)
- Partition 2: `player_id = 3` (2 rows)

---

### Step 2: Sort and Accumulate Partition 1 (`player_id = 1`)
- **Row 1:** Date `2016-03-01`, games $= 5$.
  $$
  S_1 = 5
  $$
- **Row 2:** Date `2016-05-02`, games $= 6$.
  $$
  S_2 = S_1 + 6 = 5 + 6 = \mathbf{11}
  $$
- **Row 3:** Date `2017-06-25`, games $= 1$.
  $$
  S_3 = S_2 + 1 = 11 + 1 = \mathbf{12}
  $$

---

### Step 3: Sort and Accumulate Partition 2 (`player_id = 3`)
- **Row 1:** Date `2016-03-02`, games $= 0$.
  $$
  S_1 = \mathbf{0}
  $$
- **Row 2:** Date `2018-07-03`, games $= 5$.
  $$
  S_2 = S_1 + 5 = 0 + 5 = \mathbf{5}
  $$

---

### Step 4: Final Output Relation
Emits all 5 rows with player ID, event date, and running cumulative total.

---

## 4. Complete Execution Trace

| `player_id` | `event_date` | Current `games_played` | Prior Cumulative Sum | New Cumulative Total `games_played_so_far` |
|:---:|:---:|:---:|:---:|:---:|
| **$1$** | `2016-03-01` | $5$ | $0$ | **$5$** |
| **$1$** | `2016-05-02` | $6$ | $5$ | **$11$** |
| **$1$** | `2017-06-25` | $1$ | $11$ | **$12$** |
| **$3$** | `2016-03-02` | $0$ | $0$ | **$0$** |
| **$3$** | `2018-07-03` | $5$ | $0$ | **$5$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Record per Player:** Emits the single record's `games_played` value without modification.
- **Zero Games Played ($games\_played = 0$):** Running sum correctly adds 0, maintaining the previous cumulative total.
- **Non-Consecutive Calendar Years:** Dates spanning across years (2016 to 2018) order correctly according to ISO-8601 lexicographical date ordering (`YYYY-MM-DD`).

---

## 6. Traps & Common Anti-Patterns

- **Omitting `ORDER BY` in the Window Specification:**
  Writing `SUM(games_played) OVER (PARTITION BY player_id)` without `ORDER BY event_date` sums across the *entire* partition, giving every row the final grand total (e.g. 12 for every row of player 1) instead of the running cumulative sum.
- **Quadratic Self-Joins on Large Datasets:**
  Using an inequality join `a1.event_date >= a2.event_date` generates $O(N^2)$ intermediate tuples, leading to query timeouts on production tables. Window functions run in optimal $O(N \log N)$ time.
- **Grouping with `GROUP BY` Instead of Windowing:**
  Using `GROUP BY` collapses rows, losing the individual event date rows unless all dimensions are grouped and complex subqueries are used.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting each partition of size $K$ by `event_date` takes $O(K \log K)$ time.
  - A single streaming aggregation pass over the sorted rows computes the cumulative sum in $O(K)$ time.
  - Total Time: $\mathcal{O}(N \log N)$ where $N$ is the total row count of `Activity`.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to buffer rows during partition sorting and emit results.
