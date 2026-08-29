# Guided Example: Students Report By Geography

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Student": [{"name": "Jane", "continent": "America"}, {"name": "Pascal", "continent": "Europe"}, {"name": "Xi", "continent": "Asia"}, {"name": "Jack", "continent": "America"}]}}`
- **Required output:** `{"columns": ["America", "Asia", "Europe"], "rows": [["Jack", "Xi", "Pascal"], ["Jane", null, null]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Student`

The objective is to compute `{"columns": ["America", "Asia", "Europe"], "rows": [["Jack", "Xi", "Pascal"], ["Jane", null, null]]}` from `{"tables": {"Student": [{"name": "Jane", "continent": "America"}, {"name": "Pascal", "continent": "Europe"}, {"name": "Xi", "continent": "Asia"}, {"name": "Jack", "continent": "America"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**The desired table is a rank-aligned pivot.** Each continent supplies an alphabetically sorted list of names. Row 1 should contain the first name from America, the first from Asia, and the first from Europe; row 2 should contain the second name from each list; and so on. A missing name at a rank becomes `NULL`. SQL rows do not initially contain that cross-continent alignment key, so the query first creates one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Student": [{"name": "Jane", "continent": "America"}, {"name": "Pascal", "continent": "Europe"}, {"name": "Xi", "continent": "Asia"}, {"name": "Jack", "continent": "America"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Assign an independent rank inside every continent.** The CTE computes

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS rk`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["America", "Asia", "Europe"], "rows": [["Jack", "Xi", "Pascal"], ["Jane", null, null]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Student": [{"name": "Jane", "continent": "America"}, {"name": "Pascal", "continent": "Europe"}, {"name": "Xi", "continent": "Asia"}, {"name": "Jack", "continent": "America"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["America", "Asia", "Europe"], "rows": [["Jack", "Xi", "Pascal"], ["Jane", null, null]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Three ranked CTEs plus joins:** Rank each continent separately, then full-outer-join on rank. This is visually direct but verbose, and MySQL lacks a native full outer join.
- **Session variables:** The editorial's older MySQL technique manually increments one counter per continent. Window functions are clearer, declarative, and less sensitive to evaluation-order behavior.
- **Conditional aggregation with `ROW_NUMBER`:** The exact method is compact and naturally keeps all continents, including when the promised largest partition changes.
- **Explicit final `ORDER BY rk`:** Add this to make alphabetical vertical display guaranteed rather than relying on incidental group output order.
- **Duplicate names:** `ROW_NUMBER` gives each occurrence its own rank, so duplicates are preserved as required.
- **A continent with no students:** Its conditional aggregate is `NULL` at every rank produced by other continents.
- **Only one populated continent:** Every output row contains one name and two `NULL` values.
- **Unequal continent sizes:** Shorter lists correctly become `NULL` after their last rank.
- **Unexpected continent value:** It receives ranks in the CTE and can create groups, but none of the three conditional columns displays its name. The stated domain must remain America, Asia, and Europe.
- **Equal names within one continent:** Their relative row numbers are nondeterministic, but the visible values are identical, so the report is unchanged.
- **Column order:** The three select expressions are deliberately written America, Asia, Europe; changing their order would violate the requested schema even if the values remained correct.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of rows in `Student`. Computing `ROW_NUMBER` requires arranging rows by `continent` and `name`. A general sort-based implementation costs $O(R\log R)$ time. Once ranks exist, conditional aggregation scans the rows and groups by rank in $O(R)$ expected time with hashing or $O(R\log R)$ with sorting. The manifest's overall $O(R\log R)$ time bound is therefore appropriate.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
