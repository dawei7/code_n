# Guided Example: Sequential Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"low": 100, "high": 300}`
- **Required output:** `[123, 234]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An integer has *sequential digits* if and only if each digit in the number is one more than the previous digit.

The objective is to compute `[123, 234]` from `{"low": 100, "high": 300}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every sequential-digit number is determined by its first and last digit

A positive decimal number with sequential digits must look like `12`, `2345`, or `6789`. Once the first digit is chosen, every later digit is forced to be one greater. Digits cannot pass nine, and valid multi-digit numbers cannot begin at zero under the problem's range.

The outer loop chooses starting digit `i` from one through eight. Starting at nine cannot produce a two-digit sequential number because ten is not a digit.

Variable `x` begins as that one-digit start. The inner loop chooses successive digits `j` from `i + 1` through nine and performs `x = x * 10 + j`. Multiplication shifts existing decimal digits left, and addition appends the forced next digit.

For start two, `x` evolves through `23`, `234`, `2345`, and so on through `23456789`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"low": 100, "high": 300}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter each generated candidate by the inclusive range

After every appended digit, the code checks `low <= x <= high`. Passing candidates are added to `ans`. The initial one-digit `i` is never checked, which is appropriate because `low >= 10` and answers require at least two digits.

The generation loops do not stop when `x > high`, although they safely could because further appends only increase it. The decimal alphabet is fixed and tiny, so continuing has constant cost.

Likewise, the algorithm does not restrict starting lengths based on the digit counts of `low` and `high`. It generates the complete fixed universe and filters afterward. That choice keeps boundary logic simple: the inclusive comparison alone decides membership, while the constant 36-candidate limit keeps unnecessary work negligible.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why generation is complete

Take any sequential-digit number in the requested range. Its first digit is some `i` from one through eight, and its remaining digits must be `i + 1, i + 2, ...` up to at most nine. The corresponding outer iteration constructs exactly that prefix at one inner-loop step, where the range check includes it.

Conversely, every constructed `x` begins at `i` and appends consecutive increasing digits, so every value admitted to `ans` satisfies the definition. No number is duplicated because its first digit and length uniquely identify it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[123, 234]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"low": 100, "high": 300}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[123, 234]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sliding windows over `"123456789"`:** Every sequential number is a substring. Enumerating window lengths and starts can produce values directly by length and often already in sorted order.
- **Precompute all 36 values:** Store the fixed universe once and filter it for each query. This is useful for many calls but unnecessary for one.
- **Breadth-first digit extension:** Seed digits one through nine and append the next digit. It is more general but adds queue machinery.
- **Inclusive boundaries:** Values equal to `low` or `high` are retained by the chained comparison.
- **No candidate in range:** Sorting an empty list returns `[]`.
- **Range near ten:** `12` is the smallest possible answer.
- **Upper bound one billion:** The largest sequential candidate is `123456789`; no ten-digit sequential number exists.
- **Starting digit nine:** It cannot extend and is correctly omitted from the outer range.
- **Generation order:** A final numerical sort is required because grouping by first digit is not globally ascending.
- **No duplicates:** First digit plus length uniquely determines each generated number.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. With decimal digits fixed to one through nine, at most 36 candidates are constructed and at most 36 values are sorted. Both runtime and output capacity are bounded by constants, so time is $O(1)$ and total space is $O(1)$ under the problem's fixed base and constraints.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
