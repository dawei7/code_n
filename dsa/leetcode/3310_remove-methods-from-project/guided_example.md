# Guided Example: Remove Methods From Project

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "k": 1, "invocations": [[1, 2], [0, 1], [3, 2]]}`
- **Required output:** `[0, 1, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are maintaining a project that has `n` methods numbered from `0` to $n - 1$.

The objective is to compute `[0, 1, 2, 3]` from `{"n": 4, "k": 1, "invocations": [[1, 2], [0, 1], [3, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

**First mark exactly the methods affected by the bug.** Treat every invocation `[a,b]` as a directed edge $a\to b$. The source stores these edges in `g`. Starting at `k`, `dfs` follows outgoing edges and marks every reachable node in `suspicious`. It marks before recurring, so cycles do not cause repeated traversal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "k": 1, "invocations": [[1, 2], [0, 1], [3, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

By definition, this directed reachability set is exactly the set that should be removed if removal is allowed: method $k$, everything it directly invokes, and everything reachable through longer invocation chains.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | By definition, this directed reachability set is exactly the... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Understand the removal condition as a cut condition.** Suspicious methods may be removed only if there is no edge from a normal method into the suspicious set. An edge from suspicious to normal cannot actually exist after reachability is complete: if suspicious $u$ invokes $v$, then $v$ is reachable from $k$ and would also be suspicious. Therefore every graph edge crossing between suspicious and normal nodes, if any, must point from normal to suspicious and makes removal impossible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "k": 1, "invocations": [[1, 2], [0, 1], [3, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan every directed edge after reachability:**:** - **Scan every directed edge after reachability:** If any edge has a normal source and suspicious destination, return `list(range(n))`; otherwise return the complement. This is simpler and equally $O(n+m)$.
- **In-degree adjustment:** While removing reachable outgoing edges, decrement target indegrees. Any suspicious node with remaining indegree has an incoming normal edge, as described in the editorial.
- **Iterative BFS or DFS:** Explicit stacks or a deque avoid Python recursion-limit failures on long chains while preserving the same bounds.
- **No invocations:** Only $k$ is suspicious, no normal edge enters it, and the method removes just $k$.
- **Every node reachable from $k$:** All nodes are suspicious, there is no outside method, and returning an empty list is valid.
- **Normal method invokes $k$:** The undirected component traversal reaches the whole suspicious set and clears it, so all methods remain.
- **Cycle inside the suspicious set:** Directed marking handles it through the Boolean guard, and internal edges do not block removal.
- **Disconnected normal components:** `dfs2` starts once per unvisited component. Components with no suspicious adjacency leave flags unchanged.
- **Suspicious-to-normal edge:** This cannot remain after directed reachability; its endpoint would be suspicious by definition.
- **Unused `ans` variable:** It is dead local state and does not collect the return value.
- **Deep chain:** Recursive depth can be $\Theta(n)$ and may fail in standard Python even though the abstract complexity is linear.
- **Output order:** The final range-based comprehension returns ascending IDs, a valid choice under the any-order contract.
- **All-or-none behavior:** The undirected method is correct only because all suspicious nodes are connected to $k$ and no outgoing crossing edge can exist; stating these facts is essential.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of methods and $m$ the number of invocations. Building `g` stores $m$ directed adjacency entries; `f` stores $2m$ undirected entries. Directed DFS visits each suspicious node and outgoing edge at most once. Undirected DFS across normal-started components visits each reached node and adjacency at most once. The outer scans and output construction cost $O(n)$. Total time is $O(n+m)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
