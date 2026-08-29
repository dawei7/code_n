# Guided Example: Make Number of Distinct Characters Equal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word1": "ac", "word2": "b"}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed** strings `word1` and `word2`.

The objective is to compute `false` from `{"word1": "ac", "word2": "b"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A swap's effect depends only on the two character values

Swapping one occurrence of character `c1` from `word1` with one occurrence of `c2` from `word2` changes frequencies, not string order.

For a chosen character value, every occurrence has the same effect. Therefore, it is sufficient to examine pairs of distinct character keys present in the two counters rather than every pair of string indices.

The lowercase alphabet has only 26 possibilities, so at most $26^2=676$ character-value pairs are tested.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word1": "ac", "word2": "b"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count current frequencies and distinct totals

`cnt1` and `cnt2` store character frequencies. Their key counts

`x=len(cnt1)` and `y=len(cnt2)`

are the initial numbers of distinct characters.

For every present `c1` with frequency `v1` and present `c2` with frequency `v2`, the algorithm computes what the distinct totals would become after swapping one occurrence.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case one: swap equal characters

If `c1==c2`, both strings give away and receive the same character. Their frequency maps and distinct counts remain unchanged.

Because exactly one move is required, this is still a legitimate move: choose an occurrence of that shared character in each string and swap them.

It succeeds exactly when current totals already match, `x==y`.

If the totals differ, an equal-character swap cannot change them and is useless.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word1": "ac", "word2": "b"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate every index pair:** It can cost $O(|word1||word2|)$ and repeats identical character-value effects.
- **Equal characters:** Swapping them changes nothing and works only if totals already match.
- **Frequency one:** Removing the selected occurrence deletes a distinct character.
- **Frequency above one:** The character remains represented after removal.
- **Incoming character already present:** It does not increase the distinct count.
- **Disjoint alphabets with equal totals:** Swapping one unique character from each may preserve equal counts.
- **Single-character strings:** The sole swap can be evaluated by the same formulas.
- **Exactly one move:** A no-op equal-character swap is legal only when that character occurs in both strings.
- **Lowercase alphabet:** It bounds candidate character pairs by 676.
- **Counters:** They let character identities stand in for all equivalent index choices.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{word1}\rvert+\lvert\texttt{word2}\rvert$. Building both counters costs $O(N)$ expected time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
