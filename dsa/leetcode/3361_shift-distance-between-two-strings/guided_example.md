# Guided Example: Shift Distance Between Two Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abab", "t": "baba", "nextCost": [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "previousCost": [1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `t` of the same length, and two integer arrays `nextCost` and `previousCost`.

The objective is to compute `2` from `{"s": "abab", "t": "baba", "nextCost": [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "previousCost": [1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

**Solve each string position independently.** An operation changes one selected character and has no effect on any other index. There is no shared operation budget or cross-position discount. Therefore the minimum total cost is the sum of the minimum conversion cost for every pair `(s[i], t[i])`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abab", "t": "baba", "nextCost": [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "previousCost": [1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For one source letter and target letter, the alphabet is a cycle of 26 vertices. There are two direct routes:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- repeatedly take the next-letter edge;
- repeatedly take the previous-letter edge.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abab", "t": "baba", "nextCost": [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "previousCost": [1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate both routes per character:** At most 25 steps in each direction still gives $O(26n)$ time, asymptotically linear but with repeated cost summation.
- **All-pairs shortest paths:** Floyd–Warshall on 26 letters works but ignores the simple cycle structure and costs $O(26^3)$ preprocessing.
- **Dijkstra per letter pair:** Nonnegative weights permit it, but two simple routes are the only candidates after removing backtracking.
- **Forward wrap:** Use target index `y+26` when `y<x`.
- **Backward wrap:** Use source index `x+26` when `x<y`.
- **Same source and target:** Both costs are zero.
- **Zero-cost edges:** A long route may be free and must be compared rather than rejected for using more shifts.
- **Highly asymmetric costs:** Forward and backward arrays are independent; neither direction is assumed cheaper.
- **Cost belongs to the current letter:** Forward uses `nextCost[j]` when leaving $j$, while backward uses `previousCost[j]` when leaving $j$.
- **Shifted `s2` index:** The `(i+1) % 26` term is deliberate and aligns reverse-edge costs with prefix subtraction.
- **Equal string lengths:** `zip` processes every position because the contract guarantees equal lengths.
- **Lowercase-only contract:** Ordinal subtraction maps every character safely into 0 through 25.
- **Large costs and long strings:** The total may exceed 64-bit limits in other languages; Python's integer arithmetic remains exact.
- **Input preservation:** Strings and cost arrays are read only.
- **No benefit from full cycles:** Costs are nonnegative, so adding a cycle cannot lower a route's total.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+A)$. Let $n$ be the common string length and $A=26$ the alphabet size. Building the doubled prefix arrays costs $O(A)$ time. Processing the zipped character pairs costs $O(n)$ time, so total time is $O(n+A)=O(n)$.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
