# Guided Example: Check If String Is a Prefix of Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "iloveleetcode", "words": ["i", "love", "leetcode", "apples"]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` and an array of strings `words`, determine whether `s` is a **prefix string** of `words`.

The objective is to compute `true` from `{"s": "iloveleetcode", "words": ["i", "love", "leetcode", "apples"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid boundary must occur after a complete word

The target must equal the concatenation of the first $k$ whole words for some positive $k$. Its length must therefore equal a cumulative word length at the exact boundary after word $k-1$.

The solution scans `words` in order and maintains `m`, the total length through the current word. After adding `len(w)`:

- if `m < len(s)`, more words are necessary;
- if `m == len(s)`, this is the only possible boundary where the current prefix could equal `s`;
- if `m > len(s)`, the target ends in the middle of the current concatenation and cannot become valid later because all remaining word lengths are positive.

The exact source does not explicitly break on overshoot, but cumulative length can never decrease, so equality will never be reached afterward and it ultimately returns false.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "iloveleetcode", "words": ["i", "love", "leetcode", "apples"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compare content only at the matching length

When lengths match, the method constructs `"".join(words[: i + 1])` and compares it with `s`. Equal length alone is insufficient: two different word prefixes can have the same number of characters.

The slice selects exactly the first $i+1$ words, satisfying the prefix requirement. Joining without separators models concatenation.

If the comparison is true, the function returns immediately. If it is false, returning false immediately is also correct: future prefixes are longer because words are nonempty, so no later $k$ can produce a string of target length.

For `s = "iloveleetcode"` and words beginning `"i"`, `"love"`, `"leetcode"`, cumulative length reaches the target after the third word. Their join matches and returns true. If the first word is `"apples"`, the cumulative content already differs; eventually the matching or overshooting length cannot repair the required leading characters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When lengths match, the method constructs `"".join(words[: i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why $k$ is automatically positive

Both `s` and every word are nonempty. The loop tests only after adding at least the first word, so any successful boundary uses `i + 1 >= 1` words. The empty concatenation is never accepted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "iloveleetcode", "words": ["i", "love", "leetcode", "apples"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Streaming comparison:** Walk characters across:** - **Streaming comparison:** Walk characters across words while matching successive positions in `s`, accepting only at a word boundary. This reaches $O(L)$ time and $O(1)$ auxiliary space.
- **Join every prefix:** Rebuilding the concatenation after each word can copy the same characters repeatedly and become quadratic.
- **Join all words once and use `startswith`:** That can identify a character prefix but must still verify that `s` ends at a word boundary.
- **Target shorter than first word:** Cumulative length overshoots immediately, and no valid positive word count exists.
- **Target equals first word:** The first boundary triggers a direct comparison and may return true.
- **Target ends inside a later word:** No cumulative length equals it, so the answer is false even if characters seen so far match.
- **Equal length but different content:** The join comparison rejects it.
- **Words remain after a match:** They do not matter because only some positive prefix is required.
- **Only one equality boundary:** Strictly positive word lengths prevent the cumulative total from equaling `len(s)` twice.
- **Overshoot:** Once `m > n`, later words only increase the gap; continuing the loop is harmless but unnecessary.
- **All words too short in total:** The loop ends with `m < n` and returns false.
- **Nonempty-word guarantee:** It makes cumulative length strictly increase and justifies the one-boundary argument.
- **Exact allocation:** Slicing and joining mean the source is not constant-space despite its small scalar state.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the total number of characters inspected across the relevant word prefix plus the target length.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
