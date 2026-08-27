# Guided Example: Counting Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `arr`, count how many elements `x` there are, such that $x + 1$ is also in `arr`. If there are duplicates in `arr`, count them separately.

The objective is to compute `2` from `{"arr": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Presence decides qualification, frequency decides contribution

For a value $x$, the condition is simply whether $x+1$ appears anywhere in the array. If it does, every occurrence of $x$ must be counted separately.

For example, in `[1,1,2]`, the value 2 appears once, but both copies of 1 qualify. The answer contribution from value 1 is two, not one and not limited by the frequency of 2.

This suggests grouping equal values first. The algorithm needs:

- A fast presence test for $x+1$.
- The number of copies of $x$ to add when the test succeeds.

A `Counter` supplies both.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the frequency map

`cnt = Counter(arr)` maps each distinct input value to its occurrence count. For:



the relevant mapping is:



Building this map retains duplicate information that a plain set would discard. At the same time, its keys provide expected constant-time membership-like lookups.

Python's Counter has another useful behavior: reading a missing key returns zero instead of raising `KeyError`. Therefore, `cnt[x + 1]` is positive exactly when the successor is present and zero when absent.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt = Counter(arr)` maps each distinct input value to its o... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process one distinct value at a time

The return expression is:



`cnt.items()` yields each distinct value `x` once together with its frequency `v`. The condition tests whether the successor has nonzero frequency.

If the successor exists, the generator yields `v`, thereby counting every copy of `x`. If it does not, the generator yields nothing for this key.

Summing these contributions gives the total number of qualifying array positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Set plus original-array scan:** Build `set(arr:** - **Set plus original-array scan:** Build `set(arr)`, then add one for each original `x` whose successor is in the set. It has the same expected $O(n)$ time and naturally counts duplicates.
- **Incorrect set-key scan:** Iterating only unique values and adding one undercounts repeated `x` values.
- **Direct list membership:** Testing `x + 1 in arr` for every element uses linear search and can take $O(n^2)$ time.
- **Sort and count runs:** After sorting, compare adjacent distinct runs and add the earlier run length when values differ by one. This takes $O(n\log n)$ time.
- **Fixed frequency array:** Values lie between 0 and 1000, so an array of counts can replace the hash map with constant bounded storage.
- **Duplicate current values:** Every copy contributes when one successor exists; using frequency `v` handles them together.
- **Duplicate successor values:** More than one successor copy does not increase the contribution of `x`.
- **Largest value:** If its successor is absent, its frequency contributes zero.
- **Gaps larger than one:** Only exact successor $x+1$ matters; a later value $x+2$ does not qualify `x`.
- **Counter missing-key behavior:** `cnt[x+1]` returns zero without inserting a meaningful positive count, making it safe as a Boolean test.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let $n$ be the array length and $U$ the number of distinct values. Building the Counter takes expected $O(n)$ time. Iterating its $U$ entries and performing expected constant-time successor lookups costs $O(U)$. Since $U \le n$, total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
