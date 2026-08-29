# Guided Example: Kids With the Greatest Number of Candies

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"candies": [2, 3, 5, 1, 3], "extraCandies": 3}`
- **Required output:** `[true, true, true, false, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` kids with candies. You are given an integer array `candies`, where each $\text{candies}[i]$ represents the number of candies the $i^{\text{th}}$ kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

The objective is to compute `[true, true, true, false, true]` from `{"candies": [2, 3, 5, 1, 3], "extraCandies": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare each hypothetical total with the current maximum

Each output position describes a separate hypothetical scenario: give all `extraCandies` to that particular child while every other child's candy count remains unchanged.

Before the gift, the strongest competitor has:



candies. If the chosen child reaches at least `mx` after receiving the extras, then nobody has more candies than that child. If the child remains below `mx`, the original maximum holder still has more.

This reduces every answer to:

$$
\texttt{candies}[i]+\texttt{extraCandies}\ge \max(\texttt{candies}).
$$

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"candies": [2, 3, 5, 1, 3], "extraCandies": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the comparison uses the original maximum

Only child `i` receives extra candies in the scenario used for `result[i]`. The other children keep their original counts, so their maximum remains `mx`.

There is no need to recompute a maximum after adding candies. The selected child's new total is being compared against all unchanged competitors. If it exceeds `mx`, it becomes the sole maximum or ties only with nobody; if it equals `mx`, it ties an existing maximum; if it is lower, it cannot be greatest.

Each Boolean is independent. The extras are not distributed cumulatively across children, and producing one result does not consume them for later results.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Equality must produce true

The problem asks whether a child can have the greatest number, not whether the child can have strictly more than everyone else. Multiple children may share the greatest count.

That is why the code uses `>=` rather than `>`. A child with 2 candies and 3 extras reaches 5; if another child already has 5, both have the greatest number and the result is true.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, true, true, false, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"candies": [2, 3, 5, 1, 3], "extraCandies": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, true, true, false, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Nested comparison against every child:** It directly checks each hypothetical scenario but takes $O(n^2)$ time.
- **Sort the candy counts:** The final sorted value gives the maximum, but sorting costs $O(n\log n)$ and can disturb index correspondence if used carelessly.
- **Use threshold `mx - extraCandies`:** Compare each original count with this value. It is algebraically equivalent and also linear.
- **Several original maxima:** Each already-maximal child returns true, and other children may also reach the same threshold.
- **Exactly reaches maximum:** Equality qualifies, so `>=` is essential.
- **Still below maximum:** The result is false even if the child gains many candies relative to its own starting count.
- **All counts equal:** Every child is already greatest, so every output is true.
- **Large extras:** If even the smallest count plus extras reaches `mx`, every output becomes true.
- **Independent scenarios:** Extras are hypothetically reusable for each child; results do not model a single allocation across the group.
- **Nonempty input:** The constraints guarantee at least two children, so `max` is always defined.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of children. `max(candies)` scans $n$ values. The comprehension scans them again and performs constant work each time. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
