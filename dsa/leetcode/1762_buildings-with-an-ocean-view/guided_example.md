# Guided Example: Buildings With an Ocean View

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [4, 2, 3, 1]}`
- **Required output:** `[0, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` buildings in a line. You are given an integer array `heights` of size `n` that represents the heights of the buildings in the line.

The objective is to compute `[0, 2, 3]` from `{"heights": [4, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Scan from the ocean side

The ocean lies to the right. A building at index `i` has a view exactly when its height is strictly greater than the height of every building at a larger index.

Scanning left to right would require knowing a future maximum. The exact solution instead scans from right to left, so all buildings that could block the current one have already been seen. It summarizes them with one scalar `mx`, the maximum height strictly to the right of the current index.

The current building qualifies when:

`heights[i] > mx`.

If it qualifies, its index is appended to `ans` and `mx` is updated to its height.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [4, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why strict greater-than is required

The definition says every building to the right must have a smaller height. An equal-height building blocks the view just as a taller building does.

Therefore `heights[i] == mx` must not qualify. The strict `>` comparison implements that boundary correctly. A non-strict `>=` would wrongly accept the left building of two equal-height buildings.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The definition says every building to the right must have a ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize the suffix maximum

`mx` begins at zero. All building heights are at least one, so the rightmost building is guaranteed to be greater than `mx`. It is appended, as it should be: with no building to its right, the “all buildings to the right are smaller” condition is vacuously true.

After processing an index, `mx` equals the maximum height among that index and every position to its right. Before the next iteration one step left, that is exactly the maximum strictly to the new current building's right.

If heights could be zero or negative, zero would not be a universally safe sentinel. Under the stated positive-height constraint, it is exact.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [4, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Suffix-maximum array:** Precompute the maximum:** - **Suffix-maximum array:** Precompute the maximum to the right of every index. It also gives $O(n)$ time but uses $O(n)$ extra storage beyond the result.
- **Monotonic stack:** Scan left to right and remove previously recorded buildings blocked by the current one. It is linear but more stateful than a single suffix maximum.
- **Check every right suffix:** Directly testing all blockers for each building costs $O(n^2)$ time.
- **Strictly decreasing heights:** Every building is a new suffix maximum, so all indices are returned.
- **Strictly increasing heights:** Only the rightmost, tallest building has a view.
- **Equal neighboring heights:** The left equal-height building is blocked because the comparison is strict.
- **One building:** It is appended against sentinel zero and returned.
- **Rightmost building:** It always qualifies because nothing lies to its right.
- **Positive-height guarantee:** It makes initial `mx = 0` safe.
- **Very tall leftmost building:** It qualifies if it exceeds the maximum of the entire remaining array.
- **Discovery order:** Right-to-left scanning requires reversal to satisfy increasing output order.
- **Reversed slice:** It creates a new list rather than reversing `ans` in place.
- **No building identity changes:** Only indices are stored; heights remain in the original array.
- **Large height values:** Only comparisons are used, so magnitude does not affect complexity.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of buildings. The reverse range visits every index once with constant-time comparison, append, and possible assignment. Reversing the answer takes $O(v)$ time where $v \le n$ is the number of qualifying buildings. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
