# Guided Example: Top Percentile Fraud

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Fraud": [{"policy_id": 1, "state": "California", "fraud_score": 0.92}, {"policy_id": 2, "state": "California", "fraud_score": 0.68}, {"policy_id": 3, "state": "California", "fraud_score": 0.17}, {"policy_id": 4, "state": "New York", "fraud_score": 0.94}, {"policy_id": 5, "state": "New York", "fraud_score": 0.81}, {"policy_id": 6, "state": "New York", "fraud_score": 0.77}, {"policy_id": 7, "state": "Texas", "fraud_score": 0.98}, {"policy_id": 8, "state": "Texas", "fraud_score": 0.97}, {"policy_id": 9, "state": "Texas", "fraud_score": 0.96}, {"policy_id": 10, "state": "Florida", "fraud_score": 0.97}, {"policy_id": 11, "state": "Florida", "fraud_score": 0.98}, {"policy_id": 12, "state": "Florida", "fraud_score": 0.78}, {"policy_id": 13, "state": "Florida", "fraud_score": 0.88}, {"policy_id": 14, "state": "Florida", "fraud_score": 0.66}]}}`
- **Required output:** `{"columns": ["policy_id", "state", "fraud_score"], "rows": [[1, "California", 0.92], [11, "Florida", 0.98], [4, "New York", 0.94], [7, "Texas", 0.98]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Fraud`

The objective is to compute `{"columns": ["policy_id", "state", "fraud_score"], "rows": [[1, "California", 0.92], [11, "Florida", 0.98], [4, "New York", 0.94], [7, "Texas", 0.98]]}` from `{"tables": {"Fraud": [{"policy_id": 1, "state": "California", "fraud_score": 0.92}, {"policy_id": 2, "state": "California", "fraud_score": 0.68}, {"policy_id": 3, "state": "California", "fraud_score": 0.17}, {"policy_id": 4, "state": "New York", "fraud_score": 0.94}, {"policy_id": 5, "state": "New York", "fraud_score": 0.81}, {"policy_id": 6, "state": "New York", "fraud_score": 0.77}, {"policy_id": 7, "state": "Texas", "fraud_score": 0.98}, {"policy_id": 8, "state": "Texas", "fraud_score": 0.97}, {"policy_id": 9, "state": "Texas", "fraud_score": 0.96}, {"policy_id": 10, "state": "Florida", "fraud_score": 0.97}, {"policy_id": 11, "state": "Florida", "fraud_score": 0.98}, {"policy_id": 12, "state": "Florida", "fraud_score": 0.78}, {"policy_id": 13, "state": "Florida", "fraud_score": 0.88}, {"policy_id": 14, "state": "Florida", "fraud_score": 0.66}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**What the CTE actually ranks.** The window function partitions rows by `state`, so each state's ranking starts independently. Within a state, it orders `fraud_score DESC`, assigning the highest score rank 1.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Fraud": [{"policy_id": 1, "state": "California", "fraud_score": 0.92}, {"policy_id": 2, "state": "California", "fraud_score": 0.68}, {"policy_id": 3, "state": "California", "fraud_score": 0.17}, {"policy_id": 4, "state": "New York", "fraud_score": 0.94}, {"policy_id": 5, "state": "New York", "fraud_score": 0.81}, {"policy_id": 6, "state": "New York", "fraud_score": 0.77}, {"policy_id": 7, "state": "Texas", "fraud_score": 0.98}, {"policy_id": 8, "state": "Texas", "fraud_score": 0.97}, {"policy_id": 9, "state": "Texas", "fraud_score": 0.96}, {"policy_id": 10, "state": "Florida", "fraud_score": 0.97}, {"policy_id": 11, "state": "Florida", "fraud_score": 0.98}, {"policy_id": 12, "state": "Florida", "fraud_score": 0.78}, {"policy_id": 13, "state": "Florida", "fraud_score": 0.88}, {"policy_id": 14, "state": "Florida", "fraud_score": 0.66}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`RANK` gives tied scores the same rank and leaves gaps afterward. For example, scores 100, 100, and 90 receive ranks 1, 1, and 3.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**What the outer filter actually returns.** `WHERE rk = 1` keeps only policies tied for the maximum fraud score in their state. If the maximum is unique, exactly one policy is returned for that state. If several policies share the maximum, all are returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["policy_id", "state", "fraud_score"], "rows": [[1, "California", 0.92], [11, "Florida", 0.98], [4, "New York", 0.94], [7, "Texas", 0.98]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Fraud": [{"policy_id": 1, "state": "California", "fraud_score": 0.92}, {"policy_id": 2, "state": "California", "fraud_score": 0.68}, {"policy_id": 3, "state": "California", "fraud_score": 0.17}, {"policy_id": 4, "state": "New York", "fraud_score": 0.94}, {"policy_id": 5, "state": "New York", "fraud_score": 0.81}, {"policy_id": 6, "state": "New York", "fraud_score": 0.77}, {"policy_id": 7, "state": "Texas", "fraud_score": 0.98}, {"policy_id": 8, "state": "Texas", "fraud_score": 0.97}, {"policy_id": 9, "state": "Texas", "fraud_score": 0.96}, {"policy_id": 10, "state": "Florida", "fraud_score": 0.97}, {"policy_id": 11, "state": "Florida", "fraud_score": 0.98}, {"policy_id": 12, "state": "Florida", "fraud_score": 0.78}, {"policy_id": 13, "state": "Florida", "fraud_score": 0.88}, {"policy_id": 14, "state": "Florida", "fraud_score": 0.66}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["policy_id", "state", "fraud_score"], "rows": [[1, "California", 0.92], [11, "Florida", 0.98], [4, "New York", 0.94], [7, "Texas", 0.98]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rank plus partition count:** Compute `RANK` and `COUNT(*) OVER (PARTITION BY state)`, then filter rank at or below `CEIL(count * 0.05)`. This matches the manifest's intended boundary and includes score ties.
- **`PERCENT_RANK`:** Filtering at or below 0.05 can express percentile position, but its denominator and small-group behavior should be checked against the exact ceiling definition.
- **`NTILE(20)`:** Selecting tile one is tempting, but tile sizing and ties may not match the required top-five-percent semantics.
- **One policy in a state:** The source returns it, and the ceiling top 5% also contains it.
- **Twenty or fewer distinct policies:** The ceiling cutoff is one, so maximum-only is correct unless tie rules expand the boundary.
- **More than twenty policies:** Lower-ranked policies can belong to the top 5%, exposing the source defect.
- **Several maximum-score ties:** `RANK=1` returns all of them. Depending on tie semantics, this may exceed the numeric 5% count but is consistent with including boundary ties.
- **Tie at a lower cutoff:** The exact query never reaches that cutoff and misses all such rows.
- **Output ordering:** The final three ordinal keys correctly implement state ascending, score descending, and policy ID ascending.
- **Manifest mismatch:** The source does not compute state population or a five-percent threshold, so its advertised summary is inaccurate.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. For $R$ fraud rows, the window engine partitions and orders rows by state and descending score. A typical bound is $O(R\log R)$ time, with $O(R)$ temporary space for sorting and window state. Final ordering of the selected rows is within the same asymptotic bound.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
