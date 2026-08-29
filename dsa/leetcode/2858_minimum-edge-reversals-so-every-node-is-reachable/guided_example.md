# Guided Example: Minimum Edge Reversals So Every Node Is Reachable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[2, 0], [2, 1], [1, 3]]}`
- **Required output:** `[1, 1, 0, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a **simple directed graph** with `n` nodes labeled from `0` to $n - 1$. The graph would form a **tree** if its edges were bi-directional.

The objective is to compute `[1, 1, 0, 2]` from `{"n": 4, "edges": [[2, 0], [2, 1], [1, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Ignore direction only to expose the tree.** If all edges were bidirectional, the graph would be a tree. Therefore, between any proposed starting node and every other node there is exactly one undirected path. To make all nodes reachable from a chosen root, every edge on that rooted tree must point from parent to child. The task is not choosing among alternative routes; it is counting which of those uniquely positioned edges face the wrong way.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[2, 0], [2, 1], [1, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Computing that count independently for all $n$ roots would repeat almost all work. The solution instead computes the answer for root `0` once, then changes the root across one edge at a time. This technique is called rerooting.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Encoding direction with a sign.** For every original directed edge `x -> y`, the adjacency list receives two records: from `x` to `y` it stores `(y, 1)`, and from `y` to `x` it stores `(x, -1)`. The sign describes how the original arrow looks when traversing that adjacency entry. A `1` means the arrow already follows the traversal direction. A `-1` means traversal goes against the original arrow.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 0, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[2, 0], [2, 1], [1, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 0, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative two-pass rerooting:** Build a parent and order array with an explicit stack, compute `ans[0]` during that traversal, and then process nodes in parent-before-child order using `ans[child] = ans[parent] + sign`. This avoids the recursion-limit defect while keeping $O(n)$ time and space.
- **Independent search from every root:** Recounting wrong arrows for each start node costs $O(n^2)$ time and discards the one-edge rerooting relationship.
- **Direction-sign convention:** The formulas depend on storing `+1` in the original arrow direction and `-1` in the reverse adjacency direction. Reversing that convention requires reversing both count and transition formulas.
- **Two-node tree:** The answers are necessarily `[0,1]` or `[1,0]`; crossing the sole edge changes the count by exactly one.
- **Already outward from one node:** That node receives answer zero. Rerooting still correctly measures how many arrows become wrong for other starts.
- **Tree guarantee:** The parent check `j != fa` is sufficient only because the underlying graph is a tree. A general graph would require a visited set and would not have one uniquely required orientation per edge.
- **Independent answers:** Each `answer[i]` is computed for its own optimal reversal plan. The reroot formula does not claim one fixed set of reversals works for all starts simultaneously.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Building the signed adjacency list stores two entries per one of the $n-1$ edges and takes $O(n)$ time. Each DFS visits every node once and examines every adjacency entry once, so the two traversals together remain $O(n)$. The answer array and adjacency list require $O(n)$ space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
