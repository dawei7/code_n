# Guided Example: Type of Triangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 3, 3]}`
- **Required output:** `"equilateral"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of size `3` which can form the sides of a triangle.

The objective is to compute `"equilateral"` from `{"nums": [3, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

**Sort the three side lengths first.** Let the sorted values be

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

Sorting gives one consistent role to each value: $c$ is the longest proposed side. This makes both triangle validation and equality classification simple. The exact source calls `nums.sort()`, so it rearranges the caller's three-element list in place.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Why only one triangle inequality must be tested.** Three positive lengths form a nondegenerate triangle exactly when each pair sums to more than the remaining side:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"equilateral"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"equilateral"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check all three inequalities:** This is correct but redundant for sorted positive lengths. The largest-side inequality implies the other two automatically.
- **Avoid sorting with a maximum:** One can find the largest side and compare it with the sum of the other two, then count equalities. That remains $O(1)$ but tends to require more bookkeeping than sorting three items.
- **Use a set for classification:** The number of distinct lengths distinguishes equilateral, isosceles, and scalene after validity is known. Creating a set works, but direct comparisons avoid an extra container.
- **Degenerate equality $a+b=c$:** It must return `"none"` because the required inequality is strict and the segments enclose no area.
- **One side longer than the other two combined:** The same `<=` condition rejects it immediately.
- **All three sides equal:** Positivity guarantees validity, and comparing the sorted smallest with largest correctly identifies equilateral.
- **Exactly two sides equal:** The equal values become adjacent after sorting, so one of the isosceles comparisons succeeds.
- **Three distinct valid sides:** Both equality checks fail, leaving scalene.
- **Positive-length guarantee:** The proof that two inequalities are automatic relies on positive sides. If zeros or negative values were allowed, the validation would need additional checks, but they are outside this contract.
- **Input order:** Any permutation produces the same sorted triple and therefore the same classification.
- **Input mutation:** The protected source leaves `nums` sorted. This does not change the returned answer, but callers should not assume the original ordering remains.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The list always contains exactly three values. Sorting three values performs only a bounded number of comparisons, and all later work is a bounded sequence of arithmetic and equality tests. With respect to input size, time complexity is $O(1)$ and auxiliary space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
