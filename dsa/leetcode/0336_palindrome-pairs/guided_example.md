# Guided Example: Palindrome Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["abcd", "dcba", "lls", "s", "sssll"]}`
- **Required output:** `[[0, 1], [1, 0], [2, 4], [3, 2]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of **unique** strings `words`.

The objective is to compute `[[0, 1], [1, 0], [2, 4], [3, 2]]` from `{"words": ["abcd", "dcba", "lls", "s", "sssll"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Avoid testing every pair by deriving what the partner must be.

For two words to form a palindrome, the characters outside the combined string's center must mirror each other. If one word is longer than the other, part of the longer word must match the complete shorter word in reverse, and the unmatched part of the longer word must itself be a palindrome.

That observation lets the exact source examine every split of one word and look up the only possible matching partner in a dictionary. It never guesses arbitrary second words.

The dictionary `d` maps each complete word to its input index. This gives a direct expected-time lookup from a required partner string to its index. The input strings are unique, so each key maps to exactly one candidate; no list of duplicate indices is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["abcd", "dcba", "lls", "s", "sssll"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Split one current word in every possible place.

For a current word `w` of length $L$, the loop tries `j` from `0` through $L$, inclusive. It defines

- `a = w[:j]`, the prefix before the split;
- `b = w[j:]`, the suffix after the split;
- `ra = a[::-1]`, the reversed prefix;
- `rb = b[::-1]`, the reversed suffix.

Including both endpoints matters. At `j = 0`, `a` is empty and `b` is the whole word. At `j = L`, `a` is the whole word and `b` is empty. Those boundary splits find full reverse-word pairs and pairs involving the empty string.

For each split, the source examines two orientations.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a current word `w` of length $L$, the loop tries `j` fro... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: First orientation: the current word comes first.

Suppose the unmatched suffix `b` is a palindrome, meaning `b == rb`, and suppose the dictionary contains `ra`, the reverse of prefix `a`. Then

$$
w + ra = a + b + \operatorname{reverse}(a).
$$

The outer `a` and `reverse(a)` mirror each other. The middle `b` mirrors itself. Therefore the whole concatenation is a palindrome, and the source appends

`[i, d[ra]]`.

The dictionary membership check appears before the palindrome comparison in the `and` chain. Logically, both are required. The index comparison `d[ra] != i` enforces the contract that a word cannot pair with itself. This is especially important when `w` is itself a palindrome: its reverse may be the same dictionary key, but using the same occurrence twice is forbidden.

For `w = "lls"` split as `a = "ll"` and `b = "s"`, the suffix `s` is a palindrome and `ra = "ll"`. If `ll` were present, `llsll` would be a palindrome. In the actual first example, the useful unequal-length pairing is found from a corresponding split such as `w = "sssll"`, where a palindromic unmatched region surrounds the reverse-matched partner.

At `j = L`, `b` is empty, and the empty string is a palindrome. The first orientation simply asks whether the complete reverse of `w` exists. This handles equal-length reverse pairs such as `bat` followed by `tab`.

At `j = 0`, `ra` is the empty string. If an empty word exists and `w` itself is a palindrome, the source appends `[i, empty_index]`, placing the palindrome before the empty word.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 1], [1, 0], [2, 4], [3, 2]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["abcd", "dcba", "lls", "s", "sssll"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 1], [1, 0], [2, 4], [3, 2]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Reverse trie with palindrome-remainder lists:*:** - **Reverse trie with palindrome-remainder lists:** Insert reversed words and store indices whose unmatched portions are palindromes. Properly preprocessed palindrome information can approach output-sensitive linear work in total characters. This matches the manifest summary but is not the exact source.
- **- **Test all ordered word pairs:** Concatenate and:** - **Test all ordered word pairs:** Concatenate and reverse every pair in $O(N^2K)$ time. The split dictionary method replaces the factor of $N$ partners with $O(K)$ structurally forced lookups per word.
- **- **Precompute palindromic prefixes and suffixes:*:** - **Precompute palindromic prefixes and suffixes:** A table or linear-time palindrome algorithm can avoid repeating slice-reversal comparisons. It adds preprocessing machinery but can reduce the work of deciding which splits have palindromic unmatched pieces.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(SK)$. Let $N$ be the number of words, let $L_i$ be the length of word $i$, let $S=\sum_i L_i$, and let $K=\max_i L_i$. For a word of length $L$, there are $L+1$ splits. Python slicing and reversing create strings whose total length is $O(L)$ per split, and hashing a newly created lookup string can also take $O(L)$. Palindrome equality checks are linear in the compared piece in the worst case. Therefore one word costs $O(L^2)$, and the exact total time is
- **Auxiliary Space Complexity:** $O(S + P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
