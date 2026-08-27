# Guided Example: Longer Contiguous Segments of Ones than Zeros

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "1101"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary string `s`, return `true`* if the **longest** contiguous segment of *`1`'*s is **strictly longer** than the **longest** contiguous segment of *`0`'*s in *`s`, or return `false`* otherwise*.

The objective is to compute `true` from `{"s": "1101"}` while avoiding redundant calculations and unnecessary overhead.

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

**Measure the longest run of one chosen character.** The helper `f(x)` computes the maximum length of a contiguous segment containing only character `x`. The main method calls it once for one and once for zero, then compares the two results strictly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "1101"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Inside the helper, `cnt` is the length of the current run ending at the most recently scanned character, while `mx` is the longest completed or current run seen anywhere so far.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Inside the helper, `cnt` is the length of the current run en... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Extend a matching run.** When `c == x`, `cnt += 1` extends the current contiguous segment. `mx = max(mx, cnt)` immediately records it if this is a new longest run.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "1101"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One-pass dual tracking:** Maintain the current:** - **One-pass dual tracking:** Maintain the current character, current run length, and maxima for zero and one in one traversal.
- **Split on the opposite bit:** Maximum token length after splitting can work, but creates substring lists and uses `O(n)` space.
- **Regular expressions:** They can find runs but add unnecessary machinery and allocation.
- **All ones:** Longest one run is `n` and longest zero run is zero.
- **All zeros:** Longest one run is zero, so the strict condition is false.
- **Equal maxima:** The answer is false because one must be strictly longer.
- **Alternating input:** Both maximum runs are one when both symbols occur, so the answer is false.
- **Single character one:** The maxima are one and zero, returning true.
- **Single character zero:** The maxima are zero and one, returning false.
- **Run at the end:** Updating `mx` on every match records it without a post-loop branch.
- **Several separate runs:** Resetting `cnt` prevents their lengths from being combined.
- **Input preservation:** The immutable string is scanned twice and never modified.
- **Run of length one between separators:** It raises `mx` only if no longer run has appeared; surrounding opposite bits keep it separate.
- **Historical maximum after reset:** Resetting `cnt` never resets `mx`, so a strong early segment remains recorded.
- **Strict comparison direction:** The method asks whether the one-run is longer than the zero-run, so reversing operands would solve the opposite question.
- **No integer conversion:** Direct character comparison avoids parsing and exactly matches the binary symbols supplied.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Each call to `f` visits all `n` characters and performs constant work. Two calls take `2n` operations, which is `O(n)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
