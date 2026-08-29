# Guided Example: Build the Equation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Terms": [{"power": 0, "factor": -100}]}}`
- **Required output:** `{"columns": ["equation"], "rows": [["-100=0"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Terms`

The objective is to compute `{"columns": ["equation"], "rows": [["-100=0"]]}` from `{"tables": {"Terms": [{"power": 0, "factor": -100}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Format one term according to its power

The CTE `T` converts every `Terms` row into a text fragment `it` while retaining `power` for later ordering.

Every term begins with an explicit sign. For a positive factor, the expression creates `'+'` followed by the factor. For a negative factor, using `factor` directly converts its existing minus sign into the string.

The factor is therefore represented by its sign plus absolute magnitude, even though the implementation obtains the negative form through normal numeric-to-string coercion.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Terms": [{"power": 0, "factor": -100}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle the three power shapes

The `CASE power` expression separates the required syntax:

- power 0 returns only the signed factor, with no `X`;
- power 1 appends `X` but no exponent;
- every other power appends `X^` and the numeric power.

Thus factor 3 at power 1 becomes `+3X`, factor -3 at power 0 becomes `-3`, and factor 1 at power 2 becomes `+1X^2`.

The coefficient 1 is not omitted because the required format always includes `<fact>`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort terms by descending power during aggregation

The final aggregate orders fragments by `power DESC` before concatenation. This is necessary because table row order has no semantic guarantee.

Concatenating the signed fragments needs no separator: each fragment already starts with `+` or `-`. Finally, `CONCAT(..., '=0')` appends the required right-hand side.

For powers 2, 1, and 0 with factors 1, -4, and 2, ordered fragments are `+1X^2`, `-4X`, and `+2`. Their concatenation plus `=0` gives `+1X^2-4X+2=0`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["equation"], "rows": [["-100=0"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Terms": [{"power": 0, "factor": -100}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["equation"], "rows": [["-100=0"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Valid MySQL aggregation:** Use `GROUP_CONCAT(it ORDER BY power DESC SEPARATOR '')` instead of the nonstandard exact expression.
- **Concatenate without ordering:** Incorrect because SQL row order is not guaranteed and powers must descend.
- **Omit the leading plus:** The format requires an explicit sign even for the first positive term.
- **Power zero:** Include neither `X` nor an exponent.
- **Power one:** Include `X` but omit `^1`.
- **Coefficient one:** Preserve `1` because the specified term grammar includes the absolute factor.
- **Negative factor:** Its existing minus sign supplies the term sign.
- **Unique power:** Main-problem rows need no pre-aggregation by exponent.
- **Duplicate-power follow-up:** Sum factors by power, discard zero sums, then format.
- **Any input row order:** Ordered aggregation controls final order.
- **Right-hand side:** Append exactly `=0` once after the complete LHS.
- **Dialect mismatch:** The algorithm is sound, but the exact aggregate call is not standard MySQL syntax.
- **Empty separator:** Required because signs already delimit adjacent terms.
- **Single term:** Ordered aggregation returns that one signed fragment, followed by `=0`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N log N)$. Let $N$ be the number of term rows.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
