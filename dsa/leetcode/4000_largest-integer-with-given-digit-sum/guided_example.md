# Guided Example: Largest Integer With Given Digit Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "s": 9}`
- **Required output:** `90`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two non-negative integers `n` and `s`.

The objective is to compute `90` from `{"n": 2, "s": 9}` while avoiding redundant calculations and unnecessary overhead.

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

**First decide whether the requested digit sum is possible.**  A decimal digit is at most `9`. Therefore, an integer with at most `n` digits can have digit sum at most

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "s": 9}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

If `s > 9n`, no arrangement of at most `n` digits can supply enough digit sum, and the source returns `-1` immediately.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `s > 9n`, no arrangement of at most `n` digits can supply... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

If `s <= 9n`, a solution always exists. The required sum can be distributed across `n` positions, with each position receiving between `0` and `9`. When `s > 0`, the greedy construction's first digit will be positive, so it represents an ordinary number without a leading zero. When `s = 0`, the only possible non-negative integer is `0`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `90` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "s": 9}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `90` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all numbers with at most `n` digits::** - **Enumerate all numbers with at most `n` digits:** This examines up to `10^n` candidates. The place-value exchange argument identifies the unique largest digit arrangement directly.
- **Dynamic programming over positions and remaining sum:** A DP can establish feasibility, but feasibility has the simple condition `s <= 9n`, and the lexicographically largest digits follow greedily.
- **Build a digit string:** Appending characters and converting at the end is also `O(n)` time but uses `O(n)` temporary space. The exact source accumulates the integer in constant auxiliary space.
- **Requested sum zero:** The answer is `0` for every legal `n`. Leading or trailing zero representations do not create a different integer.
- **Requested sum above capacity:** If `s > 9n`, even all `9` digits are insufficient, so `-1` is the only valid response.
- **Requested sum equal to capacity:** Every digit must be `9`, and the loop produces an `n`-digit number consisting entirely of nines.
- **Sum smaller than nine:** The result is that sum as the first digit followed by `n - 1` zeros. Those trailing zeros maximize place value without changing the sum.
- **Sum divisible by nine:** The result has a prefix of `s / 9` nines and zeros afterward; there is no partial digit.
- **At most versus exactly `n` digits:** For positive sums, using a more significant available position always increases the number. The greedy result is therefore maximal among shorter candidates as well.
- **No leading-zero problem:** When `s > 0`, `min(s, 9)` is positive at the first iteration. When `s = 0`, the valid integer is the single value zero.
- **Trailing zeros after exhaustion:** The loop must continue after `s` becomes zero. Stopping early would return a smaller integer such as `9` instead of `90`.
- **Input parameter mutation:** Only the local binding `s` is reduced. The method has no mutable input collection and no external side effect.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop performs exactly `n` iterations. Each iteration uses constant-time arithmetic on the bounded result: a minimum, multiplication by ten, addition, and subtraction.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
