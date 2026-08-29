# Guided Example: Maximum Price to Fill a Bag

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"items": [[50, 1], [10, 8]], "capacity": 5}`
- **Required output:** `55`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `items` where $\text{items}[i] = [\text{price}_{i}, \text{weight}_{i}]$ denotes the price and weight of the $i^{\text{th}}$ item, respectively.

The objective is to compute `55` from `{"items": [[50, 1], [10, 8]], "capacity": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: This is a fractional knapsack problem

Every item may be divided in any ratio, and price scales linearly with weight. Therefore, a fraction of an item has the same price per unit weight as the whole item.

For item `[p,w]`, its value density is

$$
\frac pw.
$$

To maximize total price for an exact weight capacity, consume available weight from highest density to lowest density.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"items": [[50, 1], [10, 8]], "capacity": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the stored sort key

The source sorts by:

`x[1]/x[0]`,

which is `weight/price`, the reciprocal of price density. Ascending reciprocal order is equivalent to descending `price/weight` order because all prices and weights are positive.

Thus the first item processed provides the greatest price per unit of capacity.

The manifest describes density sorting directly; the exact key reaches the same order through reciprocals.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Take as much as possible from each item

For current item with weight `w` and remaining bag capacity, choose:

`v=min(w,capacity)`.

If the item fits entirely, `v=w`. Otherwise, take exactly the fraction needed to fill the remaining capacity.

The selected fraction is `v/w`, so its proportional price is:

`v/w*p`.

This is added to `ans`, and `v` is subtracted from remaining `capacity`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `55` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"items": [[50, 1], [10, 8]], "capacity": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `55` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cross-product comparator:** Avoid floating-point density keys by comparing `p1*w2` with `p2*w1`.
- **Indivisible knapsack DP:** It is unnecessary and incorrect for freely divisible items.
- **Insufficient total weight:** Return `-1`.
- **Capacity smaller than first item:** Take only the needed fraction of the best-density item.
- **Equal densities:** Their processing order does not affect total price.
- **Capacity exactly total weight:** Every item is consumed.
- **Capacity reaches zero early:** Later iterations contribute zero.
- **Positive prices and weights:** They make reciprocal sorting well-defined.
- **Exact fill:** Unused capacity is not allowed even if current price is maximal.
- **Input preservation:** `sorted` does not reorder the original outer list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of items. Sorting costs $O(n\log n)$ time. The greedy scan is $O(n)$, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
