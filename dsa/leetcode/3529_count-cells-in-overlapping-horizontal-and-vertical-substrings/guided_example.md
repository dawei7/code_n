# Guided Example: Count Cells in Overlapping Horizontal and Vertical Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [["a"]], "pattern": "a"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix `grid` consisting of characters and a string `pattern`.

The objective is to compute `1` from `{"grid": [["a"]], "pattern": "a"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn each wrapping rule into an ordinary one-dimensional traversal

The horizontal rule reads each row left to right and, at a row boundary, continues at the first cell of the next row. This is exactly row-major flattening:

`grid[0][0], grid[0][1], ..., grid[0][columns-1], grid[1][0], ...`.

The source builds:

`horizontal = "".join("".join(row) for row in grid)`.

It does not append the first row again, so matching cannot wrap from the final row back to the top. Any ordinary substring of this flattened text corresponds exactly to one legal horizontal substring, including matches that cross row boundaries.

The vertical rule reads top to bottom and, at the bottom of a column, continues at the top of the next column. This is column-major flattening:

`grid[0][0], grid[1][0], ..., grid[rows-1][0], grid[0][1], ...`.

The source builds that ordering with the column loop outside the row loop. Again, the text stops after the last column, so there is no forbidden wrap back to the first column.

The two unusual two-dimensional searches are now two ordinary exact-pattern searches in strings of the same length `N = rows * columns`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [["a"]], "pattern": "a"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the KMP prefix table once

Searching naively from every starting position can cost `O(NP)` for pattern length `P`. Knuth-Morris-Pratt search avoids rechecking characters.

The `prefix[i]` value is the length of the longest proper prefix of `pattern[0..i]` that is also a suffix of that same pattern prefix.

While building it, `matched` is the best border length known for the preceding position. If `pattern[index]` does not extend that border, the source falls back to:

`matched = prefix[matched - 1]`.

This tries the next-longest possible border without comparing the already-known matching characters again. If the next characters agree, `matched` increases. The resulting value is saved for the current index.

The prefix table depends only on `pattern`, so the source builds it once and reuses it for both flattened texts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Searching naively from every starting position can cost `O(N... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Search a text while allowing overlapping matches

Inside `covered(text)`, `matched` means that the first `matched` pattern characters match a suffix ending immediately before the current search position.

For each text character:

- while there is a mismatch and `matched > 0`, fall back through the prefix table;
- if the current character matches `pattern[matched]`, increment `matched`;
- when `matched == length`, one complete occurrence ends at the current index.

The match start is:

`start = index - length + 1`.

After recording it, the source sets:

`matched = prefix[matched - 1]`.

This fallback is crucial for overlaps. If pattern `"aba"` matches ending at one position, its suffix `"a"` may already be the prefix of another match starting inside the first. Resetting to zero would miss that overlap.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [["a"]], "pattern": "a"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Search from every starting cell:** Comparing u:** - **Search from every starting cell:** Comparing up to `P` characters at each of `N` starts can cost `O(NP)`. KMP guarantees linear search.
- **Run a two-dimensional matcher:** The wrap definitions are not ordinary rectangular patterns. Flattening precisely follows their one-dimensional traversal and is simpler.
- **Mark every matched cell with an inner loop:** A pattern like repeated `"a"` can have many overlapping matches, making total marking `O(NP)`. Difference ranges mark each occurrence in constant time.
- **Use match counts instead of booleans:** Counts are useful only while accumulating interval coverage. The final condition is presence, so `active > 0` is sufficient.
- **Reset KMP to zero after a match:** This misses overlapping occurrences. Falling back to the last prefix value preserves overlap candidates.
- **Horizontal row boundary:** Row-major adjacency deliberately joins the end of one row to the start of the next.
- **Horizontal bottom boundary:** The flattened string ends at the final cell, so no match wraps back to row zero.
- **Vertical column boundary:** Column-major adjacency deliberately joins the bottom of one column to the top of the next.
- **Vertical last-column boundary:** No characters follow the final column, so circular wrap is impossible.
- **Pattern length one:** Every cell whose character equals the pattern is marked in each flattening; since both represent the same cell value, all matching cells qualify.
- **Pattern length N:** Only a full-text match can occur in each orientation, and all cells in a matching orientation are covered.
- **Overlapping occurrences:** Difference counts may exceed one, but the boolean union remains correct.
- **Same cell mapped differently:** The row-major and column-major formulas must both be used; comparing equal numeric indices would generally refer to different cells.
- **One-row grid:** Horizontal order is the row; vertical order advances one-cell columns, which happens to be the same sequence.
- **One-column grid:** Both traversals likewise coincide.
- **No matches in one orientation:** Its coverage array is all false, so the final answer is zero regardless of the other orientation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+P)$. Let `N = rows * columns` and `P = len(pattern)`. Building the KMP prefix table takes `O(P)` time. Constructing each flattened string takes `O(N)` time.
- **Auxiliary Space Complexity:** $O(N+P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
