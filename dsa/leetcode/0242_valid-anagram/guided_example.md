# Guided Example: Valid Anagram

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "anagram", "t": "nagaram"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

The objective is to compute `true` from `{"s": "anagram", "t": "nagaram"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reject unequal lengths first

An anagram is a rearrangement, and rearranging cannot change the number of characters. If `len(s) != len(t)`, the answer is immediately `false`. This check is both a quick rejection and an important part of the later proof: after equal numbers of increments and decrements, a “no count went negative” result is enough to conclude that every count ended at zero.

Without equal lengths, merely checking for negative counts while consuming `t` would handle the case where `t` is longer, but it could wrongly accept a shorter `t`. For example, with `s = "abc"` and `t = "ab"`, no counter becomes negative, yet one unused `c` remains. The initial length comparison rules out that situation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "anagram", "t": "nagaram"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Treat the counter as an inventory

After `cnt = Counter(s)`, `cnt[c]` is the inventory of character `c` supplied by `s`. For every character `c` in `t`, the algorithm performs `cnt[c] -= 1`, meaning one occurrence in `t` has been matched against one occurrence in `s`.

Python's `Counter` returns a zero count for a missing key. Thus, if `t` contains a character absent from `s`, its first decrement changes that implicit zero to `-1`, and the algorithm rejects immediately. No separate “does this key exist?” condition is needed.

More generally, after the first `r` characters of `t` have been processed,

$$
\text{cnt}[c]
=
\operatorname{freq}_s(c)
-
\operatorname{freq}_{t[0:r]}(c).
$$

A negative value means the processed prefix of `t` already contains more copies of `c` than the whole of `s`. Later characters cannot repair that shortage: the loop only subtracts counts and never adds them. Returning `false` at the first negative value is therefore safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After `cnt = Counter(s)`, `cnt[c]` is the inventory of chara... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no final counter scan is necessary

At first, it may seem that the function should verify that all counts are zero after scanning `t`. Equal lengths make that extra scan unnecessary.

Initially, the sum of all counts is `len(s)`. Each of the `len(t)` loop iterations subtracts exactly one from one entry. Since the lengths are equal, the final sum of all counts is zero. The early-exit rule also guarantees that every final count is nonnegative. A collection of nonnegative integers can sum to zero only when every integer is zero. Therefore, if the loop finishes without finding a negative count, every occurrence from `s` was matched exactly once and the function may return `true`.

The same fact can be viewed through contradiction. Suppose a positive count remained for some character from `s`. Because both strings have the same total length, some other character would have to be overused by `t` to compensate. That other counter would become negative, and the loop would already have returned `false`. Hence a leftover positive count cannot coexist with equal lengths and no negative count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "anagram", "t": "nagaram"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fixed 26-entry frequency array:** Map each low:** - **Fixed 26-entry frequency array:** Map each lowercase letter to an index from `0` through `25`, increment for `s`, and decrement for `t`. It avoids hashing and makes the fixed-alphabet $O(1)$ space explicit. This is the manifest's described representation, but not the exact Python source.
- **Sort both strings:** Equal anagrams become identical after sorting, giving a short solution. Sorting costs $O(n\log n)$ time and typically allocates string or character-array storage, so counting is asymptotically faster.
- **Two counters compared for equality:** `Counter(s) == Counter(t)` is conceptually direct and still $O(n)$ expected time. The implemented inventory method needs only one initial counter and can reject as soon as `t` overuses a character.
- **Unequal lengths:** Return `false` before constructing the counter. A longer or shorter string cannot be a rearrangement of the other.
- **A character absent from `s`:** `Counter` treats its prior count as zero; decrementing makes it negative and triggers immediate rejection.
- **Too many copies of an existing character:** The count becomes negative at the first unmatched extra occurrence, so later input need not be inspected.
- **Repeated letters:** Multiplicity is the central reason a Boolean set is insufficient. For example, `aab` and `abb` have the same set of letters but are not anagrams.
- **Identical strings:** Every count is consumed back to zero, so the method correctly returns `true`; no special identity check is needed.
- **Single-character strings:** Equal characters consume one available count and succeed; different characters make a missing key negative and fail.
- **Unicode follow-up:** A hash map or Python `Counter` avoids allocating an enormous fixed table and can count arbitrary code points. If “character” is intended to mean a user-perceived grapheme cluster rather than a Unicode code point, the text would first need appropriate Unicode normalization and grapheme segmentation; that is outside the lowercase-English contract.
- **Case sensitivity:** The allowed input is lowercase. In a broader setting, `A` and `a` are different keys unless the contract explicitly requests case folding.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common string length after the early check. Computing the two lengths is constant time in Python. Constructing `Counter(s)` visits all $n$ characters, and consuming `t` visits at most all $n$ characters. Counter lookup and update are expected $O(1)$ hash-table operations, so total expected running time is $O(n)$. Early rejection may stop the second scan sooner, but the worst case still processes both strings completely.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
