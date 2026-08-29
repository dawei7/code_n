# Guided Example: Maximum Array Hopping Score II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 5, 8]}`
- **Required output:** `16`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums`, you have to get the **maximum** score starting from index 0 and **hopping** until you reach the last element of the array.

The objective is to compute `16` from `{"nums": [1, 5, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

**Charge each crossed boundary to the hop's destination.** A hop from index $i$ to $j$ earns

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 5, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

There are $j-i$ unit boundaries between those indices. Think of the hop as earning `nums[j]` once for each boundary it crosses. A complete route from index zero to index $n-1$ crosses every boundary exactly once, and each boundary's contribution is the value at the next selected landing to its right.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

For the boundary immediately after index $b$, any landing $j>b$ is possible. To maximize that boundary's contribution, it should be assigned the greatest value available in suffix `nums[b+1:]`. These choices can be made consistently: whenever the suffix maximum changes as boundaries move right, land at the index responsible for the current maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `16` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 5, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `16` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Right-to-left suffix maximum:** Start from the last value, move boundaries right to left, update a running maximum, and add it. This is $O(n)$ time and $O(1)$ space and matches the manifest exactly.
- **Quadratic DP:** For each index, try every later landing and memoize the best suffix score. It is correct but costs $O(n^2)$, as in the smaller version of the problem.
- **Greedy jump to the next larger value only:** A merely larger value may be dominated by an even larger later one; suffix maxima provide the actual criterion.
- **Strictly increasing array:** Earlier indices are repeatedly popped, leaving only the last index; one direct hop is optimal.
- **Strictly decreasing array:** Every index remains. Landing at each next position uses the greatest available suffix value for that boundary.
- **Equal values:** Earlier equal indices are popped by `<=`; delaying the landing loses nothing and can cover more boundaries at the same value.
- **First index on the stack:** Its zero-distance contribution is harmless.
- **Last index:** It always survives and guarantees the route reaches the destination.
- **Positive values:** The upper-bound interpretation is direct. The stated domain excludes negative values that could change whether extra boundaries should share a landing.
- **Input preservation:** The stack stores indices and never reorders `nums`.
- **Manifest mismatch:** Time is linear, but exact auxiliary space is $O(n)$ because of `stk`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each index is pushed once and popped at most once. Although the inner `while` can pop several indices in one iteration, total stack operations across the scan are $O(n)$. The scoring loop visits at most $n$ survivors. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
