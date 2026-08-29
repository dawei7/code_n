# Guided Example: Stone Game VI

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"aliceValues": [1, 3], "bobValues": [2, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice and Bob take turns playing a game, with Alice starting first.

The objective is to compute `1` from `{"aliceValues": [1, 3], "bobValues": [2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Measure each stone’s total strategic importance

Taking stone `i` has two effects: the current player gains their own value, and the opponent permanently loses the chance to gain their value for that same stone. If Alice takes it, the swing in Alice’s score minus Bob’s score is `aliceValues[i]` compared with letting Bob later gain `bobValues[i]`. Its combined strategic importance is therefore

$$
\texttt{aliceValues[i]}+\texttt{bobValues[i]}.
$$

Both optimal players should prioritize the remaining stone with the largest combined value. The source builds `vals` as pairs of this sum and the original index, then sorts them in descending order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"aliceValues": [1, 3], "bobValues": [2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why descending combined value is the correct game order

Consider two stones `i` and `j` that will be taken on consecutive turns, first by Alice and then by Bob. If the order is `i` then `j`, their contribution to Alice-minus-Bob is

$$
a_i-b_j.
$$

If the order is reversed, it is

$$
a_j-b_i.
$$

The first order is at least as good for Alice precisely when

$$
a_i-b_j \ge a_j-b_i,
$$

which rearranges to

$$
a_i+b_i \ge a_j+b_j.
$$

Thus a larger combined-value stone belongs earlier. The same comparison reflects Bob’s optimal denial objective on Bob’s turn: choosing a large combined value prevents Alice from receiving a valuable stone as well as collecting Bob’s own value.

Repeated adjacent exchanges transform any take order into descending combined value without worsening the player whose turn owns the earlier position. This gives the optimal-play ordering.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Assign alternating positions

Alice moves first, so she receives stones at sorted positions zero, two, four, and so on. Bob receives positions one, three, five, and so on.

The source computes:

`a = sum(aliceValues[i] for _, i in vals[::2])`

and

`b = sum(bobValues[i] for _, i in vals[1::2])`.

The stored original index is necessary because the combined priority is not either player’s actual score. Once a stone is assigned to a turn, its owner receives the value from their own array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"aliceValues": [1, 3], "bobValues": [2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort indices by combined value:** This avoids storing the sum in each tuple but still needs an $O(n)$ index list and $O(n\log n)$ time.
- **Priority queue:** Repeatedly pop the largest combined value for alternating turns. It has the same $O(n\log n)$ time and more per-operation overhead.
- **Sort by Alice’s value alone:** This ignores the value denied to Bob and can choose a strategically inferior stone.
- **Sort by value difference:** The pairwise exchange derives the sum, not `a_i-b_i`; using the difference is incorrect.
- **One stone:** Alice takes it and wins because all values are positive.
- **Even number of stones:** Both players take the same count, but their scores can still differ.
- **Odd number of stones:** Alice receives one extra stone because she starts.
- **Equal combined priorities:** Any order among them gives the same Alice-minus-Bob contribution across their turn slots.
- **Equal final scores:** The source returns zero exactly for a draw.
- **Positive values:** Scores are nonnegative and every stone is taken; no pass action is available or useful.
- **Input preservation:** The source sorts a new `vals` list and does not reorder either value array.
- **Slice allocation:** A more memory-conscious loop could iterate through `vals` once and add to Alice or Bob by parity, but the exact source materializes the two slices.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of stones. Building `vals` takes $O(n)$ time and $O(n)$ space. Sorting takes $O(n\log n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
