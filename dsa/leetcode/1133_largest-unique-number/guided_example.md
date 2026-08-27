# Guided Example: Largest Unique Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 7, 3, 9, 4, 9, 8, 3, 1]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the largest integer that only occurs once*. If no integer occurs once, return `-1`.

The objective is to compute `8` from `{"nums": [5, 7, 3, 9, 4, 9, 8, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Eligibility depends on total frequency

A number is eligible only if it appears exactly once in the entire array. It is not enough to be different from its immediate neighbors or unique within a prefix.

`Counter(nums)` performs one complete frequency pass and maps each distinct value to its total occurrence count.

As Counter reads the array, every occurrence increments exactly one entry. After the scan, `cnt[x]` equals the number of indices whose value is `x`. It contains no positional information because position is irrelevant once total frequency is known.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 7, 3, 9, 4, 9, 8, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter the frequency map

The generator:

`x for x, v in cnt.items() if v == 1`

yields exactly those values whose frequency is one. Values occurring twice or more are skipped, regardless of how large they are.

The generator is lazy, so it does not first allocate a list of all unique candidates. `max` consumes candidates one at a time while retaining the greatest.

Dictionary iteration order does not matter. `max` compares numeric values and produces the same result whether a large unique value is encountered early or late.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The generator:

`x for x, v in cnt.items() if v == 1`

yield... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use a safe default

If no value has frequency one, the generator is empty. Calling `max` without a default would raise an exception.

`default=-1` supplies the required failure result. Input values are between zero and one thousand, so negative one cannot be confused with a legitimate answer. Zero remains a valid unique maximum when it is the only eligible value.

The default is consulted only when the generator yields nothing. It is not inserted as an artificial candidate alongside legal values, so it cannot influence a nonempty maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 7, 3, 9, 4, 9, 8, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed frequency array:** Count indices zero th:** - **Fixed frequency array:** Count indices zero through one thousand, then scan backward for count one. This realizes $O(n+V)$ time and $O(V)$ space directly.
- **Sorting:** Sort values, identify runs of length one, and retain the largest. It costs $O(n\log n)$ and may mutate input.
- **Repeated list count:** Calling `nums.count(x)` for many values can cost $O(n^2)$.
- **One element:** Its frequency is one, so it is returned.
- **No unique values:** The generator is empty and default negative one is returned.
- **Unique zero:** Zero is returned, not confused with failure.
- **Largest value repeated:** It is skipped and the next greatest eligible value wins.
- **Several unique values:** `max` selects the greatest numeric value, independent of input order.
- **All values distinct:** The ordinary array maximum is returned.
- **Nonempty input:** Counter always has at least one entry, though the candidate generator may be empty.
- **Sentinel safety:** Negative one lies outside the legal nonnegative domain.
- **Input preservation:** Counter reads the array without changing it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+u)$. Let $n$ be array length and $u$ the number of distinct values. Counter construction takes expected $O(n)$ time. Scanning its items takes $O(u)$, so exact expected time is $O(n+u)$, which fits the manifest’s $O(n+V)$ bound because $u\le V$.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
