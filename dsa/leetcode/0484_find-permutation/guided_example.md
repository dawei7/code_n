# Guided Example: Find Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "DI"}`
- **Required output:** `[2, 1, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A permutation `perm` of `n` integers of all the integers in the range `[1, n]` can be represented as a string `s` of length $n - 1$ where:

The objective is to compute `[2, 1, 3]` from `{"s": "DI"}` while avoiding redundant calculations and unnecessary overhead.

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

If there were no `D` requirements, the lexicographically smallest permutation of `1` through `n + 1` would simply be

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "DI"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

An `I` already agrees with that ascending order. A maximal run of `D` characters is the only place where the order must change. The solution starts with the globally smallest ascending permutation and reverses exactly the value block covered by each decrease run.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**A pattern position connects two permutation positions.** Character `s[i]` describes the comparison between `ans[i]` and `ans[i + 1]`. Therefore, if a run of `D` starts at pattern index `i` and stops just before pattern index `j`, it contains `j - i` decrease signs but affects `j - i + 1` numbers: indices `i` through `j` of `ans`. This is why the slice is `ans[i : j + 1]`. Python excludes the right endpoint of a slice, so `j + 1` is required to include `ans[j]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "DI"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Stack construction:** Push increasing values while reading `D`s and flush the stack at each `I`. Popping reverses each decrease block and also runs in $O(n)$ time, but it uses a separate stack.
- **In-place two-pointer reversal:** Swap endpoints of every affected block rather than assigning reversed slices. This preserves the same reasoning and reduces temporary auxiliary storage, at the cost of a few more implementation lines.
- **Brute-force permutations:** Enumerating all $(n+1)!$ permutations and selecting the first match is impossible for `n` up to $10^5$. The block structure determines the minimum directly.
- **All `I` characters:** Every processed slice has length one, so the answer remains `[1, 2, ..., n + 1]`, the smallest permutation overall.
- **All `D` characters:** One run reaches `j = n` and reverses the entire array, producing `[n + 1, n, ..., 1]`, the only fully decreasing permutation.
- **Run at the end:** The answer slice includes position `n` through the `j + 1` endpoint, so the final value is not omitted.
- **One `D`:** Two adjacent values are reversed. A single pattern comparison always affects two permutation positions.
- **Repeated values are impossible:** `ans` begins as the exact range `1` through `n + 1`, and reversal only changes order, so the permutation property is preserved automatically.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`, so the returned permutation has $n + 1$ values. Building `list(range(1, n + 2))` costs $O(n)$ time. The scan advances across each pattern character a constant number of times. Reversed answer slices for maximal `D` runs are disjoint except for harmless boundaries, so their total length is $O(n)$. Overall time is therefore $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
