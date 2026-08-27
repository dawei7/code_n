# Guided Example: Path Crossing

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"path": "NES"}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `path`, where $\text{path}[i] = 'N'$, `'S'`, `'E'` or `'W'`, each representing moving one unit north, south, east, or west, respectively. You start at the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

The objective is to compute `false` from `{"path": "NES"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Representing the walk with coordinates

The walk begins at the origin. The stored solution uses two integers, `i` and `j`, to represent the current grid location. Here `i` acts like a row coordinate and `j` like a column coordinate:

- North decreases `i` by one.
- South increases `i` by one.
- East increases `j` by one.
- West decreases `j` by one.

Using north as negative rather than positive does not change the geometry. It merely chooses screen-style row coordinates instead of a conventional upward-positive Cartesian y-axis. Opposite directions still cancel each other, every instruction moves exactly one unit, and equal coordinate pairs still mean equal physical locations.

The code uses Python structural pattern matching to translate each path character into one coordinate update. The input contract guarantees that every character is one of the four listed directions, so no default case is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"path": "NES"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a set detects crossing

The set `vis` contains every coordinate occupied so far. It is initialized as `{(0, 0)}` before any instruction is processed because the starting location counts as visited. This detail is essential: a path that leaves the origin and later returns to it crosses itself even if no post-move location was repeated before that return.

After applying one movement, the code checks `if (i, j) in vis`. If the pair is present, the walk has arrived at a location occupied at an earlier time, which is exactly the definition of crossing in this problem. It returns true immediately because later instructions cannot undo the fact that a crossing already occurred.

If the new coordinate has not appeared, `vis.add((i, j))` records it before the next move. When the loop completes without a repeated pair, the method returns false.

Python tuples are immutable and hashable, so a coordinate tuple can be stored directly in a set. The set compares both components, distinguishing positions that share only one coordinate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The set `vis` contains every coordinate occupied so far.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The invariant after every instruction

After processing any prefix of the path without returning, two facts hold:

1. `(i, j)` is the location reached by executing exactly that prefix.
2. `vis` contains precisely the origin and every location reached after each move in that prefix, with no duplicates.

Both facts are true before the loop: the empty prefix ends at the origin and the set contains only the origin. For the next character, the matching case applies the correct unit displacement, so the coordinate becomes the endpoint of the extended prefix.

If that endpoint is already in `vis`, the algorithm correctly reports a crossing. Otherwise, inserting it preserves the exact visited-location set and its uniqueness. This induction covers the entire path.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"path": "NES"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **List of visited coordinates:** It is correct b:** - **List of visited coordinates:** It is correct but membership is linear, causing $O(N^2)$ worst-case time.
- **Boolean grid:** An offset grid can give direct lookup, but a square covering all possible coordinates consumes $O(N^2)$ space even though the path visits only $O(N)$ locations.
- **Complex-number coordinates:** Directions can be mapped to complex displacements and positions stored in a set. It is concise but may be less beginner-friendly than integer pairs.
- **Return to origin:** This is detected only because the origin is inserted before processing the first move.
- **Immediate reversal:** Paths such as `NS` revisit the origin on the second step and return true.
- **Repeated edge:** Traversing an old edge in reverse necessarily revisits its endpoint, so the set detects it.
- **Straight path:** Every coordinate is new, and the method returns false after the loop.
- **North sign convention:** Decreasing the first coordinate is arbitrary but consistent; crossing detection depends on equality, not orientation.
- **Single instruction:** It reaches one new neighboring point and cannot cross under the valid-direction contract.
- **Invalid direction character:** The match would make no movement and could cause a false repeat, but such characters are explicitly excluded.
- **Python version:** The `match` statement requires Python 3.10 or newer.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the path length. Each character is processed once. Direction matching, integer updates, tuple construction, expected set membership, and expected set insertion take constant time, giving expected $O(N)$ total time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
