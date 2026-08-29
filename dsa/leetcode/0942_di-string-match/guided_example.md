# Guided Example: DI String Match

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "IDID"}`
- **Required output:** `[0, 4, 1, 3, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A permutation `perm` of $n + 1$ integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

The objective is to compute `[0, 4, 1, 3, 2]` from `{"s": "IDID"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the extreme remaining value to satisfy each sign immediately

The result must be a permutation of every integer from `0` through `n`. At each position, the current character says only whether the next permutation value must be larger or smaller. It does not prescribe an exact difference.

The solution maintains the interval of values not yet used:

- `low` is the smallest unused value;
- `high` is the largest unused value.

Initially every required value is available, so `low = 0` and `high = n`.

When the current sign is `I`, the algorithm places `low`. Every value that remains afterward is larger, so whichever value is chosen next will satisfy the required increase.

When the current sign is `D`, it places `high`. Every remaining value is smaller, so the next choice will satisfy the required decrease.

This extreme-choice rule turns a condition involving the unknown next value into a guarantee against all possible next values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "IDID"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Processing an `I`

For character `I`, the code appends the current `low` and increments `low`.

Before the update, unused values form the inclusive interval `[low, high]`. After using the smallest one, the future unused interval is `[low + 1, high]`. Every member of that interval exceeds the appended value.

Therefore, the next appended value is guaranteed to be larger, regardless of whether the next character asks the algorithm to choose its new low endpoint or high endpoint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Processing a `D`

For character `D`, the code appends `high` and decrements `high`.

After the largest value is removed, every future unused value is at most the old `high - 1` and is therefore smaller than the appended value. The descent is guaranteed before the algorithm even knows which remaining value will be selected next.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 4, 1, 3, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "IDID"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 4, 1, 3, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Construct from runs of `D`:** Start with increasing values and reverse segments corresponding to consecutive decreases. This also yields `O(n)` time, but the low/high invariant is more direct.
- **Backtracking over permutations:** It may find an answer but explores an enormous search space even though an extreme choice always guarantees progress.
- **Sort values after assigning inequalities:** Postponing exact values creates an unnecessary constraint-solving problem. The endpoint method assigns a valid unused value immediately.
- **All `I` characters:** The algorithm repeatedly takes the low endpoint and returns `[0, 1, ..., n]`.
- **All `D` characters:** It repeatedly takes the high endpoint and returns `[n, n - 1, ..., 0]`.
- **Alternating signs:** Low and high endpoints alternate, producing a zigzag such as `[0, n, 1, n - 1, ...]` while preserving uniqueness.
- **String length one:** One endpoint is selected for the single sign and the other is appended, giving either `[0, 1]` or `[1, 0]`.
- **Multiple valid permutations:** The problem permits any valid answer. This method deterministically returns one particular extreme-based permutation.
- **Strict comparisons:** Values never repeat, and the next unused interval lies strictly above an old low or strictly below an old high, so equality cannot occur.
- **Final endpoint equality:** After processing all signs, `low` and `high` must coincide. If they did not, the endpoint-removal invariant or loop count would have been violated.
- **Output-space convention:** Some analyses call the working space `O(1)` by excluding the answer list. Including the returned permutation gives `O(n)` total additional storage, which matches this package's manifest.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `s`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
