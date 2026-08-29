# Guided Example: Minimum Difference Between Largest and Smallest Value in Three Moves

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 3, 2, 4]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `0` from `{"nums": [5, 3, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why changing an extreme is equivalent to removing it

After at most three changes, only the final minimum and maximum matter. If an original extreme is changed to any value inside the eventual surviving range, it no longer influences that range. For purposes of minimizing maximum minus minimum, changing that element is equivalent to removing it from consideration.

Changing a value strictly inside the current minimum and maximum does not shrink the range. Therefore, an optimal set of useful moves targets elements at the low or high ends after sorting.

The stored solution first handles short arrays, then sorts and evaluates the four possible ways to distribute three changes between the two ends.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 3, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why arrays shorter than five return zero

If `n < 5`, there are at most four elements. With up to three moves, all but at most one element can be changed to equal the remaining value. The final maximum and minimum are then equal, so their difference is zero.

Zero is the smallest possible difference, so returning immediately is optimal. This also avoids indexing assumptions used by the later four-case loop.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The four distributions of moves

After sorting, let `l` be the number of smallest values changed and `r` the number of largest values changed. Spending three useful moves gives

$$
l+r=3.
$$

There are exactly four nonnegative possibilities:

- Change zero smallest and three largest.
- Change one smallest and two largest.
- Change two smallest and one largest.
- Change three smallest and zero largest.

The source loops `l` through zero, one, two, and three and sets `r = 3 - l`.

After removing those extremes from range consideration, the smallest unchanged value is `nums[l]` and the largest unchanged value is `nums[n - 1 - r]`. Their difference is the best range for that distribution because changed values can be placed anywhere inside it.

`ans` starts at positive infinity and keeps the minimum of the four differences.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 3, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track four smallest and four largest:** Maintain only the extreme candidates during one scan, then evaluate the same four differences. This achieves the manifest's $O(N)$ time and $O(1)$ space.
- **Partial selection:** Selection algorithms can find the necessary order statistics without fully sorting, but are more complex than the four-extreme scan.
- **Fewer than five values:** Three moves can make all values equal, so the answer is zero.
- **Exactly five values:** Each three-move scenario leaves two unchanged endpoint candidates.
- **Already equal values:** Every evaluated difference may already be zero.
- **Negative numbers:** Sorting and subtraction handle them normally.
- **Duplicate extremes:** Changing copies one at a time is correctly represented by moving the retained endpoint index inward.
- **At most versus exactly three:** Extra useful endpoint changes cannot enlarge the best achievable range.
- **Input mutation:** The sorted order remains visible to the caller.
- **Positive infinity:** `inf` must be available in the module environment.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the number of values. The short-array branch is $O(1)$. Otherwise, Python sorting costs $O(N\log N)$ time. The four-case loop is constant time, so total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
