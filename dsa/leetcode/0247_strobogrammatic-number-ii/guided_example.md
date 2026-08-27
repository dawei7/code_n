# Guided Example: Strobogrammatic Number II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2}`
- **Required output:** `["11", "69", "88", "96"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return all the **strobogrammatic numbers** that are of length `n`. You may return the answer in **any order**.

The objective is to compute `["11", "69", "88", "96"]` from `{"n": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The helper's precise promise

`dfs(u)` returns all strobogrammatic strings of length `u` that may be used as the current inner portion of the final length-`n` number. Inner portions are allowed to begin with `0`; only the outermost digit of the final number is forbidden from being zero.

That distinction explains why the helper needs access to the original `n` through its closure. At an internal level, `u != n`, so wrapping with `"0" + v + "0"` is allowed. At the outermost level, `u == n`, so `00` is skipped to prevent a leading zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why construction begins at the center

Every recursive call decreases the remaining length by two, corresponding to reserving one position at each end. The parity never changes, so there are two base cases.

- For `u == 0`, return `['']`. The empty string acts as the neutral center of an even-length number. Wrapping it with `11`, for example, produces `11`.
- For `u == 1`, return `['0', '1', '8']`. An odd-length number has one center position that maps to itself, and only these three digits do so.

The empty-string base case is especially important. If the recursion instead began with only the valid two-digit numbers, it would omit `00` as an inner block and could never generate valid values such as `1001` or `6009`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every recursive call decreases the remaining length by two, ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How each recursive level expands the inner results

For every inner string `v`, the loop always creates four wrappers:



It deliberately leaves `00` out of that tuple and appends it separately only when `u != n`. This layout makes it impossible to accidentally generate a final number with a leading zero while still permitting zeros at internal mirrored positions.

For `n = 2`, `dfs(0)` produces `['']`. The outer `dfs(2)` wraps the empty center with the four nonzero pairs, yielding `['11', '88', '69', '96']`. The `00` pair is skipped because `u == n`.

For `n = 4`, recursion first computes `dfs(2)` as an **inner** level. Here `u = 2` differs from the final `n = 4`, so it includes `['11', '88', '69', '96', '00']`. The outer level wraps each of those five centers with four nonzero pairs. This includes values such as `1001`, whose inner `00` is necessary even though an outer leading zero would be invalid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["11", "69", "88", "96"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["11", "69", "88", "96"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Backtracking into a fixed character array:** F:** - **Backtracking into a fixed character array:** Fill mirrored positions from the outside inward and emit a copy at the center. It generates the same search space and can avoid repeatedly concatenating intermediate strings, though each completed answer still needs an $O(n)$ copy.
- **Iterative center expansion:** Start with `['']` for even `n` or `['0', '1', '8']` for odd `n`, then wrap level by level. It mirrors this recursion exactly and removes call-stack usage.
- **Generate all digit strings and filter:** Trying $10^n$ strings ignores the strong pair constraints and is exponentially much larger than generating only valid candidates.
- **`n = 1`:** Return `0`, `1`, and `8`. These are the only digits unchanged by rotation and `0` is a valid one-digit number.
- **`n = 2`:** The inner empty string is wrapped by the four nonzero pairs. `00` is excluded because it is not a two-digit number.
- **Zeros inside longer numbers:** Internal `00` pairs are necessary. Values such as `1001` are valid even though `0000` is not a valid four-digit result.
- **Leading zero:** The condition `u != n` is what distinguishes an internal layer from the final outer layer. Removing it would generate strings whose written length is `n` but whose numeric representation has fewer digits.
- **Odd center `6` or `9`:** These digits rotate into each other rather than themselves, so neither can occupy the fixed center position.
- **Pair orientation:** `69` and `96` are both valid and distinct. Pairs `66` and `99` are invalid because each digit rotates into the other digit, not itself.
- **Output ordering:** The exact code emits wrappers in the order `11`, `88`, `69`, `96`, followed by internal `00`. Sorting is unnecessary and would add work because any return order is accepted.
- **Duplicate generation:** Each result has one unique sequence of outer pairs and optional center, so different construction paths cannot produce the same string.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot 5^{n/2})$. Let $h=\lfloor n/2\rfloor$, the number of mirrored position pairs. For even $n=2h$ with $h\ge1$, the outer pair has four choices and each of the remaining $h-1$ inner pairs has five choices, so the exact result count is
- **Auxiliary Space Complexity:** $O(n \cdot 5^{n/2})$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
