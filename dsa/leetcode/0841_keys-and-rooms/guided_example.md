# Guided Example: Keys and Rooms

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rooms": [[1], [2], [3], []]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` rooms labeled from `0` to $n - 1$ and all the rooms are locked except for room `0`. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

The objective is to compute `true` from `{"rooms": [[1], [2], [3], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Interpret keys as directed edges

Treat every room as a graph vertex. A key `j` found in room `i` creates a directed edge from `i` to `j`: once room `i` has been visited, that key makes room `j` reachable.

Room 0 is the only initially unlocked room, so the question becomes:

> Are all graph vertices reachable from vertex 0?

Depth-first search answers exactly that.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rooms": [[1], [2], [3], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The visited set represents rooms already unlocked and entered

Set `vis` starts empty. Calling `dfs(0)` models entering the initially open room.

When `dfs(i)` is called, it first checks `if i in vis`. If so, that room and all keys reachable through it have already been processed, so the call returns.

Otherwise, it adds `i` to `vis` before following any key. Marking before recursion is essential. If room 0 contains a key to room 1 and room 1 contains a key back to room 0, the second call to room 0 sees it already marked and stops rather than recursing forever.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Set `vis` starts empty.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Follow every key

For each key `j` in `rooms[i]`, the function calls `dfs(j)`.

If `j` is new, the key unlocks a new reachable room, which is entered and explored. If it was already visited through another route, the early check makes the call constant work.

Taking keys is never harmful and has no capacity cost, so exploring every listed edge is the right action. A key can point to the current room, a previously visited room, or a future room; the same logic handles all cases.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rooms": [[1], [2], [3], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Breadth-first search:** A queue-based traversa:** - **Breadth-first search:** A queue-based traversal discovers the same reachable set and avoids recursion depth concerns.
- **- **Repeatedly scan for newly unlocked rooms:** It:** - **Repeatedly scan for newly unlocked rooms:** It can require many passes. Graph traversal processes each room and key once.
- **- **No visited set:** Cycles such as room 0 keying:** - **No visited set:** Cycles such as room 0 keying room 1 and room 1 keying room 0 would recurse forever or repeat work.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+K)$. Let `n` be the number of rooms and
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
