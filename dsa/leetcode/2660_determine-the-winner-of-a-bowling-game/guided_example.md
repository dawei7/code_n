# Guided Example: Determine the Winner of a Bowling Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"player1": [5, 10, 3, 2], "player2": [6, 5, 7, 3]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed** integer arrays `player1` and `player2`, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The objective is to compute `1` from `{"player1": [5, 10, 3, 2], "player2": [6, 5, 7, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Score each player's turns independently

The rule for one turn depends only on that player's own previous two raw pin counts.

Helper `f(arr)` computes one total. The main function calls it for both arrays, then compares the two scores.

No state is shared between players, and one player's strikes never affect the other's multiplier.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"player1": [5, 10, 3, 2], "player2": [6, 5, 7, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Check the two eligible prior indices

At turn $i$, current pin count is $x$.

Its multiplier is two when either:

$$
i\ge1\ \text{ and }\ \texttt{arr[i-1]}=10,
$$

or:

$$
i\ge2\ \text{ and }\ \texttt{arr[i-2]}=10.
$$

Otherwise, multiplier is one.

The exact condition uses:

`(i and arr[i - 1] == 10) or (i > 1 and arr[i - 2] == 10)`.

In Python, zero is falsy and positive indices are truthy, so `i` safely guards the first previous-index access.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why raw previous pins are inspected

The rule says a strike in either previous turn doubles the current turn. It does not depend on the previous turn's already multiplied score.

The source reads `arr[i-1]` and `arr[i-2]` directly. A previous turn that scored 20 only because it was doubled does not count as a strike unless its raw pin value was ten.

This distinction prevents multiplier effects from propagating incorrectly beyond two turns.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"player1": [5, 10, 3, 2], "player2": [6, 5, 7, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track a two-turn bonus countdown:** Maintain how many future turns remain doubled after strikes; correct but raw-array lookback is simpler.
- **Precompute multipliers:** Uses $O(n)$ space unnecessarily.
- **First turn strike:** It scores ten normally but doubles turns one and two.
- **Strike one turn ago:** Current pins are doubled.
- **Strike two turns ago:** Current pins are also doubled.
- **Both prior turns strikes:** Multiplier remains two, not four.
- **No strikes:** Score is ordinary sum of pins.
- **One-turn game:** No bonus can apply to the only turn.
- **Equal totals:** Return zero.
- **Raw versus scored prior value:** Only raw ten triggers the bonus.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For $n$ turns, each helper performs $O(n)$ work. Running it twice is still $O(n)$ total time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
