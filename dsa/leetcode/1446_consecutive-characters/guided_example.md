# Guided Example: Consecutive Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "leetcode"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **power** of the string is the maximum length of a non-empty substring that contains only one unique character.

The objective is to compute `2` from `{"s": "leetcode"}` while avoiding redundant calculations and unnecessary overhead.

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

**A valid substring is one run of equal characters.** The power of the string is not about how often a character appears in total. It is about the longest contiguous block in which every character is the same. For example, two occurrences of `a` separated by another letter cannot be combined. The string can therefore be viewed as consecutive runs, and the task is to find the maximum run length.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "leetcode"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

- `t` is the length of the equal-character run that ends at the current position.
- `ans` is the largest run length seen anywhere so far.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Both begin at one because the input is guaranteed to be nonempty. Even a one-character string has power one, and before any adjacent pair is examined, the first character already forms a run of length one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "leetcode"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual index loop:** Iterate `i` from one through `n - 1` and compare `s[i]` with `s[i - 1]`. This has identical time and space bounds and may be preferable where `pairwise` is unavailable.
- **Track the previous character explicitly:** Loop over characters, store `previous`, and update a count. This is the editorial's equivalent formulation and handles the first character with either a sentinel or a special initialization.
- **Group consecutive characters:** `itertools.groupby` can form each run lazily, after which the maximum group length is measured. It is expressive, but counting each group usually introduces more iterator machinery than the two-counter scan.
- **Frequency map:** Counting total occurrences per character is incorrect because equal letters separated by other characters do not form one substring.
- **Generate every substring:** Testing all substrings repeats work and needs at least quadratic candidates. A run is fully determined by adjacent equality, so one pass is sufficient.
- **Sort the characters:** Sorting destroys original adjacency, which is the defining property of a substring. It would answer a different frequency question.
- **One-character string:** There are no adjacent pairs. The initial value one is returned, which is the only nonempty substring's length.
- **All characters equal:** Every pair matches, `t` grows from one to `n`, and `ans` finishes at `n`.
- **All neighboring characters different:** Every iteration resets `t` to one. The power is one.
- **Longest run at the beginning:** `ans` records that run before later differences reset `t`, so it is not lost.
- **Longest run at the end:** The equal-pair branch updates `ans` immediately on each extension, so no special end-of-loop flush is needed.
- **Several equally long runs:** Taking `max` keeps their common length. The task asks only for the length, not a location or character.
- **Lowercase-only guarantee:** The algorithm would also work for other comparable characters, but it needs no case normalization because the input is already restricted.
- **Substring versus subsequence:** Only adjacent positions count. The pair scan enforces contiguity automatically and never skips intervening characters.
- **Empty string outside the contract:** Initialization to one would be wrong for an empty input. The stated lower bound of one makes this case impossible; a generalized function would need a separate empty check.
- **Lazy iterator requirement:** Calling `pairwise` directly keeps space constant. Materializing all pairs would change auxiliary space to `O(n)` without improving the result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `s`. A nonempty string has exactly `n - 1` adjacent pairs. The loop processes each pair once, doing one character comparison and a constant number of integer operations. Total running time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
