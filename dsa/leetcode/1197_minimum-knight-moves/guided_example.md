# Guided Example: Minimum Knight Moves

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"x": 2, "y": 1}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In an **infinite** chess board with coordinates from `-infinity` to `+infinity`, you have a **knight** at square `[0, 0]`.

The objective is to compute `1` from `{"x": 2, "y": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent the eight legal moves

The tuple `dirs` contains every combination where one coordinate changes by two and the other by one, with all required signs and orientations. From `(i, j)`, adding `(a, b)` produces neighbor `(i + a, j + b)`.

The board is infinite, so there is no boundary check. Negative and positive coordinates are equally valid.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"x": 2, "y": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Queue and visited set start at the origin

The deque `q` initially contains `(0, 0)`. The set `vis` also contains the origin. Recording a position when it is enqueued, rather than later when it is removed, prevents several parents from inserting the same coordinate into the queue.

Without `vis`, the graph’s cycles would cause endless repeated exploration. A knight can revisit previously reached squares through many different paths.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process one distance layer at a time

`ans` is the move count of every coordinate currently in the queue at the start of an outer iteration. The loop captures `len(q)` and removes exactly that many positions in the inner loop. Any neighbors appended during this processing are one move farther and remain for the next outer iteration.

For each removed coordinate, the code first tests whether it equals the target. If so, it immediately returns `ans`. Otherwise, it generates all eight legal neighbors, inserts each unseen one into `vis`, and appends it to the queue.

After the entire current layer is processed, `ans += 1` advances the distance associated with the next queue layer.

Starting with `ans = 0` is important. The origin is reachable in zero moves. If the target is `(0, 0)`, it is detected in the first layer and zero is returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"x": 2, "y": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Symmetry-reduced memoized recursion:** Reflect the target into the first quadrant and recursively approach the origin with two move patterns plus small base cases. Memoization reduces repeated work.
- **Bidirectional BFS:** Expand from both origin and target until the visited regions meet. It can reduce explored constants, though its asymptotic two-dimensional bound remains similar.
- **Closed-form knight-distance formula:** A mathematical solution can run in $O(1)$ time but requires careful exceptions near the origin and is harder to derive safely.
- **Target is the origin:** The first queue removal matches and returns zero.
- **Negative coordinates:** All eight signed moves are present, so the BFS handles them without normalization.
- **Coordinate symmetry:** Targets related by sign changes or swapping coordinates have equal answers, but this exact implementation does not exploit that fact.
- **No board boundary:** Generating negative or overshooting coordinates is legal and sometimes necessary for shortest paths near the origin.
- **Visited-on-enqueue:** Marking before append prevents duplicate queue entries from different parents in the same layer.
- **Layer length capture:** `range(len(q))` evaluates the current size once, so newly appended neighbors wait for the next distance layer.
- **Unreachable fallback:** `-1` should never occur under the guarantee; it exists only as a defensive final return.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R^2)$. Let $R=\max(\lvert x\rvert,\lvert y\rvert)$, with a constant additive margin for the knight’s possible overshoot near the target.
- **Auxiliary Space Complexity:** $O(R^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
