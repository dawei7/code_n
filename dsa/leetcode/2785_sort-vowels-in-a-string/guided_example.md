# Guided Example: Sort Vowels in a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "lEetcOde"}`
- **Required output:** `"lEOtcede"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** string `s`, **permute** `s` to get a new string `t` such that:

The objective is to compute `"lEOtcede"` from `{"s": "lEetcOde"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate movable characters from fixed positions

Consonants must stay at their original indices. Vowels may be permuted among only the vowel positions and must appear in nondecreasing ASCII order. The exact solution therefore performs three phases:

1. collect every vowel character;
2. sort that vowel collection;
3. walk the original positions and refill only the vowel slots in sorted order.

Sorting the entire string would move consonants and violate the first requirement. Sorting only the movable characters preserves the fixed layout.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "lEetcOde"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize both uppercase and lowercase vowels

The test `c.lower() in "aeiou"` converts one character to lowercase for classification. It returns true for `A, E, I, O, U` and their lowercase forms, and false for every consonant.

The original character is appended to `vs`, not its lowercase version. Case must be preserved because ASCII ordering distinguishes uppercase and lowercase vowel characters. Lowercasing is used only to answer “is this a vowel?”

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Python character sorting matches ASCII order here

`vs.sort()` orders one-character strings by their Unicode code points. For English ASCII letters, code-point order is ASCII order. All uppercase letters have codes smaller than all lowercase letters, and vowels within each case follow alphabetic order:

`A < E < I < O < U < a < e < i < o < u`.

Thus ordinary Python sorting implements exactly the required nondecreasing ASCII sequence.

For `s = "lEetcOde"`, collected vowels are `["E", "e", "O", "e"]`. Sorting yields `["E", "O", "e", "e"]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"lEOtcede"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "lEetcOde"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"lEOtcede"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count the ten vowel characters:** A fixed frequency table and the order `AEIOUaeiou` yield `O(n)` time and constant counting storage beyond the output. This matches the manifest but not the exact code.
- **Sort the whole string:** It moves consonants and violates the fixed-position requirement.
- **Use lowercase characters in the collected list:** That loses original case and produces the wrong ASCII order.
- **No vowels:** `vs` is empty, no positions are replaced, and joining returns the original string.
- **All vowels:** Every position is refilled, so the result is the fully ASCII-sorted string.
- **One vowel:** Sorting and replacement leave it unchanged.
- **Mixed case:** Uppercase vowels precede lowercase vowels in ASCII even when lowercase alphabetic comparison might suggest another human ordering.
- **Repeated vowels:** Sorting preserves their multiplicities and the refill consumes each copy once.
- **Consonant classification:** Every English letter not among the ten vowel forms remains fixed, including `Y` and `y`.
- **Immutable strings:** The character list is necessary for indexed replacement in Python.
- **Input preservation:** The original string cannot be mutated; the method returns a newly joined string.
- **Manifest mismatch:** Real worst-case time is `O(n log n)` because `vs.sort()` is present.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + v\log v)$. Let `n` be `len(s)` and `v` be the number of vowels. Collecting vowels takes `O(n)` time. Sorting them takes `O(v log v)`. Creating `cs`, scanning it, and joining the result each take `O(n)`. Total time is:
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
