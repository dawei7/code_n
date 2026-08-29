# Guided Example: How Many Apples Can You Put into the Basket

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"weight": [100, 200, 150, 1000]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have some apples and a basket that can carry up to `5000` units of weight.

The objective is to compute `4` from `{"weight": [100, 200, 150, 1000]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort apples by increasing weight

The call `weight.sort()` rearranges the input list in nondecreasing order. After sorting, the prefix of length $r$ contains the $r$ lightest apple occurrences. Repeated weights remain separate because every array position represents a distinct apple.

The in-place mutation is part of the exact implementation. The method does not need the original input order because order has no meaning for subset selection, but a caller that reused the same list would observe that it has been sorted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"weight": [100, 200, 150, 1000]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Add the lightest remaining apple

The running value `s` is the total weight of the sorted prefix considered so far. The loop uses `enumerate(weight)`, so `i` is the current zero-based position and `x` is that apple’s weight. It adds `x` before testing the limit.

If the new total is at most 5000, every apple from index zero through `i` fits. The loop simply continues.

If `s > 5000`, the just-added apple makes the prefix infeasible. Exactly `i` apples appeared before it, because zero-based index `i` counts preceding positions. The method returns `i`.

The comparison is strict. A total of exactly 5000 is allowed and must not stop the scan. Only a total greater than capacity fails.

If the loop finishes, the total weight of all apples is at most 5000, so `len(weight)` is returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why failure of the lightest prefix rules out every larger selection

For any desired count $r$, the $r$ lightest apples have the minimum possible total weight among all subsets of $r$ apples. To see this, take any $r$-apple subset. If it contains a heavier apple while excluding a lighter one, swapping the heavier for the lighter never increases total weight. Repeating such exchanges transforms the subset into the sorted prefix without increasing weight.

Therefore:

- If the first $r$ sorted apples fit, selecting that prefix proves that at least $r$ apples are achievable.
- If the first $r$ sorted apples exceed 5000, every other $r$-apple subset is at least as heavy and also exceeds 5000.

When the algorithm first overflows at index `i`, the prefix of length `i` fit before adding the current apple, so `i` apples are achievable. The prefix of length `i + 1` is the lightest possible selection of that size and does not fit, so no selection with `i + 1` apples can fit. Any still larger count contains even more positive-weight apples and is impossible as well. The returned count is exactly optimal.

For `weight = [900, 950, 800, 1000, 700, 800]`, sorting gives `[700, 800, 800, 900, 950, 1000]`. The first five total 4150. Adding the sixth raises the sum to 5150, so the overflow occurs at index five and the method returns five.

For `[100, 200, 150, 1000]`, the sorted running total never exceeds 5000. The method returns four, showing that sorting does not force the basket to become full; it simply includes every apple that can be included while maximizing count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"weight": [100, 200, 150, 1000]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Counting frequencies by weight:** Because weights are at most 1000, count each weight and take as many as possible from one upward. This can achieve $O(n+W)$ time and $O(W)$ space for maximum weight $W$.
- **Min-heap:** Heapify the list and repeatedly pop the lightest apple while it fits. This takes $O(n+k\log n)$ time for $k$ selected apples and also mutates the input.
- **Capacity dynamic programming:** A knapsack table can find a maximum count, but its $O(n\cdot5000)$ work is unnecessary given the equal value of all apples.
- **All apples fit:** The loop never returns early and the method returns `len(weight)`.
- **First apple is too heavy:** Under the stated maximum weight of 1000 this cannot happen with capacity 5000, but the logic would overflow at index zero and return zero.
- **Total exactly 5000:** The strict `> 5000` check accepts the prefix, as required.
- **Repeated weights:** Sorting preserves each occurrence, and every occurrence increments the count separately.
- **Positive weights:** Once a prefix overflows, adding more apples cannot restore feasibility. The proof relies on every weight being at least one.
- **Input mutation:** `weight.sort()` changes the caller-visible list order. Use `sorted(weight)` if preserving input is an external requirement, at the cost of another list.
- **Zero-based return at overflow:** When index `i` causes failure, there are exactly `i` earlier apples, so returning `i` is not an off-by-one error.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of apples.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
