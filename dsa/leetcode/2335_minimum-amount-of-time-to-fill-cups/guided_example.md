# Guided Example: Minimum Amount of Time to Fill Cups

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"amount": [1, 4, 2]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up `2` cups with **different** types of water, or `1` cup of any type of water.

The objective is to compute `4` from `{"amount": [1, 4, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each second should reduce the two largest remaining needs

At most two cups can be filled per second, and they must have different water types. The method repeatedly sorts the three remaining amounts. It always reduces the largest entry and, when positive, also reduces the second-largest entry.

Sorting makes `amount[2]` the largest and `amount[1]` the second largest. Filling one cup of the largest type is always necessary while work remains. Pairing it with the largest other positive type uses the second available dispenser slot without consuming the same type twice.

If only one type remains positive, `amount[1]` is zero. The assignment `max(0, amount[1] - 1)` leaves it at zero, so that second fills only one cup.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"amount": [1, 4, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why pairing the two largest is safe

Suppose a schedule fills the largest type together with a smaller positive type while a larger alternative type is also waiting. Exchanging the smaller partner for the larger partner cannot increase the number of remaining dominant cups and makes the remaining demands no more imbalanced.

The difficult case is always a type that could be left with many cups after the other two run out. Reducing the largest two prevents avoidable imbalance. Repeating the exchange argument transforms an optimal schedule so its first second matches the greedy choice, then applies the same reasoning to the remaining amounts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Two lower bounds explain the optimum

Let `S` be the total number of cups and `M` the largest type count.

Since one second fills at most two cups, at least `ceil(S/2)` seconds are necessary.

Since a second can fill at most one cup of any particular type, the dominant type alone requires at least `M` seconds.

Thus every schedule needs at least

`max(M, ceil(S/2))`

seconds.

The greedy simulation attains this bound. If `M` exceeds the total of the other two types, pair the dominant type with another type until those are exhausted, then finish the remaining dominant cups alone; total time is `M`. Otherwise, no type dominates the combined remainder, so two positive different types can keep being paired until at most one cup remains; total time is `ceil(S/2)`.

Selecting the two largest types maintains exactly the conditions needed for this construction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"amount": [1, 4, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Closed-form bound:** Return `max(max(amount), (sum(amount) + 1) // 2)`. This is the simplest true `O(1)` implementation and follows directly from the two lower bounds.
- **Max heap:** Repeatedly pop the two largest positive counts, decrement, and reinsert. This generalizes to more types but adds unnecessary machinery for exactly three.
- **Pair arbitrary positive types:** It can waste pairing capacity and leave a dominant type to be filled alone longer. Choosing the two largest prevents that imbalance.
- **Fill one cup even when two types remain:** This can never improve the schedule because filling a second different cup in the same second is free.
- **All zeros:** The loop is skipped and the answer is zero.
- **Only one positive type:** Every iteration fills one cup of it, so time equals that amount.
- **Two positive types with equal counts:** Every second pairs them, and time equals either count.
- **One dominant type:** The answer equals its count because at most one cup of that type can be filled each second.
- **Balanced totals:** The answer is total cups rounded up by two.
- **Odd total:** At least one second fills only one cup, accounted for by the ceiling.
- **Second-largest zero:** The `max(0, ...)` guard prevents a negative count.
- **Repeated sorting:** It restores the meaning of indices one and two after decrements; fixed water-type identities are irrelevant to the count.
- **Input mutation:** The source consumes and reorders `amount` until it becomes three zeros.
- **Fixed constraints:** Calling the simulation `O(1)` relies on the numeric cap. In terms of total cups `S`, its literal complexity is linear.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let `S = sum(amount)` initially. Each iteration fills at least one cup, so there are at most `S` iterations. Sorting exactly three elements is constant time, as are the sum and updates. Parameterized running time is `O(S)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
