# Guided Example: Verbal Arithmetic Puzzle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["SEND", "MORE"], "result": "MONEY"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an equation, represented by `words` on the left side and the `result` on the right side.

The objective is to compute `true` from `{"words": ["SEND", "MORE"], "result": "MONEY"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treating the result as a signed final row

`isSolvable` appends `result` to `words`. The last row is then treated differently from all preceding rows:

- letters in addend rows have `sign = 1`;
- letters in the final result row have `sign = -1`.

For one column, the recursion accumulates

$$
\text{incoming balance}
+\text{sum of addend digits}
-\text{result digit}.
$$

For the column equation to hold, this quantity must be divisible by ten. Dividing it by ten produces the carry-like balance passed to the next more significant column.

Appending `result` mutates the caller-provided `words` list. The algorithm relies on the result being the final row after that append.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["SEND", "MORE"], "result": "MONEY"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reading columns from least significant to most significant

`col = 0` means the rightmost character, `col = 1` means the next character to the left, and so on. For a row string `w`, the current character is

`w[len(w) - 1 - col]`.

This indexing reverses the usual left-to-right string order without reversing or padding the strings.

Words can have different lengths. If `col >= len(w)`, that word has no digit in the current column, so the recursion advances to `row + 1` without changing `bal`.

`totalCols` is the maximum row length after including the result. Once `col == totalCols`, every real digit position has been processed. The puzzle is solvable along the current branch exactly when `bal == 0`, meaning no unmatched carry or difference remains.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `col = 0` means the rightmost character, `col = 1` means the... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Moving from one column to the next

When `row == totalRows`, all addends and the result have contributed their current-column digits. The code requires `bal % 10 == 0`. If the units digit of the signed balance is nonzero, no choice in a more significant column can repair the current decimal column, so the branch fails immediately.

If divisible, recursion restarts at row zero, advances `col` by one, and passes `bal // 10`. This is the decimal carry relation. Because division happens only after exact divisibility is confirmed, Python's floor division also gives the exact integer quotient if the signed balance is negative.

This early column test is the main pruning mechanism. Backtracking does not wait until all letters are assigned before noticing an impossible units or tens column.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["SEND", "MORE"], "result": "MONEY"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Whole-assignment brute force:** Assign every d:** - **Whole-assignment brute force:** Assign every distinct letter before checking the equation. It has the same factorial ceiling but misses powerful per-column pruning and repeatedly converts full words.
- **Column backtracking with an explicit carry:** A more conventional formulation processes addend rows in a column, determines the result digit from the sum modulo ten, and passes a nonnegative carry. It can reduce branching and keeps the arithmetic invariant easier to read.
- **Coefficient equation:** Precompute each letter's signed place-value coefficient and search assignments for a weighted sum of zero. This makes full-equation evaluation fast but may prune less locally than column arithmetic unless bounds are added.
- **More than ten letters:** No injective digit assignment can exist. The local contract already caps distinct letters at ten; a generalized implementation can reject larger sets immediately.
- **Single-character word mapped to zero:** This is legal because there is no leading-zero representation with extra digits.
- **Multi-character leading letter mapped to zero:** The branch must be rejected. Reassigning a previously fixed letter in place complicates the exact source's map invariant.
- **Repeated letter in one or several words:** `letToDig` ensures every occurrence uses the same digit.
- **Digit uniqueness:** `digToLet` prevents a new letter from choosing an occupied digit.
- **Different word lengths:** Missing high-order positions are skipped and contribute zero to that column.
- **Result longer than every addend:** Carry propagation can fill the leading result position; the final balance test decides whether it is possible.
- **Result too short:** A nonzero remaining balance after the last column causes false.
- **Early column failure:** If `bal % 10 != 0` after a column, more significant assignments cannot change that column's units digit, so pruning is safe.
- **Input mutation:** `words.append(result)` permanently changes the supplied list. A side-effect-free version would create `words + [result]` instead.
- **No official local editorial:** The explanation is derived from the exact recursive source and local statement, with the mapping caveat called out rather than importing a different implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(10!)$. Let $U$ be the number of distinct letters, at most ten, and let $L$ represent the total row-position work across the puzzle's columns.
- **Auxiliary Space Complexity:** $O(U+L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
