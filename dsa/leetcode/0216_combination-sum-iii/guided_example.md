# Guided Example: Combination Sum III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"k": 3, "n": 7}`
- **Required output:** `[[1, 2, 4]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

The objective is to compute `[[1, 2, 4]]` from `{"k": 3, "n": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat every valid answer as an increasing subset

The available values are only 1 through 9, and each may be used at most once.
The order of numbers inside a combination does not create a different answer:
`[1, 2, 6]` and `[6, 1, 2]` describe the same chosen set. The exact solution
eliminates both repeated values and reordered duplicates by considering digits
in increasing order.

The recursive call `dfs(i, s)` means: digits smaller than `i` have already
received their final include-or-exclude decisions, `s` is the sum still needed,
and the shared list `t` contains the digits selected on the current path. The
only current candidate is `i`. Both recursive calls advance to `i + 1`, so a
chosen digit can never be chosen again, and every completed list in `t` is
strictly increasing.

Starting with `dfs(1, n)` means no digit has yet been decided, the complete
target sum remains, and `t` is empty.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"k": 3, "n": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: At each digit, explore the two exhaustive choices

If the current state is still viable, the search first includes `i`:

1. Append `i` to `t`.
2. Call `dfs(i + 1, s - i)` because that amount has been paid toward the sum.
3. Pop `i` from `t` when the recursive branch returns.

The `pop` is the backtracking step. `t` is one mutable list shared by all
calls. Removing the included digit restores the list to exactly the state it
had before this choice, allowing the sibling branch to be evaluated correctly.
When a completed answer is stored, the source uses `t[:]` to copy the current
contents. Appending `t` itself would make every saved answer refer to the same
list and later pops would corrupt previously recorded results.

After restoring the path, the source explores the second choice with
`dfs(i + 1, s)`: exclude `i`, leave the remaining sum unchanged, and move to
the next digit. Include and exclude are the only possibilities for a value
that can be used at most once, so the two branches cover every subset.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If the current state is still viable, the search first inclu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognize a solution as soon as the remaining sum reaches zero

The first base case checks `s == 0`. If the current path also has exactly
`k` digits, it is copied into `ans`. Whether its length is correct or not, the
function then returns.

Returning immediately is safe because all available future digits are
positive. Once the remaining sum is zero, adding another digit would make the
chosen sum exceed `n`; exclusions would merely leave the same path and cannot
repair a wrong length. Thus a zero-sum path either is a complete answer now or
can never become one.

The order of this check before `len(t) >= k` is important for accepting a
solution that reaches both conditions at the same time. For example, after the
third digit of a required three-digit combination is included, the next call
has `s == 0` and `len(t) == k`; it must append the answer before the full-length
prune can reject further expansion.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2, 4]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"k": 3, "n": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2, 4]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Increasing-candidate loop backtracking:** At e:** - **Increasing-candidate loop backtracking:** At each depth, loop from a `start` digit through 9 and recurse after choosing one. It visits combinations directly instead of representing explicit exclusion branches and has the same uniqueness principle.
- **Enumerate all bitmasks:** Each mask from 0 through $2^9-1$ describes one subset. Check its bit count and sum, then emit matching masks. It is compact but less naturally pruned and still examines all 512 subsets.
- **Combination library:** Generate `combinations(range(1, 10), k)` and filter by sum. It is concise and examines exactly $\binom{9}{k}$ candidates, but hides the search reasoning an interview solution may be expected to demonstrate.
- **Minimum/maximum achievable-sum pruning:** With `r = k - len(t)` slots remaining, compare `s` against the sum of the next `r` smallest candidates and the `r` largest available digits. This can reject branches earlier but adds arithmetic not present in the exact source.
- **Target below the minimum possible sum:** For `k = 4, n = 1`, even `1+2+3+4` is too large. The exact `i > s` and length checks eventually reject all paths and return `[]`.
- **Target above 45:** The sum of all legal digits is 45, so no answer exists. The finite-candidate check eventually ends every path; an upfront bound could return earlier but is unnecessary.
- **`k = 9`:** The only possible selection is all digits, whose sum is 45. Thus only `n = 45` can produce an answer.
- **Reaching the target too early:** If `s == 0` with fewer than `k` digits, the branch returns rather than adding positive digits that would overshoot.
- **Filling all slots too early:** If `len(t) == k` while `s > 0`, the branch returns because adding another digit would violate the required size.
- **No duplicate-output set:** Strictly increasing construction makes permutations impossible, so `ans` can remain a list and needs no deduplication pass.
- **Input preservation:** `k` and `n` are integers and are never mutated. The changing state is confined to local parameters, `t`, and `ans`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^9k)$. There are nine possible digits, each with an include or exclude choice, so a
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
