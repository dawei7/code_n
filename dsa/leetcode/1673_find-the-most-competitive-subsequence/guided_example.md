# Guided Example: Find the Most Competitive Subsequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 5, 2, 6], "k": 2}`
- **Required output:** `[2, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` and a positive integer `k`, return *the most** competitive** subsequence of *`nums` *of size *`k`.

The objective is to compute `[2, 6]` from `{"nums": [3, 5, 2, 6], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Lexicographic quality is decided as early as possible

Two length-`k` subsequences are compared at their first differing position. A smaller value there wins regardless of all later values. The algorithm should therefore discard an already selected large ending value when a smaller current value can legally take its place.

A stack is ideal for this decision. Its contents are always a subsequence of the processed prefix because values are appended in input order. Its last value is the most recently selected one and is the only value that can be removed without disturbing the order of earlier selections.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 5, 2, 6], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When a previous value should be removed

For current value `v` at index `i`, the loop removes the stack top only when all three conditions hold:

1. `stk` is nonempty;
2. `stk[-1] > v`, so replacing the top with `v` improves the earliest position that changes;
3. `len(stk) + n - i > k`, so enough values remain to finish a length-`k` answer after one removal.

The third condition deserves careful counting. At index `i`, there are `n - i` values still available including the current `v`. Before popping, the maximum possible final length using the current stack plus all not-yet-consumed values is `len(stk) + n - i`. If this number is greater than `k`, at least one selected value may safely be discarded. After a pop it decreases by one; the loop rechecks before possibly popping again.

If it equals `k`, every selected and remaining value is required. Popping would make it impossible to reach the demanded length, even if `v` is smaller.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For current value `v` at index `i`, the loop removes the sta... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the comparison is strict

The loop pops only when `stk[-1] > v`. If the values are equal, replacing the earlier occurrence with the later one does not improve the value sequence and throws away flexibility: the earlier copy leaves more future indices available. Keeping it is therefore at least as good.

Repeated pops are useful. A very small current value may improve the subsequence by replacing several larger values at the end, provided the feasibility count allows all removals.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 5, 2, 6], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit deletion budget:** Initialize `drop =:** - **Explicit deletion budget:** Initialize `drop = n-k`, pop while the top is larger and `drop > 0`, then return the first `k` values. This is equivalent to the source’s remaining-capacity inequality.
- **Deque:** End-only stack operations are sufficient; a deque adds no benefit unless the implementation later removes a prefix separately.
- **Enumerate every subsequence:** There are combinatorially many length-`k` choices, so exhaustive comparison is infeasible.
- **Sort the values:** Sorting destroys original index order and can produce a sequence that is not a subsequence.
- **`k == n`:** The feasibility expression never permits a pop, so every input value is appended and the original array is returned.
- **`k == 1`:** Safe pops discard larger selected values while future choices remain, leaving the smallest value, with the earliest occurrence retained on ties.
- **Strictly increasing input:** No top exceeds the current value. The stack fills with the first `k` entries, which are lexicographically smallest because skipping one would replace it with a larger later value.
- **Strictly decreasing input:** Values are repeatedly popped while the remaining capacity permits, choosing the latest small values without losing the ability to reach length `k`.
- **Duplicate values:** Equal tops are not popped. Keeping the earlier equal occurrence preserves more choices for later positions.
- **Stack already full:** A smaller current value may still enter by first popping; a non-improving value is ignored.
- **Several consecutive pops:** The feasibility inequality is recomputed after each pop, so the algorithm stops exactly before it would become impossible to collect `k` values.
- **Zero-valued elements:** They are valid and naturally displace larger stack endings whenever capacity allows.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `nums`. Every input value is considered once and appended at most once. A value that is popped never returns to the stack, so across the entire run there are at most `n` pops. Although the `while` loop can run many times in one iteration, total stack work is $O(n)$.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
