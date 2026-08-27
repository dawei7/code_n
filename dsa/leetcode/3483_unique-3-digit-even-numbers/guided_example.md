# Guided Example: Unique 3-Digit Even Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"digits": [1, 2, 3, 4]}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of digits called `digits`. Your task is to determine the number of **distinct** three-digit even numbers that can be formed using these digits.

The objective is to compute `12` from `{"digits": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

**Choose positions for the units, tens, and hundreds digits.** The protected source enumerates three indices, not merely three digit values. This distinction enforces the rule that each copy in `digits` can be used only once per number while still allowing equal values from different copies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"digits": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The outer loop chooses index `i` and value `a` for the units place. A decimal number is even exactly when its units digit is even. The bit test `a & 1` is one for an odd digit, so those candidates are skipped. Values $0,2,4,6,8$ continue.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer loop chooses index `i` and value `a` for the units... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The middle loop chooses index `j` and value `b` for the tens place. `i == j` is rejected because the same physical array element cannot fill two positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"digits": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Digit-frequency enumeration:** Count copies of:** - **Digit-frequency enumeration:** Count copies of digits zero through nine, try value triples, and decrement counts temporarily. This matches the manifest and has linear input processing plus constant-domain work.
- **Count valid index triples directly:** This overcounts when duplicate copies produce the same decimal number; a set or value-based enumeration is required.
- **Generate all numbers from 100 through 999:** Checking digit availability is correct and bounded by 900 candidates, but differs from the protected construction.
- **Leading zero:** Zero is legal in the tens or units place but rejected only when chosen as `c` for hundreds.
- **Even units zero:** Numbers ending in zero are correctly considered even.
- **One copy used twice:** Equal indices are forbidden even when the desired digit values match.
- **Two equal copies:** Different indices allow both copies to appear in one number.
- **All copies identical and even:** Many index triples collapse to one distinct number.
- **All units candidates odd:** No even number can be formed and the set stays empty.
- **Insufficient nonzero digits:** If every possible hundreds copy is zero, no three-digit number is added.
- **Distinctness meaning:** The output counts unique numeric values, not the number of ways to select copies.
- **Source-complexity fidelity:** The small constraint makes cubic enumeration fast, but it should not be documented as the unimplemented linear count method.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^3)$. The outer, middle, and inner loops each range over $n$ entries in the worst case. Filters can skip work on particular inputs, but worst-case time is $O(n^3)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
