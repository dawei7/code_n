# Guided Example: Maximum Subarray Sum After at Most K Swaps

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, -1, 0, 2], "k": 1}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `3` from `{"nums": [1, -1, 0, 2], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Coordinate compression

The source creates `values = sorted(set(nums))`. This is the increasing list of the `M` distinct array values. The dictionary `ranks` maps each original value to its zero-based position in that list.

Compression preserves all comparisons and equalities: a lower rank means a smaller value, and equal values share a rank. It lets the algorithm store count and sum information in arrays of length `M` even when the input values are negative or far apart.

The array `global_frequency` counts how many times each compressed value occurs in the entire array. Its cumulative version, `global_prefix`, tells how many global elements have value at most a given rank.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, -1, 0, 2], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Fenwick trees store both multiplicity and sum

The source builds two Fenwick trees over the complete array:

- `total_count_tree` stores how many values occupy each rank;
- `total_sum_tree` stores the sum of the actual values at those ranks.

For each new left endpoint, it also creates corresponding `inside_count_tree` and `inside_sum_tree` structures, initially empty. As the right endpoint advances, the newly included value is added to both inside trees and to `current_sum`.

A count tree makes it possible to locate the rank containing the `t`-th smallest item, including duplicate values. A parallel sum tree then gives the sum of all fully selected smaller ranks. If only some copies at the boundary rank are required, their contribution is the remaining count multiplied by the value at that rank.

The source performs this selection through Fenwick binary lifting. Starting with no selected prefix, it tries powers of two from large to small. It skips a Fenwick block only when adding the whole block would leave the cumulative count strictly below the requested count. At the end, `index` identifies the compressed value containing the requested order statistic. The expression



adds exactly the needed number of duplicate boundary values.

This mechanism finds the sum of several smallest items in `O(\log M)` time; it does not enumerate or sort the current subarray.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Counting only strictly profitable swaps

The algorithm must know how many paired swaps have positive gain. It avoids a separate binary search over the two changing multisets by precomputing a global pivot for every possible outside size.

Let `q` be the current `outside_size`. For `1 \le q < n`, `pivot[q]` is the rank of the `q`-th smallest value in the complete array, counting duplicates. Let that pivot value be `v`. The stored `prefix_at_pivot[q]` is the number of global elements whose value is at most `v`.

For the current subarray, define:

- `L` as the number of inside values strictly less than `v`;
- `T` as the number of inside values less than or equal to `v`;
- `H` as the number of outside values strictly greater than `v`.

The source obtains `L` by querying the inside count tree before the pivot rank. It obtains `T` by adding `inside_frequency[position]`, the number of inside copies exactly equal to the pivot. The global count at most the pivot is known, so

$$
H
=q-\bigl(\text{global values at most }v-\text{inside values at most }v\bigr)
=q-\text{prefixAtPivot}[q]+T.
$$

This is the second expression inside the source's `max`.

The number of strictly profitable ordered pairs is

$$
\max(L,H).
$$

To see why, consider the two sides of the pivot.

- If `L \ge H`, every outside value above `v` can be paired with a smaller inside value first. The remaining inside values below `v` can then be paired with available outside values at least `v`, and those pairs are still strict improvements. Thus all `L` low inside values are profitable.
- If `H>L`, pair all inside values below `v` first. The remaining outside values above `v` can be paired with available inside values at most `v`, so all `H` high outside values are profitable.
- After `\max(L,H)` such pairs, any additional inside candidate is at least `v` while any additional outside candidate is at most `v`. The next gain is therefore nonpositive.

The choice of `v` as the global `q`-th order statistic guarantees that the necessary partners exist in both cases. It also handles duplicate pivot values correctly. Equal values produce zero gain and are deliberately excluded from the profitable count.

The exact source computes



so it never uses more than `k` swaps and never spends a swap on a zero or negative improvement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, -1, 0, 2], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Re-sort inside and outside for every subarray:** The fixed-boundary greedy rule could be implemented by materializing both sides and sorting them each time, but doing so repeats substantial work and pushes the running time well beyond the required quadratic-logarithmic approach.
- **Enumerate swap sequences:** Exploring actual index-pair sequences branches explosively and treats different operation orders as different even when they produce the same inside multiset. Choosing removed and inserted order statistics captures exactly what affects the sum.
- **Use heaps for each fixed left endpoint:** Two heaps can expose extremes, but deletions, duplicate management, and reconstructing the outside complement for every moving right endpoint are delicate. The paired count-and-sum Fenwick trees support both multiplicity and prefix sums uniformly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the array length and `M` the number of distinct values, with `M \le n`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
