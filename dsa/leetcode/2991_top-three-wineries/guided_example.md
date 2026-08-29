# Guided Example: Top Three Wineries 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Wineries": [{"id": 103, "country": "Australia", "points": 84, "winery": "WhisperingPines"}, {"id": 737, "country": "Australia", "points": 85, "winery": "GrapesGalore"}, {"id": 848, "country": "Australia", "points": 100, "winery": "HarmonyHill"}, {"id": 222, "country": "Hungary", "points": 60, "winery": "MoonlitCellars"}, {"id": 116, "country": "USA", "points": 47, "winery": "RoyalVines"}, {"id": 124, "country": "USA", "points": 45, "winery": "Eagle'sNest"}, {"id": 648, "country": "India", "points": 69, "winery": "SunsetVines"}, {"id": 894, "country": "USA", "points": 39, "winery": "RoyalVines"}, {"id": 677, "country": "USA", "points": 9, "winery": "PacificCrest"}]}}`
- **Required output:** `{"columns": ["country", "top_winery", "second_winery", "third_winery"], "rows": [["Australia", "HarmonyHill (100)", "GrapesGalore (85)", "WhisperingPines (84)"], ["Hungary", "MoonlitCellars (60)", "No second winery", "No third winery"], ["India", "SunsetVines (69)", "No second winery", "No third winery"], ["USA", "RoyalVines (86)", "Eagle'sNest (45)", "PacificCrest (9)"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Wineries`

