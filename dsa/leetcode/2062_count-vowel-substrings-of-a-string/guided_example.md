# Guided Example: Count Vowel Substrings of a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "aeiouu"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **substring** is a contiguous (non-empty) sequence of characters within a string.

The objective is to compute `2` from `{"word": "aeiouu"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Fix a start and extend every vowel-only substring

The source considers every index `i` as a possible substring start. For that start, it scans characters in `word[i:]` from left to right.

Set `t` stores which of the five vowel kinds have appeared in the current substring. Each encountered vowel is added, and once `len(t) == 5`, the substring ending at that character contains all five vowels and contributes one.

Extending farther through vowels keeps all previously seen vowel kinds, so every later endpoint is evaluated independently and may also contribute.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "aeiouu"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Stop at the first consonant

A valid vowel substring may contain only vowels. Once the inner scan encounters `c not in s`, every longer substring with the same start also contains that consonant.

The source breaks immediately. No later endpoint for this start can recover validity, even if more vowels appear afterward.

This pruning separates the string into vowel-only runs implicitly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A valid vowel substring may contain only vowels.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a set captures the all-five requirement

The required property depends on presence, not frequency. Seeing several `a` characters still supplies only one of the five required vowel types.

`t.add(c)` automatically ignores repeated values. Because the vowel universe has exactly five elements, `len(t)==5` is equivalent to having `a,e,i,o,u` all present.

The outer set `s = set("aeiou")` provides constant-time membership testing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "aeiouu"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Last-occurrence linear scan:** Track all five :** - **Last-occurrence linear scan:** Track all five latest vowel indices and the last consonant to count valid starts per endpoint in $O(N)$ time.
- **Index-based nested loop:** Avoid suffix allocations but still takes $O(N^2)$ time.
- **Fewer than five characters:** Cannot contain all five vowels, so answer is zero.
- **All consonants:** Every inner scan breaks on its first character.
- **Repeated vowel:** Does not increase the set size but may create additional valid endpoints after all five exist.
- **Consonant boundary:** Vowels on opposite sides cannot belong to one valid substring.
- **All-vowel word:** Produces the quadratic worst case.
- **Exactly one occurrence of each vowel:** The whole five-character run contributes once.
- **Different vowel order:** Presence matters, not ordering.
- **Manifest mismatch:** Exact source is quadratic time with linear peak slice space.
- **Input preservation:** The string is immutable; slices are new strings.
- **Small constraint:** $N\le100$ makes the exhaustive implementation practical despite the mismatch.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let $N=len(word)$. In the worst case of all vowels, the nested scan performs $\Theta(N^2)$ character visits. Creating every suffix slice also totals $\Theta(N^2)$ copied characters over the execution. Exact time is $O(N^2)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
