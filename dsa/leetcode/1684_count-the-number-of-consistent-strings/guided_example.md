# Guided Example: Count the Number of Consistent Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"allowed": "ab", "words": ["ad", "bd", "aaab", "baa", "badab"]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `allowed` consisting of **distinct** characters and an array of strings `words`. A string is **consistent **if all characters in the string appear in the string `allowed`.

The objective is to compute `2` from `{"allowed": "ab", "words": ["ad", "bd", "aaab", "baa", "badab"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the allowed alphabet into a lookup structure

A word is consistent when every one of its characters belongs to `allowed`. Repeatedly searching the original string for each character would work, but a set expresses membership directly.

`s = set(allowed)` stores each allowed character once. The input already guarantees that characters in `allowed` are distinct, but set conversion still provides expected constant-time `c in s` tests.

Because all characters are lowercase English letters, the set contains at most 26 entries.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"allowed": "ab", "words": ["ad", "bd", "aaab", "baa", "badab"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Check one complete word

For a word `w`, the expression

`all(c in s for c in w)`

tests its characters lazily from left to right. The inner generator produces one Boolean membership result at a time. `all` returns true only if every produced value is true.

If an unallowed character is found, `all` short-circuits immediately. Later characters in that word do not matter because one violation is enough to make the entire word inconsistent.

If the generator reaches the end without a false membership test, every character belongs to `s` and `all` returns true.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count Boolean results

The outer generator applies that word check to every string in `words`. Python Booleans act as integers during addition: `true` contributes one and `false` contributes zero. Therefore

`sum(all(...) for w in words)`

counts exactly the words for which the condition succeeds.

No list of per-word results is created. `sum` consumes one Boolean at a time and maintains a numeric accumulator.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"allowed": "ab", "words": ["ad", "bd", "aaab", "baa", "badab"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **26-element Boolean array:** Map each character to `ord(c)-ord('a')` and test a fixed slot. This gives deterministic constant-time lookup and constant space.
- **26-bit mask:** Store allowed letters in one integer and test character bits. It is compact and matches the fixed alphabet but less immediately readable to beginners.
- **Search `allowed` directly:** `c in allowed` can scan up to 26 characters for every word character. It remains bounded here but repeats work that preprocessing avoids.
- **Explicit nested loops:** They can maintain a counter and break on the first forbidden character. This is semantically identical to the generator and `all`.
- **Every word consistent:** Every inner `all` returns true, so the result equals `len(words)`.
- **No word consistent:** Every word encounters a forbidden character and the sum remains zero.
- **One-character allowed set:** Only words composed entirely of repetitions of that character pass.
- **Repeated characters in a word:** Each occurrence is checked, but repetition is allowed and does not make a word inconsistent.
- **Distinctness of `allowed`:** Set construction would remove duplicates even without the guarantee, so behavior remains natural.
- **Nonempty words:** The constraints avoid the vacuous-empty-word case; mathematically `all` of an empty generator would be true.
- **Lowercase-only guarantee:** It keeps the lookup universe at 26 and makes the constant-space claim valid.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A+S)$. Let `A = len(allowed)` and define
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
