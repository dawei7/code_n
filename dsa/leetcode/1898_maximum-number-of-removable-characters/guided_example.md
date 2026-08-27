# Guided Example: Maximum Number of Removable Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcacb", "p": "ab", "removable": [3, 1, 0]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `p` where `p` is a **subsequence **of `s`. You are also given a **distinct 0-indexed **integer array `removable` containing a subset of indices of `s` (`s` is also **0-indexed**).

The objective is to compute `2` from `{"s": "abcacb", "p": "ab", "removable": [3, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

**Search over a prefix length, not arbitrary removals.** Choosing `k` means removing exactly the first `k` indices of `removable`. If `p` remains a subsequence after `k` removals, it also remains one after any smaller prefix because restoring characters cannot destroy an existing subsequence. If it fails after `k` removals, every larger prefix also fails because deleting more characters cannot create a missing subsequence. Feasibility is therefore monotone: true values of `k` form a prefix followed by false values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcacb", "p": "ab", "removable": [3, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Implement one feasibility check literally.** `check(k)` creates Boolean list `rem` with one entry per position of `s`. It marks each index in `removable[:k]` as true. The removable indices are distinct, so every mark corresponds to one deleted character, although repeated marking would not otherwise hurt the Boolean representation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Implement one feasibility check literally.** `check(k)` cr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The original string is not rebuilt. Instead, two pointers scan it logically. Pointer `i` visits every original position; pointer `j` is the next character of `p` that still needs a match. A character advances `j` only when its position is not removed and `s[i] == p[j]`. Regardless of a match, `i` advances. If `j` reaches `len(p)`, every pattern character has been found in order among surviving positions, which is exactly the subsequence definition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcacb", "p": "ab", "removable": [3, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Removal-time array:** Store for each index the:** - **Removal-time array:** Store for each index the step at which it is removed, then a check treats positions with time below `k` as absent. This avoids a fresh prefix slice and repeated marking while preserving $O(n\log r)$ time.
- **Try every `k` sequentially:** Monotonicity permits binary search; checking all prefixes can cost $O(nr)$.
- **Rebuild the surviving string:** Joining unremoved characters and then testing a subsequence works but allocates another length-$n$ string per check. Logical skipping is sufficient.
- **Maximum answer zero:** The first listed removal can destroy the only possible embedding. Initial zero remains the last feasible bound.
- **Every listed index removable:** If `p` can still be formed after all removals, the upper endpoint stays feasible and is returned.
- **Removed matching character:** The scan must test `not rem[i]` before accepting equality; marked characters do not exist logically.
- **Repeated letters:** Earliest greedy matching remains correct and avoids backtracking among equivalent occurrences.
- **Empty removable list:** Both bounds are zero, the loop does not run, and zero is returned.
- **Distinct-index guarantee:** Boolean marking naturally supports it. The guarantee also means `k` truly represents removing `k` characters rather than fewer unique positions.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n+r)$. Let $n=\lvert s\rvert$ and $r=\lvert\texttt{removable}\rvert$. Binary search performs $O(\log(r+1))$ checks. One check allocates and initializes $n$ Booleans, copies a slice of up to $r$ indices, marks it, and scans at most $n$ characters. Its cost is $O(n+r)$, which is $O(n)$ here because $r<n$. Total time is $O((n+r)\log(r+1))$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
