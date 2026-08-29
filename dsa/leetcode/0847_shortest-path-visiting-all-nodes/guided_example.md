# Guided Example: Shortest Path Visiting All Nodes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"graph": [[1, 2, 3], [0], [0], [0]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have an undirected, connected graph of `n` nodes labeled from `0` to $n - 1$. You are given an array `graph` where $\text{graph}[i]$ is a list of all the nodes connected with node `i` by an edge.

The objective is to compute `4` from `{"graph": [[1, 2, 3], [0], [0], [0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The current node alone is not enough state

The path may revisit nodes and edges. Reaching node 3 after visiting only `{0,3}` is different from reaching node 3 after visiting `{0,1,2,3}`, because the remaining work differs.

A search state must therefore contain:

- the current node `i`;
- the set of nodes visited so far.

The solution encodes the visited set as a bitmask `st`. Bit `v` is one exactly when node `v` has appeared in the path.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"graph": [[1, 2, 3], [0], [0], [0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Bitmask operations

The mask containing only start node `i` is `1 << i`.

When moving to neighbor `j`, the updated mask is:

`nst = st | (1 << j)`.

Bitwise OR sets `j`'s bit while preserving every previously set bit. Revisiting an already visited node leaves the mask unchanged, which is allowed.

The all-visited mask has its lowest `n` bits set:

`(1 << n) - 1`.

For example, when `n=4`, `1 << 4` is binary `10000` and subtracting one gives `1111`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start from every node simultaneously

The path may begin anywhere. Instead of running a separate BFS from every possible start, the solution initializes the same queue with all `n` singleton states:

`(i, 1 << i)` for every `i`.

All have distance zero. This multi-source BFS explores paths from every allowed starting point together. The first complete state found is therefore optimal across all starts.

The same states are inserted into `vis` immediately, preventing duplicate initial work.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"graph": [[1, 2, 3], [0], [0], [0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **BFS separately from every start:** It repeats much search work. Multi-source BFS finds the best start in one state graph traversal.
- **DFS with subset DP:** Memoize a recurrence over node and visited mask. It can solve the same state graph but shortest unweighted distance is especially natural with BFS.
- **Mark only nodes visited:** Incorrect, because the same current node with different masks represents different remaining tasks.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2 \cdot 2^n)$. There are `n` choices for current node and `2^n` possible visited masks, giving at most `n2^n` states. The queue and visited set therefore use `O(n2^n)` space.
- **Auxiliary Space Complexity:** $O(n \cdot 2^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
