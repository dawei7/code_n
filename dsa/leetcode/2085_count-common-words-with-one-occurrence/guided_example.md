# Guided Example: Count Common Words With One Occurrence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words1": ["b", "bb", "bbb"], "words2": ["a", "aa", "aaa"]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two string arrays `words1` and `words2`, return *the number of strings that appear **exactly once** in **each** of the two arrays.*

The objective is to compute `0` from `{"words1": ["b", "bb", "bbb"], "words2": ["a", "aa", "aaa"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The condition requires two independent exact frequencies

A word contributes to the answer only when both of these statements are true:

- it appears exactly once in `words1`;
- it appears exactly once in `words2`.

Being present in both arrays is not enough. A word that occurs twice in either array must be rejected even if it occurs once in the other.

The solution builds `cnt1 = Counter(words1)` and `cnt2 = Counter(words2)`. Each counter maps a word to its complete frequency in one array. Keeping separate counters is essential because combining the arrays would lose which side supplied each occurrence.

For the first example, the relevant frequencies are:

- `"leetcode"` has counts 1 and 1;
- `"amazing"` has counts 1 and 1;
- `"is"` has counts 2 and 1;
- `"as"` has counts 1 and 0.

Only the first two satisfy both exact-equality tests.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words1": ["b", "bb", "bbb"], "words2": ["a", "aa", "aaa"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Inspect only words that occur in the first array

The return expression iterates through `cnt1.items()`. Each pair `w, v` contains a distinct word from `words1` and that word's first-array frequency.

There is no need to iterate over every key in both counters. A word absent from `words1` has first-array frequency zero and cannot possibly appear exactly once in each array. Every possible valid word must therefore already be among `cnt1`'s keys.

For each such word, the expression

`v == 1 and cnt2[w] == 1`

tests the full condition. The first comparison rejects duplicates in `words1`. Only if it is true does Python evaluate the second part because `and` short-circuits. The second comparison then requires exactly one occurrence in `words2`.

When `w` is absent from `cnt2`, a `Counter` lookup returns zero, so the second comparison is false without a separate membership check.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use Boolean values as count contributions

In Python, `true` behaves numerically as 1 and `false` as 0. The generator passed to `sum` therefore contributes one for every word meeting both tests and zero for every other word.

Conceptually, the expression is equivalent to:

- initialize an answer to zero;
- for each distinct word in the first counter, check both frequencies;
- increment the answer only when both are one.

The generator form is compact, but its meaning is still a direct count of qualifying distinct words.

Each word is examined once regardless of how many times it appeared in `words1`. Its frequency `v` already summarizes all those occurrences.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words1": ["b", "bb", "bbb"], "words2": ["a", "aa", "aaa"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Set intersection:** This counts words present at least once in both arrays but loses occurrence counts. It fails whenever a common word is duplicated on either side.
- **Nested scans:** For every word in one array, counting occurrences in both arrays repeatedly can take quadratic time. Counters summarize frequencies once.
- **One combined counter:** A total frequency of two could mean one occurrence in each array or two occurrences in only one array. Separate counters preserve the required source distinction.
- **Filtering unique words into sets:** One can construct a set of words whose count is one in each array and intersect those sets. That is correct but creates additional collections after the counters.
- **Word absent from `words2`:** `cnt2[w]` returns zero, so it does not contribute.
- **Word duplicated only in `words1`:** The first comparison fails, and short-circuit evaluation avoids an unnecessary second-counter lookup.
- **Word duplicated only in `words2`:** The first comparison passes, the second fails, and the word is excluded.
- **Word duplicated in both arrays:** Both exact-once requirements fail; it still contributes zero rather than one.
- **Repeated textual values:** Counter keys use complete string equality, so identical spellings are treated as the same word and their occurrences are accumulated.
- **Arrays with no common words:** Every second-counter lookup is zero and the sum returns zero.
- **One word in each array:** The answer is one when the two strings are equal and zero otherwise.
- **Input preservation:** Counters are new summary structures; neither source array is sorted or changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
