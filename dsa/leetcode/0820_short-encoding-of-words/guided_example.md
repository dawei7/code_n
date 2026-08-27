# Guided Example: Short Encoding of Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["time", "me", "bell"]}`
- **Required output:** `10`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **valid encoding** of an array of `words` is any reference string `s` and array of indices `indices` such that:

The objective is to compute `10` from `{"words": ["time", "me", "bell"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A word can share an encoding only as a suffix

In a reference string, a word is read from its starting index up to the next `#`. Suppose `"time#"` occurs in the encoding. Starting at its first character reads `"time"`, while starting two characters later reads `"me"`. Therefore, one stored word automatically encodes all input words that are its suffixes.

This is the only useful sharing relationship. A prefix such as `"tim"` cannot be read from inside `"time#"` through the same terminating `#`, because reading continues through the final `e`. Likewise, a substring in the middle that is not a suffix cannot end at the same delimiter.

The shortest encoding therefore needs one explicit `word#` segment for every distinct input word that is not a suffix of another input word. The answer is the sum of `len(word) + 1` over those maximal words, with one extra character for each `#`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["time", "me", "bell"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reverse words to turn suffixes into prefixes

Suffix comparisons are awkward in an ordinary prefix trie. Reversing every word transforms them into prefix relationships:

- `"time"` becomes `"emit"`;
- `"me"` becomes `"em"`.

Now reversed `"me"` is a prefix of reversed `"time"`. If all reversed words are inserted into one trie, an original word is a suffix of another exactly when its trie path ends at an internal node that continues to at least one child.

An original word that is not a suffix of a longer input ends at a leaf. Thus, only leaf paths contribute explicit segments to the shortest encoding.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suffix comparisons are awkward in an ordinary prefix trie.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The trie node representation

Each `Trie` object contains `children = [null] * 26`. Index 0 represents `a`, index 1 represents `b`, and so on through index 25 for `z`.

For character `c`, the code computes

`idx = ord(c) - ord("a")`.

Because input words contain only lowercase English letters, `idx` is always a valid array position from 0 to 25.

An array of 26 child slots gives constant-time navigation for each letter. A dictionary could store only existing children and use less space for sparse nodes, but the fixed array is simple and predictable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `10` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["time", "me", "bell"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `10` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Set and proper-suffix removal:** Put distinct :** - **Set and proper-suffix removal:** Put distinct words in a set, discard every proper suffix of every word, and sum the survivors' lengths plus one. It is simpler, but generating sliced suffix strings can take `O(\sum |w|^2)` time; word length is small here, while the reversed trie is linear in total characters.
- **- **Sort reversed words:** After reversing and sor:** - **Sort reversed words:** After reversing and sorting, prefix relationships become adjacent and can be detected without a trie. This adds sorting comparisons but can be concise.
- **- **Forward trie:** It groups common prefixes, whi:** - **Forward trie:** It groups common prefixes, which do not provide encoding sharing. Reversal is what aligns the trie structure with suffixes.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
