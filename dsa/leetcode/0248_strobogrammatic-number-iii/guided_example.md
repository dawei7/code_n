# Guided Example: Strobogrammatic Number III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"low": "50", "high": "100"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings low and high that represent two integers `low` and `high` where $low \le high$, return *the number of **strobogrammatic numbers** in the range* `[low, high]`.

The objective is to compute `3` from `{"low": "50", "high": "100"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only relevant digit lengths are generated

Let `a = len(low)` and `b = len(high)`. Any integer in the interval has between `a` and `b` digits because the endpoints contain no leading zeros. The outer loop therefore calls the generator for every length `n` in `range(a, b + 1)` and no other length.

This digit-length filtering is already powerful. Every generated number of a length strictly between `a` and `b` must lie between the endpoints numerically. Only candidates having the same length as a boundary can potentially fall outside. The source nevertheless applies one uniform inclusive check to every candidate, keeping the logic simple and safe.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"low": "50", "high": "100"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate a length from its center

The nested helper `dfs(u)` generates strobogrammatic strings of the current remaining length `u`.

- If `u == 0`, it returns `['']`. The empty string is the neutral center used to build even-length strings.
- If `u == 1`, it returns `['0', '1', '8']`, the only legal fixed centers for odd-length strings.
- Otherwise, it obtains every inner string from `dfs(u - 2)` and surrounds it with rotation-compatible pairs.

For each inner string `v`, four pairs are always allowed: `11`, `88`, `69`, and `96`. The pair `00` is appended only when `u != n`, meaning the current layer is internal rather than the full requested number.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why zero depends on recursion depth

A multi-digit integer cannot begin with zero, but zeros are perfectly valid inside it. For example, `1001` is a valid four-digit strobogrammatic number and requires the inner string `00`. On the other hand, `0110` is not a four-digit integer representation under the contract.

The outer loop variable `n` is captured by the helper. During `dfs(n)`, only the outermost call has `u == n`, so only that call suppresses `00`. Recursive calls have smaller `u` and may create zero-wrapped inner strings. Python closures use the current loop value of `n` when the helper runs, so each length receives the appropriate outer-length comparison.

For `n = 2`, recursion reaches the empty center. The outer layer creates `11`, `88`, `69`, and `96`, but not `00`. For `n = 4`, the internal length-two layer includes `00`; the outer layer can then turn it into `1001`, `8008`, `6009`, or `9006`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"low": "50", "high": "100"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **In-place backtracking with a character buffer:** Fill mirrored positions and check a completed candidate immediately instead of returning a list. This preserves the $O(d\cdot5^{d/2})$ time but can reduce auxiliary working space to $O(d)$ excluding recursion and the count, matching the manifest's space claim.
- **Lexicographic boundary comparison:** For equal-length canonical decimal strings, compare directly with `low` and `high` rather than converting to integers. This is useful in languages without arbitrary-precision integers; the exact Python source safely uses `int`.
- **Test every integer in the range:** This can require work proportional to the numeric width of the interval, potentially near $10^{15}$, and ignores the sparse constructive structure.
- **Inclusive endpoints:** The `<=` checks count `low` or `high` whenever the endpoint itself is strobogrammatic.
- **Different endpoint lengths:** All generated lengths strictly between them automatically fit numerically, while the common filter correctly handles both boundary lengths.
- **Single value `0`:** The one-digit base contains `0`, and the inclusive check counts it exactly once.
- **No leading zeros:** `00` is excluded only at the outermost recursive level. Internal zeros remain necessary for values such as `1001`.
- **Odd-length center:** Only `0`, `1`, and `8` remain unchanged in place. A center `6` or `9` would rotate into the other digit and invalidate the number.
- **Pair direction:** Both `69` and `96` must be generated. Neither `66` nor `99` is valid.
- **Repeated generation by length:** `dfs` has no cache, but each call forms a single chain of decreasing lengths, so no sublength is recomputed within one outer iteration. A later outer-loop length starts a fresh generation.
- **Closure over `n`:** The zero-pair rule relies on the current target length captured from the loop. Moving the helper elsewhere or evaluating it later would require passing the final length explicitly to preserve this meaning.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d\cdot5^{d/2})$. Let $d=\text{len(high)}$, the maximum generated length. A length with $h=\lfloor n/2\rfloor$ mirrored pairs has four choices for the outer pair, five choices for each inner pair, and three center choices when odd. Its count is therefore $\Theta(5^{n/2})$ up to parity-dependent constants.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
