# Guided Example: Maximum Odd Binary Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "010"}`
- **Required output:** `"001"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **binary** string `s` that contains at least one `'1'`.

The objective is to compute `"001"` from `{"s": "010"}` while avoiding redundant calculations and unnecessary overhead.

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

**Oddness fixes the final bit.** In binary, every position except the last represents a multiple of two: $2^1,2^2,\ldots$. Only the rightmost position contributes $2^0=1$, so a binary number is odd exactly when its final character is `"1"`. The input guarantees at least one one-bit, which means an odd rearrangement is always possible.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "010"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

One `"1"` must therefore be reserved for the last position. After reserving it, the remaining bits should be arranged to make the fixed-length binary string as large as possible.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | One `"1"` must therefore be reserved for the last position.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Why all remaining ones go left.** In a fixed-length binary number, an earlier position has greater place value than every later position. If a `"0"` appears before a `"1"`, swapping them increases the number: the one moves to a higher power of two and the zero moves to a lower one. Repeating this exchange until no such inversion remains puts every available one before every zero. No other arrangement of the same remaining bits can be larger.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"001"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "010"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"001"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort then rearrange:** Sorting the characters :** - **Sort then rearrange:** Sorting the characters and moving a one to the end works, but costs $O(n\log n)$ time when a linear count is sufficient.
- **Two-pointer partition:** Move ones left and zeros right, then reserve the last one. It remains $O(n)$ but needs mutable character storage and more moving parts.
- **Exactly one one-bit:** That bit must be last, so every preceding character is zero; leading zeros are allowed.
- **All one-bits:** There are no zeros, and the construction returns the unchanged all-ones string, which is already odd and maximal.
- **Length one:** The guarantee forces `s = "1"`; both repeated prefixes are empty and the final one is returned.
- **Leading zeros:** They do not invalidate the answer because the required return value is a fixed-length rearranged string, not a canonical integer spelling.
- **Missing-one scenario:** The source relies on the promise that at least one `"1"` exists. Without it, no odd rearrangement would be possible and `cnt - 1` would be negative.
- **Lexicographic versus numeric order:** For equal-length binary strings, lexicographic order and numeric order agree, so placing ones as far left as possible maximizes both.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. `s.count("1")` scans the input once, taking $O(n)$ time. Repeating and concatenating strings creates an output of length $n$, also taking $O(n)$ time. Overall time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
