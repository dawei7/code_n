# Guided Example: K-diff Pairs in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 1, 4, 1, 5], "k": 2}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums` and an integer `k`, return *the number of **unique** k-diff pairs in the array*.

The objective is to compute `2` from `{"nums": [3, 1, 4, 1, 5], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

The result counts unique **value pairs**, not pairs of array indices. Duplicate occurrences may prove that a pair exists, especially when `k = 0`, but they must not make the same value pair count multiple times.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 1, 4, 1, 5], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Because `k >= 0`, every valid pair can be written canonically as:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

The smaller endpoint `a` uniquely identifies that pair. The solution stores these smaller endpoints in `ans`, a set, so repeated discoveries automatically collapse into one result.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 1, 4, 1, 5], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency map:** For `k > 0`, count keys whose `x + k` exists; for `k = 0`, count values with frequency at least two. It has the same asymptotic bounds.
- **Sort and use two pointers:** It can find each distinct difference in $O(n\log n)$ time, but sorting is slower asymptotically and may modify or copy the input.
- **Check every index pair:** It takes $O(n^2)$ time and requires an additional mechanism to deduplicate value pairs.
- **`k = 0`:** A value qualifies only after a second occurrence; the set prevents further duplicates from increasing the result.
- **One array element:** No earlier complement exists, so the answer is zero.
- **Repeated valid pair:** Every discovery adds the same smaller endpoint and counts once.
- **Reverse arrival order:** The two complement checks make discovery independent of which endpoint appears first.
- **Negative values:** Canonical smaller endpoints and set membership remain valid.
- **No valid pair:** `ans` stays empty and `len(ans)` returns zero.
- **Distinct-index rule:** Delaying `vis.add(x)` until after checks prevents an occurrence from pairing with itself.
- **Large `k`:** Complements may lie far outside observed values; failed set membership simply contributes nothing.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. The solution scans the array once. Each iteration performs a constant number of expected-$O(1)$ set lookups and insertions, giving expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
