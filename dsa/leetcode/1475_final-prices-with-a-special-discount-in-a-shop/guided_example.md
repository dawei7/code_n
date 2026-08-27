# Guided Example: Final Prices With a Special Discount in a Shop

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"prices": [8, 4, 6, 2, 3]}`
- **Required output:** `[4, 2, 4, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `prices` where $\text{prices}[i]$ is the price of the $$i^{\text{th}}$$ item in a shop.

The objective is to compute `[4, 2, 4, 2, 3]` from `{"prices": [8, 4, 6, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Scan from right to left so future prices are already known.** For item `i`, the discount is the first later price no greater than its original price. Processing from the end lets a stack summarize useful candidates to the right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"prices": [8, 4, 6, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source saves `x = prices[i]` before modifying the array. This original value must be pushed later; a discounted final price must never serve as another item's discount.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source saves `x = prices[i]` before modifying the array.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Remove candidates that current x dominates.** While the stack top is strictly greater than `x`, it is popped. Such a value cannot discount `x`. It also cannot be the first useful discount for an earlier item in preference to `x` when `x` is closer and smaller, so it is permanently dominated.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 2, 4, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"prices": [8, 4, 6, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 2, 4, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Left-to-right index stack:** Keep unresolved i:** - **Left-to-right index stack:** Keep unresolved item indices and apply the current price when it is the first smaller-or-equal value. It is the common equivalent formulation.
- **Nested scan:** Search rightward from every item and stop at the first qualifying price. It is simpler but `O(N^2)` in the worst case.
- **Equal next price:** Equality qualifies; the strict pop condition preserves it for subtraction.
- **No qualifying later price:** The stack empties after larger values are removed, so the original price remains unchanged.
- **Last item:** It has no later item and is pushed without a discount.
- **Strictly increasing prices:** No item finds a no-greater later price, so values remain unchanged.
- **Repeated prices:** The nearest equal price supplies the discount.
- **Original versus final price:** The stack receives `x` captured before mutation, never the discounted value.
- **Zero final price:** Equal price can be subtracted completely, which is valid.
- **Nearest rather than cheapest:** A farther smaller price must not replace an earlier qualifying price; stack position preserves this rule.
- **Stack value order:** Strictly larger tops are removed, while equal values remain long enough to serve as valid discounts.
- **Single item:** The stack is initially empty, so its price remains unchanged.
- **Input mutation:** The caller's `prices` list is changed and returned.
- **Amortized proof:** Popped entries never return, bounding all while iterations by `N`.
- **Nearest-index requirement:** Dominance removal is safe specifically because the current value is closer to all future left-side items.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Each of `N` original prices is pushed once and popped at most once. Although a while loop is nested inside the scan, total stack operations are `O(N)`, so time is `O(N)`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
