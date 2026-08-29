# Guided Example: Count Houses in a Circular Street

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"street": [0, 0, 0, 0], "k": 10}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an object `street` of class `Street` that represents a circular street and a positive integer `k` which represents a maximum bound for the number of houses in that street (in other words, the number of houses is less than or equal to `k`). Houses' doors could be open or closed initially.

The objective is to compute `4` from `{"street": [0, 0, 0, 0], "k": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The initial door states cannot identify one full lap

The street is circular and the interface exposes only the current door plus left and right movement. There is no coordinate, house ID, or direct length operation. An initially open door cannot safely serve as a marker because other doors may also be open.

The upper bound $n\le k$ supplies the missing leverage: moving $k$ consecutive steps is guaranteed to visit every house at least once, regardless of the unknown $n$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"street": [0, 0, 0, 0], "k": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First phase: make every door open

The first loop repeats $k$ times:

1. call `openDoor()` at the current house;
2. call `moveLeft()`.

Moving left around an $n$-house circle visits houses cyclically. Because $k\ge n$, the first $n$ iterations already visit every house exactly once before returning to the first. Extra iterations, when $k>n$, revisit some houses and open doors that are already open, which is harmless.

At the end of this phase, every door is definitely open. The current position depends on $k\bmod n$, but its identity does not matter. The important invariant is uniformity: no closed door remains from the unknown initial state.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Second phase: turn the current house into the stopping marker

`ans` starts at zero. While the current door is open, the algorithm:

1. closes that door;
2. moves one house left;
3. increments `ans`.

On the first iteration, it closes the current house. Think of that house as the unique marker. All other doors are still open.

As the loop continues left, it reaches each next house, sees an open door, closes it, moves again, and counts it. Because the street is circular, after exactly $n$ such moves it returns to the first house. That marker is now closed, so `isDoorOpen()` is false and the loop stops.

Thus `ans` has been incremented exactly once for every house.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"street": [0, 0, 0, 0], "k": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use an initially open door as a marker:** Incorrect because several doors may begin open, causing an early stop.
- **First close every door, then open one marker:** A symmetric strategy can work, but the exact solution uses the all-open state and closes while counting.
- **Store visited house identities:** Impossible through the supplied interface because houses expose no IDs, and unnecessary.
- **Move inconsistently:** Reversing direction during counting can hit the marker before a full lap.
- **One house:** Initialization opens it; one counting iteration closes it, moves back to it, and returns one.
- **n equals k:** The first phase completes exactly one full lap and opens every door.
- **k larger than n:** Repeated openings are idempotent and do not affect correctness.
- **All doors initially open:** Initialization is redundant but harmless.
- **All doors initially closed:** Initialization creates the uniform marker-ready state.
- **Final door states:** Every door is closed after counting; restoration is not required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k+n)$. The initialization loop performs exactly $k$ constant-interface operations. The counting loop performs exactly $n$ iterations. Total time is $O(k+n)$, and because $n\le k$, this simplifies to $O(k)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
