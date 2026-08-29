# Guided Example: Count Valid Word Occurrences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"chunks": ["hello wor", "ld hello"], "queries": ["hello", "world", "wor"]}`
- **Required output:** `[2, 1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `chunks`. Concatenate all strings in `chunks` in order to form a string `s`.

The objective is to compute `[2, 1, 0]` from `{"chunks": ["hello wor", "ld hello"], "queries": ["hello", "world", "wor"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Important defect in the exact source artifact

As currently stored, `solution.py` calls `defaultdict(int)` but has no `from collections import defaultdict` import. The exact file therefore raises `NameError: name 'defaultdict' is not defined` as soon as `countWordOccurrences` reaches that line, even for empty input. The scanning algorithm described below is the algorithm written in the source, and it behaves correctly when `defaultdict` is available, but the missing import means the present Optimal artifact is not executable on its own. This approach records the defect without silently pretending the source contains a fix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"chunks": ["hello wor", "ld hello"], "queries": ["hello", "world", "wor"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count once, answer many queries

The intended source creates `cnt` as a mapping from a complete word to its number of occurrences. It scans the reconstructed string once, increments the mapping for every word it finds, and then answers each query with one lookup. This is better than rescanning the whole string separately for every query.

Two indices control the scan:

- `i` searches for the beginning of the next word;
- `j` advances from that beginning to the first character that does not belong to that word.

The outer loop first checks `s[i] in " -"`. Under the stated alphabet, a character is a lowercase letter, a space, or a hyphen. Thus skipping spaces and hyphens means that every accepted starting position `i` is a lowercase letter. A word can never start with a joiner hyphen because a joiner requires a letter before it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reading the inner-loop condition in plain language

Starting at a letter, the inner loop continues while all of these facts hold:

1. `j` is still inside the string.
2. `s[j]` is not a space.
3. Either `s[j]` is not a hyphen, or it is a hyphen whose next character exists and is neither a space nor a hyphen.

Because the input alphabet contains only lowercase letters, spaces, and hyphens, “the next character is neither a space nor a hyphen” means exactly “the next character is a lowercase letter.” Therefore a hyphen is admitted only when it has a lowercase letter on its right.

The condition does not explicitly inspect the character to the left of the current hyphen, but the structure of the scan already guarantees that side. The word begins at a lowercase letter. To reach a later hyphen without stopping, every earlier character must have been accepted. Two consecutive hyphens cannot both be accepted: at the first hyphen, the next character would be a hyphen, so the scan would stop. Consequently, whenever the inner loop reaches and accepts a hyphen, the preceding accepted character is a lowercase letter. The code's right-side test, combined with how `j` arrived there, enforces both halves of the joiner rule.

Letters pass automatically: they are not spaces, and the parenthesized hyphen restriction is true because the character is not `"-"`. The scan stops at a space, at a trailing hyphen, at a hyphen followed by a space, or at the first hyphen in a consecutive run.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"chunks": ["hello wor", "ld hello"], "queries": ["hello", "world", "wor"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Required source repair:** The exact file needs `from collections import defaultdict`, or an equivalent defined mapping strategy, before the intended algorithm can run. The approach does not apply that repair because only documentation is in scope.
- **Split only on spaces:** This incorrectly keeps leading, trailing, or repeated non-joiner hyphens inside tokens. Hyphen classification depends on adjacent characters and cannot be modeled by spaces alone.
- **Replace every hyphen with a separator:** This breaks valid words such as `"well-known"`, where a hyphen has lowercase letters on both sides.
- **Tokenize each chunk independently:** Chunk boundaries are not separators. Independent scans can split one word or misclassify a hyphen whose neighbor lies in another chunk.
- **Run one scan per query:** That can cost $O(C)$ for each query. Counting all words once reduces the total expected time to $O(C+Q)$.
- **Regular expression matching:** A carefully designed expression can work, but boundary behavior around repeated hyphens is easy to get wrong. The explicit scan makes every accepted and rejected character visible.
- **Leading hyphen:** It is skipped by the outer loop because no word can begin there.
- **Trailing hyphen:** The inner loop stops before it because there is no next lowercase letter; the outer loop then skips it.
- **Consecutive hyphens:** The first cannot be a joiner because its right neighbor is a hyphen. The run acts as separators between surrounding letter sequences.
- **Hyphen next to a space:** It fails the right-neighbor test or is encountered after a word has stopped, so it is excluded from every word.
- **Word spanning chunks:** Joining before scanning correctly treats adjacent letters as continuous and evaluates cross-chunk joiners against the reconstructed neighbors.
- **Repeated queries:** The list comprehension performs a lookup for every query position, preserving repetitions and input order.
- **Absent query:** With the intended default dictionary available, its count is zero; the lookup may also add that query key to the map.
- **Alphabet guarantee:** The test `s[j + 1] not in " -"` treats any other character as letter-like. It is exact only because the contract restricts content to lowercase letters, spaces, and hyphens.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C+Q)$. Let $C$ be the total number of characters across all chunks, and let $Q$ be the total number of characters across all query strings.
- **Auxiliary Space Complexity:** $O(C+Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
