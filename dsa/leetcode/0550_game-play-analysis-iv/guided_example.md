# Guided Example: Game Play Analysis IV

We trace the step-by-step player cohort identification ($\min(event\_date)$), next-day consecutive calendar interval joining ($b.event\_date = a.event\_date + 1$), left-join nullability indicator testing ($b.event\_date \text{ IS NOT NULL}$), cohort size normalization, and 2-decimal rounded fraction calculation on representative gaming logs:

- **Input:**
  - `Activity` table:
    | `player_id` | `device_id` | `event_date` | `games_played` |
    |:---:|:---:|:---:|:---:|
    | $1$ | $2$ | `2016-03-01` | $5$ |
    | $1$ | $2$ | `2016-03-02` | $6$ |
    | $2$ | $3$ | `2017-06-25` | $1$ |
    | $3$ | $1$ | `2016-03-02` | $0$ |
    | $3$ | $4$ | `2018-07-03` | $5$ |
- **Required output:**
  | `fraction` |
  |:---:|
  | $0.33$ |
  - Business objective: Calculate the **day-one retention rate**:
    $$
    \text{fraction} = \frac{\text{Count of players who logged in on the exact day after their first login}}{\text{Total count of unique players}}
    $$
    rounded to $2$ decimal places.
- **Relational Step-by-Step Execution Trace:**
  - **Step 1: Compute First Login Date for Each Player (Subquery $a$):**
    - Group by `player_id` and compute $\min(event\_date)$:
      - Player 1: dates are `2016-03-01` and `2016-03-02` $\implies$ First login:
        $$
        d_1 = \text{'2016-03-01'}
        $$
      - Player 2: single record $\implies$ First login:
        $$
        d_2 = \text{'2017-06-25'}
        $$
      - Player 3: dates are `2016-03-02` and `2018-07-03` $\implies$ First login:
        $$
        d_3 = \text{'2016-03-02'}
        $$
    - Subquery relation $a$ ($3$ total unique players):
      | `player_id` | `first_login` |
      |:---:|:---:|
      | $1$ | `2016-03-01` |
      | $2$ | `2017-06-25` |
      | $3$ | `2016-03-02` |
  - **Step 2: Left Join on Consecutive Next Day ($b.event\_date = first\_login + 1$):**
    - **Player 1:**
      - Target return date: $\text{'2016-03-01'} + 1 \text{ day} = \mathbf{\text{'2016-03-02'}}$.
      - Look up in `Activity` for `player_id = 1` on `2016-03-02`: **Found!**
      - Join outcome: `(1, '2016-03-01', '2016-03-02')` $\to$ **Retained (1)**.
    - **Player 2:**
      - Target return date: $\text{'2017-06-25'} + 1 \text{ day} = \mathbf{\text{'2017-06-26'}}$.
      - Look up in `Activity` for `player_id = 2` on `2017-06-26`: **Not Found**.
      - Join outcome: `(2, '2017-06-25', NULL)` $\to$ **Not Retained (0)**.
    - **Player 3:**
      - Target return date: $\text{'2016-03-02'} + 1 \text{ day} = \mathbf{\text{'2016-03-03'}}$.
      - Player 3 logged in on `2018-07-03` (over 2 years later), but **not** on `2016-03-03`.
      - Join outcome: `(3, '2016-03-02', NULL)` $\to$ **Not Retained (0)**.
  - **Step 3: Aggregate Retention Fraction:**
    - Total unique players in denominator: $N = 3$.
    - Number of retained players in numerator: $M = 1$ (only Player 1).
    - Mean retention:
      $$
      \text{fraction} = \frac{M}{N} = \frac{1}{3} \approx 0.3333\dots
      $$
    - Rounded to 2 decimal places:
      $$
      \text{ROUND}(0.3333\dots, \; 2) = \mathbf{0.33}
      $$
- **All Players Retained Instance:**
  - If all 3 players log in on their consecutive second day $\implies 3 / 3 = \mathbf{1.00}$.
- **Zero Retained Players:**
  - If no player returns the next day $\implies 0 / 3 = \mathbf{0.00}$.
- **Single Player Table:**
  - Player returns next day $\implies 1 / 1 = \mathbf{1.00}$.

This instance demonstrates cohort survival analysis in relational database management systems, mathematically proves why anchoring on $\min(event\_date)$ isolates true day-one retention from general activity frequency, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the `Activity` table:
Report the **fraction of players that logged in again on the exact day after their first login date**, rounded to 2 decimal places.

```text
First Logins:
  Player 1: 2016-03-01 -> Logged in next day (2016-03-02)? YES
  Player 2: 2017-06-25 -> Logged in next day (2017-06-26)? NO
  Player 3: 2016-03-02 -> Logged in next day (2016-03-03)? NO

Retained = 1, Total Players = 3
Fraction = 1 / 3 = 0.33
```

### Day-One Retention vs Arbitrary Consecutive Days
- The problem specifically requires checking the day **immediately following the first login date**.
- Consecutive days later in the player's lifecycle (e.g. logging in on day 100 and day 101) do **not** qualify if day 2 was missed.
- The two-step relational structure:
  1. Find the earliest login date $d_0 = \min(event\_date)$ for each player.
  2. Test whether record $(player\_id, d_0 + 1)$ exists in the activity log.

