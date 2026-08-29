# Guided Example: Maximum Total Beauty of the Gardens

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"flowers": [1, 3, 1, 1], "newFlowers": 7, "target": 6, "full": 12, "partial": 1}`
- **Required output:** `14`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice is a caretaker of `n` gardens and she wants to plant flowers to maximize the total beauty of all her gardens.

The objective is to compute `14` from `{"flowers": [1, 3, 1, 1], "newFlowers": 7, "target": 6, "full": 12, "partial": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate complete-garden value from incomplete minimum value

For any final arrangement, beauty has two components: `x * full` for `x` complete gardens, and `y * partial` where `y` is the minimum flower count among all remaining incomplete gardens. The solution enumerates the possible number `x` of complete gardens. For each fixed `x`, it spends the remaining flowers as efficiently as possible to maximize `y`.

Sorting `flowers` is the key first step. After sorting, the cheapest gardens to make complete are the largest incomplete ones because they are closest to `target`. Therefore, for a fixed count `x`, an optimal arrangement can choose the last `x` sorted gardens as complete and leave the first `n - x` incomplete.

Any garden already at least `target` is unavoidably complete because planted flowers cannot be removed. `bisect_left(flowers, target)` finds the first already-complete position, so

`i = n - bisect_left(flowers, target)`

is the initial number of complete gardens. The outer loop starts at `i` and tries every count through `n`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"flowers": [1, 3, 1, 1], "newFlowers": 7, "target": 6, "full": 12, "partial": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain the cost of completing the largest gardens

`newFlowers` is mutated into the budget remaining for the current `x`. At the start of an iteration, the statement

`newFlowers -= 0 if x == 0 else max(target - flowers[n - x], 0)`

adds one more garden to the complete suffix compared with the preceding iteration.

At the first iteration, if some gardens were already complete, index `n - x` points to the first of those and its cost is clamped to zero. If none were complete and `x = 0`, the conditional also subtracts zero. Each later iteration subtracts the flowers needed to raise the next-largest incomplete garden to `target`.

Because this cost accumulates, after the subtraction for `x`, the current `newFlowers` is exactly what remains after making the largest `x` gardens complete as cheaply as possible. If it becomes negative, that count is impossible, and every larger count costs at least as much, so the loop safely breaks.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use prefix sums to price a minimum level

The first `n - x` gardens remain incomplete. To raise their minimum, flowers must go to the smallest values first. The prefix-sum array

`s = list(accumulate(flowers, initial=0))`

lets the method compute the cost to raise sorted positions zero through `p` to `flowers[p]`:

$$
\texttt{flowers}[p](p+1) - \texttt{s}[p+1].
$$

The product is the total those `p + 1` gardens would contain at the common level, and the prefix sum is what they already contain. Their difference is the required additions.

As `p` grows, this leveling cost never decreases. The code binary-searches the largest feasible prefix endpoint between zero and `n - x - 1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `14` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"flowers": [1, 3, 1, 1], "newFlowers": 7, "target": 6, "full": 12, "partial": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `14` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Binary-search the minimum flower value for every `x`:** This can yield the manifest's `O(n \log target)` component, but the exact code searches prefix endpoints and derives the level arithmetically.
- **Try every flower allocation:** The number of distributions is enormous and ignores the sorted exchange and water-filling structure.
- **Always make as many gardens complete as possible:** A high `partial` reward can make leaving one garden incomplete at a large minimum more valuable than completing all gardens.
- **Never complete additional gardens:** A high `full` reward can make the opposite choice optimal; enumeration handles both extremes.
- **Initially complete gardens:** They are counted from the first iteration and cost zero additional flowers.
- **All gardens initially complete:** The first case has `x = n` and `y = 0`.
- **Budget cannot complete another garden:** The loop still optimizes the partial minimum for the current feasible `x`, then breaks when the next count becomes negative.
- **One incomplete garden:** All remaining useful partial-budget flowers can raise it, capped at `target - 1`.
- **Partial cap:** Without the cap, the calculation could label a garden incomplete while raising its minimum to the completion threshold.
- **Unused flowers:** Planting at most `newFlowers` is allowed, so budget beyond all useful capped levels need not be spent.
- **Repeated flower counts:** Sorting and prefix-cost formulas work unchanged; leveling equal values costs zero.
- **Large budget:** Python integers safely store cumulative costs and beauty values.
- **Input order:** Sorting mutates the list; callers needing original order must copy it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Sorting takes `O(n \log n)` time, and prefix sums take `O(n)`. The outer loop has at most `n + 1` iterations. Each performs a binary search over at most `n` incomplete indices, costing `O(\log n)`. Total time for the exact implementation is `O(n \log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
