# Guided Example: Minimum Operations to Make Median of Array Equal to K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 5, 6, 8, 5], "k": 4}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and a **non-negative** integer `k`. In one operation, you can increase or decrease any element by 1.

The objective is to compute `2` from `{"nums": [2, 5, 6, 8, 5], "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

**Sort so the median has a fixed index.** The source sorts `nums` in nondecreasing order and defines `m = n >> 1`, which is integer division by two. For odd $n$, this is the unique middle index. For even $n$, it is the second of the two central indices, matching the contract's instruction to use the larger median.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 5, 6, 8, 5], "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

After sorting, making the median equal to `k` is an order-statistics requirement. It is not enough merely to change the current middle value: values on the relevant side may also have to cross `k` so that `k` remains at index `m` after all modifications.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After sorting, making the median equal to `k` is an order-st... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Always pay for the middle element.** `ans` starts as `abs(nums[m] - k)`. Increasing or decreasing an integer by one costs one operation, so this is the exact unavoidable cost to move the current median value to `k`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 5, 6, 8, 5], "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Selection instead of full sorting:** Find the :** - **Selection instead of full sorting:** Find the upper median with a linear-time selection algorithm, then partition and sum required deviations. It can reduce expected time but is more complex.
- **Sort and scan all values:** Sum every relevant excess using index conditions without early breaks. It remains $O(n)$ after sorting but does extra constant work.
- **Odd length:** `n // 2` is the unique middle.
- **Even length:** `n // 2` selects the larger of the two central sorted values as required.
- **Median already `k`:** The cost is zero and sorted neighbors cannot force extra changes.
- **All values above `k`:** The middle and enough left-side values are lowered; farther right values may remain.
- **All values below `k`:** The middle and necessary right-side values are raised.
- **Duplicate values:** Each occurrence is a separate array element and contributes its own unavoidable distance when it lies on the required side.
- **Values equal to `k`:** They need no operations and trigger the sorted early-stop condition.
- **Strict scan conditions:** Only `> k` on the left or `< k` on the right costs operations.
- **Input mutation:** Sorting changes `nums` in place, an observable implementation detail.
- **No need to rebuild final order:** The cost calculations describe feasible changes; the method returns only their minimum number.
- **One-element array:** The answer is simply the absolute difference from `k`.
- **Large total:** Use a wide integer outside Python.
- **Why not change an opposite-side value:** It cannot repair the rank condition more cheaply than moving a violating value directly to `k`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Python sorting takes $O(n\log n)$ time. The subsequent directional scan visits at most $n$ values once, so sorting dominates and total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