The objective is to compute `{"columns": ["country", "top_winery", "second_winery", "third_winery"], "rows": [["Australia", "HarmonyHill (100)", "GrapesGalore (85)", "WhisperingPines (84)"], ["Hungary", "MoonlitCellars (60)", "No second winery", "No third winery"], ["India", "SunsetVines (69)", "No second winery", "No third winery"], ["USA", "RoyalVines (86)", "Eagle'sNest (45)", "PacificCrest (9)"]]}` from `{"tables": {"Wineries": [{"id": 103, "country": "Australia", "points": 84, "winery": "WhisperingPines"}, {"id": 737, "country": "Australia", "points": 85, "winery": "GrapesGalore"}, {"id": 848, "country": "Australia", "points": 100, "winery": "HarmonyHill"}, {"id": 222, "country": "Hungary", "points": 60, "winery": "MoonlitCellars"}, {"id": 116, "country": "USA", "points": 47, "winery": "RoyalVines"}, {"id": 124, "country": "USA", "points": 45, "winery": "Eagle'sNest"}, {"id": 648, "country": "India", "points": 69, "winery": "SunsetVines"}, {"id": 894, "country": "USA", "points": 39, "winery": "RoyalVines"}, {"id": 677, "country": "USA", "points": 9, "winery": "PacificCrest"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rank wineries only after combining their rows

A winery may appear in several rows. Its ranking score is its total points, not the largest single row and not the number of appearances. The innermost query groups by `country` and `winery` and calculates `SUM(points) AS points`.

After this stage, each country/winery pair has exactly one row. For example, RoyalVines has rows worth 47 and 39 points in the sample, so its grouped total is 86 before any ranking occurs.

Grouping by both columns is necessary because the same winery name in different countries would represent separate country rankings.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Wineries": [{"id": 103, "country": "Australia", "points": 84, "winery": "WhisperingPines"}, {"id": 737, "country": "Australia", "points": 85, "winery": "GrapesGalore"}, {"id": 848, "country": "Australia", "points": 100, "winery": "HarmonyHill"}, {"id": 222, "country": "Hungary", "points": 60, "winery": "MoonlitCellars"}, {"id": 116, "country": "USA", "points": 47, "winery": "RoyalVines"}, {"id": 124, "country": "USA", "points": 45, "winery": "Eagle'sNest"}, {"id": 648, "country": "India", "points": 69, "winery": "SunsetVines"}, {"id": 894, "country": "USA", "points": 39, "winery": "RoyalVines"}, {"id": 677, "country": "USA", "points": 9, "winery": "PacificCrest"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rank within each country with the required tie-breaker

CTE `T` applies:

`RANK() OVER (PARTITION BY country ORDER BY points DESC, winery) AS rk`.

`PARTITION BY country` restarts the ranking for every country. Descending points put the largest total first. When totals tie, ascending `winery` name determines their order.

Because the grouped relation has one row per winery name, the two ordering keys together distinguish rows within a country. Thus ranks progress as one, two, three, and so on even though the function used is `RANK`. The winery-name tie-break removes point ties before rank assignment.

The same CTE formats each candidate as:

`CONCAT(winery, ' (', points, ')')`.

This produces strings such as `"HarmonyHill (100)"`, already in the exact output form.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Pivot ranks into one country row

The desired output has separate columns for the top, second, and third wineries. The query treats `T AS t1` as the rank-one row by applying `WHERE t1.rk = 1`.

It left joins `T AS t2` on the same country and `t1.rk = t2.rk - 1`. Since `t1.rk` is one, this seeks rank two. It then left joins `T AS t3` through `t2` with the analogous condition, seeking rank three.

Left joins are crucial. An inner join would remove countries having fewer than three wineries. With left joins, missing rank-two or rank-three rows become `NULL` while the top winery remains.

`COALESCE` converts those nulls to the required text:

- `'No second winery'`;
- `'No third winery'`.

The top winery needs no fallback because every country present in the grouped table has at least one winery and therefore a rank-one row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["country", "top_winery", "second_winery", "third_winery"], "rows": [["Australia", "HarmonyHill (100)", "GrapesGalore (85)", "WhisperingPines (84)"], ["Hungary", "MoonlitCellars (60)", "No second winery", "No third winery"], ["India", "SunsetVines (69)", "No second winery", "No third winery"], ["USA", "RoyalVines (86)", "Eagle'sNest (45)", "PacificCrest (9)"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Wineries": [{"id": 103, "country": "Australia", "points": 84, "winery": "WhisperingPines"}, {"id": 737, "country": "Australia", "points": 85, "winery": "GrapesGalore"}, {"id": 848, "country": "Australia", "points": 100, "winery": "HarmonyHill"}, {"id": 222, "country": "Hungary", "points": 60, "winery": "MoonlitCellars"}, {"id": 116, "country": "USA", "points": 47, "winery": "RoyalVines"}, {"id": 124, "country": "USA", "points": 45, "winery": "Eagle'sNest"}, {"id": 648, "country": "India", "points": 69, "winery": "SunsetVines"}, {"id": 894, "country": "USA", "points": 39, "winery": "RoyalVines"}, {"id": 677, "country": "USA", "points": 9, "winery": "PacificCrest"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["country", "top_winery", "second_winery", "third_winery"], "rows": [["Australia", "HarmonyHill (100)", "GrapesGalore (85)", "WhisperingPines (84)"], ["Hungary", "MoonlitCellars (60)", "No second winery", "No third winery"], ["India", "SunsetVines (69)", "No second winery", "No third winery"], ["USA", "RoyalVines (86)", "Eagle'sNest (45)", "PacificCrest (9)"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rank raw rows:** This would treat repeated winery entries separately instead of summing their points first.
- **Use `LIMIT 3` globally:** It would return three wineries across all countries, not three per country.
- **Omit winery-name tie-break:** Equal totals would have ambiguous order and `RANK` could assign the same rank, breaking the pivot joins.
- **Conditional aggregation pivot:** `MAX(CASE WHEN rk=1 THEN ... END)` is an equivalent and often simpler pivot; the exact source uses self-joins.
- **Only one winery:** The top value is shown and both fallback messages appear.
- **Exactly two wineries:** Rank two fills `second_winery` and rank three falls back.
- **Repeated winery rows:** `SUM(points)` combines them before ranking.
- **Equal total points:** Ascending winery name establishes a unique order.
- **Output formatting:** Points are summed numerically before being embedded in `"name (points)"`.
- **Country ordering:** `ORDER BY 1` sorts countries ascending.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the input-row count and $W$ the number of distinct country/winery pairs. Aggregating is $O(R)$ expected with hashing or $O(R\log R)$ with sorting. Window ranking sorts the $W$ totals by country, points, and name, costing $O(W\log W)$ in a general plan.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
