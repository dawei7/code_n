# Guided Example: Design an ATM Machine

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"], "arguments": [[], [[0, 0, 1, 2, 1]], [600], [[0, 1, 0, 1, 1]], [600], [550]]}`
- **Required output:** `[null, null, [0, 0, 1, 0, 1], null, [-1], [0, 1, 0, 0, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an ATM machine that stores banknotes of `5` denominations: `20`, `50`, `100`, `200`, and `500` dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.

The objective is to compute `[null, null, [0, 0, 1, 0, 1], null, [-1], [0, 1, 0, 0, 1]]` from `{"operations": ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"], "arguments": [[], [[0, 0, 1, 2, 1]], [600], [[0, 1, 0, 1, 1]], [600], [550]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store inventory in the contract's denomination order

The ATM has exactly five denominations. `d = [20, 50, 100, 200, 500]` stores their values, and `cnt` stores available counts at matching indices. `m` is five.

This parallel layout means index zero always refers to twenty-dollar notes and index four to five-hundred-dollar notes. Returned withdrawal arrays must use the same order.

The constructor initializes every count to zero, matching an empty ATM.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"], "arguments": [[], [[0, 0, 1, 2, 1]], [600], [[0, 1, 0, 1, 1]], [600], [550]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Deposit is component-wise addition

`deposit` enumerates the five supplied counts and adds each to the corresponding inventory slot:

`cnt[i] += x`.

Deposits never replace existing notes; they accumulate. Zero entries leave a denomination unchanged. Because the input order is guaranteed, no denomination lookup is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Withdrawal must obey mandated greedy priority

This is not a general “find any combination of notes” problem. The ATM is required to try larger denominations first, even when that choice later makes the request fail.

`reversed(range(m))` visits indices four down to zero, corresponding to values `500, 200, 100, 50, 20`. For denomination `d[i]`, the machine could use at most `amount // d[i]` notes without exceeding the current remainder, but it may own fewer. Therefore, it selects

`min(amount // d[i], cnt[i])`.

That count is stored in `ans[i]`, and its value is subtracted from `amount`.

Taking the maximum possible count at every denomination exactly implements “prioritizes using banknotes of larger values.” The algorithm must not backtrack to replace a selected large note with smaller ones.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, [0, 0, 1, 0, 1], null, [-1], [0, 1, 0, 0, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"], "arguments": [[], [[0, 0, 1, 2, 1]], [600], [[0, 1, 0, 1, 1]], [600], [550]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, [0, 0, 1, 0, 1], null, [-1], [0, 1, 0, 0, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **General coin-change search:** It could find a combination that succeeds when greedy fails, but that would violate the ATM's mandated behavior.
- **Backtracking after a greedy dead end:** The `600` example explicitly forbids replacing the selected `500` with three `200` notes.
- **Mutate inventory during planning:** This requires rollback on failure and risks corrupting state. Staging `ans` keeps failure atomic.
- **Deposit zero notes:** The corresponding inventory counts remain unchanged.
- **Withdraw more value than total inventory:** A positive remainder remains and the call returns `[-1]` without modification.
- **Exact large-note match:** The greedy pass uses that note and succeeds immediately for the remaining lower denominations.
- **Insufficient low denominations after large selection:** The request fails even if a smaller-note alternative existed before selecting the large note.
- **Successful withdrawal:** Every used count is subtracted exactly once during commit.
- **Repeated calls:** Each sees the state left by all prior successful operations and deposits.
- **Denomination order:** Internal storage and returned arrays are ascending even though withdrawal processing is descending.
- **Amount not divisible by any available combination:** The nonzero remainder detects failure.
- **Fixed denomination count:** Constant-time claims rely on exactly five supported values.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q)$. Each deposit visits exactly five positions. Each withdrawal performs one five-denomination planning pass and, on success, one five-position commit pass. Every individual operation is therefore `O(1)` time because the denomination count is fixed.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
