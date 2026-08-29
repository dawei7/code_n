# Guided Example: Premier League Table Ranking II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Chelsea", "matches_played": 22, "wins": 13, "draws": 2, "losses": 7}, {"team_id": 2, "team_name": "Nottingham Forest", "matches_played": 27, "wins": 6, "draws": 6, "losses": 15}, {"team_id": 3, "team_name": "Liverpool", "matches_played": 17, "wins": 1, "draws": 8, "losses": 8}, {"team_id": 4, "team_name": "Aston Villa", "matches_played": 20, "wins": 1, "draws": 6, "losses": 13}, {"team_id": 5, "team_name": "Fulham", "matches_played": 31, "wins": 18, "draws": 1, "losses": 12}, {"team_id": 6, "team_name": "Burnley", "matches_played": 26, "wins": 6, "draws": 9, "losses": 11}, {"team_id": 7, "team_name": "Newcastle United", "matches_played": 33, "wins": 11, "draws": 10, "losses": 12}, {"team_id": 8, "team_name": "Sheffield United", "matches_played": 20, "wins": 18, "draws": 2, "losses": 0}, {"team_id": 9, "team_name": "Luton Town", "matches_played": 5, "wins": 4, "draws": 0, "losses": 1}, {"team_id": 10, "team_name": "Everton", "matches_played": 14, "wins": 2, "draws": 6, "losses": 6}]}}`
- **Required output:** `{"columns": ["team_name", "points", "position", "tier"], "rows": [["Sheffield United", 56, 1, "Tier 1"], ["Fulham", 55, 2, "Tier 1"], ["Newcastle United", 43, 3, "Tier 1"], ["Chelsea", 41, 4, "Tier 1"], ["Burnley", 27, 5, "Tier 2"], ["Nottingham Forest", 24, 6, "Tier 2"], ["Everton", 12, 7, "Tier 2"], ["Luton Town", 12, 7, "Tier 2"], ["Liverpool", 11, 9, "Tier 3"], ["Aston Villa", 9, 10, "Tier 3"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `TeamStats`

The objective is to compute `{"columns": ["team_name", "points", "position", "tier"], "rows": [["Sheffield United", 56, 1, "Tier 1"], ["Fulham", 55, 2, "Tier 1"], ["Newcastle United", 43, 3, "Tier 1"], ["Chelsea", 41, 4, "Tier 1"], ["Burnley", 27, 5, "Tier 2"], ["Nottingham Forest", 24, 6, "Tier 2"], ["Everton", 12, 7, "Tier 2"], ["Luton Town", 12, 7, "Tier 2"], ["Liverpool", 11, 9, "Tier 3"], ["Aston Villa", 9, 10, "Tier 3"]]}` from `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Chelsea", "matches_played": 22, "wins": 13, "draws": 2, "losses": 7}, {"team_id": 2, "team_name": "Nottingham Forest", "matches_played": 27, "wins": 6, "draws": 6, "losses": 15}, {"team_id": 3, "team_name": "Liverpool", "matches_played": 17, "wins": 1, "draws": 8, "losses": 8}, {"team_id": 4, "team_name": "Aston Villa", "matches_played": 20, "wins": 1, "draws": 6, "losses": 13}, {"team_id": 5, "team_name": "Fulham", "matches_played": 31, "wins": 18, "draws": 1, "losses": 12}, {"team_id": 6, "team_name": "Burnley", "matches_played": 26, "wins": 6, "draws": 9, "losses": 11}, {"team_id": 7, "team_name": "Newcastle United", "matches_played": 33, "wins": 11, "draws": 10, "losses": 12}, {"team_id": 8, "team_name": "Sheffield United", "matches_played": 20, "wins": 18, "draws": 2, "losses": 0}, {"team_id": 9, "team_name": "Luton Town", "matches_played": 5, "wins": 4, "draws": 0, "losses": 1}, {"team_id": 10, "team_name": "Everton", "matches_played": 14, "wins": 2, "draws": 6, "losses": 6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

The query must compute three related facts for every team: league points, competition position, and one of three tiers. A common table expression first calculates the reusable ranking context, and the outer query converts that context into tiers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Chelsea", "matches_played": 22, "wins": 13, "draws": 2, "losses": 7}, {"team_id": 2, "team_name": "Nottingham Forest", "matches_played": 27, "wins": 6, "draws": 6, "losses": 15}, {"team_id": 3, "team_name": "Liverpool", "matches_played": 17, "wins": 1, "draws": 8, "losses": 8}, {"team_id": 4, "team_name": "Aston Villa", "matches_played": 20, "wins": 1, "draws": 6, "losses": 13}, {"team_id": 5, "team_name": "Fulham", "matches_played": 31, "wins": 18, "draws": 1, "losses": 12}, {"team_id": 6, "team_name": "Burnley", "matches_played": 26, "wins": 6, "draws": 9, "losses": 11}, {"team_id": 7, "team_name": "Newcastle United", "matches_played": 33, "wins": 11, "draws": 10, "losses": 12}, {"team_id": 8, "team_name": "Sheffield United", "matches_played": 20, "wins": 18, "draws": 2, "losses": 0}, {"team_id": 9, "team_name": "Luton Town", "matches_played": 5, "wins": 4, "draws": 0, "losses": 1}, {"team_id": 10, "team_name": "Everton", "matches_played": 14, "wins": 2, "draws": 6, "losses": 6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

