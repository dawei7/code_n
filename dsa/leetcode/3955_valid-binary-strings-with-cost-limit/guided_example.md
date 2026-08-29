# Guided Example: Valid Binary Strings With Cost Limit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "k": 1}`
- **Required output:** `["000", "010", "100"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integers `n` and `k`.

The objective is to compute `["000", "010", "100"]` from `{"n": 3, "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The zero branch

The source first appends `"0"`, calls `dfs(i + 1, tot)`, and then pops the character.

Zero adds nothing to the cost and cannot create consecutive ones, so this branch never needs a guard. It also guarantees that every valid prefix has at least one completion: append zero at every remaining position.

Popping after recursion restores `path` to its exact state before the choice. This backtracking step is essential; otherwise the later one branch would still contain the zero just explored.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The one branch and adjacency check

After the zero branch has been popped, `path` again contains exactly the first `i` chosen characters. The expression

`not path or path[-1] == "0"`

means:

- at index zero, there is no previous character, so one is allowed;
- at any later index, one is allowed only when position `i - 1` contains zero.

This prevents `"11"` from ever becoming a prefix. Once two consecutive ones appear, no later suffix can repair them, so pruning at the moment of creation is complete and safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The cost guard

Placing one at index `i` adds exactly `i` to the defined cost. The new cost would be `tot + i`, so the source also requires:

`tot + i <= k`.

All future cost additions are nonnegative indices. If this inequality fails now, extending the prefix can never bring the cost back down, and the branch contains no valid output. It is therefore safe to omit it entirely.

When both guards pass, the source appends `"1"`, recurses with `tot + i`, and pops afterward.

Index zero contributes zero. This is why a one at the first position remains legal even when `k = 0`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["000", "010", "100"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["000", "010", "100"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all $2^n$ strings then filter:** This wastes work on prefixes that already contain `11` or exceed the cost. Backtracking prunes both immediately.
- **Dynamic programming that only counts strings:** Counting can be faster when only a number is required, but it cannot produce the requested list without reconstruction.
- **Track remaining budget instead of total cost:** This is equivalent; subtract index `i` when placing one and require the result to remain nonnegative.
- **Check adjacency only at the leaf:** Invalid `11` prefixes would generate exponentially many useless descendants.
- **Prune a high current cost assuming later zeroes help:** Zeroes add no cost but cannot reduce it. Once above `k`, the branch is permanently invalid.
- **`n = 1, k = 0`:** Both `"0"` and `"1"` are valid because the only one would be at index zero and costs zero.
- **`k = 0` with larger `n`:** A one is possible only at index zero; all positive-index ones exceed the cost.
- **All-zero string:** It is always generated and always valid.
- **One at index zero:** It contributes no cost but still prevents a one at index one through the adjacency guard.
- **Maximum `k`:** Cost pruning may disappear, but adjacency pruning still generates only Fibonacci-many no-consecutive-one strings.
- **Backtracking pop operations:** Each append is paired with a pop, ensuring sibling branches begin from the same prefix.
- **No duplicates:** Each leaf corresponds to one unique sequence of binary choices.
- **Recursion depth:** The constraint $n\le12$ keeps Python recursion safely shallow.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n * R)$. Let $R$ be the number of returned strings. Materializing each output string requires joining $n$ characters, so output construction alone costs $\Theta(nR)$ time and $\Theta(nR)$ output space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
