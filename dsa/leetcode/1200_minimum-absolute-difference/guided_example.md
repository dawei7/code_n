# Guided Example: Minimum Absolute Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [4, 2, 1, 3]}`
- **Required output:** `[[1, 2], [2, 3], [3, 4]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

The objective is to compute `[[1, 2], [2, 3], [3, 4]]` from `{"arr": [4, 2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why only adjacent sorted values matter

Suppose sorted values `a` and `b` are not adjacent, with `a < x < b` for some input value `x` between them. Then both `x - a` and `b - x` are positive and smaller than `b - a`. Therefore, the nonadjacent pair `[a, b]` cannot achieve the global minimum difference.

Every pair that can be globally minimal is consequently among the $n-1$ adjacent pairs after sorting. Because the input values are distinct, every adjacent difference is positive.

The code begins with `arr.sort()`. This both orders the candidate pairs and guarantees that for adjacent values `a, b`, the absolute difference is simply `b - a`; no `abs` call is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [4, 2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the minimum adjacent gap

`pairwise(arr)` yields consecutive tuples:

`(arr[0], arr[1])`, `(arr[1], arr[2])`, and so forth.

The generator expression `b - a for a, b in pairwise(arr)` produces every adjacent gap. Applying `min` finds the smallest one and stores it in `mi`. The constraint that the array has at least two values guarantees that this generator is nonempty.

The exact code makes a second `pairwise` traversal rather than storing all gaps. A `pairwise` iterator is consumed as it runs, so constructing a new one for the result pass is necessary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `pairwise(arr)` yields consecutive tuples:

`(arr[0], arr[1]... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Collect every adjacent pair with that gap

The list comprehension again visits adjacent sorted values and includes `[a, b]` exactly when `b - a == mi`.

Every returned pair automatically satisfies `a < b` because input values are distinct and sorted. The pairs themselves appear in ascending order because their first elements follow sorted array order. No additional sorting of the output is needed.

For `arr = [4, 2, 1, 3]`, sorting gives `[1, 2, 3, 4]`. The gaps are one, one, and one, so `mi` is one and all three adjacent pairs are returned.

For `[3, 8, -10, 23, 19, -4, -14, 27]`, the sorted values are `[-14, -10, -4, 3, 8, 19, 23, 27]`. The smallest adjacent gap is four. The second pass returns `[-14, -10]`, `[19, 23]`, and `[23, 27]` in the required order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2], [2, 3], [3, 4]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [4, 2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2], [2, 3], [3, 4]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One post-sort pass:** Track the smallest gap a:** - **One post-sort pass:** Track the smallest gap and current answer simultaneously, clearing the answer when a smaller gap appears. It removes one linear pass but retains the same $O(n\log n)$ bound.
- **Counting over the bounded value range:** Mark all values from the allowed range and scan in numerical order. This can take $O(n+R)$ time and $O(R)$ space for range width $R$.
- **Brute-force all pairs:** It is simple but costs $O(n^2)$ time and ignores the ordering insight.
- **Exactly two values:** There is one adjacent pair, `min` receives one gap, and that pair is returned.
- **Negative values:** Sorting and subtraction work unchanged; adjacent order ensures `b - a` is positive.
- **Equal minimum gaps:** The comprehension includes all of them, not only the first.
- **Distinctness guarantee:** It ensures `a < b` and a positive minimum. Duplicate inputs would introduce zero-gap pairs and require interpreting whether duplicate occurrences are allowed.
- **Output ordering:** Scanning adjacent pairs from left to right after sorting automatically gives lexicographic pair order.
- **Consumed iterator:** The first `pairwise` generator cannot be reused after `min`. The code correctly constructs a second iterator.
- **Input mutation:** Use a sorted copy if preserving the caller’s original order is required outside this contract.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the length of `arr`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
