# Guided Example: Sum of Prefix Scores of Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["abc", "ab", "bc", "b"]}`
- **Required output:** `[5, 4, 3, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `words` of size `n` consisting of **non-empty** strings.

The objective is to compute `[5, 4, 3, 2]` from `{"words": ["abc", "ab", "bc", "b"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turning many prefix questions into one shared structure

For every word, the required answer is the sum of the scores of all its non-empty prefixes. The score of a prefix is the number of input words that begin with that prefix. A direct solution could generate every prefix as a separate string, count it in a dictionary, and later look those strings up again. That can work, but repeatedly creating slices such as `word[:i]` copies characters. The solution instead uses a trie, also called a prefix tree, so common prefixes are represented only once and can be followed one character at a time.

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert
$$

be the total number of characters across all input words. The trie contains a root that represents the empty prefix. Moving from a node through the child for a letter extends the represented prefix by that letter. For example, after following the children for `a` and then `b`, the current node represents the prefix `"ab"`. Words that start the same way share these nodes, which is precisely the sharing this problem needs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["abc", "ab", "bc", "b"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What each trie node stores

The `Trie` class has two fields. Its `children` field is a list of 26 positions, one for each lowercase English letter. Character `c` is converted to a zero-based position by `ord(c) - ord("a")`. A missing child is `null`; a present child points to another `Trie` object. This fixed array makes choosing the next edge a constant-time operation.

The `cnt` field records how many inserted words pass through that node. Importantly, the root's count is never used because the empty prefix must not contribute to an answer. Every non-root node corresponds to one non-empty prefix, and its count becomes exactly that prefix's score.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: First pass: insert every word and build the counts

The method creates one root named `trie` and calls `insert` for every word. Inserting begins at the root. For each character, it finds the appropriate child position, creates a node if that path has not appeared before, moves to the child, and increments that child's `cnt`.

The order of the last two actions matters conceptually: the count belongs to the node for the prefix including the current character. Suppose `"abc"` is inserted. The nodes representing `"a"`, `"ab"`, and `"abc"` each receive one increment. If `"ab"` is inserted afterward, the first two nodes receive another increment while the third does not. Their final counts are therefore 2, 2, and 1, exactly the three prefix scores needed for `"abc"`.

Duplicate words are also handled naturally. Inserting the same path again increments every node on it again, because each occurrence is another string in `words`. No terminal marker is needed: the problem asks how many words pass through each prefix, not how many distinct words end at a node.

After all insertions, consider any trie node representing a prefix `p`. A word increments that node if and only if insertion follows every character of `p`. That happens if and only if `p` is a prefix of the word. Consequently, `node.cnt` equals the number of input words having `p` as a prefix. This establishes the central fact on which the second pass relies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 4, 3, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["abc", "ab", "bc", "b"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 4, 3, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dictionary of materialized prefix strings:** Count every slice such as `word[:i]` and then sum the stored counts. It is easy to describe, but constructing and hashing each growing prefix can copy or inspect $O(i)$ characters, making the total work potentially quadratic in word lengths rather than linear in $S$.
- **Dictionary keyed by incremental immutable strings:** Building a prefix one character at a time still creates new Python strings because strings are immutable. A trie avoids those repeated full-prefix objects and compares only the next character.
- **Sparse child dictionaries:** Replacing every 26-slot child array with a dictionary stores only edges that exist. It can use less memory when nodes have few children, at the cost of hashing and larger per-edge overhead. The fixed lowercase alphabet makes the array representation straightforward and predictable.
- **Sorting adjacent words:** Lexicographic sorting can expose shared prefixes between neighbors, but converting those relationships into the score of every prefix requires extra bookkeeping. The trie expresses the needed prefix groups directly.
- **One word:** Every prefix is shared by exactly that one word, so a word of length $m$ receives score $m$. The insert and search passes produce this without a special case.
- **Duplicate words:** Each occurrence must count separately. Repeated insertion increments the same path once per occurrence, so duplicates correctly raise every shared-prefix score.
- **A word that is a prefix of another:** Its complete path is shared with the longer word. No terminal-node logic should stop traversal or prevent the longer word from increasing those counts.
- **Completely different first letters:** Such words immediately occupy different root children and share no non-empty prefix, which is exactly why the root's count is excluded.
- **Maximum lengths:** The total-character bound, rather than only the number of words or maximum individual length, is the right measure because every character is processed twice and can create at most one node.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Using $S$ for the total number of input characters, insertion examines every character once, for $O(S)$ time. Searching examines every character once again, also $O(S)$. Character-to-index conversion, child access, count increments, and additions are constant-time operations, so the combined time is $O(S)$; the factor of two is discarded in asymptotic notation.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
