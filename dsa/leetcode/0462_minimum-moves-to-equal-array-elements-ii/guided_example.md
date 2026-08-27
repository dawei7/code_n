# Guided Example: Minimum Moves to Equal Array Elements II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

The objective is to compute `2` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the median minimizes absolute distance

Imagine moving a proposed target `k` one unit to the right. Every input value to the left of `k` becomes one unit farther away, increasing the total cost by one for each such value. Every input value to the right becomes one unit closer, decreasing the cost by one for each such value.

If more values lie to the right than to the left, moving right decreases the total cost. If more lie to the left, moving right increases it. A minimum is reached where neither side has a numerical majority—that is exactly the median region.

After sorting, a median has at most half the values below it and at most half above it. Moving away from that region causes distances on the larger side to increase at least as fast as distances on the smaller side decrease. No target outside the median region can improve the sum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A pairing view of the same fact

Sort values as

$$
a_0\le a_1\le\cdots\le a_{n-1}.
$$

Pair the smallest with the largest, the second smallest with the second largest, and so on. For any target `k` lying between a pair's endpoints,

$$
\lvert a_i-k\rvert+\lvert a_{n-1-i}-k\rvert=a_{n-1-i}-a_i.
$$

This contribution is already as small as possible; moving `k` outside the pair's interval makes the sum larger. A median lies inside every nested outer-pair interval, so it simultaneously minimizes every pair's combined contribution. If `n` is odd, the unpaired center value is itself the median and contributes zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Sort values as

$$
a_0\le a_1\le\cdots\le a_{n-1}.
$$

Pair ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the exact median index is selected

After `nums.sort()`, the code computes

`k = nums[len(nums) >> 1]`.

Shifting a nonnegative integer right by one bit is integer division by two, so `len(nums) >> 1` equals `len(nums) // 2`.

For odd `n`, this is the unique middle index. For even `n`, it selects the upper of the two central values. Every target between the lower and upper medians minimizes the absolute-distance sum, so choosing the upper median is fully optimal. The target is allowed to be any integer; selecting an existing array value is convenient and sufficient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Quickselect the median:** Expected $O(n)$ time:** - **Quickselect the median:** Expected $O(n)$ time finds the middle order statistic without fully sorting, followed by an $O(n)$ distance scan. It mutates the array and has quadratic worst-case time with naive pivots.
- **Deterministic median of medians:** Guarantees $O(n)$ worst-case selection but is considerably more complex and usually unnecessary for these bounds.
- **Try every possible target:** The numerical range can span billions, making range enumeration infeasible.
- **Use the arithmetic mean:** It minimizes squared error, not the sum of unit moves, and can be suboptimal here.
- **Odd length:** The middle sorted value is the unique median region and is optimal.
- **Even length:** Any target between the two central values is optimal; the exact code chooses the upper one.
- **One element:** It is its own median, its distance is zero, and no moves are needed.
- **All values equal:** Every absolute difference is zero.
- **Negative values:** Sorting and absolute differences work across zero without special handling.
- **Duplicate medians:** Repeated central values simply make the optimal target explicit and do not affect the proof.
- **Input mutation:** Callers needing the original order must sort a copy rather than reuse this exact in-place implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of elements. Python sorting takes $O(n\log n)$ time. Selecting the middle element is $O(1)$. The generator inside `sum` then visits all $n$ values and performs constant-time arithmetic under the standard fixed-width model, adding $O(n)$ time. Sorting dominates, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
