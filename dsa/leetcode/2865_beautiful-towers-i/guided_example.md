# Guided Example: Beautiful Towers I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [5, 3, 4, 1, 1]}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `heights` of `n` integers representing the number of bricks in `n` consecutive towers. Your task is to remove some bricks to form a **mountain-shaped** tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.

The objective is to compute `13` from `{"heights": [5, 3, 4, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Fix a peak and make every other tower as tall as legality permits.** A mountain can rise non-decreasingly toward a chosen peak index `i` and fall non-increasingly after it. Towers may be shortened but never raised above `maxHeights[j]`. Once peak `i` is fixed at its maximum allowed height `x = maxHeights[i]`, the best height at every other position is forced greedily.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [5, 3, 4, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Moving left from the peak, each tower must be no taller than the tower immediately to its right; otherwise the sequence would decrease while approaching the peak. It must also be no taller than its own cap. If `y` is the height chosen for the position to the right, the greatest legal current height is

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Moving right is symmetric: each tower must be no taller than the previously chosen tower on its left and no taller than its cap, so the same minimum rule applies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [5, 3, 4, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Monotonic-stack prefix and suffix sums:** Compute the best constrained sum ending at every index from the left and from the right, then combine them. This gives $O(n)$ time and $O(n)$ space and is the true optimal asymptotic method.
- **Materializing each mountain:** Building a full temporary array per peak is conceptually similar but adds unnecessary $O(n)$ working space; the source accumulates its sum directly.
- **Peak at an endpoint:** One side loop is empty, and the other side's running minima correctly form a one-sided mountain.
- **Flat peak plateau:** Equal adjacent maximum heights are allowed because mountain inequalities are non-strict. Testing every index safely covers any plateau.
- **Single tower:** Both inner loops are empty, so the only cap is used and returned.
- **Very low cap away from the peak:** Once the running minimum drops, all farther towers on that side can be no higher until an even lower cap appears.
- **Large sums:** Fixed-width implementations need 64-bit accumulation even though individual heights fit 32 bits.
- **Manifest mismatch:** Complexity documentation must follow the loops that execute; calling this exact source a monotonic-stack solution would be misleading.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For peak `i`, the two inner loops together visit exactly `i + (n-1-i) = n-1` non-peak positions. Repeating for all $n$ peaks performs $n(n-1)$ position updates, so time is $\Theta(n^2)$, not $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
