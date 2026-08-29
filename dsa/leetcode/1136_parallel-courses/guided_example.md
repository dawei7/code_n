# Guided Example: Parallel Courses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "relations": [[1, 3], [2, 3]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where $\text{relations}[i] = [\text{prevCourse}_{i}, \text{nextCourse}_{i}]$, representing a prerequisite relationship between course $\text{prevCourse}_{i}$ and course $\text{nextCourse}_{i}$: course $\text{prevCourse}_{i}$ has to be taken before course $\text{nextCourse}_{i}$.

The objective is to compute `2` from `{"n": 3, "relations": [[1, 3], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the prerequisite rules into a directed graph

Each course is a vertex. A relation `[prev, next]` is a directed edge from `prev` to `next` because completing `prev` is a condition for taking `next`. The important value for a course is its *indegree*: the number of prerequisite edges currently pointing into it. An indegree of zero means that none of its prerequisites remain unfinished, so the course is available in the next semester.

The solution stores outgoing edges in `g`. For every relation, it converts the one-based course labels to zero-based indices, appends `nxt` to `g[prev]`, and increments `indeg[nxt]`. The queue is then initialized with every course whose indegree is zero. Those courses have no prerequisites at all, so they are exactly the courses that can be taken in semester one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "relations": [[1, 3], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why taking every available course is always optimal

There is no upper bound on the number of courses taken in one semester. Therefore, postponing an available course cannot create any advantage. Taking it now does not compete for a limited seat, time slot, or course allowance. On the other hand, postponing it may postpone every course that depends on it. Consequently, an optimal schedule may take all currently available courses together.

This observation turns Kahn's topological-sort algorithm into a semester simulation. One queue layer represents one semester. At the start of the `while q` iteration, every course already in `q` is eligible for the semester about to begin. The code increments `ans` once, records the layer size through `range(len(q))`, and removes exactly that many courses.

Capturing the queue length is essential. While a course is processed, each outgoing edge is removed conceptually by decrementing the destination's indegree. If that indegree becomes zero, the destination is appended to the queue. It cannot be taken in the current semester because one of its prerequisites was completed only during this semester, whereas the contract requires prerequisites to have been taken in a previous semester. Since the loop processes only the queue's original length, newly appended courses remain for the following `while` iteration and therefore for the following semester.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the mutable counter means

The parameter `n` initially holds the total number of courses. The solution reuses it as a count of courses not yet processed. Whenever a course is removed from the queue, `n -= 1` marks that course as completed. This mutation does not affect the graph indices or any loop bound; after graph construction, the original total is no longer needed. At the end, `n == 0` means every course appeared in some valid semester. A positive value means some courses were never eligible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "relations": [[1, 3], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Depth-first search with three visitation states:** A DFS can detect a cycle and memoize the longest path beginning at every course, also achieving `O(n + r)` time and space. It is a valid optimal alternative, but the layered breadth-first method maps semesters directly to queue layers and avoids recursion-depth concerns for as many as 5,000 courses.
- **Repeatedly scan all courses for newly available ones:** This can simulate semesters without a queue, but rescanning every course after each layer can require quadratic time on a long prerequisite chain. Maintaining indegrees and a queue records exactly what changed.
- **Take only one available course per semester:** That is legal but not generally minimal. Because there is no per-semester course limit, all eligible courses should be taken together.
- **No initial zero-indegree course:** With at least one course, this means every course has a remaining prerequisite. The graph contains a directed cycle, the loop never starts, and the result must be `-1`.
- **A cycle in only one component:** Other components may be processed completely, but the courses in or below the cyclic component remain unprocessed. Checking the final remaining count catches this case even when the initial queue was nonempty.
- **Several prerequisites for one course:** The course is appended only when the last incoming edge is removed. Earlier decrements leave a positive indegree, so it cannot be scheduled prematurely.
- **Several outgoing relations from one course:** Processing that course decrements every dependent course independently. Any of them whose final prerequisite has now been completed becomes eligible for the next layer.
- **Independent courses:** Every course begins in the queue, all are processed in the first layer, and the answer is `1`.
- **A single long chain:** Exactly one course becomes available per layer. The algorithm returns `n`, which is unavoidable because every course after the first depends on a course from the preceding layer.
- **Unique relations:** The input guarantee prevents duplicate edges from artificially inflating indegrees. The implementation relies on the relations representing distinct prerequisite requirements.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + r)$. Let `n` denote the number of courses and let `r` denote `len(relations)`.
- **Auxiliary Space Complexity:** $O(n + r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
