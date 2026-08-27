# Guided Example: Course Schedule

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"numCourses": 2, "prerequisites": [[1, 0]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are a total of `numCourses` courses you have to take, labeled from `0` to $numCourses - 1$. You are given an array `prerequisites` where $\text{prerequisites}[i] = [a_{i}, b_{i}]$ indicates that you **must** take course $b_{i}$ first if you want to take course $a_{i}$.

The objective is to compute `true` from `{"numCourses": 2, "prerequisites": [[1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model prerequisite order as directed edges

For prerequisite pair `[a, b]`, course `b` must occur before course `a`.
Represent that requirement with directed edge `b -> a`. If the graph has no
directed cycle, its courses admit a topological order and all can be finished.
If it has a cycle, every course in that cycle waits for another cycle member,
so no valid completion order exists.

The method uses Kahn's topological-sorting algorithm to remove courses whose
prerequisites have all been satisfied.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"numCourses": 2, "prerequisites": [[1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build outgoing neighbors and indegrees together

`g` is an adjacency list with one list per course. For pair `(a, b)`, appending
`a` to `g[b]` records that completing `b` helps unlock `a`.

`indeg[a]` counts how many incoming prerequisite edges still point to course
`a`. It begins at zero and increases once for every prerequisite of `a`.
Course `b` does not receive the increment because the pair says `b` is required,
not that `b` depends on `a`.

The pairs are guaranteed unique, so no dependency edge is accidentally counted
twice. The algorithm would still work with matching duplicate adjacency entries
and indegree increments, but the graph would then contain redundant constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `g` is an adjacency list with one list per course.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Seed the process with immediately available courses

The list comprehension collects every course whose initial indegree is zero.
Such a course has no unfinished prerequisites and can legally be taken first.

There may be several zero-indegree courses. Their relative order does not
matter because none depends on another still-unprocessed prerequisite. The task
asks only whether some valid order exists, not to return a unique schedule.

An empty prerequisite list places every course into `q` immediately.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"numCourses": 2, "prerequisites": [[1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Deque-based Kahn algorithm:** Use `popleft()` :** - **Deque-based Kahn algorithm:** Use `popleft()` for explicit queue semantics; equally linear and less reliant on list-iterator growth knowledge.
- **Indexed list queue:** Maintain an integer cursor into `q`; makes appended-element processing explicit without front removal.
- **DFS coloring:** Mark nodes unvisited, active, or complete; encountering an active node proves a cycle but recursion can reach depth $V$.
- **No prerequisites:** Every course starts at indegree zero and the answer is true.
- **Self-dependency:** Pair `[a,a]` gives positive indegree with no way to unlock the course, returning false.
- **Disconnected graph:** All components are processed independently; a cycle in any one leaves courses remaining.
- **Several prerequisites:** A course is appended only after the last incoming edge is removed.
- **Several initial courses:** Any processing order among them is valid.
- **Unique pair guarantee:** Avoids redundant edges but is not required for the count-based mechanics if duplicates are represented consistently.
- **Missing typing import:** Supply `List` in standalone Python execution.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let $V$ be `numCourses` before it is decremented and $E$ the number of
- **Auxiliary Space Complexity:** $O(V+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
