# Guided Example: Longest Uncommon Subsequence II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"strs": ["aba", "cdc", "eae"]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `strs`, return *the length of the **longest uncommon subsequence** between them*. If the longest uncommon subsequence does not exist, return `-1`.

The objective is to compute `3` from `{"strs": ["aba", "cdc", "eae"]}` while avoiding redundant calculations and unnecessary overhead.

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

With many input strings, a candidate is uncommon only if it is a subsequence of one string and is **not** a subsequence of every other string. The key simplification is that it is enough to test each entire input string as a candidate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"strs": ["aba", "cdc", "eae"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Suppose some deletion-produced subsequence `u` of `strs[i]` is uncommon. If the whole `strs[i]` is not a subsequence of any other input, then that whole string is also uncommon and is at least as long as `u`. If the whole string is a subsequence of another input, `u` may or may not occur there, but an optimal uncommon answer can always be represented by some full input string: choose the source string of a longest uncommon subsequence; if its whole string appeared as a subsequence elsewhere, every subsequence of it—including the candidate—would also appear there, a contradiction.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The algorithm therefore evaluates each `strs[i]` as a full candidate `s` and asks whether any other string `t` contains it as a subsequence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"strs": ["aba", "cdc", "eae"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort by decreasing length:** The first full candidate not contained in another string gives the answer, but sorting adds $O(k\log k)$ organization and does not eliminate the pairwise containment checks.
- **Count exact duplicates first:** Duplicate values can be ruled out quickly, yet unique candidates must still be tested as subsequences of longer strings.
- **Enumerate all subsequences:** Each short string has exponentially many deletion patterns; the full-candidate transitivity proof makes this unnecessary.
- **Identical strings at different indices:** `i != j` still compares them, and each duplicate correctly disqualifies the other.
- **Candidate longer than container:** The helper cannot advance `i` enough before `j` ends, so it returns false naturally.
- **Candidate equal to container value:** At a different index, every character matches and the candidate is rejected.
- **Shorter string embedded in a longer one:** It is not uncommon even if it appears only once as an exact array value.
- **Same-length different strings:** One can be a subsequence of the other only if they are equal, so different values do not disqualify each other.
- **No valid candidate:** `ans` is never updated and remains `-1`.
- **Several valid candidates with equal maximum length:** Only the length is requested, so `max` needs no tie-breaking.
- **Greedy earliest match:** Choosing the earliest usable character in `t` cannot block a solution that a later choice would enable.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $k$ be the number of strings and $L$ their maximum length. There are $k^2$ index pairs in the nested loops up to constant exclusions. One `check(s, t)` scans at most $L$ characters of `t` and advances the candidate pointer at most $L$ times, so it costs $O(L)$. Worst-case time is $O(k^2L)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
