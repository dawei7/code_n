# Guided Example: Count Number of Maximum Bitwise-OR Subsets

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a subset of `nums` and return *the **number of different non-empty subsets** with the maximum bitwise OR*.

The objective is to compute `2` from `{"nums": [3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The OR of all elements is the maximum possible OR

Bitwise OR can add set bits but never remove a bit that is already set. If a subset has OR value `v`, adding another array element changes it to `v | x`, which contains every bit of `v` and possibly more.

Therefore no subset can have a bit that is absent from the OR of the entire array, and including all elements achieves every bit that appears anywhere. The source computes this target as

`mx = reduce(lambda x, y: x | y, nums)`.

The array is guaranteed nonempty, so `reduce` has at least one value and needs no initializer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Represent subset construction as binary choices

The recursive helper `dfs(i, t)` means:

- indices zero through `i-1` have already been decided;
- `t` is the bitwise OR of exactly those chosen indices;
- index `i` is the next decision.

At each index, every subset belongs to one of two disjoint categories. It either excludes `nums[i]`, leading to `dfs(i + 1, t)`, or includes it, leading to `dfs(i + 1, t | nums[i])`.

These two calls enumerate the complete binary decision tree of index subsets.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The recursive helper `dfs(i, t)` means:

- indices zero thro... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why duplicate values still produce different subsets

The recursion branches by index, not by value. If `nums[0]` and `nums[1]` are equal, selecting only index zero and selecting only index one follow different include/exclude paths and reach different leaves.

They may have the same OR, but the problem defines them as different subsets. The leaf counter increments separately, preserving exactly the required multiplicity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Early count after reaching `mx`:** Once a part:** - **Early count after reaching `mx`:** Once a partial OR equals the maximum, add `2^(remaining indices)` instead of exploring all continuations.
- **Dynamic programming by OR value:** Track how many subsets produce each OR; useful when the number of distinct OR states is small.
- **Bitmask loop:** Iterate masks from one through `2^N-1`; same exponential class with explicit subset masks.
- **Memoized recursion:** States with the same index and OR can be merged, though counts rather than Boolean reachability must be preserved.
- **One element:** Its singleton subset is counted once.
- **All values equal:** Every nonempty subset reaches the same maximum OR.
- **Duplicate indices with equal values:** They remain distinct choices and are counted separately.
- **Subset already at maximum:** Adding more elements cannot reduce its OR.
- **Empty subset:** Visited but not counted because the positive inputs make `mx>0`.
- **All-zero array outside constraints:** Would expose the empty-subset issue in the exact source.
- **Maximum OR target:** OR of all elements is reachable and dominates every subset bitwise.
- **Input preservation:** Recursion reads values without editing `nums`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^N)$. Let $N$ be the number of elements. The recursion has $2^N$ leaves and fewer than $2^{N+1}$ total calls. Each call performs constant work apart from its child calls, so time is $O(2^N)$. Computing `mx` adds $O(N)$, which is dominated.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
