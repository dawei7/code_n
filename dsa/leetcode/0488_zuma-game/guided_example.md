# Guided Example: Zuma Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": "WRRBBW", "hand": "RB"}`
- **Required output:** `-1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing a variation of the game Zuma.

The objective is to compute `-1` from `{"board": "WRRBBW", "hand": "RB"}` while avoiding redundant calculations and unnecessary overhead.

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

Every move changes two resources: the visible board and the multiset of balls still in hand. The objective is to minimize how many insertions are made, so the solution explores possible game states with breadth-first search. Breadth-first search is appropriate because every edge in the state graph represents exactly one insertion and therefore has the same cost.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": "WRRBBW", "hand": "RB"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The queue begins with `(board, hand)`. A queue entry contains the current reduced board string and the still-available hand string. States are removed in first-in, first-out order, so all states reached with zero insertions are examined before states reached with one, all one-insertion states before two-insertion states, and so on. Consequently, when an empty board is first removed from the queue, its depth is the minimum number of balls needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The code does not store depth explicitly. Every transition removes exactly one character from `balls`, while the original `hand` never changes. Thus

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `-1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": "WRRBBW", "hand": "RB"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `-1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Depth-first search with memoization:** Explore insertions recursively and return the minimum remaining cost. It can use the same collapse routine, but breadth-first search obtains the minimum naturally from levels.
- **Count-based run removal search:** Process maximal board runs and insert only the number of matching balls required to reach three. This prunes many unproductive placements but needs careful reasoning about cascades and hand counts.
- **Full state deduplication:** Use `(board, sorted_remaining_hand)` as the visited key. This avoids merging equal boards that retain different color resources and gives the cleanest general correctness argument, at the cost of more states.
- **Insertion at index zero:** The source tries boundaries `1` through the end. A fully exhaustive formulation includes zero as well; same-color insertion at the first run is already equivalent to an internal position.
- **Repeated colors in hand:** `set(balls)` removes duplicate branches only for the current choice. `replace(..., 1)` consumes one copy, so remaining identical balls are not lost.
- **Chain reactions:** One regex substitution is insufficient. `remove` repeats until no deletion occurs, ensuring the queued board is stable.
- **Board clears immediately after insertion:** `remove` returns the empty string, which is enqueued and then recognized when popped at the next BFS step.
- **Hand becomes empty while the board remains:** That state generates no children because `set(balls)` is empty. If every branch reaches this condition, the queue drains and the result is `-1`.
- **Initial board stability:** The contract guarantees no initial run of three, so the source does not call `remove` before starting BFS.
- **Color alphabet:** The regular expression explicitly lists all five allowed colors. A new color outside that contract would never be removed and would require updating the pattern.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n + h)^{h + 1})$. Let $n$ be the initial board length and $h$ the hand length. Search depth is at most $h$. At a level, a state can branch on at most $h$ colors and at most $n+h$ insertion positions. A loose upper bound on the number of generated configurations is exponential in the hand size; the manifest records $O((n+h)^{h+1})$ time.
- **Auxiliary Space Complexity:** $O((n + h)^h)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
