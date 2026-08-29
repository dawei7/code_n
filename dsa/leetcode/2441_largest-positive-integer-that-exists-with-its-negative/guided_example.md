# Guided Example: Largest Positive Integer That Exists With Its Negative

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-1, 2, -3, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` that **does not contain** any zeros, find **the largest positive** integer `k` such that `-k` also exists in the array.

The objective is to compute `3` from `{"nums": [-1, 2, -3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Membership is the only relationship that matters

For a positive candidate $k$, the condition is that both $k$ and $-k$ appear somewhere in `nums`. Their positions, order, and multiplicities do not matter. A hash set is therefore the natural representation: it keeps one copy of each value and supports expected constant-time membership tests.

The solution creates `s = set(nums)`. It then generates every `x` in `s` for which `-x in s` and takes the maximum, using `default=-1` when the generator is empty.

The generator does not explicitly require `x > 0`. That may first look like a bug, but it is still correct. Whenever a valid magnitude $k$ exists, both $k$ and $-k$ satisfy the generator condition. The maximum of that pair is the positive value $k$. Across several valid magnitudes, the maximum over all signed qualifying values is the largest positive magnitude requested.

If no opposite pair exists, no value passes the generator and `max` returns the specified default -1.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-1, 2, -3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why zero does not create ambiguity

Zero is its own negative, so if zero were allowed, `-0 in s` would be true with only one zero and the generator could treat it as a pair. The constraints explicitly exclude zero. The exact implementation relies on that guarantee when using the symmetric generator without a positivity filter.

Even if zero were present alongside no valid positive pair, `max` could return zero instead of -1, violating the contract. This is why constraints are part of correctness, not merely performance information.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the set behavior

For `nums = [-1,2,-3,3]`, the set contains all four values. Both -3 and 3 pass because their opposites exist. Neither -1 nor 1 forms a stored pair, and 2 fails because -2 is absent. The maximum qualifying value is 3.

For `[-1,10,6,7,-7,1]`, the qualifying signed values are -7, 7, -1, and 1. Taking their maximum gives 7.

For `[-10,8,6,7,-2,-3]`, every opposite lookup fails. The generator produces nothing, so the answer is -1.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-1, 2, -3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit positive filter:** Use candidates satisfying `x > 0 and -x in s`. This makes intent more obvious and produces the same result under the no-zero constraint.
- **Sort and use two pointers:** Sorting permits a scan for opposite values in $O(n\log n)$ time and can use less auxiliary hash storage, but it is slower asymptotically.
- **Brute-force pairs:** Compare every pair for a zero sum and track the positive magnitude. This takes $O(n^2)$ time.
- **Fixed boolean presence array:** Offset values by 1000 and mark the bounded domain. It gives $O(n+U)$ time and $O(U)$ storage for fixed $U=2001$.
- **Duplicate values:** A set removes them without changing existence or the largest valid magnitude.
- **Only one side present:** The membership test fails and the value is ignored.
- **Several valid pairs:** Taking the maximum selects the greatest positive member.
- **All values negative or all positive:** No opposite pair can exist, so the default -1 is returned.
- **Zero exclusion:** The symmetric generator is correct because zero cannot appear; without that constraint it would need an explicit positive test.
- **Default value:** Supplying `default=-1` avoids an exception when no generator candidate exists and matches the required sentinel.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Building the set takes expected $O(n)$ time. Iterating through at most $n$ distinct values and performing one expected constant-time hash lookup per value takes another expected $O(n)$ time. The total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