---

## 2. Conceptual Foundation & Invariants

### 1. The Mathematical Metric:
Let $\mathcal{P}$ be the set of all unique players:
$$
\text{Total} = |\mathcal{P}|
$$
Let $\mathcal{R}$ be the subset of players who logged in on their consecutive second day:
$$
\mathcal{R} = \{p \in \mathcal{P} \mid (\min_{r \in \text{Activity}(p)} r.date) + 1 \in \text{Activity}(p)\}
$$
The requested fraction is:
$$
\text{fraction} = \text{ROUND}\left(\frac{|\mathcal{R}|}{|\mathcal{P}|}, \; 2\right)
$$

### 2. Left Join Nullability Indicator:
- Joining the initial login table $a$ with $b \in Activity$ on:
  $$
  a.player\_id = b.player\_id \quad \land \quad b.event\_date = a.first\_login + 1
  $$
- Using a `LEFT JOIN` preserves all players in the denominator.
- If a player returned the next day, $b.event\_date$ is non-null ($1$).
- If not, $b.event\_date$ is `NULL` ($0$).
- Averaging this boolean indicator yields the exact fraction:
  $$
  \text{AVG}(b.event\_date \text{ IS NOT NULL})
  $$

> **Cohort Base Invariant.** Grouping by $player\_id$ to find $\min(event\_date)$ guarantees that each player contributes exactly one row to the denominator, preventing hyper-active players from skewing retention proportions.

---

## 3. Step-by-Step Worked Execution

We trace the sample data with 3 players:

---

### Step 1: Subquery $a$ (First Logins)
- Player 1: $\min = \text{'2016-03-01'}$
- Player 2: $\min = \text{'2017-06-25'}$
- Player 3: $\min = \text{'2016-03-02'}$
Result: 3 rows.

---

### Step 2: Left Join with Activity $b$ on $(first\_login + 1)$
- **Player 1:**
  - Target: $\text{'2016-03-01'} + 1 = \text{'2016-03-02'}$.
  - Record exists in $b$.
  - Joined row: `(1, '2016-03-01', '2016-03-02')`.
  - Indicator: `b.event_date IS NOT NULL` $\implies \mathbf{True}$.
- **Player 2:**
  - Target: $\text{'2017-06-25'} + 1 = \text{'2017-06-26'}$.
  - Record does not exist in $b$.
  - Joined row: `(2, '2017-06-25', NULL)`.
  - Indicator: $\mathbf{False}$.
- **Player 3:**
  - Target: $\text{'2016-03-02'} + 1 = \text{'2016-03-03'}$.
  - Record does not exist in $b$.
  - Joined row: `(3, '2016-03-02', NULL)`.
  - Indicator: $\mathbf{False}$.

---

### Step 3: Compute Average and Round
- Indicators: $[\text{True}, \text{False}, \text{False}] \implies [1, 0, 0]$.
- Average:
  $$
  \frac{1 + 0 + 0}{3} = \frac{1}{3} \approx 0.33333\dots
  $$
- Round to 2 decimal places:
  $$
  \mathbf{0.33}
  $$

---

## 4. Complete Execution Trace

| `player_id` | First Login Date | Expected Day 2 Date | Record Found in Activity? | Retained Boolean | Contribution to Numerator |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | `2016-03-01` | `2016-03-02` | **Yes** | **True** | $+1$ |
| **$2$** | `2017-06-25` | `2017-06-26` | No | False | $0$ |
| **$3$** | `2016-03-02` | `2016-03-03` | No | False | $0$ |
| **Final Ratio** | — | — | — | — | **$1 / 3 = 0.33$** |

---

## 5. Boundary Cases & Failure Modes

- **100% Retention:** All players return the next day $\implies 1.00$.
- **0% Retention:** No player returns the next day $\implies 0.00$.
- **Consecutive Days Across Months (`2016-01-31` to `2016-02-01`):** Proper SQL date arithmetic (`date + 1` or `(a.event_date - b.event_date) = -1`) accounts for leap years and variable month lengths automatically.
- **Player with Multiple Logins on Same Date:** Primary key $(player\_id, event\_date)$ guarantees unique dates per player.

---

## 6. Traps & Common Anti-Patterns

- **Inner Join Instead of Left Join:** Using an `INNER JOIN` drops un-retained players from the intermediate table, causing the denominator to shrink and calculating $1 / 1 = 1.00$ instead of $1 / 3 = 0.33$.
- **Checking Consecutive Days Anywhere in History:** Checking `b.event_date = a.event_date + 1` without filtering $a$ to only the *first* login date counts players who returned consecutively on later days even if they churned after day 1.
- **Integer Division Truncation:** In SQL engines like PostgreSQL or SQL Server, dividing two integers `1 / 3` evaluates to `0` due to integer division. Using `AVG(...)` or casting to `::numeric` preserves decimal precision before rounding.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding $\min(event\_date)$ per player with `GROUP BY` takes $O(N)$ time (or $O(N \log N)$ with sorting).
  - Joining on indexed primary key $(player\_id, event\_date)$ takes $O(K \log N)$ where $K$ is the number of unique players.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ intermediate memory to store the cohort first login table.
