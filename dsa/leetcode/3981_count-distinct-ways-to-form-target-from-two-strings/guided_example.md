# Guided Example: Count Distinct Ways to Form Target from Two Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word1": "abc", "word2": "bac", "target": "abc"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three strings `word1`, `word2`, and `target`.

The objective is to compute `5` from `{"word1": "abc", "word2": "bac", "target": "abc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One-based stored indices

Let `n_1=\lvert word1\rvert` and `n_2=\lvert word2\rvert`. The source uses table indices from zero through each word length.

- stored value zero means that source word has never been used;
- stored value `p\ge1` means the last chosen character was at ordinary zero-based index `p-1`.

This one-based representation is useful because zero simultaneously means “no previous index” and proves that the source has not contributed any character.

After some target prefix has been processed, `dp[last1][last2]` counts constructions of that prefix whose latest selected positions have those stored values.

The initial empty target prefix has one construction that uses neither word:



Every other initial state is impossible and remains zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word1": "abc", "word2": "bac", "target": "abc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A new table for each target character

For each required character `needed`, the source creates a zero-filled `next_dp`. Every transition chooses exactly one matching source position for this target character and moves from `dp` to `next_dp`.

Using a separate next table is essential. Updating `dp` in place could allow one target character to be chosen multiple times during the same outer iteration.

After all transitions for `needed`, `dp = next_dp` advances the represented target prefix by exactly one character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each required character `needed`, the source creates a z... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choosing the next character from `word1`

Suppose the new stored index in `word1` will be `new1`, meaning actual position `new1-1` is chosen. Its character must satisfy:



The previous stored `last1` may be zero or any positive value strictly smaller than `new1`. This exactly enforces increasing actual indices. The latest `word2` index remains unchanged.

For fixed `last2`, the desired transition count is:

$$
\texttt{nextDp}[new1][last2]
=
\sum_{p=0}^{new1-1}\texttt{dp}[p][last2].
$$

Computing that sum from scratch for every `new1` would add another factor of `n_1`. The source maintains a running prefix:



At iteration `new1`, `prefix` contains exactly table rows zero through `new1-1`. It therefore sums every legal predecessor once.

The assignment rather than addition is safe here because this loop is the only collection of transitions that choose the current target character from `word1` and end at this exact `(new1,last2)` state. All eligible old histories have already been combined into `prefix`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word1": "abc", "word2": "bac", "target": "abc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every source assignment:** Even befo:** - **Enumerate every source assignment:** Even before choosing indices, each of `t` target positions has two source choices, giving up to `2^t` assignments.
- **- **Backtracking over matching indices:** Repeated:** - **Backtracking over matching indices:** Repeated characters can create exponentially many increasing subsequences. Dynamic programming aggregates histories with the same future constraints.
- **- **Track only how many characters were consumed f:** - **Track only how many characters were consumed from each word:** A source may skip arbitrary characters, so the last selected index—not merely the number selected—determines future choices.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(tnm)$. Let
- **Auxiliary Space Complexity:** $O(nm)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
