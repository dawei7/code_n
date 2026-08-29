# Guided Example: Unique Word Abbreviation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"dictionary": ["a", "a"], "words": ["a", "b"]}`
- **Required output:** `[true, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **abbreviation** of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an **abbreviation** of itself.

The objective is to compute `[true, true]` from `{"dictionary": ["a", "a"], "words": ["a", "b"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Preprocess by abbreviation because queries repeat

Each query asks how its abbreviation relates to a fixed dictionary. Scanning every dictionary word for every call would repeat the same grouping work up to 5000 times. The exact solution performs that work once in the constructor.

It builds a mapping `d` from an abbreviation to the set of distinct dictionary words having that abbreviation. A set is important because the dictionary may contain the same word more than once conceptually; repeated copies of one identical word must not be mistaken for different conflicting words.

After preprocessing, a query needs to inspect only the group for its own abbreviation rather than the entire dictionary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"dictionary": ["a", "a"], "words": ["a", "b"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct the abbreviation exactly

For a string of length at least three, `abbr` returns:



The interior count is `len(s) - 2` because the first and last characters are kept literally. Thus:

- `"dog"` has one interior character and becomes `"d1g"`;
- `"internationalization"` has 18 interior characters and becomes `"i18n"`.

For lengths below three, the source returns the original string unchanged. A two-character word has zero interior characters, but the problem defines it as its own abbreviation rather than a form such as `i0t`. A one-character word likewise remains itself.

The decimal count may contain several digits. It is appended as a string, so length 12 uses interior count `10`, not a single encoded character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Group distinct words, not dictionary occurrences

For every dictionary word `s`, the constructor computes `abbr(s)` and executes `d[abbr].add(s)`. The `defaultdict(set)` creates an empty set automatically on the first encounter of a new abbreviation.

Suppose the dictionary contains `"deer"` and `"door"`. Both abbreviate to `"d2r"`, so that key maps to the set `{"deer", "door"}`. The set proves the abbreviation is shared by different words.

If the dictionary instead contains `"cake"` twice, both insertions target `"c2e"`, but the set remains `{"cake"}`. The uniqueness rule concerns whether another word conflicts, not how many times the identical word was listed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"dictionary": ["a", "a"], "words": ["a", "b"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sole word or ambiguity marker:** Map an abbreviation to its one owner until a different owner appears, then replace it with a conflict sentinel. This preserves enough information for queries with less retained collision data and matches the manifest summary, but it is not the exact source.
- **Scan the dictionary per query:** Compare the query against every word's length and endpoint characters. It uses little preprocessing space but costs $O(C)$ per query.
- **Map abbreviation to count only:** A count cannot distinguish repeated copies of the same dictionary word from different colliding words, and it cannot confirm that a singleton owner equals the query without another dictionary set.
- **Duplicate identical dictionary entries:** Set insertion deduplicates them, so querying that word remains unique if no different word shares its abbreviation.
- **Query absent but abbreviation present:** The result is false because every stored owner differs from the query.
- **Query present with no conflicting owner:** The bucket is exactly `{word}`, so the result is true.
- **Query present with another owner:** The differing set member makes `all(...)` false.
- **One-character word:** It abbreviates to itself and is grouped by that exact string.
- **Two-character word:** It also remains unchanged, following the explicit definition.
- **Three-character word:** It uses a one-character interior count, such as `dog -> d1g`.
- **Different lengths:** Their numeric interior counts differ, so words with the same endpoints but different lengths normally occupy different keys.
- **Set iteration order:** It is irrelevant to the Boolean result. Short-circuit timing may vary, but a conflicting group always contains a differing member.
- **Lowercase contract:** Stored and queried words are case-sensitive strings; the legal domain uses lowercase only, so no normalization is needed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let $C$ be the total number of characters across dictionary words, let $D$ be the number of dictionary entries, and let $L$ be a query word's length.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
