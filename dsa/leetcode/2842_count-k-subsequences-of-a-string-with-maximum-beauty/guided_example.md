# Guided Example: Count K-Subsequences of a String With Maximum Beauty

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "bcca", "k": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an integer `k`.

The objective is to compute `4` from `{"s": "bcca", "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Beauty depends only on which character identities are chosen.** A valid length-`k` subsequence uses `k` distinct characters. If character `c` is included, its contribution to beauty is the global frequency `f(c)`, regardless of which occurrence of `c` supplies the subsequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "bcca", "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Therefore, maximum beauty is obtained by choosing `k` character identities with the largest global frequencies.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**First check whether a valid subsequence exists.** `Counter(s)` records one frequency per distinct lowercase character. If there are fewer than `k` keys, it is impossible to choose `k` unique characters, so the method returns zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "bcca", "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency buckets:** Since each frequency is at most $n$, group how many characters have each frequency and scan downward. This avoids sorting but uses $O(n)$ buckets unless a sparse map is used.
- **Select top `k` with a heap:** It can find the cutoff without fully sorting, but the alphabet has only 26 characters, so sorting is simpler.
- **Fewer than `k` distinct characters:** No valid unique-character subsequence exists, and zero is returned immediately.
- **`k = 1`:** Choose any character with maximum frequency and any one of its occurrences; the formula counts all such index choices.
- **All frequencies equal:** No character is mandatory above the cutoff; choose any `k` identities and one occurrence of each.
- **No tie at cutoff:** `x = k_remaining = 1` for that group in the relevant sense, so the combination factor is one.
- **Repeated subsequence text:** Different selected indices still count separately, and frequency multiplication captures them.
- **Modulo timing:** Identity and occurrence counts are derived in ordinary combinatorics, then multiplied modulo the required prime.
- **Mutating `k` locally:** The parameter is intentionally reused as remaining slots; no later step needs its original value.
- **Subsequence ordering:** It is determined by index order, so no permutation factor should be introduced.
- **Lower-frequency characters:** Including any one would strictly lower beauty and is never counted.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert s\rvert$ and let $\sigma\le26$ be the number of distinct characters. Building the Counter takes $O(n)$ time. Sorting frequencies takes $O(\sigma\log\sigma)$, which is $O(1)$ for the fixed alphabet. The remaining loop and count are $O(\sigma)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
