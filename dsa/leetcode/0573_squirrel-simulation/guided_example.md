# Guided Example: Squirrel Simulation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"height": 5, "width": 7, "tree": [2, 2], "squirrel": [4, 4], "nuts": [[3, 0], [2, 5]]}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers `height` and `width` representing a garden of size `height x width`. You are also given:

The objective is to compute `12` from `{"height": 5, "width": 7, "tree": [2, 2], "squirrel": [4, 4], "nuts": [[3, 0], [2, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

After the squirrel delivers its first nut, it is at the tree. Every later nut trip must start at the tree, travel to the nut, and return to the tree. Therefore only the choice of the **first** nut differs from a simple round-trip baseline.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"height": 5, "width": 7, "tree": [2, 2], "squirrel": [4, 4], "nuts": [[3, 0], [2, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Movement is horizontal and vertical on an obstacle-free grid, so distance between positions is Manhattan distance:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Movement is horizontal and vertical on an obstacle-free grid... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
\lvert r_1-r_2\rvert+\lvert c_1-c_2\rvert.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"height": 5, "width": 7, "tree": [2, 2], "squirrel": [4, 4], "nuts": [[3, 0], [2, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every complete nut order:** There are $n!$:** - **Try every complete nut order:** There are $n!$ orders, but only the first choice affects cost.
- **Always choose the nut nearest the squirrel:** The correct comparison is `b-a`; a slightly farther nut may save a much longer tree outbound leg.
- **Always choose the nut farthest from the tree:** Squirrel distance also matters.
- **One nut:** The formula becomes squirrel-to-nut plus nut-to-tree.
- **Squirrel starts at tree:** For every nut `a=b`, all first choices equal the baseline.
- **Nut at squirrel position:** Its first outbound cost is zero.
- **Nut at tree position:** Its tree distance is zero; choosing it first may still require travel from the squirrel.
- **Several optimal first nuts:** Minimum total is the same; only the distance is returned.
- **Garden boundaries:** Manhattan routes between valid coordinates need no explicit boundary simulation.
- **One-nut carrying limit:** It is what makes later trips independent tree round trips.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of nuts. Baseline construction visits every nut once, and evaluating first choices visits each once again. Constant arithmetic per nut gives $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
