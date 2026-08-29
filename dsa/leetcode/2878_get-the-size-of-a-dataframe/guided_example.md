# Guided Example: Get the Size of a DataFrame

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"players": [{"player_id": 846, "name": "Mason", "age": 21, "position": "Forward", "team": "RealMadrid"}, {"player_id": 749, "name": "Riley", "age": 30, "position": "Winger", "team": "Barcelona"}, {"player_id": 155, "name": "Bob", "age": 28, "position": "Striker", "team": "ManchesterUnited"}, {"player_id": 583, "name": "Isabella", "age": 32, "position": "Goalkeeper", "team": "Liverpool"}, {"player_id": 388, "name": "Zachary", "age": 24, "position": "Midfielder", "team": "BayernMunich"}, {"player_id": 883, "name": "Ava", "age": 23, "position": "Defender", "team": "Chelsea"}, {"player_id": 355, "name": "Violet", "age": 18, "position": "Striker", "team": "Juventus"}, {"player_id": 247, "name": "Thomas", "age": 27, "position": "Striker", "team": "ParisSaint-Germain"}, {"player_id": 761, "name": "Jack", "age": 33, "position": "Midfielder", "team": "ManchesterCity"}, {"player_id": 642, "name": "Charlie", "age": 36, "position": "Center-back", "team": "Arsenal"}]}}`
- **Required output:** `[10, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to calculate and display the **number of rows and columns** of `players`.

The objective is to compute `[10, 5]` from `{"tables": {"players": [{"player_id": 846, "name": "Mason", "age": 21, "position": "Forward", "team": "RealMadrid"}, {"player_id": 749, "name": "Riley", "age": 30, "position": "Winger", "team": "Barcelona"}, {"player_id": 155, "name": "Bob", "age": 28, "position": "Striker", "team": "ManchesterUnited"}, {"player_id": 583, "name": "Isabella", "age": 32, "position": "Goalkeeper", "team": "Liverpool"}, {"player_id": 388, "name": "Zachary", "age": 24, "position": "Midfielder", "team": "BayernMunich"}, {"player_id": 883, "name": "Ava", "age": 23, "position": "Defender", "team": "Chelsea"}, {"player_id": 355, "name": "Violet", "age": 18, "position": "Striker", "team": "Juventus"}, {"player_id": 247, "name": "Thomas", "age": 27, "position": "Striker", "team": "ParisSaint-Germain"}, {"player_id": 761, "name": "Jack", "age": 33, "position": "Midfielder", "team": "ManchesterCity"}, {"player_id": 642, "name": "Charlie", "age": 36, "position": "Center-back", "team": "Arsenal"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**A DataFrame already knows its dimensions.** pandas stores axis metadata for every DataFrame: one index object describes the rows, and one columns object describes the column labels. The `shape` attribute exposes the lengths of those two axes as a tuple:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"players": [{"player_id": 846, "name": "Mason", "age": 21, "position": "Forward", "team": "RealMadrid"}, {"player_id": 749, "name": "Riley", "age": 30, "position": "Winger", "team": "Barcelona"}, {"player_id": 155, "name": "Bob", "age": 28, "position": "Striker", "team": "ManchesterUnited"}, {"player_id": 583, "name": "Isabella", "age": 32, "position": "Goalkeeper", "team": "Liverpool"}, {"player_id": 388, "name": "Zachary", "age": 24, "position": "Midfielder", "team": "BayernMunich"}, {"player_id": 883, "name": "Ava", "age": 23, "position": "Defender", "team": "Chelsea"}, {"player_id": 355, "name": "Violet", "age": 18, "position": "Striker", "team": "Juventus"}, {"player_id": 247, "name": "Thomas", "age": 27, "position": "Striker", "team": "ParisSaint-Germain"}, {"player_id": 761, "name": "Jack", "age": 33, "position": "Midfielder", "team": "ManchesterCity"}, {"player_id": 642, "name": "Charlie", "age": 36, "position": "Center-back", "team": "Arsenal"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The source returns `list(players.shape)`. If `players.shape` is `(10, 5)`, converting it to a list produces `[10, 5]`, exactly the format required by the problem.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Why the order is rows first.** A DataFrame is two-dimensional. Axis zero is the row or index axis, and axis one is the column axis. pandas follows the common array convention that `shape[0]` is the number of rows and `shape[1]` is the number of columns. The solution preserves this order when converting the tuple. It does not need to name the elements separately.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[10, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"players": [{"player_id": 846, "name": "Mason", "age": 21, "position": "Forward", "team": "RealMadrid"}, {"player_id": 749, "name": "Riley", "age": 30, "position": "Winger", "team": "Barcelona"}, {"player_id": 155, "name": "Bob", "age": 28, "position": "Striker", "team": "ManchesterUnited"}, {"player_id": 583, "name": "Isabella", "age": 32, "position": "Goalkeeper", "team": "Liverpool"}, {"player_id": 388, "name": "Zachary", "age": 24, "position": "Midfielder", "team": "BayernMunich"}, {"player_id": 883, "name": "Ava", "age": 23, "position": "Defender", "team": "Chelsea"}, {"player_id": 355, "name": "Violet", "age": 18, "position": "Striker", "team": "Juventus"}, {"player_id": 247, "name": "Thomas", "age": 27, "position": "Striker", "team": "ParisSaint-Germain"}, {"player_id": 761, "name": "Jack", "age": 33, "position": "Midfielder", "team": "ManchesterCity"}, {"player_id": 642, "name": "Charlie", "age": 36, "position": "Center-back", "team": "Arsenal"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[10, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Separate axis lengths:** `[len(players.index), len(players.columns)]` is correct but more verbose than using `shape`.
- **Use `len(players)` alone:** It returns only rows, so it cannot satisfy the two-number contract.
- **Count with iteration:** Scanning records wastes $O(r)$ time and may mishandle an empty DataFrame; axis metadata already provides the answer.
- **Empty rows, known columns:** A DataFrame may have shape `(0, c)`, and the method correctly returns `[0, c]`.
- **Rows but no columns:** A specially constructed table can have shape `(r, 0)`; shape still reports both axes correctly.
- **Missing values:** Null cells do not affect dimensions because shape counts positions, not non-null entries.
- **Duplicate labels:** Duplicate row or column labels still occupy separate positions and are included in shape.
- **Tuple-versus-list contract:** Returning `players.shape` directly gives correct numbers but the wrong Python container type for the requested array result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Reading DataFrame `shape` is $O(1)$ with respect to the number of rows and columns because pandas already has the two axis objects and their lengths. Converting a fixed two-element tuple into a list also takes $O(1)$ time. The returned list contains exactly two integers, so additional space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
