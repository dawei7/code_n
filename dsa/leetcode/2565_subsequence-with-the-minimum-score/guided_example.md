# Guided Example: Subsequence With the Minimum Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abacaba", "t": "bzaa"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `t`.

The objective is to compute `1` from `{"s": "abacaba", "t": "bzaa"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: An optimal removal may be treated as one contiguous block

The score is determined only by the smallest and largest removed indices. If some characters between those endpoints were originally kept, removing them too does not increase the score because the endpoints remain the same. Removing additional characters from `t` also cannot destroy the fact that the remaining string is a subsequence of `s`.

Therefore, an optimal solution can remove one contiguous block `t[k:k+x]` of length $x$. The kept string consists of a prefix `t[:k]` followed by a suffix `t[k+x:]`. The problem becomes finding the smallest $x$ for which some split $k$ lets both kept pieces appear in `s` in the correct order.

Length zero represents removing nothing. Length `len(t)` represents removing all of `t`, leaving the empty string, which is always a subsequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abacaba", "t": "bzaa"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Record the earliest match for every prefix endpoint

Let $m=|s|$ and $n=|t|$. The array `f` has one entry per index of `t`. A left-to-right greedy scan matches `t` against `s`. Whenever `s[i] == t[j]`, it sets `f[j] = i` and advances $j$.

Thus, when finite, `f[p]` is the earliest position in `s` where the prefix `t[:p+1]` can finish. Greedily using the earliest possible match is optimal because it leaves the largest remaining suffix of `s` available for whatever must come afterward.

Entries for unmatched prefix characters remain `inf`. Such a prefix cannot be embedded in `s`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let $m=|s|$ and $n=|t|$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Record the latest match for every suffix start

The array `g` is built symmetrically from right to left. When `s[i] == t[j]`, the scan sets `g[j] = i` and moves to the preceding character of `t`.

When valid, `g[q]` is the latest position in `s` where the suffix `t[q:]` can begin. Taking suffix matches as late as possible leaves the largest amount of room before them for a kept prefix.

Entries that cannot start a fully matched suffix remain $-1$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abacaba", "t": "bzaa"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Linear two-pointer optimization:** Prefix and :** - **Linear two-pointer optimization:** Prefix and suffix match information can be combined in one monotone sweep to find the minimum gap in $O(m+n)$ time, matching the manifest but differing from this implementation.
- **Try every removed interval:** There are $O(n^2)$ intervals, and checking each subsequence separately is much too slow.
- **General subsequence dynamic programming:** A two-dimensional table over both strings is unnecessary and can require $O(mn)$ time or space.
- **Already a subsequence:** `check(0)` succeeds, and binary search returns score zero.
- **No shared useful characters:** Only removing all of `t` works, so the answer is $n$.
- **Empty kept prefix:** The $-1$ sentinel ensures a valid suffix alone can satisfy the check.
- **Empty kept suffix:** The `m + 1` sentinel ensures a valid prefix alone can satisfy the check.
- **Unmatched prefix or suffix:** `inf` and $-1$ deliberately make `l < r` false for an impossible real piece.
- **Repeated characters:** Greedy earliest prefix matches and latest suffix matches preserve maximum separation even when many choices exist.
- **Lazy search range:** `range(n + 1)` does not allocate an $O(n)$ list of candidate lengths.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+n)$. Building `f` and `g` takes $O(m+n)$ time because each two-pointer scan advances through each string only once. One `check(x)` call loops over up to $n$ split positions and costs $O(n)$ time. Binary search calls it $O(\log n)$ times.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
