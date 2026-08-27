# Guided Example: Maximum Value of an Alternating Sequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "s": 3, "m": 5}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three integers `n`, `s`, and `m`.

The objective is to compute `12` from `{"n": 4, "s": 3, "m": 5}` while avoiding redundant calculations and unnecessary overhead.

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

**Replace the sequence with a sequence of rises and falls.**  The first value is fixed at `s`, so the only freedom is choosing how much each later value rises or falls. Because the sequence must alternate strictly, every adjacent step has a direction:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "s": 3, "m": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- an upward step increases the value by at least `1` and at most `m`;
- a downward step decreases the value by at least `1` and at most `m`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - an upward step increases the value by at least `1` and at ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The lower bound of `1` is important. The elements are integers and the inequalities are strict, so a downward step cannot keep the value unchanged. Likewise, an upward step cannot have size zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "s": 3, "m": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dynamic programming over positions and values::** - **Dynamic programming over positions and values:** One could track reachable high and low values after every position, but `n` can be as large as `10^9`. The extremal rise/fall argument collapses all of that state into one formula.
- **Building the maximizing sequence:** Repeatedly adding `m` and subtracting `1` makes the construction visible, but it takes `O(n)` time and stores information the return value does not require.
- **Starting with a fall:** This orientation is legal, but every upward move is preceded by a loss of at least `1`. It cannot recover the one-unit advantage of rising first.
- **Length one:** There are no adjacent comparisons, so the only element `s` is the answer. This is why the early return must precede the closed formula.
- **Even length:** The last position can be the largest peak, and there are `n / 2` rises.
- **Odd length:** The largest peak occurs one position before the end; the final fall does not reduce the maximum already attained.
- **The case `m = 1`:** Every legal rise and fall must have magnitude exactly `1`. Later peaks cannot exceed the first peak, and the formula correctly returns `s + 1` for every `n > 1`.
- **Strict inequalities:** Treating a fall as allowed to have size zero would incorrectly change each two-step gain from `m - 1` to `m`. The extra `+1` in the final expression follows directly from paying only `q - 1` falls before the last peak.
- **Values below zero:** The fixed start is positive, but the sequence elements are otherwise integers. The maximizing construction never needs a large downward move, so no lower-bound assumption is used.
- **Overflow outside Python:** The product `(n // 2) * (m - 1)` can exceed a 32-bit signed integer even though each individual input fits. Use 64-bit arithmetic in languages with fixed-width integer types.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a constant number of integer comparisons, divisions, multiplications, additions, and subtractions. It never constructs the sequence because the constraints ask only for its maximum possible element.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
