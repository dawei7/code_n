# Guided Example: Maximum K to Sort a Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 3, 2, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`, where `nums` is a **permutation** of the numbers in the range `[0..n - 1]`.

The objective is to compute `1` from `{"nums": [0, 3, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the permutation property to identify exactly what must move

Because `nums` is a permutation of `0` through `n - 1`, the sorted array is completely determined: value `i` belongs at index `i`. An entry is already correct when `nums[i] == i`. Such an entry does not have to participate in any swap.

Let `S` be the set of values currently at incorrect indices:

`S = { nums[i] : nums[i] != i }`.

If `S` is empty, the array is already sorted and the required return value is zero. Otherwise, every value in `S` must eventually move, because its present index is not its final index.

The surprising result is that the maximum feasible swap parameter is simply the bitwise AND of all values in `S`. The source computes that AND in one pass without explicitly storing the set.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 3, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every feasible `k` is bounded by the misplaced values

An allowed swap exchanges two current values `a` and `b` only when

`a AND b = k`.

Every bit that is set in `k` must therefore be set in both `a` and `b`. In particular, whenever a value participates in an allowed swap, it contains every set bit of `k`.

Each initially misplaced value must participate in at least one swap before the array can become sorted. Consequently, every set bit of a feasible `k` must appear in every value in `S`. The largest bit pattern with that property is

`K = AND of all values in S`.

Any feasible `k` can contain only bits present in `K`; in bitmask language, `k` must be a submask of `K`. Removing set bits never increases a non-negative integer, so no feasible parameter can be numerically larger than `K`. This establishes an upper bound, but an upper bound alone is not enough—we must also know that `K` really permits sorting.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The value `K` itself is a universal swap pivot

The permutation contains every integer from zero to `n - 1` exactly once. Since a bitwise AND cannot exceed any non-negative operand, `0 <= K <= x <= n - 1` for every `x` in `S`. Thus the value `K` exists somewhere in the permutation, even if it happens to be already at index `K`.

By definition of `K`, every misplaced value `x` contains all bits of `K`. ANDing `x` with the value `K` removes any extra bits of `x` and leaves exactly `K`:

`x AND K = K`.

Therefore, for the chosen parameter `k = K`, the item whose value is `K` may be swapped with every misplaced value. It acts as a universal pivot.

This remains useful even when `K` began in its correct position. Correct elements are not forbidden from moving temporarily; only the final arrangement matters. The pivot can leave its home, help rearrange other values, and return afterward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 3, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build the misplaced set explicitly:** Collecting all `nums[i]` with `nums[i] != i` and reducing them afterward yields the same answer, but it spends `O(n)` extra space that the streaming AND does not need.
- **Binary search the numeric value of `k`:** Feasibility is not monotone in ordinary numeric order, because changing bits can create or destroy exact-AND edges unpredictably. The common-bit argument derives the unique maximum directly.
- **Build an allowed-swap graph:** For a candidate `k`, one could connect pairs whose AND equals `k` and analyze whether permutation cycles can be resolved. Considering all pairs is quadratic, and the value-`K` pivot proves connectivity without constructing the graph.
- **AND every array value:** Correctly placed values impose no necessary swap condition. Including them can erase bits and produce an answer smaller than the true maximum.
- **OR instead of AND:** OR records bits present in at least one misplaced value. A permitted `k` needs each of its bits in every value that must move, so intersection by AND is the required operation.
- **Already sorted permutation:** No value needs a swap. The running sentinel remains `-1`, and `max(ans, 0)` returns the explicitly required zero.
- **Exactly two misplaced values:** A permutation cannot have exactly one misplaced position. With two, their values must exchange, and the answer is their direct bitwise AND.
- **Answer zero:** Zero is always a valid pivot value because the permutation contains zero and `0 AND x = 0`. A zero answer does not mean sorting is impossible; it means the misplaced values share no positive bit.
- **Pivot initially fixed:** The value `K` may temporarily leave index `K`. Three pivot swaps can exchange two other values and restore it, so being initially correct does not make it unusable.
- **Duplicate values:** The proof relies on `nums` being a permutation. If duplicates or missing values were allowed, value `K` might not exist as a pivot, and the same formula would no longer be justified.
- **Why `K` stays in range:** A bitwise AND of non-negative operands cannot introduce a bit absent from an operand, so `K` is no larger than each misplaced value and is one of the permutation’s legal value-domain integers.
- **Python’s `-1` sentinel:** The identity `-1 & x = x` is language-specific bitwise behavior. In a fixed-width unsigned implementation, initialize with all bits set over the value domain or handle the first misplaced value separately.
- **Missing type import:** The stored source uses `List` without importing it. The judge may provide that typing symbol, while standalone Python would require `from typing import List`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the permutation length. The loop visits each index-value pair exactly once. Each comparison and bitwise AND operates on values bounded by `n - 1` and is treated as constant time under the usual machine-integer model. Total time is therefore `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
