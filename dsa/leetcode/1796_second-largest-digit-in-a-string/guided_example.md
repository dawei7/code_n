# Guided Example: Second Largest Digit in a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "dfa12321afd"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an alphanumeric string `s`, return *the **second largest** numerical digit that appears in *`s`*, or *`-1`* if it does not exist*.

The objective is to compute `2` from `{"s": "dfa12321afd"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track the two largest distinct digits while scanning

The answer depends on distinct numerical digits, not on how many times each digit appears. The protected solution keeps two variables:

- `a` is the largest distinct digit seen so far;
- `b` is the second-largest distinct digit seen so far.

Both start at -1. Every valid digit is between 0 and 9, so -1 is smaller than any possible digit and also serves as the required return value when a second distinct digit never appears.

The loop reads every character `c` in `s`. Letters are ignored. When `c.isdigit()` is true, `int(c)` converts the one-character digit to its numerical value `v`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "dfa12321afd"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Update when a new largest digit appears

If `v > a`, the new value becomes the largest. The old largest does not disappear; it becomes the best candidate for second largest. The simultaneous assignment

`a, b = v, a`

stores the new largest in `a` and the previous value of `a` in `b`.

For example, if the tracked digits are `a = 5` and `b = 3` and the scan finds 8, the state becomes `a = 8` and `b = 5`. Value 3 is no longer among the top two.

Simultaneous assignment matters conceptually: Python evaluates the right-hand values before changing either variable, so `b` receives the old `a` rather than the new `v`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `v > a`, the new value becomes the largest.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update when a value belongs strictly between them

If `v` is not greater than `a`, it cannot replace the largest. It replaces the second largest only when

`b < v < a`.

Both inequalities are strict. The upper inequality excludes another copy of the largest, because the second-largest digit must be distinct. The lower inequality excludes values that cannot improve `b`, including another copy of the current second largest.

If neither update applies, the digit is a duplicate of an existing maximum or is too small to affect the top two.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "dfa12321afd"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boolean array of ten digits:** Mark each encou:** - **Boolean array of ten digits:** Mark each encountered digit and scan from 9 downward afterward. This is also $O(n)$ time and $O(1)$ space, but uses more explicit state.
- **Set plus sorting:** Collecting distinct digits and sorting them works, yet it obscures the one-pass top-two invariant.
- **Sort all digit occurrences:** Duplicates must then be skipped, and copying plus sorting is unnecessary.
- **Convert every character directly:** Calling `int` on a letter would fail, so classification must occur first.
- **No digits:** Both variables remain -1, and returning -1 correctly reports no second largest digit.
- **Exactly one distinct digit:** The largest is tracked in `a` while `b` remains -1.
- **Repeated largest digit:** Strict comparison prevents it from being mistaken for the second-largest distinct digit.
- **Repeated second-largest digit:** It leaves `b` unchanged and is counted only as the same value.
- **Digit zero:** Zero is greater than the -1 sentinel and is handled normally.
- **Digits zero and one only:** The final state becomes `a = 1` and `b = 0`, so zero can be a valid answer.
- **Descending encounter order:** A smaller digit can fill `b` without changing `a`.
- **Ascending encounter order:** Every new maximum shifts the old maximum into `b`.
- **Letters between digits:** They have no effect on the invariant.
- **ASCII input guarantee:** It makes `isdigit` followed by `int` safe for every valid digit character.
- **Input preservation:** The solution reads the string without constructing a modified copy.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. The loop examines every character once and performs constant work, giving $O(n)$ time. It may not stop early because a larger digit near the end can change both tracked positions.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
