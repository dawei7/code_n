# Guided Example: Maximum Number of Equal Length Runs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "hello"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters.

The objective is to compute `3` from `{"s": "hello"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat maximal runs as the objects being counted

A run is not any substring of repeated letters. It is the entire maximal block that cannot be extended with the same character. For `"aaabbcca"`, the runs have lengths 3, 2, 2, and 1. The two length-two runs may be selected together even though one contains `b` and the other contains `c`, because compatibility depends only on length.

The answer is therefore the largest frequency among run lengths:

1. identify each maximal run exactly once;
2. count one occurrence of its length;
3. return the largest count.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "hello"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Let `groupby` discover the boundaries

`groupby(s)` groups consecutive equal characters. It starts a new group whenever the current character differs from the previous one. This is exactly the maximal-run boundary rule.

For each pair `(_, g)`, the key is the repeated character and `g` is an iterator over that run's occurrences. The character is irrelevant after the boundary has been determined, so the source names it `_`.

The expression `list(g)` consumes the current group iterator and materializes its characters. Its length is the run length. The update

`cnt[len(list(g))] += 1`

then records one more run of that length in a `Counter`.

Materializing the group is important to understanding the exact source: `g` does not already expose a stored length. It is a one-pass iterator tied to the surrounding `groupby` traversal, so the code consumes it before advancing to the next group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count lengths rather than letters

`cnt` maps a length to the number of maximal runs having that length. It does not use a pair such as `(character, length)`. This allows equal-length runs containing different letters to contribute to the same selectable collection, as required.

For `"hello"`, `groupby` yields lengths 1, 1, 2, and 1. The counter becomes `{1: 3, 2: 1}`, and the largest frequency is three.

For `"aaabaaa"`, the run lengths are 3, 1, and 3. The length-three counter reaches two, even though the two `a` runs are separated by `b` and are distinct maximal runs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "hello"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual two-pointer scan:** Advancing an end pointer to each character change obtains the same lengths without materializing group lists.
- **Count total character frequencies:** Widely separated occurrences do not form one run, so global letter counts answer a different question.
- **Count by character and length:** This wrongly prevents different letters with equal run length from being selected together.
- **Split a long run into smaller runs:** Runs must be maximal and cannot be divided to increase a length frequency.
- **Merge separated equal letters:** A different intervening character creates two distinct runs that cannot be merged.
- **Single-character string:** It has one run of length one, so the answer is one.
- **All characters equal:** There is one run of length `N`, so the answer is one.
- **Strictly alternating characters:** Every run has length one, so the answer is `N`.
- **Same length, different letters:** Both runs increment the same counter entry.
- **Same letter in separated runs:** Each maximal group is counted separately.
- **Nonempty guarantee:** It ensures `max` never receives an empty sequence.
- **Iterator lifetime:** Each `g` must be consumed before `groupby` advances, which `list(g)` does.
- **Input preservation:** Strings are immutable; the scan creates counts but does not alter `s`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the string length. `groupby` visits each character once. Converting all group iterators to lists also processes each character exactly once across disjoint groups, so total time is $O(N)$. Finding the maximum over the counter's keys costs at most $O(N)$ and does not change the bound.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
