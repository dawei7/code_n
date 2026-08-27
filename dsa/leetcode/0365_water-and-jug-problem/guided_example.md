# Guided Example: Water and Jug Problem

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"x": 3, "y": 5, "target": 4}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two jugs with capacities `x` liters and `y` liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach `target` using the following operations:

The objective is to compute `true` from `{"x": 3, "y": 5, "target": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What one state represents.

`dfs(i, j)` means that the first jug currently contains `i` liters and the second contains `j` liters. Capacities guarantee

$$
0\le i\le x
\quad\text{and}\quad
0\le j\le y.
$$

The initial call `dfs(0, 0)` represents both jugs being empty. The source names the desired amount `z` even though the local Reference calls it `target`; this is only a parameter-name difference.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"x": 3, "y": 5, "target": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the visited set is necessary.

Jug operations create many cycles. From `(0, 0)`, filling the first jug reaches `(x, 0)`, and emptying it returns immediately to `(0, 0)`. Without cycle detection, recursive search could repeat these states forever.

At the beginning of `dfs`, the pair is checked in `vis`. A repeated pair returns false because all states reachable from it were already scheduled or explored during its first visit. A new pair is inserted before generating neighbors, preventing even a recursive edge back to an ancestor from reopening the cycle.

Returning false for a repeated state cannot hide a solution. Future possibilities depend only on the current amounts, not on the sequence used to reach them. Reaching the same `(i, j)` twice gives exactly the same available operations and goal condition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Jug operations create many cycles.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognizing a successful state.

The contract asks whether the total water across both jugs can equal `target`. The source accepts when `i + j == z`. It also checks `i == z` and `j == z`; those are consistent special cases in which one jug alone holds the desired amount, regardless of whether the other is empty in the current state.

In the ordinary jug formulation, measuring `z` liters in either jug is accepted, and measuring `z` in total is accepted by this statement. Checking all three conditions exactly covers the source's success semantics.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"x": 3, "y": 5, "target": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Bézout and Euclid:** A target is measurable ex:** - **Bézout and Euclid:** A target is measurable exactly when it does not exceed `x + y` and is divisible by `gcd(x, y)`. Euclid computes the gcd in $O(\log\min(x,y))$ time and $O(1)$ iterative space. This matches the manifest but is not the checked-in source.
- **- **Breadth-first search:** Use an explicit queue :** - **Breadth-first search:** Use an explicit queue with the same six transitions. It has the same reachable-state complexity, avoids recursion-depth failure, and can find a shortest operation sequence if parent links are retained.
- **- **Full two-dimensional Boolean table:** Mark eve:** - **Full two-dimensional Boolean table:** Mark every `(i, j)` pair in an array. It gives deterministic lookup but allocates $O(xy)$ space despite only boundary states being reachable.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(x+y)$. The boundary contains at most $2(y+1)+2(x+1)$ state positions, with corners counted more than once in that expression. Each newly visited state performs constant work and generates six transitions. Expected visited-set lookup and insertion are $O(1)$, so the exact search takes expected $O(x+y)$ time and $O(x+y)$ visited-set space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
