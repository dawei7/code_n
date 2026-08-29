# Guided Example: Check if Word Can Be Placed In Crossword

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "word": "abc"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix `board`, representing the** current **state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), `' '` to represent any **empty **cells, and `'#'` to represent any **blocked** cells.

The objective is to compute `true` from `{"board": [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "word": "abc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid placement must occupy one complete slot

A word cannot have an unblocked letter or space immediately before or after it along its direction. Therefore it must exactly fill a run bounded by board edges or `'#'` cells.

The source tries every cell as a possible start in four directions, but calls the detailed checker only when the cell immediately before that start is blocked or outside the board.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "word": "abc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Verify the boundary after the word

Helper `check(i,j,a,b)` uses direction vector $(a,b)$. For word length `k`, coordinate

`(i + a * k, j + b * k)`

is the cell immediately after the proposed word.

If that coordinate is in bounds and is not blocked, the slot continues beyond the word and placement is invalid. Returning false before scanning letters enforces exact slot length at the far boundary.

The caller's direction-specific condition enforces the near boundary. Together, both ends are closed by an edge or block.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Match each word character

The helper iterates through `word` from its first character to last while advancing by the direction vector.

At each position, it rejects an out-of-bounds coordinate. An empty space accepts any character. An existing letter accepts only the same character. A block rejects because it is neither a space nor the required letter.

If all characters fit and the post-word boundary was valid, the placement succeeds.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "word": "abc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Split rows and columns on blocks:** Compare each exact-length segment with the word and its reverse; clear but may allocate strings or lists.
- **Transpose the board:** Reuse horizontal logic for vertical slots, at the cost of $O(MN)$ extra storage.
- **Check letters without slot boundaries:** Incorrectly allows the word inside a longer unblocked run.
- **One-cell word:** Requires a one-cell slot bounded on both sides in its direction.
- **Existing matching letters:** Allowed and need no board mutation.
- **Existing mismatching letter:** Immediately rejects that orientation.
- **Blocked cell inside the word:** Rejected by compatibility checking.
- **Right-to-left and bottom-to-top:** Direction changes traversal; `word` itself remains in normal character order.
- **Board edge:** Serves as a valid slot boundary.
- **Several valid placements:** The first discovered returns true, which is sufficient.
- **Short-circuiting:** Avoids checker calls when the near boundary is invalid.
- **Input preservation:** Placement is tested logically without writing letters into `board`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(MN)$. Let $M$ and $N$ be board dimensions. The outer loops visit $MN$ cells. Across all row and column slot starts and four directions, checked cell work is $O(MN)$. Total time is $O(MN)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
