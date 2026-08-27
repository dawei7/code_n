# Guided Example: Movement of Robots

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-2, 0, 2], "s": "RLL", "d": 3}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Some robots are standing on an infinite number line with their initial coordinates given by a **0-indexed** integer array `nums` and will start moving once given the command to move. The robots will move a unit distance each second.

The objective is to compute `8` from `{"nums": [-2, 0, 2], "s": "RLL", "d": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Collisions can be ignored when robot identities do not matter

Every robot moves at the same unit speed. When two robots moving in opposite directions collide, both reverse. From the viewpoint of labeled robots, their individual paths bounce. From the viewpoint of occupied positions, the event is indistinguishable from the two robots passing straight through each other and exchanging labels.

Imagine a right-moving robot arriving at a collision from the left and a left-moving robot arriving from the right. After bouncing, one trajectory leaves left and one leaves right. If they instead pass through, one trajectory also leaves left and one leaves right; only which robot name follows which trajectory changes.

The requested answer sums distances over all unordered pairs of positions. Renaming robots does not change that multiset of positions or its pairwise-distance sum. Therefore the algorithm can pretend every robot continues in its original direction without reacting to collisions.

This equivalence also covers a meeting between integer timestamps or the example where adjacent robots cross without sharing an integer position at the next whole second. Their labels swap conceptually, while the final collection of coordinates remains the same.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-2, 0, 2], "s": "RLL", "d": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute collision-free final coordinates

A robot beginning at `nums[i]` and moving right travels distance `d` to:

$$
\texttt{nums}[i]+d.
$$

A left-moving robot ends at:

$$
\texttt{nums}[i]-d.
$$

The first loop applies this directly, adding `d` for `'R'` and subtracting it for `'L'`.

The exact implementation mutates `nums` in place. After this loop, the array no longer contains initial coordinates; it contains the collision-free final coordinates whose multiset is also the true final multiset.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A robot beginning at `nums[i]` and moving right travels dist... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort so absolute values become ordinary differences

For arbitrary coordinates, summing every `abs(a-b)` pair directly takes $O(n^2)$ time. Sorting the final positions as:

$$
x_0\le x_1\le\cdots\le x_{n-1}
$$

removes the absolute-value ambiguity. For every earlier index $j<i$, the distance to $x_i$ is $x_i-x_j$.

Equal final coordinates are allowed after movement. Their pairwise distance is zero, and nondecreasing sorting handles them naturally.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-2, 0, 2], "s": "RLL", "d": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate collisions over time:** Can require e:** - **Simulate collisions over time:** Can require enormous work for large `d` and adds identity bookkeeping that the aggregate answer does not need.
- **Enumerate all pairs after movement:** Correct but costs $O(n^2)$ time instead of using sorted prefix sums.
- **Reduce modulo at every iteration:** Also correct and can be useful in fixed-width languages; Python safely delays it.
- **d equal to zero:** Coordinates remain unchanged, and the same sorted pair-sum computation applies.
- **Two robots:** The prefix formula produces their one absolute distance.
- **Equal final coordinates:** Their mutual contribution is zero.
- **Negative coordinates:** Sorting and subtraction remain valid; no special case is required.
- **Many collisions:** Pass-through equivalence removes them all from the computation.
- **Input mutation:** Callers observe `nums` changed into sorted final coordinates.
- **Robot labels:** The method is valid because the result depends only on positions, not on which original label occupies each position.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of robots. Computing final coordinates takes $O(n)$ time. Sorting dominates at $O(n\log n)$, and the prefix-sum pass is $O(n)$. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
