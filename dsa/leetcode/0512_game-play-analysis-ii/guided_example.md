# Guided Example: Game Play Analysis II

We trace the step-by-step composite tuple matching (`(player_id, event_date)`), earliest login timestamp identification ($\min(event\_date)$), associated attribute retrieval (`device_id`), subquery filtering (`WHERE ... IN`), and projection on representative gaming activity logs:

- **Input Table (`Activity`):**
  | `player_id` | `device_id` | `event_date` | `games_played` |
  |:---:|:---:|:---:|:---:|
  | $1$ | $2$ | `2016-03-01` | $5$ |
  | $1$ | $2$ | `2016-05-02` | $6$ |
  | $2$ | $3$ | `2017-06-25` | $1$ |
  | $3$ | $1$ | `2016-03-02` | $0$ |
  | $3$ | $4$ | `2018-07-03` | $5$ |
- **Required output:**
  | `player_id` | `device_id` |
  |:---:|:---:|
  | $1$ | $2$ |
  | $2$ | $3$ |
  | $3$ | $1$ |
  - Table primary key: `(player_id, event_date)`
  - Objective: For each player, report the `device_id` used on their very first login date.
- **Relational subquery filtering execution trace:**
  - **Phase 1: Subquery to Find First Login per Player:**
    - Group table `Activity` by `player_id`:
      - Player 1: dates $\{ \text{"2016-03-01"}, \text{"2016-05-02"} \} \implies \min = \mathbf{\text{"2016-03-01"}}$
      - Player 2: dates $\{ \text{"2017-06-25"} \} \implies \min = \mathbf{\text{"2017-06-25"}}$
      - Player 3: dates $\{ \text{"2016-03-02"}, \text{"2018-07-03"} \} \implies \min = \mathbf{\text{"2016-03-02"}}$
    - Target composite key set:
      $$
      \mathcal{K} = \left\{ (1, \text{"2016-03-01"}), \; (2, \text{"2017-06-25"}), \; (3, \text{"2016-03-02"}) \right\}
      $$
  - **Phase 2: Filtering Outer Table with Composite Key Set:**
    - Scan every row of `Activity` and check if $(player\_id, event\_date) \in \mathcal{K}$:
      - **Row 1:** $(1, \text{"2016-03-01"})$:
        - In set $\mathcal{K}$? **Yes!**
        - Associated `device_id`: $\mathbf{2}$
        - Retain: $(1, 2)$
      - **Row 2:** $(1, \text{"2016-05-02"})$:
        - In set $\mathcal{K}$? No (later login date).
        - Discard.
      - **Row 3:** $(2, \text{"2017-06-25"})$:
        - In set $\mathcal{K}$? **Yes!**
        - Associated `device_id`: $\mathbf{3}$
        - Retain: $(2, 3)$
      - **Row 4:** $(3, \text{"2016-03-02"})$:
        - In set $\mathcal{K}$? **Yes!**
        - Associated `device_id`: $\mathbf{1}$
        - Retain: $(3, 1)$
      - **Row 5:** $(3, \text{"2018-07-03"})$:
        - In set $\mathcal{K}$? No (later login date).
        - Discard.
  - **Phase 3: Final Projection:**
    - Project columns `(player_id, device_id)`:
      $$
      (1, 2), \quad (2, 3), \quad (3, 1)
      $$
- **Device Switch Instance:**
  - Notice Player 3 logged in on `device_id = 1` in 2016, and switched to `device_id = 4` in 2018. The filter correctly identifies device $1$ as the first device and ignores device $4$.
- **Single-Device Player Instance:**
  - Player 2 used only device $3 \implies (2, 3)$ emitted directly.

This instance demonstrates correlated semi-join filtering on composite keys, mathematically proves why joining on the primary key $(player\_id, event\_date)$ uniquely recovers non-aggregated row attributes, and derives $O(N)$ runtime and $O(P)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the `Activity` table with schema `(player_id, device_id, event_date, games_played)`:
The composite primary key is `(player_id, event_date)`.
Find the **device** that was logged into first for each player.

```text
Table Activity:
  Row 1: Player 1, Device 2, 2016-03-01  <- First login for Player 1!
  Row 2: Player 1, Device 2, 2016-05-02
  Row 3: Player 2, Device 3, 2017-06-25  <- First login for Player 2!
  Row 4: Player 3, Device 1, 2016-03-02  <- First login for Player 3!
  Row 5: Player 3, Device 4, 2018-07-03

Result:
  Player 1 -> Device 2
  Player 2 -> Device 3
  Player 3 -> Device 1
```

### The Non-Aggregated Attribute Challenge in SQL
- In standard SQL, you cannot simply write:
  `SELECT player_id, device_id, MIN(event_date) FROM Activity GROUP BY player_id`
