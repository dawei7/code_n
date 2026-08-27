# Guided Example: Guess the Word

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["hamada", "khaled"], "master": {"secret": "hamada", "allowed_guesses": 10}}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of unique strings `words` where $\text{words}[i]$ is six letters long. One word of `words` was chosen as a secret word.

The objective is to compute `true` from `{"words": ["hamada", "khaled"], "master": {"secret": "hamada", "allowed_guesses": 10}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each guess partitions the remaining candidates

Every word has six positions. When `master.guess(guess)` returns a score from 0 through 6, it tells us how many positions the guess shares with the secret.

For any remaining candidate, we can compute the score it would produce against the guess. Only candidates producing the returned score can still be the secret. Thus, a guess partitions the candidate set into at most seven buckets, one for each possible match count.

After observing the actual score, we retain exactly one bucket.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["hamada", "khaled"], "master": {"secret": "hamada", "allowed_guesses": 10}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count matching positions

Helper `matches(first, second)` zips the two six-letter strings and sums `left == right`.

Each equality is a Boolean, which contributes one for a positional match and zero otherwise. This is exactly the feedback definition; characters appearing at different positions do not count.

All words have length six, so `zip` compares every position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Helper `matches(first, second)` zips the two six-letter stri... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the candidate invariant

`candidates` begins as a copy of `words`. Its invariant is:

> Every word in `candidates` is consistent with all feedback received so far, and the secret is among them.

The secret belongs initially because the contract says it appears in `words`.

After guessing `guess` and receiving `score`, the filtering expression keeps candidate `candidate` only when:

`matches(guess, candidate) == score`.

The actual secret necessarily satisfies this equality because `score` came from comparing the guess with that secret. Every candidate with a different hypothetical score contradicts the observed feedback and is safely discarded. The invariant is preserved.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["hamada", "khaled"], "master": {"secret": "hamada", "allowed_guesses": 10}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Guess candidates in arbitrary order:** It even:** - **Guess candidates in arbitrary order:** It eventually finds the secret but may exceed the limited call budget.
- **- **Random guessing:** Often works on generated ca:** - **Random guessing:** Often works on generated cases but provides no deliberate worst-bucket control and makes behavior nondeterministic.
- **- **Choose from all original words, not only candi:** - **Choose from all original words, not only candidates:** A noncandidate probe can sometimes partition better, but the exact source restricts guesses to current candidates and guarantees every guess remains valid.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(qg^2\ell)$. Let `g` be the initial number of candidates, let the fixed word length be six, and let `q` be the number of guess rounds.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
