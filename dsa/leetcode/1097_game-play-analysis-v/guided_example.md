# Guided Example: Game Play Analysis V

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-03-02", "games_played": 6}, {"player_id": 2, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-01", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2016-07-03", "games_played": 5}]}}`
- **Required output:** `{"columns": ["install_dt", "installs", "Day1_retention"], "rows": [["2016-03-01", 2, 0.5], ["2017-06-25", 1, 0.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Activity`

The objective is to compute `{"columns": ["install_dt", "installs", "Day1_retention"], "rows": [["2016-03-01", 2, 0.5], ["2017-06-25", 1, 0.0]]}` from `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-03-02", "games_played": 6}, {"player_id": 2, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-01", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2016-07-03", "games_played": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Attach each player’s install date to every activity row

The install date is the minimum `event_date` for one `player_id`. The common table expression `T` computes it with `MIN(event_date) OVER (PARTITION BY player_id)`. Unlike a grouped minimum, this window function preserves every activity row while adding the player-level minimum beside it.

This preserved detail is important because the query must later see whether an activity occurred exactly one day after installation. Every row for a player now carries the same `install_dt`, making the difference between that row’s date and the first date directly testable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-03-02", "games_played": 6}, {"player_id": 2, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-01", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2016-07-03", "games_played": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create one cohort per install date

The outer query groups `T` by `install_dt` through `GROUP BY 1`, where one refers to the first selected expression. All players whose first login occurred on the same date enter the same cohort.

Because `T` contains one row per activity rather than one row per player, a player with many logins appears several times in the cohort. `COUNT(DISTINCT player_id)` is therefore necessary for `installs`. It counts each player once regardless of later activity frequency.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count exact next-day returns

`DATEDIFF(event_date, install_dt)` gives the number of calendar-day boundaries between an activity row and installation. Comparing it with one yields true only for a login on the immediately following date. In MySQL numeric aggregation, true contributes one and false contributes zero, so:

`SUM(DATEDIFF(event_date, install_dt) = 1)`

counts next-day activity rows.

The composite primary key `(player_id, event_date)` guarantees that one player has at most one activity row on a given date. Therefore, a retained player can contribute at most one true row. The sum is not merely a count of events; under this key it is exactly the number of distinct retained players.

The installation row itself has difference zero and contributes nothing. A return two days later has difference two and also contributes nothing. Device changes and games played never enter the calculation, correctly reflecting the contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["install_dt", "installs", "Day1_retention"], "rows": [["2016-03-01", 2, 0.5], ["2017-06-25", 1, 0.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-03-02", "games_played": 6}, {"player_id": 2, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-01", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2016-07-03", "games_played": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["install_dt", "installs", "Day1_retention"], "rows": [["2016-03-01", 2, 0.5], ["2017-06-25", 1, 0.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Grouped installs plus self join:** First compute one row per player with `MIN(event_date)`, then left join Activity on the same player and date plus one day. This makes the player-level numerator explicit and avoids relying on the primary key when summing events.
- **Conditional distinct count:** Use `COUNT(DISTINCT CASE WHEN DATEDIFF(...) = 1 THEN player_id END)`. It remains correct even if the source allowed multiple same-day rows per player.
- **Correlated existence check:** For each player’s install row, test whether a next-day row exists. This expresses retention directly but may require careful indexing for performance.
- **Multiple logins after installation:** Only the row exactly one day later contributes; all later rows are false in the Boolean sum.
- **No next-day return:** The numerator is zero, so the rounded ratio is `0.00` numerically.
- **Single-player cohort:** Retention is either zero or one depending on that player’s next-day row.
- **Several players with many activities:** `COUNT(DISTINCT player_id)` ensures each player contributes once to installs.
- **Same-day installation activity:** Its date difference is zero and is not mistaken for retention.
- **Calendar boundaries:** `DATEDIFF` handles month and year changes, so December 31 to January 1 is exactly one day.
- **Composite primary key:** It is what makes the plain Boolean sum safe as a player count. Without date uniqueness, repeated next-day rows could inflate the numerator.
- **Empty table:** No window rows means no grouped cohorts and therefore an empty result.
- **Result casing:** The alias is written `day1_retention` while the displayed contract uses different capitalization. SQL identifiers are normally case-insensitive here, and the semantic column is the same.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A \log A)$. Let $A$ be the number of Activity rows. A typical execution sorts or otherwise partitions rows by `player_id` to compute the window minimum, then groups them by install date. Sort-based implementations take $O(A\log A)$ time, matching the package manifest.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
