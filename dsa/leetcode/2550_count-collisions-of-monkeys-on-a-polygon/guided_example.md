# Guided Example: Count Collisions of Monkeys on a Polygon

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `688423208`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a regular convex polygon with `n` vertices. The vertices are labeled from `0` to $n - 1$ in a clockwise direction, and each vertex has **exactly one monkey**. The following figure shows a convex polygon of `6` vertices.

The objective is to compute `688423208` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count all movement assignments first

Each of the `n` monkeys independently chooses one of two neighboring directions:

- clockwise;
- anticlockwise.

Therefore, there are:

$$
2^n
$$

total simultaneous movement assignments.

It is easier to subtract the collision-free assignments than to count every possible collision pattern directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Two uniform assignments have no collision

If every monkey moves clockwise, each leaves its vertex and arrives at the next clockwise vertex. This is a cyclic rotation:

- every destination receives exactly one monkey;
- all monkeys traverse different polygon edges in the same orientation.

No vertices or edge interiors contain two monkeys.

The all-anticlockwise assignment is symmetric and also collision-free.

These give at least two non-collision assignments.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If every monkey moves clockwise, each leaves its vertex and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every mixed-direction assignment collides

Write each monkey's direction around the cyclic vertex order. If both directions occur, the cyclic sequence has a boundary where direction changes.

Among the cyclic boundaries, one has adjacent monkeys moving toward each other along their shared edge: one moves clockwise from one endpoint while the other moves anticlockwise from the other endpoint.

They traverse that same edge in opposite directions and intersect, which the statement defines as a collision.

Equivalently, another kind of direction boundary can send two monkeys toward a common neighboring vertex. In either view, a nonuniform direction pattern cannot be collision-free on the cycle.

Thus the only collision-free assignments are the two uniform rotations.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `688423208` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `688423208` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate assignments:** It costs $O(2^n)$ and:** - **Enumerate assignments:** It costs $O(2^n)$ and is impossible for large `n`.
- **Count collision patterns directly:** Assignments with multiple collisions make inclusion-exclusion unnecessarily difficult.
- **All clockwise:** Collision-free cyclic rotation.
- **All anticlockwise:** Collision-free cyclic rotation.
- **Mixed directions:** A cyclic transition forces a collision.
- **Edge intersection:** It counts even when final vertices differ.
- **Multiple collisions:** The movement assignment is counted only once.
- **`n=3`:** Six of eight assignments collide.
- **Large exponent:** Use modular exponentiation rather than building $2^n$.
- **Modulo subtraction:** Final `%mod` returns the canonical residue.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(log n)$. Binary modular exponentiation takes $O(\log n)$ modular multiplication steps. The subtraction and final modulo are constant time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