In CTE `T`, points are `wins * 3 + draws` because wins contribute three, draws one, and losses zero. `RANK() OVER (ORDER BY wins * 3 + draws DESC)` assigns position one to the greatest total. Equal totals share a position because points are the window's only ordering key.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`RANK` leaves competition gaps. If two teams share position seven, the following team is position nine. This matters to the tier calculation because a tied group is treated according to its shared first position.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["team_name", "points", "position", "tier"], "rows": [["Sheffield United", 56, 1, "Tier 1"], ["Fulham", 55, 2, "Tier 1"], ["Newcastle United", 43, 3, "Tier 1"], ["Chelsea", 41, 4, "Tier 1"], ["Burnley", 27, 5, "Tier 2"], ["Nottingham Forest", 24, 6, "Tier 2"], ["Everton", 12, 7, "Tier 2"], ["Luton Town", 12, 7, "Tier 2"], ["Liverpool", 11, 9, "Tier 3"], ["Aston Villa", 9, 10, "Tier 3"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Chelsea", "matches_played": 22, "wins": 13, "draws": 2, "losses": 7}, {"team_id": 2, "team_name": "Nottingham Forest", "matches_played": 27, "wins": 6, "draws": 6, "losses": 15}, {"team_id": 3, "team_name": "Liverpool", "matches_played": 17, "wins": 1, "draws": 8, "losses": 8}, {"team_id": 4, "team_name": "Aston Villa", "matches_played": 20, "wins": 1, "draws": 6, "losses": 13}, {"team_id": 5, "team_name": "Fulham", "matches_played": 31, "wins": 18, "draws": 1, "losses": 12}, {"team_id": 6, "team_name": "Burnley", "matches_played": 26, "wins": 6, "draws": 9, "losses": 11}, {"team_id": 7, "team_name": "Newcastle United", "matches_played": 33, "wins": 11, "draws": 10, "losses": 12}, {"team_id": 8, "team_name": "Sheffield United", "matches_played": 20, "wins": 18, "draws": 2, "losses": 0}, {"team_id": 9, "team_name": "Luton Town", "matches_played": 5, "wins": 4, "draws": 0, "losses": 1}, {"team_id": 10, "team_name": "Everton", "matches_played": 14, "wins": 2, "draws": 6, "losses": 6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["team_name", "points", "position", "tier"], "rows": [["Sheffield United", 56, 1, "Tier 1"], ["Fulham", 55, 2, "Tier 1"], ["Newcastle United", 43, 3, "Tier 1"], ["Chelsea", 41, 4, "Tier 1"], ["Burnley", 27, 5, "Tier 2"], ["Nottingham Forest", 24, 6, "Tier 2"], ["Everton", 12, 7, "Tier 2"], ["Luton Town", 12, 7, "Tier 2"], ["Liverpool", 11, 9, "Tier 3"], ["Aston Villa", 9, 10, "Tier 3"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`NTILE(3)`:** It balances row counts but can separate teams with equal points, so it does not honor the higher-tier tie rule.
- **`DENSE_RANK`:** It keeps ties together but changes numeric positions by removing gaps. The examples require competition positions from `RANK`.
- **Percent-rank functions:** `PERCENT_RANK` and `CUME_DIST` have different boundary semantics, especially for ties, and do not directly reproduce the stated ceiling thresholds.
- **CTE for points first, second CTE for windows:** This could avoid repeating the points expression inside `RANK` and make stages even more explicit. The source keeps both computations in one CTE.
- **Fewer than three teams:** Ceiling thresholds can overlap, but top-to-bottom `CASE` evaluation still gives a deterministic highest applicable tier.
- **Team count not divisible by three:** `CEIL` allocates cumulative cutoffs upward, with the remainder effectively reducing the bottom nominal group before tie expansion.
- **Tie at the first boundary:** A tied block whose rank is at most the first cutoff is entirely Tier 1, even if later rows extend beyond the nominal top-third row count.
- **Tie at the second boundary:** The same logic keeps the block in Tier 2.
- **Tie beginning after a boundary:** Its shared rank is already in the lower tier, so the whole block remains there; it does not actually straddle the ranked cutoff.
- **All teams tied:** Every team has position one and enters Tier 1. This follows the instruction that boundary ties go to the higher tier, even though it produces an expanded top tier.
- **Text ordering:** Team names use MySQL collation rules for the final ascending tie order.
- **Null wins or draws:** The source does not replace nulls with zero. Intended rows must contain usable statistics for the arithmetic and rank policy to be meaningful.
- **Ordinal order references:** `ORDER BY 2, 1` is concise but coupled to select-column positions; aliases would be more robust to later projection changes.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t\log t)$. Let $t$ be the number of teams. Calculating points and total count is linear. Ranking requires ordering rows by points, and final presentation may require an ordering by points and name. The general time bound is $O(t\log t)$.
- **Auxiliary Space Complexity:** $O(t)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
