# Guided Example: Minimum Cost to Merge Sorted Lists

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"lists": [[1, 3, 5], [2, 4], [6, 7, 8]]}`
- **Required output:** `18`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `lists`, where each $\text{lists}[i]$ is a non-empty array of integers **sorted** in **non-decreasing** order.

The objective is to compute `18` from `{"lists": [[1, 3, 5], [2, 4], [6, 7, 8]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent a merged collection by an original-list subset

Every intermediate list contains the elements of some subset of the original lists. A bitmask records that subset: bit `i` is one when original list `i` is included.

The sorted contents, length, and median of a subset are independent of the order used to merge it. This allows dynamic programming over masks rather than over concrete merge histories.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"lists": [[1, 3, 5], [2, 4], [6, 7, 8]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute every subset size

For nonzero `mask`, `lowest_bit = mask & -mask` isolates one included list. `owner` is its index.

Removing that bit gives a smaller subset whose size is already known:

`sizes[mask] = sizes[mask ^ lowest_bit] + len(lists[owner])`.

This computes the total element count for every subset in constant time after its predecessor.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For nonzero `mask`, `lowest_bit = mask & -mask` isolates one... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Precompute left medians of merged subsets

All input elements are flattened as pairs `(value,owner)` and sorted globally. For one subset mask, filtering this global order by included owners produces exactly the sorted merge of those lists.

The left-middle median index is

`target = (sizes[mask]-1)//2`.

The source scans `ordered`, increments `seen` only for included owners, and records the value when `seen==target`.

Duplicate numeric values remain separate pairs. Python's secondary owner ordering among equal values does not affect the median value.

This scan costs linear total-element work per mask but avoids materializing a merged list for every subset.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `18` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"lists": [[1, 3, 5], [2, 4], [6, 7, 8]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `18` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Greedily merge the cheapest current pair:** Me:** - **Greedily merge the cheapest current pair:** Median changes can make a locally cheap choice globally suboptimal.
- **Huffman merging by length:** The additional median-distance term invalidates pure length-based optimality.
- **Materialize every subset merge:** This uses much more storage; the global ordered owner list yields medians by filtering.
- **Use the right median:** The contract specifies the left middle, implemented by `(size-1)//2`.
- **Enumerate both split orders:** The anchor condition removes exact symmetry.
- **Singleton subset:** It needs no merge and has DP cost zero.
- **Exactly two lists:** The full DP state performs their single required merge.
- **Duplicate values:** They remain separate occurrences and median value selection stays correct.
- **Negative elements:** Only ordering and absolute median difference matter.
- **Input sortedness:** The source still builds one global sorted flattened sequence.
- **Output list:** Only minimum cost is returned; no merge sequence is reconstructed.
- **Constraint role:** Exponential dependence is feasible because `L<=12`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(3^L+N2^L+N\log N)$. Let $L$ be the number of lists and $N$ their total number of elements.
- **Auxiliary Space Complexity:** $O(2^L + N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
