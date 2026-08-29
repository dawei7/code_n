# Guided Example: Finish Time of Tasks I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 5, 3]}`
- **Required output:** `17`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` representing the number of tasks in a project, numbered from 0 to $n - 1$. These tasks are connected as a **tree** rooted at task 0. This is represented by a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates that task $u_{i}$ is the parent of task $v_{i}$.

The objective is to compute `17` from `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 5, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building child lists

The line



creates one empty child list per task. For each directed pair `u,v`, the source appends `v` only to `g[u]`:



It does not add the reverse edge because `v` is not the parent of `u`. It also needs no visited set or parent parameter: following child lists in a valid rooted tree can never move back upward or enter a cycle.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 5, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What `dfs(i)` returns

The nested function `dfs(i)` returns the finish time of task `i` after completely evaluating the subtree rooted at `i`.

If `g[i]` is empty, task `i` has no children. The leaf rule applies directly:



For a non-leaf, the function recursively calls `dfs(j)` for every child `j`. Each call returns a child finish time only after resolving all descendants below that child. While those values arrive, the source retains just their minimum and maximum:



Intermediate child finish times do not otherwise affect the parent's formula, so no list of them is required.

After all children have been processed, the function calculates



which is exactly the rule from the description.

Finally, `dfs(0)` evaluates the entire tree and returns the root's finish time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the recursive values are the required values

Every leaf return is correct by the leaf definition. Consider a non-leaf task after assuming each recursive child call has returned that child's correct finish time. The loop computes the minimum and maximum of precisely those values. Substituting them into the given non-leaf formula produces task `i`'s required finish time.

Because a finite tree has leaves and every parent appears above its descendants, this reasoning propagates from the leaves through every subtree to task `0`. Each task is reached exactly once because it has exactly one parent except for the root.

For a node with only one child whose finish time is `a`, both `earliest` and `latest` equal `a`. The spread is zero, so the parent finish is `a+\texttt{baseTime}[i]`. The general code handles this without a special branch.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `17` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 5, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `17` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative preorder plus reversed order:** Build an order in which every parent precedes its children, then process that list backward. This preserves `O(n)` time and space while safely supporting a chain of `10^5` tasks. It would also match the manifest's reverse-traversal summary, but it is not what the stored source currently does.
- **Memoized recursion:** Memoization is unnecessary on a tree because every non-root node has one parent and is requested once. It would not repair missing imports or the call-stack limit.
- **Recompute each subtree repeatedly:** Evaluating descendants anew for every ancestor can become quadratic on a chain. Returning each subtree's finish time once gives the linear traversal.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For the intended execution, let `n` be the number of tasks and let `h` be the height of the rooted tree.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