- Why? Because `device_id` is neither in the `GROUP BY` clause nor wrapped in an aggregate function. SQL engines cannot know which row's `device_id` should accompany the minimum `event_date`.
- Solution:
  1. Find the unique `(player_id, MIN(event_date))` pairs using a subquery.
  2. Filter the original table where the composite pair matches the subquery output!
  3. This cleanly retrieves the exact `device_id` corresponding to that earliest login date.

---

## 2. Conceptual Foundation & Invariants

### 1. Composite Tuple Filtering:
The query structure:
$$
\sigma_{(player\_id, event\_date) \in \mathcal{K}}(\text{Activity})
$$
where $\mathcal{K}$ is defined by:
$$
\mathcal{K} = \gamma_{player\_id, \min(event\_date)}(\text{Activity})
$$

### 2. Primary Key Uniqueness:
Because `(player_id, event_date)` is the primary key of `Activity`:
- For any player $p$, their minimum event date $D_{min}$ corresponds to **exactly one row** in the table!
- There is never any ambiguity or multiple devices on the exact same minimum date.

> **Primary Key Join Invariant.** Filtering on the composite pair $(player\_id, \min(event\_date))$ guarantees that exactly one unique row per player is selected from the outer table.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Execute Subquery
Group by `player_id` to compute minimum dates:
- Player 1: $\min = \text{"2016-03-01"}$
- Player 2: $\min = \text{"2017-06-25"}$
- Player 3: $\min = \text{"2016-03-02"}$
Subquery output set:
$$
\mathcal{K} = \{(1, \text{"2016-03-01"}), \; (2, \text{"2017-06-25"}), \; (3, \text{"2016-03-02"})\}
$$

---

### Step 2: Filter Rows Against $\mathcal{K}$
- Row 1: $(1, \text{"2016-03-01"})$ matches $\mathcal{K} \implies$ Output `(1, 2)`.
- Row 2: $(1, \text{"2016-05-02"})$ does not match $\implies$ Filtered out.
- Row 3: $(2, \text{"2017-06-25"})$ matches $\mathcal{K} \implies$ Output `(2, 3)`.
- Row 4: $(3, \text{"2016-03-02"})$ matches $\mathcal{K} \implies$ Output `(3, 1)`.
- Row 5: $(3, \text{"2018-07-03"})$ does not match $\implies$ Filtered out.

---

### Step 3: Emit Final Table
| `player_id` | `device_id` |
|:---:|:---:|
| $1$ | $2$ |
| $2$ | $3$ |
| $3$ | $1$ |

---

## 4. Complete Execution Trace

| Row | `player_id` | `device_id` | `event_date` | In Subquery Set $\mathcal{K}$? | Included in Result? | Output Columns Projected |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | $1$ | $2$ | `2016-03-01` | **Yes** | **Yes** | `(1, 2)` |
| **2** | $1$ | $2$ | `2016-05-02` | No | No | — |
| **3** | $2$ | $3$ | `2017-06-25` | **Yes** | **Yes** | `(2, 3)` |
| **4** | $3$ | $1$ | `2016-03-02` | **Yes** | **Yes** | `(3, 1)` |
| **5** | $3$ | $4$ | `2018-07-03` | No | No | — |

---

## 5. Boundary Cases & Failure Modes

- **Player with Multiple Different Devices on Different Dates:** Correctly selects only the device from the earliest date (Player 3 used device 1 first, then device 4).
- **Single Activity Row per Player:** Subquery matches the only row $\implies$ returns that device.
- **Multiple Players Using the Same Device ID:** Different players logging into the same device (e.g. shared console) are preserved independently because partitioning is strictly by `player_id`.

---

## 6. Traps & Common Anti-Patterns

- **Filtering by `event_date IN (SELECT MIN(event_date) FROM Activity)`:** This checks against the *global* minimum date across the entire table, returning only the single player who logged in first globally, instead of the first login for *each* player. Filtering by the composite tuple `(player_id, event_date)` is mandatory.
- **Using Non-Standard Window Functions in Strict SQL:** While `ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date)` works, standard tuple `IN` subqueries are portable across MySQL, PostgreSQL, SQLite, and Oracle.
- **Misordering Output Columns:** The problem requires `(player_id, device_id)`, not `(device_id, player_id)`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The subquery aggregates $N$ rows using a hash map or index: $\mathcal{O}(N)$.
  - Storing the $P$ subquery results in a hash set takes $O(P)$ time.
  - The outer query checks $N$ rows against the set in $O(1)$ time per row.
  - Total Time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(P)$ memory where $P$ is the number of distinct players.
