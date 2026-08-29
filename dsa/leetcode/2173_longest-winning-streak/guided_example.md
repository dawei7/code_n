# Guided Example: Longest Winning Streak

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Matches": [{"player_id": 1, "match_day": "2022-01-17", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-18", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-25", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-31", "result": "Draw"}, {"player_id": 1, "match_day": "2022-02-08", "result": "Win"}, {"player_id": 2, "match_day": "2022-02-06", "result": "Lose"}, {"player_id": 2, "match_day": "2022-02-08", "result": "Lose"}, {"player_id": 3, "match_day": "2022-03-30", "result": "Win"}]}}`
- **Required output:** `{"columns": ["player_id", "longest_streak"], "rows": [[1, 3], [2, 0], [3, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Matches`

The objective is to compute `{"columns": ["player_id", "longest_streak"], "rows": [[1, 3], [2, 0], [3, 1]]}` from `{"tables": {"Matches": [{"player_id": 1, "match_day": "2022-01-17", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-18", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-25", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-31", "result": "Draw"}, {"player_id": 1, "match_day": "2022-02-08", "result": "Win"}, {"player_id": 2, "match_day": "2022-02-06", "result": "Lose"}, {"player_id": 2, "match_day": "2022-02-08", "result": "Lose"}, {"player_id": 3, "match_day": "2022-03-30", "result": "Win"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create a chronological row number

Inside CTE `S`, the first window expression is

`ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day)`.

For each player independently, this numbers all matches one, two, three, and so forth in date order. Different players restart at one. The primary key guarantees only one match per player per day, so `match_day` provides an unambiguous order.

Call this sequence the overall position. It advances on every result: win, draw, or loss.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Matches": [{"player_id": 1, "match_day": "2022-01-17", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-18", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-25", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-31", "result": "Draw"}, {"player_id": 1, "match_day": "2022-02-08", "result": "Win"}, {"player_id": 2, "match_day": "2022-02-06", "result": "Lose"}, {"player_id": 2, "match_day": "2022-02-08", "result": "Lose"}, {"player_id": 3, "match_day": "2022-03-30", "result": "Win"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create a row number within each result

The second window expression also partitions by `result`:

`ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day)`.

It counts how many times that player has produced this particular result up to the current row. A player's first win has win-number one, the second win has win-number two, even if a draw occurs between them. Draws and losses have their own independent sequences.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Subtract the sequences to label consecutive runs

The query stores overall position minus result-specific position as `rk`. Within consecutive rows having the same result, both row numbers increase by one at every next row, so their difference stays constant.

Suppose a player begins `Win, Win, Win`. The overall positions are `1, 2, 3` and the win-specific positions are also `1, 2, 3`, giving `rk = 0` for all three rows. A following draw has overall position four and draw-specific position one, so its difference is three. If another win follows, its overall position is five and its win-specific position is four, giving difference one rather than zero. The later win therefore does not merge with the opening streak.

For win rows in particular, `rk` equals the number of earlier non-win rows. Every interruption increases that number, so distinct winning streaks for the same player receive distinct labels.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["player_id", "longest_streak"], "rows": [[1, 3], [2, 0], [3, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Matches": [{"player_id": 1, "match_day": "2022-01-17", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-18", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-25", "result": "Win"}, {"player_id": 1, "match_day": "2022-01-31", "result": "Draw"}, {"player_id": 1, "match_day": "2022-02-08", "result": "Win"}, {"player_id": 2, "match_day": "2022-02-06", "result": "Lose"}, {"player_id": 2, "match_day": "2022-02-08", "result": "Lose"}, {"player_id": 3, "match_day": "2022-03-30", "result": "Win"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["player_id", "longest_streak"], "rows": [[1, 3], [2, 0], [3, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cumulative non-win labels:** Sum a one for each draw or loss over each player's chronological rows, then group wins by that cumulative value. This matches the manifest summary and often makes the streak reset especially explicit.
- **Lag plus cumulative starts:** Compare each row with its predecessor, mark the start of a win run, cumulatively number runs, and aggregate. It is flexible but needs additional window stages.
- **Correlated subqueries:** Counting neighboring wins per row is harder to reason about and can become quadratic without careful indexing.
- **Player with no wins:** Retaining non-win rows makes `SUM(result = 'Win')` zero, so the player still appears with longest streak zero.
- **Player with one win:** Its run sum and final maximum are one.
- **Draw and loss both interrupt:** Both make the next win's number of preceding non-wins larger, even though the second row-number window partitions the two result labels separately.
- **Alternating results:** Every isolated win receives a different `rk` from the next isolated win, so the maximum is one.
- **All wins:** Both row-number sequences advance together, `rk` stays constant, and one group counts every row.
- **Same calendar day across players:** Partitioning by `player_id` keeps their sequences independent.
- **Unique day per player:** The composite primary key makes chronological row numbering deterministic without an extra tie-breaker.
- **Boolean arithmetic:** `SUM(result = 'Win')` is MySQL-specific. Other SQL dialects may require `SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END)`.
- **Follow-up for non-losing streaks:** Classify both wins and draws as one “non-loss” category before constructing the row-number difference, and count that category. Merely changing the final sum while still partitioning by the three original results would incorrectly split alternating wins and draws.
- **No output order:** Omitting `ORDER BY` complies with the “any order” contract.
- **Manifest discrepancy:** The stored query labels runs with row-number differences rather than a cumulative non-win count; the explanation follows the actual SQL.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of rows in `Matches`. The two window functions must organize rows by player and date and ordinarily require sorting work. This gives an $O(N\log N)$ time bound in the general case. The two grouping stages then process $O(N)$ intermediate rows.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
