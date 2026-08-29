# Guided Example: Find the Largest Almost Missing Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 9, 2, 1, 7], "k": 3}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `7` from `{"nums": [3, 9, 2, 1, 7], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

**Count windows containing a value, not just its occurrences.** An integer is almost missing when it appears in exactly one length-$k$ subarray. Repeated appearances inside one window count as presence in that one window, while one occurrence can belong to several overlapping windows. The source avoids explicit window enumeration by separating the two extreme window sizes from the general case.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 9, 2, 1, 7], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**When \(k=1\), windows and positions are identical.** Every length-one subarray contains exactly one array position. A value appears in exactly as many size-one windows as its total frequency in `nums`. The source builds `Counter(nums)` and considers exactly the entries whose count is one. `max(..., default=-1)` returns the largest globally unique value or $-1$ when none exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For `nums = [0,0]` and `k=1`, zero has frequency two, so the generator contains no candidate and the answer is $-1$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 9, 2, 1, 7], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count raw occurrences for every \(k\):** A single occurrence can lie in several overlapping windows, so frequency alone is insufficient except when `k == 1` or for the endpoint uniqueness test.
- **Enumerate every window and every distinct value in it:** This can require $O(nk)$ work and hides the endpoint structure.
- **Sliding sets with a per-value window counter:** It is correct but more machinery than needed for this special question.
- **Interior unique value:** Even one occurrence belongs to at least two windows when $1<k<n$, so uniqueness does not make it a candidate.
- **Duplicate endpoint value:** Any second occurrence creates presence in another window and invalidates that endpoint candidate.
- **Same value at both endpoints:** Because `k < n` in the middle branch, the two endpoint windows differ, so the value is not almost missing.
- **\(k=1\):** Only globally unique values appear in exactly one singleton window.
- **\(k=n\):** Every present value appears in the sole whole-array window, regardless of frequency.
- **One-element array:** Both boundary cases coincide with `k=n=1`, and `max(nums)` returns the sole value.
- **Value zero:** The sentinel is $-1$, so a qualifying zero is preserved as a valid answer.
- **No candidate:** Empty counter filtering or two rejected endpoints correctly yields $-1$.
- **Helper parameter naming:** The nested `f(k)` receives an array index, not the original window size; reading it as an index is necessary to understand the source.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For `k == 1`, building the counter and scanning its entries take $O(n)$ time and $O(n)$ space in the worst case. For `k == n`, `max(nums)` takes $O(n)$ time and $O(1)$ auxiliary space. In the middle case, helper `f` is called twice and each scans at most $n$ positions, so time is $O(n)$ and auxiliary space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
