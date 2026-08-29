# Guided Example: Classifying Triangles by Lengths

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Triangles": [{"A": 20, "B": 20, "C": 23}, {"A": 20, "B": 20, "C": 20}, {"A": 20, "B": 21, "C": 22}, {"A": 13, "B": 14, "C": 30}]}}`
- **Required output:** `{"columns": ["triangle_type"], "rows": [["Isosceles"], ["Equilateral"], ["Scalene"], ["Not A Triangle"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Triangles`

The objective is to compute `{"columns": ["triangle_type"], "rows": [["Isosceles"], ["Equilateral"], ["Scalene"], ["Not A Triangle"]]}` from `{"tables": {"Triangles": [{"A": 20, "B": 20, "C": 23}, {"A": 20, "B": 20, "C": 20}, {"A": 20, "B": 21, "C": 22}, {"A": 13, "B": 14, "C": 30}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Reject invalid triples before classifying equality.** Three side lengths form a nondegenerate triangle only when all strict triangle inequalities hold:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Triangles": [{"A": 20, "B": 20, "C": 23}, {"A": 20, "B": 20, "C": 20}, {"A": 20, "B": 21, "C": 22}, {"A": 13, "B": 14, "C": 30}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

`A + B <= C OR A + C <= B OR B + C <= A`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["triangle_type"], "rows": [["Isosceles"], ["Equilateral"], ["Scalene"], ["Not A Triangle"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Triangles": [{"A": 20, "B": 20, "C": 23}, {"A": 20, "B": 20, "C": 20}, {"A": 20, "B": 21, "C": 22}, {"A": 13, "B": 14, "C": 30}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["triangle_type"], "rows": [["Isosceles"], ["Equilateral"], ["Scalene"], ["Not A Triangle"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort side values per row:** Then only the two-smallest sum needs testing, but expressing a three-value sort in SQL is less direct than symmetric inequalities.
- **Use `GREATEST` and total sum:** Validity can be expressed as total minus largest greater than largest. The current conditions are clearer and avoid null-propagation surprises beyond normal comparisons.
- **Count distinct side lengths:** For valid rows, one, two, or three distinct lengths map to equilateral, isosceles, or scalene. Per-row distinct counting is more cumbersome than direct equality.
- **Degenerate equality:** A sum equal to the third side is `Not A Triangle` because the inequalities are strict.
- **Equilateral row:** It must be checked before isosceles to receive the requested specific label.
- **Exactly two equal sides:** Exactly one of the three pairwise comparisons is true.
- **All sides different:** Equality sum is zero, so a valid row reaches scalene.
- **Nonpositive sides:** The schema excerpt does not state positivity; the all-inequalities check rejects ordinary zero or negative configurations in many cases, but explicit positivity would be safer outside the intended dataset.
- **NULL values:** A primary-key tuple normally makes these columns non-null in MySQL. If nulls were allowed, three-valued logic would require explicit handling.
- **Any order:** No final sort is necessary because the statement permits arbitrary output order.
- **CASE short-circuit semantics:** MySQL returns the result of the first true `WHEN`. Later equality tests cannot overwrite an invalid classification, which is exactly why branch ordering forms part of correctness.
- **Why equality sum cannot be two:** For ordinary values, if $A=B$ and $B=C$, transitivity also gives $A=C$, producing three true comparisons. Otherwise at most one pair is equal. The only possible sums are therefore zero, one, or three.
- **Column-name case:** The lowercase `c` in `B = c` resolves to column `C` under MySQL's identifier rules; it is not a separate variable or string literal.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. For $R$ table rows, the query performs a fixed number of additions, comparisons, and Boolean operations per row. Logical time is $O(R)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
