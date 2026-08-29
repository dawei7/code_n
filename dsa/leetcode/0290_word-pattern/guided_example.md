# Guided Example: Word Pattern

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"pattern": "abba", "s": "dog cat cat dog"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

The objective is to compute `true` from `{"pattern": "abba", "s": "dog cat cat dog"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The required relationship is a bijection

Matching positions is not enough unless the mapping works in both directions. Every pattern character must always represent the same word, and every word must always belong to the same pattern character.

For example, pattern `"abba"` and words `"dog cat cat dog"` are valid because `a -> dog` and `b -> cat` remain consistent. Pattern `"ab"` with words `"dog dog"` is invalid even though each character could individually be assigned a word: two different characters would map to the same word, violating uniqueness in the reverse direction.

The exact solution enforces the bijection with two dictionaries:

- `d1` maps each pattern character to its word;
- `d2` maps each word back to its pattern character.

Keeping both directions makes every consistency check an expected constant-time hash lookup.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"pattern": "abba", "s": "dog cat cat dog"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Split the sentence and reject a cardinality mismatch first

The source uses `s.split()` to obtain the sequence of words. Under the contract, words are separated by single spaces with no leading or trailing space. Python's no-argument `split()` also tolerates repeated or surrounding whitespace, although legal inputs do not require that extra robustness.

There must be exactly one word for every pattern position. If `len(pattern) != len(ws)`, no full position-by-position match is possible, so the method returns false immediately.

This check is also essential before using `zip`. Python's `zip(pattern, ws)` stops when the shorter input ends. Without the explicit length comparison, an extra character or extra word would be silently ignored and an incomplete match could incorrectly return true.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check the forward mapping

For each aligned pair `(a, b)`, where `a` is a pattern character and `b` is a word, the first possible violation is:



If this occurs, one character is trying to represent two different words. For example, in pattern `"aaaa"` and words `"dog cat cat dog"`, the first pair establishes `a -> dog`, while the second asks for `a -> cat`. The forward check rejects that contradiction immediately.

If `a` has never appeared, no forward commitment exists yet, so this direction alone permits establishing `a -> b`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"pattern": "abba", "s": "dog cat cat dog"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One forward map only:** It detects one character mapping to several words but misses two characters mapping to the same word. A reverse map or used-word set is required.
- **Forward map plus used-word set:** For a new character, reject an already-used word; otherwise record both. This enforces the same bijection with slightly less reverse information.
- **First-occurrence indices:** Record where each character and each word first appeared and require paired first-occurrence indices to match. It can use one carefully namespaced map but is less direct than explicit inverse maps.
- **Scan map values for collisions:** A single map can test whether a new word is already among its values, but value lookup is linear in the number of mappings rather than expected constant time.
- **More words than characters:** The length check rejects before `zip` can hide the extra suffix.
- **More characters than words:** The same check rejects the unmatched pattern suffix.
- **Repeated valid pair:** Reassigning the same forward and reverse entries changes nothing and remains valid.
- **One character, multiple words:** The forward check rejects the first differing word.
- **One word, multiple characters:** The reverse check rejects the second character.
- **All positions identical:** A pattern of repeated one character is valid only when every word is also the same.
- **Single position:** One character and one nonempty word always form a valid bijection.
- **Whitespace behavior:** Legal input uses single spaces. No-argument `split()` would also normalize multiple whitespace characters rather than creating empty words.
- **Case sensitivity:** Legal strings are lowercase. Without that restriction, Python keys would still treat uppercase and lowercase forms as distinct.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $P$ be the pattern length and $S$ be the number of characters in `s`. Splitting the sentence takes $O(S)$ time and creates word strings whose total character content is $O(S)$. The pair loop runs $P$ iterations.
- **Auxiliary Space Complexity:** $O(S+P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
