# Guided Example: Minimum Cost of Buying Candies With Discount

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"cost": [1, 2, 3]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A shop is selling candies at a discount. For **every two** candies sold, the shop gives a **third** candy for **free**.

The objective is to compute `5` from `{"cost": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Take the maximum possible number of free candies

Each free candy requires two paid candies to support it. Therefore no plan can make more than $\lfloor n/3\rfloor$ candies free.

An optimal plan reaches this maximum count. If fewer than $\lfloor n/3\rfloor$ free candies were used, at least three candies would remain outside complete promotional triples. Among any three such candies, pay for the two more expensive ones and take the cheapest for free. This lowers the cost, contradicting optimality.

So the remaining question is not how many freebies to take, but which $\lfloor n/3\rfloor$ candies can be made free while satisfying the price restriction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"cost": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort from most expensive to least expensive

The exact source calls `cost.sort(reverse=true)`. After sorting, `cost[0] >= cost[1] >= ... >= cost[n - 1]`.

Consider the first three prices. The candy at index two is no more expensive than those at indexes zero and one, so the first two may be bought and the third taken free. The same is true for indexes three, four, and five, then six, seven, and eight, and so on.

Thus every index congruent to two modulo three—`2, 5, 8, ...`—is a legal free candy. The two immediately preceding prices pay for it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why these are the most valuable possible freebies

The most expensive free candy in any valid plan cannot be more expensive than the third-most-expensive candy overall, `cost[2]`. A free candy needs two candies at least as expensive to support it, and only the first two positions can be strictly ahead of index two.

After accounting for one free candy and its two supporting paid candies, the second-most-expensive free candy cannot exceed `cost[5]`. More generally, the $(q+1)$-st most expensive free candy cannot exceed `cost[3q+2]`: obtaining $q+1$ free candies requires at least $2(q+1)$ paid candies that can support them, so at least $3(q+1)$ candies participate.

The descending triples achieve each upper bound exactly by making `cost[3q+2]` free. Therefore they maximize the total saved price among all plans with the maximum number of free candies. Maximizing savings minimizes money paid.

For `[6,5,7,9,2,2]`, sorting gives `[9,7,6,5,2,2]`. The freebies are prices six and two, while `9,7,5,2` are paid. Total cost is 23.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"cost": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Loop over sorted indexes:** Add `cost[i]` only when `i % 3 != 2`. This avoids the free-candy slice allocation but keeps the same sorting time and greedy proof.
- **Counting sort:** Prices are between one and 100, so a frequency array can compute the answer in $O(n+100)$ time and $O(100)$ space. It is asymptotically linear under the fixed price range but is not the exact source.
- **Sort ascending:** One can process from the end in groups of three, but the index pattern is less direct. Taking every third element from the front of ascending order would be wrong.
- **Choose cheapest candy free globally:** Taking the globally cheapest freebies satisfies legality but may waste the opportunity to save more expensive eligible candies.
- **Fewer than three candies:** The free slice is empty, so every candy is paid for.
- **Exactly three candies:** The two largest are paid and the smallest is free.
- **Length not divisible by three:** One or two cheapest candies remain after full triples and must be paid because no complete supporting pair remains.
- **Equal prices:** The free candy may cost exactly the minimum of the paid pair, so triples of equal prices are legal.
- **One candy:** Both sums behave correctly: total price minus zero savings.
- **Already descending input:** Sorting leaves the order effectively unchanged; the same index rule applies.
- **Duplicate prices:** Candy identity does not affect cost minimization, and stable ordering among equal values is irrelevant.
- **Input mutation:** Callers that need the original order must copy `cost` before invoking this exact implementation.
- **Savings viewpoint:** Subtraction is safe because every sliced price corresponds to one valid free candy and no price is subtracted twice.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $n$ be the number of candies. Sorting costs $O(n\log n)$ time. Both calls to `sum` process at most $n$ elements in total up to a constant factor, so they add $O(n)$ time. Sorting dominates, giving $O(n\log n)$ total time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
