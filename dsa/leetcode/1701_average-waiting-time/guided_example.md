# Guided Example: Average Waiting Time

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"customers": [[1, 2], [2, 5], [4, 3]]}`
- **Required output:** `5.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a restaurant with a single chef. You are given an array `customers`, where $\text{customers}[i] = [\text{arrival}_{i}, \text{time}_{i}]:$

The objective is to compute `5.0` from `{"customers": [[1, 2], [2, 5], [4, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track when the single chef becomes free

Customers must be served in input order, and the chef can prepare only one order at a time. The entire state needed for the next customer is therefore one time value: `t`, the completion time of the most recently processed order. Before any customer, the source initializes `t = 0`.

For a customer represented by `[a, b]`, `a` is the arrival time and `b` is the preparation duration. The chef cannot start before both conditions hold:

- the customer has arrived, and
- the previous order has finished.

The earliest valid start time is consequently `max(t, a)`. Adding `b` gives the current order's completion time:

`t = max(t, a) + b`.

This one assignment handles both an idle restaurant and a waiting line.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"customers": [[1, 2], [2, 5], [4, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Case one: the chef is still busy

If the old `t` is greater than `a`, the customer arrives while an earlier order is being prepared. The maximum chooses `t`, so the new completion time is `old_t + b`. The customer waits from arrival `a` through the remaining busy period and through preparation of their own order.

For example, if the chef is free at time eight, a customer arrives at four, and preparation takes three, delivery happens at eleven. The total waiting time for that customer is `11 - 4 = 7`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case two: the chef has been idle

If `a` is at least the old `t`, no pending work delays this customer. The maximum chooses `a`, and completion becomes `a + b`. Any gap between the old completion time and this arrival is idle time; it must not be added to the customer's wait.

The resulting waiting time is exactly `b`, because the problem's definition includes preparation time. This point is easy to misread: “waiting time” here runs until the food is finished, not merely until cooking begins.

When `a == t`, either branch interpretation gives the same start time. The next order begins immediately when the previous one ends.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"customers": [[1, 2], [2, 5], [4, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store every completion time:** A DP-style array can record each finish, but only the preceding finish is needed, so it wastes $O(n)$ space.
- **Event simulation with a queue:** Explicit arrival and completion events reproduce the same process with unnecessary machinery because service order is fixed.
- **Sort the customers:** Arrival order is already non-decreasing, and equal-arrival input order must be preserved; sorting is not needed.
- **Average incrementally:** Updating a floating mean on every customer can introduce repeated rounding. Summing exact integer waits and dividing once is simpler.
- **One customer:** `t` becomes arrival plus preparation, `tot` becomes the preparation duration, and the returned average is that duration.
- **Long idle gap:** `max(t,a)` discards idle time and starts at arrival.
- **Continuous backlog:** When every next arrival precedes `t`, completion simply advances by each preparation duration.
- **Equal arrival times:** The first such customer starts when possible, and subsequent ones wait in their given order.
- **Arrival exactly at completion:** The chef starts the new order immediately, with no extra idle or queue delay.
- **Preparation time is included:** The contribution is completion minus arrival, not start minus arrival.
- **Nonempty input:** The constraint guarantees at least one customer, so division by `len(customers)` cannot divide by zero.
- **Output precision:** Python true division produces a float; the judge accepts answers within the stated tolerance.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of customers. The loop visits each input pair exactly once and performs a maximum, additions, and a subtraction, all constant-time under the usual fixed-width arithmetic model. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
