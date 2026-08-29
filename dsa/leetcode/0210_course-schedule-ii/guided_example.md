# Guided Example: Course Schedule II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"numCourses": 2, "prerequisites": [[1, 0]]}`
- **Required output:** `[0, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are a total of `numCourses` courses you have to take, labeled from `0` to $numCourses - 1$. You are given an array `prerequisites` where $\text{prerequisites}[i] = [a_{i}, b_{i}]$ indicates that you **must** take course $b_{i}$ first if you want to take course $a_{i}$.

The objective is to compute `[0, 1]` from `{"numCourses": 2, "prerequisites": [[1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate prerequisites into directed edges in the useful direction

Treat each course as a vertex in a directed graph. A pair `[a, b]` says that
course `b` must be completed before course `a`, so the graph needs the edge
`b -> a`. The direction matters: once `b` has been taken, that edge tells the
algorithm which dependent course may have become available.

The exact solution stores these outgoing edges in `g`, a `defaultdict(list)`.
For every pair `[a, b]`, it appends `a` to `g[b]`. At the same time,
`indeg[a]` is incremented. The indegree of a course is the number of its
prerequisites that have not yet been removed from consideration. Initially no
course has been processed, so the constructed value is simply its total number
of prerequisite edges.

Reversing the edge would break both structures' meaning. If `[a, b]` were
stored as `a -> b`, processing `a` would appear to unlock `b`, even though the
contract requires `b` first. The chosen `b -> a` direction makes each later
indegree decrement correspond to satisfying one real prerequisite.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"numCourses": 2, "prerequisites": [[1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The next legal course always has indegree zero

A course can be placed next in the answer only when none of its prerequisites
remain unprocessed. In the graph, that condition is exactly indegree zero.
The solution initializes a `deque` named `q` with every course whose entry in
`indeg` is zero, including isolated courses that do not appear in any pair.

There can be several zero-indegree courses at once. Their relative order does
not matter because none currently depends on another through an unprocessed
incoming edge. The problem permits any valid ordering, so the deque's order is
acceptable. With the exact initialization, courses are inserted in increasing
numeric order, while newly unlocked courses are appended as they become
available; this determines one possible result but is not a requirement of the
problem.

The algorithm is Kahn's topological-sort algorithm. While the deque is not
empty, it removes one course `i` from the front and appends it to `ans`. At that
moment, `i` has no remaining prerequisite, so placing it after the courses
already in `ans` is legal. Processing `i` conceptually removes `i` and all of
its outgoing edges from the remaining graph.

For every dependent course `j` in `g[i]`, removing edge `i -> j` satisfies one
of `j`'s prerequisites, so the solution decrements `indeg[j]`. If the new value
is zero, every prerequisite of `j` has now been processed, and `j` is appended
to the deque. If the value remains positive, at least one required course is
still missing, so enqueuing `j` would be premature.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a course is never emitted twice

Each input pair is distinct, and every directed edge is processed once, when
its source is removed from the deque. A course enters the deque initially if
its indegree begins at zero. Otherwise, it enters exactly on the one decrement
that changes its indegree from one to zero. Later decrements cannot happen for
a valid count after it reaches zero because those would correspond to other
incoming edges that should already have kept the count above zero. Thus each
course is queued and appended to `ans` at most once.

The array `indeg` is deliberately mutated. It no longer represents original
prerequisite counts after processing starts; it represents counts in the
remaining, not-yet-emitted graph. That evolving meaning is what makes the
constant-time availability test possible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"numCourses": 2, "prerequisites": [[1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **DFS with three colors:** Mark each course unvisited, active, or complete; an edge to an active course reveals a cycle, and courses appended after exploring descendants form a reverse postorder. It has the same $O(V+E)$ bounds but recursive Python implementations can reach depth $V$ and require careful reversal and cycle-state handling.
- **Stack instead of deque:** Kahn's algorithm remains correct if an available course is removed last-in-first-out. It merely selects a different valid topological ordering. The exact solution uses FIFO order with `popleft()`.
- **Repeatedly scan for an available course:** It avoids a queue but can rescan many blocked vertices after every removal, degrading toward $O(V^2+E)$. Maintaining the zero-indegree frontier makes each availability transition explicit.
- **No prerequisites:** Every course begins with indegree zero. The exact initialization queues courses `0` through `numCourses - 1`, and the returned list contains them all in that order.
- **One course:** With no self-edge allowed by the contract, course 0 begins available and the method returns `[0]`.
- **Several disconnected components:** Initial zero-indegree vertices from all components may be interleaved. This is valid because there are no prerequisite edges constraining the relative order of separate components.
- **A directed cycle:** No vertex in a closed cycle can reach indegree zero after outside prerequisites are removed. The final length check rejects the partial order and returns an empty list, as required.
- **A cycle plus independent courses:** Independent courses may appear in `ans` before the queue stalls. The method still returns `[]`, not that partial list, because the contract requires an ordering of every course.
- **Multiple prerequisites for one course:** Its indegree decreases once per prerequisite edge, and it is queued only after the last one is processed. This prevents a course from appearing after merely some of its requirements.
- **Distinct-pair guarantee:** The reference says prerequisite pairs are distinct. If duplicate edges were accepted without normalization, both the initial count and later decrements would be duplicated consistently, so this implementation would often still balance them, but relying on duplicates as separate requirements would be an unnecessary representation of invalid input.
- **Input preservation:** The algorithm mutates only its newly created graph, indegree array, deque, and answer. It reads but does not alter `prerequisites` or its pairs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let $V$ be `numCourses` and $E$ be `len(prerequisites)`. Building `g` and
- **Auxiliary Space Complexity:** $O(V+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
