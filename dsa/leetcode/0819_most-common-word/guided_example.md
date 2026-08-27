# Guided Example: Most Common Word

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"paragraph": "a, a, a, a, b,b,b,c, c", "banned": ["a"]}`
- **Required output:** `"b"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `paragraph` and a string array of the banned words `banned`, return *the most frequent word that is not banned*. It is **guaranteed** there is **at least one word** that is not banned, and that the answer is **unique**.

The objective is to compute `"b"` from `{"paragraph": "a, a, a, a, b,b,b,c, c", "banned": ["a"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize before counting

Words are case-insensitive, and punctuation separates words rather than belonging to them. Therefore, `"Ball"`, `"BALL"`, and `"ball,"` must all contribute to the same lowercase key `"ball"`.

The exact solution performs normalization and tokenization in two connected operations:

1. `paragraph.lower()` converts every letter to lowercase.
2. `re.findall('[a-z]+', ...)` extracts every maximal nonempty run of lowercase English letters.

The regular expression `[a-z]+` means “one or more characters from `a` through `z`.” Because `findall` returns nonoverlapping matches from left to right, punctuation and spaces are simply gaps between matches.

For the fragment `"ball, the hit BALL"`, lowercasing yields `"ball, the hit ball"`, and the matches are `"ball"`, `"the"`, `"hit"`, and `"ball"`. The comma is neither retained nor joined to a neighboring word.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"paragraph": "a, a, a, a, b,b,b,c, c", "banned": ["a"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why maximal matches matter

The `+` quantifier makes each match consume the entire consecutive letter run. Without it, the regex could return one character at a time. With it, `"leetcode"` becomes one word rather than eight letters.

The Reference guarantees that paragraph characters are English letters, spaces, or listed punctuation symbols. Thus, `[a-z]+` captures exactly the problem's words after lowercasing. There are no digits or accented letters that need a separate interpretation.

Adjacent punctuation causes no empty words. For example, `"word!!next"` yields `"word"` and `"next"`. Leading or trailing punctuation is also ignored because it does not match the pattern.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The `+` quantifier makes each match consume the entire conse... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count every normalized occurrence

`Counter(...)` receives the list of extracted words and builds a frequency map. Each distinct lowercase word becomes a key, and its value is the number of occurrences in the paragraph.

This stage counts banned and non-banned words alike. That is safe because banning affects eligibility for the answer, not what constitutes an occurrence. Filtering afterward keeps tokenization and frequency counting simple.

For the main example, the counter includes `"hit": 3` and `"ball": 2`. Although `"hit"` has the largest raw frequency, it will be skipped because it belongs to the banned set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"b"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"paragraph": "a, a, a, a, b,b,b,c, c", "banned": ["a"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"b"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Single-pass character buffer:** Scan character:** - **Single-pass character buffer:** Scan characters once, build one lowercase word at a time, and update its count when punctuation is reached. This avoids the regex occurrence list and can update the best word during counting.
- **- **Replace punctuation then split:** Mapping ever:** - **Replace punctuation then split:** Mapping every non-letter to a space and calling `split()` is easy to debug and has the same normalization semantics.
- **- **Scan counter items for a maximum:** Using `max:** - **Scan counter items for a maximum:** Using `max` over only non-banned entries avoids sorting all distinct words, giving the manifest's linear `O(p+b)` time target.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p + b)$. Let `p` be the number of characters in `paragraph`, let `b` be the total number of characters across `banned`, and let `u` be the number of distinct paragraph words.
- **Auxiliary Space Complexity:** $O(p+b+u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
