# Guided Example: Word Search

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [["Z"]], "word": "Z"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The objective is to compute `true` from `{"board": [["Z"]], "word": "Z"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Try every cell as the beginning of the path

The first character of `word` can occur anywhere on the board. The final expression calls `dfs(i, j, 0)` for cells in row-major order and lets `any` stop at the first successful start. A failed start does not rule out another occurrence of the same first character, because its surrounding letters may be different.

Inside `dfs(i, j, k)`, the current cell is intended to match `word[k]`. If it does not, the path fails immediately. If it does, the search must choose a horizontally or vertically adjacent unused cell for the next character.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [["Z"]], "word": "Z"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle the final character before marking or moving

When `k == len(word) - 1`, every earlier character has already been matched along a legal path. The current call needs only to compare `board[i][j]` with the last required character. A successful equality completes the word; there is no reason to mark the final cell or make another recursive move.

This base case appears before the general mismatch check but performs its own equality. Since `word` is nonempty, index `len(word) - 1` is valid. It also makes a one-character word a direct collection of board-cell comparisons.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use the board itself as the visited set

After a nonfinal character matches, the source saves it in `c` and writes the sentinel string `"0"` into that board cell. The input contract allows only uppercase and lowercase English letters, so `"0"` cannot be a legitimate board value. A later neighbor check requiring `board[x][y] != "0"` therefore prevents the current path from using that cell again.

This is path-local marking rather than permanent global visitation. A cell that is inappropriate for one attempted path may be needed in another path. After every unsuccessful exploration from the cell, the source restores `board[i][j] = c`, giving sibling branches and later starting cells the original board.

The saved character is also the exact value needed for restoration; it is not inferred from `word`, even though they match at that moment.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [["Z"]], "word": "Z"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Restore before returning success:** Save a Boolean from child exploration, restore `board[i][j]`, then return it. This preserves the board on every path.
- **Explicit visited set or matrix:** Avoid mutating the board, at the cost of up to $O(mn)$ additional storage.
- **Import requirement:** Add `from itertools import pairwise`, or replace it with a literal four-direction tuple.
- **Character-frequency precheck:** If `word` requires more copies of a letter than the board contains, return false before backtracking.
- **Reverse the word:** Starting from its rarer endpoint can reduce branching while preserving existence.
- **One-character word:** Direct base-case comparisons find it without marking or direction generation.
- **Word longer than the number of cells:** No non-reusing path can exist; the source discovers this through search rather than an explicit precheck.
- **Repeated board letters:** They may cause the exponential worst case because character comparisons prune less.
- **Marker safety:** `"0"` is outside the promised alphabet and cannot collide with a valid cell.
- **Orthogonal-only movement:** The four offsets deliberately exclude diagonals.
- **No cell reuse:** All earlier cells on the current path carry the sentinel.
- **Failed search:** Every mark is restored, so the board remains unchanged when all branches fail.
- **Successful search:** The exact source leaves nonfinal successful-path cells marked, an important observable caveat.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn\cdot3^L)$. Let $m$ and $n$ be board dimensions and $L$ the word length. There are $mn$ potential starts. The first matched cell has at most four moves and later levels at most three forward choices, giving intended worst-case time $O(mn\cdot3^L)$ after absorbing constants. This matches the manifest.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
