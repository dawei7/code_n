# Guided Example: All the Matches of the League

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Teams": [{"team_name": "Leetcode FC"}, {"team_name": "Ahly SC"}, {"team_name": "Real Madrid"}]}}`
- **Required output:** `{"columns": ["home_team", "away_team"], "rows": [["Real Madrid", "Leetcode FC"], ["Real Madrid", "Ahly SC"], ["Leetcode FC", "Real Madrid"], ["Leetcode FC", "Ahly SC"], ["Ahly SC", "Real Madrid"], ["Ahly SC", "Leetcode FC"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Teams`

The objective is to compute `{"columns": ["home_team", "away_team"], "rows": [["Real Madrid", "Leetcode FC"], ["Real Madrid", "Ahly SC"], ["Leetcode FC", "Real Madrid"], ["Leetcode FC", "Ahly SC"], ["Ahly SC", "Real Madrid"], ["Ahly SC", "Leetcode FC"]]}` from `{"tables": {"Teams": [{"team_name": "Leetcode FC"}, {"team_name": "Ahly SC"}, {"team_name": "Real Madrid"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A match is an ordered pair of different teams

The home and away roles matter. A match with team `A` at home and team `B` away is different from the match with `B` at home and `A` away.

Therefore the desired result is not a collection of unordered two-team combinations. It is every ordered pair

`(home_team, away_team)`

whose two names differ.

With `t` teams, each team has `t - 1` possible opponents while it is home, so the output contains `t(t - 1)` rows.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Teams": [{"team_name": "Leetcode FC"}, {"team_name": "Ahly SC"}, {"team_name": "Real Madrid"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use two independent aliases of the same table

The query reads `Teams` twice:

- `t1` supplies the home-team candidate;
- `t2` supplies the away-team candidate.

Joining a table to itself forms every possible pairing between a row from the first role and a row from the second role. Before filtering, this includes `t^2` ordered pairs.

Aliases are required because both sources have a column named `team_name`. `t1.team_name` and `t2.team_name` make the role of each reference unambiguous.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Remove self-matches

The condition

`t1.team_name != t2.team_name`

eliminates pairs in which the same team occupies both roles. The uniqueness guarantee means equal names identify the same team, so this test removes exactly the `t` diagonal self-pairs.

Every remaining row contains two distinct teams and is a legal match.

The query uses `JOIN Teams AS t2` without an `ON` relation and places the relationship in `WHERE`. In MySQL this acts as a Cartesian self-join followed by the inequality filter. Writing `CROSS JOIN` would make the Cartesian intent more explicit, while `JOIN ... ON t1.team_name != t2.team_name` would express the same result.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["home_team", "away_team"], "rows": [["Real Madrid", "Leetcode FC"], ["Real Madrid", "Ahly SC"], ["Leetcode FC", "Real Madrid"], ["Leetcode FC", "Ahly SC"], ["Ahly SC", "Real Madrid"], ["Ahly SC", "Leetcode FC"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Teams": [{"team_name": "Leetcode FC"}, {"team_name": "Ahly SC"}, {"team_name": "Real Madrid"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["home_team", "away_team"], "rows": [["Real Madrid", "Leetcode FC"], ["Real Madrid", "Ahly SC"], ["Leetcode FC", "Real Madrid"], ["Leetcode FC", "Ahly SC"], ["Ahly SC", "Real Madrid"], ["Ahly SC", "Leetcode FC"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`CROSS JOIN` with a WHERE filter:** This is the clearest spelling of the same Cartesian pairing and inequality logic.
- **Inequality in the `ON` clause:** `JOIN Teams t2 ON t1.team_name != t2.team_name` returns the same directed pairs.
- **Use `t1.team_name < t2.team_name`:** This emits only one unordered orientation per team pair and would miss the reverse home-away match.
- **Union two orientations of unordered pairs:** Select each pair once, then union its reversal. This is correct but longer than allowing the Cartesian product to generate both naturally.
- **Include equality:** That creates invalid matches in which a team plays itself.
- **One team:** The Cartesian product has one self-pair, the filter removes it, and the correct result is empty.
- **Two teams:** Exactly two rows remain, one for each home-away direction.
- **Unique names:** They ensure equality identifies the same team and prevent duplicate ordered outputs.
- **Duplicate-name invalid input:** Without uniqueness, source-row duplicates could multiply identical match names.
- **Null names:** The stated team-name model is used as an identifier. Under SQL three-valued logic, null inequality would be unknown; valid source data is expected to provide actual unique names.
- **Any output order:** No sort is required, avoiding unnecessary work.
- **Column aliases:** Without them, both output expressions would share the source name `team_name` and fail to present the requested role labels clearly.
- **Output-size lower bound:** Any correct solution must produce quadratic rows for many teams, so quadratic time is inherent.
- **No aggregation:** Each pair is already one desired match and should not be grouped.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t^2)$. Let `t` be the number of teams. The Cartesian self-join considers `t^2` candidate row pairs and filters `t` self-pairs, so time is `O(t^2)`. This is also asymptotically unavoidable because the required output itself contains `t(t-1) = O(t^2)` rows.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
