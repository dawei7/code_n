# Guided Example: Count Visited Nodes in a Directed Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"edges": [1, 2, 0, 0]}`
- **Required output:** `[3, 3, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a **directed** graph consisting of `n` nodes numbered from `0` to $n - 1$ and `n` directed edges.

The objective is to compute `[3, 3, 3, 4]` from `{"edges": [1, 2, 0, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

**The graph is a collection of paths feeding cycles.** Every node has exactly one outgoing edge, so starting anywhere produces one deterministic sequence. Eventually a node repeats because the graph is finite. The repeated portion is a directed cycle, while any earlier nodes form a tail leading into that cycle. The number of distinct visited nodes is

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"edges": [1, 2, 0, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\text{tail length}+\text{cycle length}.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Different starting paths can also merge before reaching a cycle. Once a path reaches a node whose answer is already known, its remaining number of visits is known too.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 3, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"edges": [1, 2, 0, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 3, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Indegree pruning:** Remove all indegree-zero nodes with a queue, leaving only cycles; assign cycle lengths, then process removed nodes in reverse. This matches the manifest summary and also runs in $O(n)$ time and space.
- **Three-color DFS:** Track unseen, active, and finished states to detect cycles, but recursive Python implementations risk stack overflow on a chain of length $10^5$.
- **Naive simulation per start:** A fresh visited set from every node can take $O(n^2)$ time because shared tails and cycles are rediscovered.
- **Path merging into solved work:** `cnt + ans[j]` reuses the complete known suffix without entering it again.
- **Pure directed cycle:** Every node receives the cycle length.
- **Long tail into a short cycle:** Answers decrease by one along the tail and become constant on the cycle.
- **Persistent `vis` values:** They need not be cleared because any node from an older traversal also has a completed `ans` value.
- **Self-loop:** The constraints exclude `edges[i] == i`, but the formula would still identify a cycle of length one correctly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Across all starts, each node is first stamped at most once and assigned an answer at most once. Following outgoing edges therefore totals $O(n)$ time, not $O(n)$ per start. Arrays `ans` and `vis` each contain $n$ integers, so auxiliary space is $O(n)$. The algorithm is iterative and has no recursion-depth risk.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
