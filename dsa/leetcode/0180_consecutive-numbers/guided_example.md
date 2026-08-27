# Guided Example: Consecutive Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Logs": [{"id": 1, "num": 5}, {"id": 2, "num": 5}]}}`
- **Required output:** `{"columns": ["ConsecutiveNums"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Logs`

The objective is to compute `{"columns": ["ConsecutiveNums"], "rows": []}` from `{"tables": {"Logs": [{"id": 1, "num": 5}, {"id": 2, "num": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent a three-row window with three aliases

The query reads the `Logs` table three times as `l1`, `l2`, and `l3`. These are
not three different tables; they are three roles for rows in one possible
consecutive window.

The first join requires:

- `l1.id = l2.id - 1`, so the second ID immediately follows the first;
- `l1.num = l2.num`, so their logged values match.

The second join applies the same conditions from `l2` to `l3`. A joined triple
therefore consists of IDs $i,i+1,i+2$ with one common `num`.

The presence of such a triple is exactly evidence that the value appears at
least three times consecutively.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Logs": [{"id": 1, "num": 5}, {"id": 2, "num": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why three rows prove “at least three”

A run of exactly three produces one qualifying window. A longer run also
contains at least one three-row window, so it qualifies without needing to
count the entire run.

For a run of four equal values at IDs one through four, the joins produce
windows `(1,2,3)` and `(2,3,4)`. Both prove the same value qualifies.

The query does not require the run to end after `l3`; it tests a minimum length,
not an exact length.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A run of exactly three produces one qualifying window.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Deduplicate qualifying values

`SELECT DISTINCT l2.num AS ConsecutiveNums` returns one row per qualifying
numeric value.

`DISTINCT` is necessary for two reasons. One long run can produce overlapping
three-row windows, and the same number can have separate qualifying runs later
in the log. The required result is a set of values, not one row per witnessed
window.

Any of `l1.num`, `l2.num`, or `l3.num` could be selected because the join proves
they are equal. Choosing the middle alias communicates the center of the
three-row window.

The alias `ConsecutiveNums` exactly matches the required output column.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["ConsecutiveNums"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Logs": [{"id": 1, "num": 5}, {"id": 2, "num": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["ConsecutiveNums"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LAG` window functions:** Compare each row wit:** - **`LAG` window functions:** Compare each row with the preceding two rows in ID order; this directly expresses sequence and handles row-order adjacency with gaps.
- **Run-length grouping:** Detect value changes with window functions, assign run IDs, group, and keep counts at least three.
- **User variables:** Can track a running count in older MySQL, but evaluation order is fragile and requires explicit ordering.
- **Exactly three:** Produces one window and one output value.
- **More than three:** Overlapping windows are collapsed by `DISTINCT`.
- **Separate runs of one value:** Still produce one output row.
- **Only two consecutive rows:** No three-alias chain exists.
- **Alternating values:** Equality joins reject every window.
- **ID gaps:** Direct `id + 1` logic assumes challenge-style consecutive identifiers.
- **Any order:** No final sorting is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of log rows. With the primary-key index, an engine can
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
