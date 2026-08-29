# Guided Example: Maximum Difference Between Increasing Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [7, 1, 5, 4]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** integer array `nums` of size `n`, find the **maximum difference** between $\text{nums}[i]$ and $\text{nums}[j]$ (i.e., $\text{nums}[j] - \text{nums}[i]$), such that $0 \le i < j < n$ and $\text{nums}[i] < \text{nums}[j]$.

The objective is to compute `4` from `{"nums": [7, 1, 5, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Fix the later index and choose the best earlier value

For a current value at index `j`, the best possible earlier partner is the minimum value among indices zero through `j-1`. Subtracting the smallest earlier value maximizes `nums[j] - nums[i]` while automatically respecting `i<j`.

The source keeps that prefix minimum in `mi` and scans left to right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [7, 1, 5, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start before any real prefix exists

`mi` is initialized to positive infinity and `ans` to -1. At the first value, `x > mi` is false, so the else branch sets `mi=x`. No pair is evaluated because no earlier index exists.

From the second element onward, `mi` is a real value from a strictly earlier position.

This initialization lets one loop handle the first item without separate indexing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Evaluate only positive differences

If `x > mi`, the current value is strictly larger than some earlier value, so the pair satisfies the increasing-value condition. `x - mi` is positive and is the greatest valid difference ending at the current index.

The source updates `ans = max(ans, x - mi)` to retain the best across all later endpoints.

If `x <= mi`, no positive difference ending here can exist. The value becomes the new prefix minimum through `mi=x`. Equality may replace the minimum with an equal value at a later index, but that does not change any future numerical difference.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [7, 1, 5, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every index pair:** Direct but takes $O(N^2)$ time.
- **Suffix maximum for each earlier index:** Also linear with an array, but uses $O(N)$ space when one rolling prefix minimum suffices.
- **Sort the values:** Incorrect because sorting destroys the required index order.
- **Strictly decreasing array:** No current value exceeds its prefix minimum, so return -1.
- **All equal values:** Equality is not increasing; return -1.
- **Best pair uses nonadjacent indices:** Prefix minimum retains it regardless of distance.
- **First value:** Establishes the prefix minimum and cannot be a later endpoint with an earlier partner.
- **Large values:** Difference fits comfortably in Python integers.
- **Strict comparison:** `x > mi` enforces `nums[i] < nums[j]`; equality must not qualify.
- **Several equal minima:** Any occurrence gives the same numerical candidate, and the earliest/later identity is irrelevant.
- **Answer sentinel:** -1 remains only when no positive valid difference exists.
- **Input preservation:** The scan performs no sorting or writes.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be array length. The loop visits every value once and performs constant-time comparisons and arithmetic, so time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
