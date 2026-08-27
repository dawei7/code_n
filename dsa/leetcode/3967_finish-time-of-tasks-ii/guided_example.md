# Guided Example: Finish Time of Tasks II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 1, 5]}`
- **Required output:** `14`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` representing the number of tasks in a project, numbered from 0 to $n - 1$. These tasks are connected as an undirected** tree**. This is represented by a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an undirected connection between task $u_{i}$ and task $v_{i}$.

The objective is to compute `14` from `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 1, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The message carried along a directed edge

For adjacent tasks `u` and `v`, imagine cutting edge `\{u,v\}`. Define the message

$$
F(u\to v)
$$

as the finish time of `u` when `v` is treated as `u`'s parent. Equivalently, `u` combines information from every neighbor except `v`.

If a candidate root is `u`, then every neighbor `v` is a child and contributes `F(v\to u)`. Once all incoming neighbor messages are known, the finish time for root `u` is simply

$$
\operatorname{combine}\bigl(u;\{F(v\to u):v\text{ adjacent to }u\}\bigr).
$$

The whole algorithm is therefore about producing both directed messages for every undirected edge without recomputing complete components.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 1, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building one temporary orientation

The source first stores both directions of every edge in `graph`. It then temporarily roots the tree at task zero solely to establish parent-child order:



Python's list iterator continues to see items appended during this loop. Consequently, `order` grows until it contains every task. A parent is appended before any of its children.

Checking only `neighbor != parent[task]` is sufficient because the input is a tree. After excluding the one edge back to the parent, every remaining edge leads to an unvisited child; there are no cycles or cross edges.

Assigning `parent[0]=0` gives the temporary root a harmless self-marker. Task zero is not its own graph neighbor because tree edges connect distinct tasks.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source first stores both directions of every edge in `gr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Bottom-up messages from child side to parent side

The array `downward` stores messages following the temporary orientation. For a non-root task `u`,

$$
\texttt{downward}[u]=F(u\to\texttt{parent}[u]).
$$

Since parents precede children in `order`, traversing `reversed(order)` processes every child before its parent. The source gathers `downward` values only from neighbors whose recorded parent is the current task.

If there are no such children, `u` is a leaf in the temporary orientation, so its message is `baseTime[u]`. Otherwise, applying the combine rule to the child messages gives



This completes every message directed from a node toward its temporary parent. It also computes a value for task zero using all its temporary children, although zero has no parent that needs that particular message.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `14` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "edges": [[0, 1], [1, 2]], "baseTime": [9, 1, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `14` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recompute from every root:** Running a complet:** - **Recompute from every root:** Running a complete postorder evaluation `n` times is easy to conceptualize but costs `O(n^2)` in the worst case. Directed edge messages reuse the unchanged component results.
- **- **Recursive rerooting:** Two recursive DFS passe:** - **Recursive rerooting:** Two recursive DFS passes can express the same message equations, but a chain of length `10^5` can exceed Python's recursion limit. The stored iterative order avoids that failure mode.
- **- **Rescan all other neighbors for every child:** :** - **Rescan all other neighbors for every child:** At a star center, excluding each child and scanning the remaining `O(n)` messages would make that one node cost `O(n^2)`. First and second extrema make every exclusion constant time after one scan.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of tasks. A tree has `n-1` edges, so the undirected adjacency lists contain `2(n-1)` neighbor entries.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
