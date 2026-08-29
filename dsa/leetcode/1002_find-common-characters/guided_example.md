# Guided Example: Find Common Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["bella", "label", "roller"]}`
- **Required output:** `["e", "l", "l"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string array `words`, return *an array of all characters that show up in all strings within the *`words`* (including duplicates)*. You may return the answer in **any order**.

The objective is to compute `["e", "l", "l"]` from `{"words": ["bella", "label", "roller"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat each word as a multiset of characters

The answer must include duplicates. A character appearing once in one word and three times in every other word can appear only once in the result. Therefore, ordinary set intersection is insufficient; the algorithm must intersect occurrence counts.

For each character `c`, the number of copies common to all words is:

`min(count of c in each word)`.

The solution maintains these running minima with Python `Counter` objects.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["bella", "label", "roller"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize candidates from the first word

`cnt = Counter(words[0])`

records the complete frequency of every character in the first word. Before any other word is considered, these are the maximum copies that could possibly be common: the final result can never use a character more often than the first word contains it.

The input guarantees at least one word, so accessing `words[0]` is safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Intersect one word at a time

For current word `w`, `t = Counter(w)` builds its character frequencies. Then, for every character already tracked in `cnt`:

`cnt[c] = min(cnt[c], t[c])`.

If `w` contains fewer copies, the common allowance shrinks. If it contains at least as many, the existing allowance stays. If it does not contain `c` at all, `t[c]` returns zero and the common count becomes zero.

Counts only decrease as more words are processed. Once a character has been shown absent from one word, no later word can make it common again.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["e", "l", "l"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["bella", "label", "roller"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["e", "l", "l"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed arrays of length twenty-six:** Count letters by `ord(c) - ord('a')` and take elementwise minima. This avoids hashing and makes the constant-space bound explicit.
- **Set intersection:** Finds distinct common letters but cannot return duplicate copies, so it is insufficient.
- **Sort every word:** Common characters can be found with several pointers, but sorting costs extra time and mutates or copies the strings' character order.
- **Repeated list removal:** Start with the first word's characters and remove matches while scanning others. It can become quadratic because list search and deletion are linear.
- **One word:** Its full character multiset is common to all supplied words, so the method returns all of its characters.
- **No common character:** Every tracked count falls to zero and `elements()` produces an empty list.
- **Different multiplicities:** The smallest frequency across words controls exactly how many copies are returned.
- **Character absent from the first word:** It is never tracked because it cannot be common to all words.
- **Zero-count keys retained:** They use at most constant alphabet space and are ignored by `elements()`.
- **Output order:** Counter iteration order is irrelevant because any character order is accepted.
- **Input preservation:** Strings and the word list are only read.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
