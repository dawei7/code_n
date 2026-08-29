# Guided Example: Find and Replace Pattern

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "pattern": "abb"}`
- **Required output:** `["mee", "aqq"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a list of strings `words` and a string `pattern`, return *a list of* $\text{words}[i]$ *that match* `pattern`. You may return the answer in **any order**.

The objective is to compute `["mee", "aqq"]` from `{"words": ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "pattern": "abb"}` while avoiding redundant calculations and unnecessary overhead.

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

A word matches the pattern when character relationships are identical. Whenever two pattern positions contain the same letter, the corresponding word positions must also contain the same letter. Whenever the pattern positions contain different letters, the corresponding word positions must contain different letters. Together these conditions describe a bijection.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "pattern": "abb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The helper `match(s, t)` compares a candidate word `s` with pattern `t` using two arrays of last-seen positions:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `m1[ord(a)]` stores the latest position where word character `a` appeared.
- `m2[ord(b)]` stores the latest position where pattern character `b` appeared.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["mee", "aqq"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "pattern": "abb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["mee", "aqq"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two dictionaries:** Store pattern-to-word and word-to-pattern mappings explicitly. This is equally correct and often more readable, with $O(L)$ per-check mapping space.
- **Normalize each string:** Replace each character by the index of its first occurrence and compare normalized forms. This also tests the same equality pattern in $O(L)$ time.
- **Only one forward map:** It ensures a pattern letter stays consistent but does not stop two different pattern letters from mapping to the same word letter. A reverse constraint is required.
- **Compare character frequency counts:** Equal multiplicities alone do not preserve positions; strings can have the same counts but different occurrence patterns.
- **One-character pattern:** Every one-character word matches because any single letter can map bijectively to any other.
- **All pattern letters equal:** A matching word must also repeat one identical letter at every position.
- **All pattern letters distinct:** A matching word must have distinct letters at every position.
- **Repeated blocks:** Last-seen positions capture arbitrary recurrence patterns, not merely adjacent duplicates.
- **Equal word and pattern:** Their histories evolve identically and the word matches.
- **Same length guarantee:** Without it, `zip` would ignore an unmatched suffix; a general-purpose helper should compare lengths first.
- **ASCII-sized arrays:** `ord` values for lowercase letters fit within 128. A broader Unicode alphabet would require dictionaries.
- **Any answer order:** The comprehension preserves input order, which is valid even though the problem does not require it.
- **Original words returned:** The output contains the existing strings, not transformed versions or mappings.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(NL)$. Let $N$ be the number of words and $L$ the common word and pattern length. Each match attempt scans $L$ paired characters and performs constant-time array operations.
- **Auxiliary Space Complexity:** $O(N+L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
