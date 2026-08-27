# Guided Example: Swap Adjacent in LR String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"start": "RXXLRXRXL", "end": "XRLXXRRLX"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In a string composed of `'L'`, `'R'`, and `'X'` characters, like `"RXXLRXRXL"`, a move consists of either replacing one occurrence of `"XL"` with `"LX"`, or replacing one occurrence of `"RX"` with `"XR"`. Given the starting string `start` and the ending string `result`, return `true` if and only if there exists a sequence of moves to transform `start` to `result`.

The objective is to compute `true` from `{"start": "RXXLRXRXL", "end": "XRLXXRRLX"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the replacement rules into movement rules

The character `X` represents an empty position. Replacing `XL` with `LX` moves an `L` one position to the left across an empty position. Replacing `RX` with `XR` moves an `R` one position to the right across an empty position.

Those directions can never be reversed:

- An `L` may move left, but it can never move right.
- An `R` may move right, but it can never move left.
- Two non-`X` characters can never pass through one another, because every move swaps a letter only with `X`.

These facts are more useful than trying to simulate an unknown sequence of swaps. A simulation would have to decide which legal move to make at every step, even though many different move sequences can lead to the same result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"start": "RXXLRXRXL", "end": "XRLXXRRLX"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Ignore empty positions to expose the fixed letter order

Because `L` and `R` never cross, deleting every `X` from both strings must leave exactly the same sequence of letters. For example, `"RXXLR"` becomes `"RLR"`. If the other string becomes `"RRL"`, the transformation is impossible regardless of where its empty positions occur.

The implementation checks this condition without building filtered strings. Pointer `i` scans `start` and pointer `j` scans `end`. Each inner loop skips consecutive `X` characters. The next positions, if they exist, are therefore the next nonempty pieces in their respective strings.

If only one pointer reaches the end, one string still has an unmatched letter. If both point to letters but those letters differ, the non-`X` order differs. Either situation must return `false`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Because `L` and `R` never cross, deleting every `X` from bot... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Match each physical piece with its destination

When `start[i] == end[j]`, the two pointers refer to the same piece in the preserved left-to-right letter order. Its original index is `i` and its requested final index is `j`.

For an `L`, legal moves can only decrease its index. Therefore its destination must satisfy $j \le i$. The code detects the forbidden case `i < j`, which would require that `L` to move right.

For an `R`, legal moves can only increase its index. Its destination must satisfy $j \ge i$. The code detects the forbidden case `i > j`, which would require that `R` to move left.

After a matching letter passes its direction test, both pointers advance once. The following iteration skips any new run of `X` characters and examines the next preserved piece.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"start": "RXXLRXRXL", "end": "XRLXXRRLX"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build filtered strings plus position lists:** :** - **Build filtered strings plus position lists:** Comparing the non-`X` sequences and then comparing corresponding indices expresses the same proof clearly, but the new lists require $O(n)$ auxiliary space.
- **- **Breadth-first search over strings:** It could :** - **Breadth-first search over strings:** It could discover a move sequence for tiny inputs, but the number of configurations is enormous at length $10^4$ and the sequence itself is not requested.
- **- **Greedy swap simulation:** Choosing currently a:** - **Greedy swap simulation:** Choosing currently available moves can perform unnecessary work and needs careful scheduling; the invariant-based scan decides reachability directly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common string length. Each pointer moves only from left to right and advances at most $n$ times. Although the scans contain nested `while` loops, no position is revisited, so the total time is $O(n)$ rather than $O(n^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
