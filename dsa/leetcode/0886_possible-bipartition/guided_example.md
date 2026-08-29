# Guided Example: Possible Bipartition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "dislikes": [[1, 2], [1, 3], [2, 4]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

The objective is to compute `true` from `{"n": 4, "dislikes": [[1, 2], [1, 3], [2, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

Treat each person as a graph vertex and each dislike pair as an undirected edge. The two people at the endpoints of every edge must be placed in different groups. The requested split exists exactly when this graph is bipartite, meaning its vertices can be colored with two colors so every edge connects different colors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "dislikes": [[1, 2], [1, 3], [2, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution first converts labels 1 through `n` to zero-based indices 0 through `n - 1`. Each dislike is inserted in both adjacency lists because the restriction is mutual for grouping purposes: if `a` and `b` cannot share a group, each must be seen as a neighbor of the other during traversal.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

- 0 means the person has not been assigned.
- 1 means the first group.
- 2 means the second group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "dislikes": [[1, 2], [1, 3], [2, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first coloring:** A queue can assign alternating colors level by level. It has the same $O(n+m)$ bounds and avoids recursion-depth concerns.
- **Union-find:** For each person, union all disliked neighbors into the opposite side and detect contradictions. This works but is less direct than two-color traversal.
- **Try all two-group assignments:** There are $2^n$ assignments, while graph coloring resolves forced choices in linear time.
- **Check only one connected component:** This can miss an odd cycle elsewhere. The outer `all(...)` must cover every uncolored vertex.
- **No dislikes:** Every vertex begins a trivial component or is harmlessly colored; any partition works and the result is true.
- **Isolated people:** They can join either group. Starting them with color 1 creates no edge conflict.
- **One dislike pair:** Its endpoints receive opposite colors and the result is true.
- **Odd cycle:** Alternation returns to the start with the wrong color and correctly produces false.
- **Even cycle:** Alternation closes consistently and is valid.
- **Repeated traversal edges:** The undirected edge appears in both adjacency lists, but already colored opposite endpoints pass the check without recursion.
- **Any group size:** Neither group is required to be nonempty or balanced. Color counts do not enter the decision.
- **One-based input labels:** Subtracting one before adjacency construction is required because `color` uses zero-based indexing.
- **Unique pairs:** The contract prevents duplicate dislikes, though duplicates would not change coloring correctness.
- **Deep graph:** Iterative BFS or DFS is preferable if the runtime's recursion limit is below the maximum component depth.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of people and $m$ the number of dislike pairs. Building the undirected adjacency list stores two entries per pair. Across all DFS calls, every vertex is colored once and every adjacency entry is inspected once.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
