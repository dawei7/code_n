# Guided Example: Longest Balanced Substring I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abbac"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters.

The objective is to compute `4` from `{"s": "abbac"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turning the definition into something that can be checked quickly

A substring is balanced when every distinct character appearing in it has the same frequency. The word “distinct” matters: letters that do not occur in the substring are irrelevant. For example, `"aabb"` is balanced because its two present letters both occur twice, and `"zzz"` is balanced because its only present letter occurs three times. On the other hand, `"aab"` is not balanced because the frequencies are two and one.

The direct way to examine a substring would be to count all its letters and then compare all positive counts. Doing that independently for every pair of endpoints would repeat a large amount of work. The Optimal solution still considers every possible substring, which is acceptable because the input length is at most 1,000, but it reuses the counts while moving the right endpoint and reduces each balance test to one arithmetic equality.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abbac"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Fix the left endpoint and grow the substring

The outer loop chooses `i`, the left endpoint of a possible substring. For this new `i`, the solution creates an empty frequency counter and sets both `mx` and `v` to zero:

- `cnt[c]` is the number of occurrences of character `c` in the current substring `s[i:j + 1]`.
- `mx` is the largest frequency among all characters currently present.
- `v` is the number of distinct characters currently present.

The inner loop advances `j` from `i` to the end of the string. When `s[j]` is appended, only that character's count changes. The code increments `cnt[s[j]]` and updates `mx` with the new count. It increments `v` only when that new count is one, because a count changes to one precisely when this character appears in the current substring for the first time. A second or later occurrence must not increase the number of distinct characters.

This incremental update is the main reuse of work. Once the counts for `s[i:j]` are known, the counts for `s[i:j + 1]` require only one counter increment and two small bookkeeping updates. There is no need to scan the substring again.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer loop chooses `i`, the left endpoint of a possible ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every possible answer is considered

Every nonempty substring has one unique pair of endpoints `(i, j)` with `0 <= i <= j < n`. The outer loop visits every possible `i`, and for each such `i` the inner loop visits every possible `j` at or to its right. Therefore, the balance test is applied to every nonempty substring exactly once.

Whenever the condition is true, the solution updates `ans` with the maximum of its old value and the current length. Because the test is exact and no substring is skipped, `ans` is the greatest length among all balanced substrings after both loops finish.

The initialization `ans = 0` is safe even though a nonempty input always has an answer of at least one. On the first inner-loop iteration, the substring contains a single character, so `mx = 1`, `v = 1`, and its length is one. The condition succeeds and raises `ans` to at least one naturally.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abbac"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recount every substring from scratch:** One co:** - **Recount every substring from scratch:** One could choose `i` and `j`, build a new frequency table for `s[i:j + 1]`, and then test its counts. Recounting costs up to $O(n)$ per substring, producing $O(n^3)$ time. Incrementally extending each fixed-left substring removes that unnecessary factor.
- **Compare the minimum and maximum positive frequencies:** A substring is balanced when its minimum positive count equals its maximum count. This is valid, but scanning the frequency table after every extension adds work and requires care not to include zero counts. The equality `mx * v == length` captures the same fact with the maintained statistics.
- **Prefix counts for all 26 letters:** Prefix-frequency arrays can recover the 26 counts of any substring in constant time relative to `n`, leading to $O(26n^2)=O(n^2)$ time and $O(26n)=O(n)$ space. It is correct, but the running-counter method is simpler and uses less memory.
- **Single-character substrings:** Every one-character substring is balanced because it has one distinct character with frequency one. The code detects these without a special case, which also guarantees a positive answer for every valid nonempty input.
- **A substring containing only one repeated letter:** A run such as `"aaaa"` remains balanced at every extension. Here `v` stays one, `mx` equals the length, and the equality continues to hold.
- **A newly introduced character:** When a letter first appears, its count becomes one and `v` increases. Forgetting this update would make `mx * v` too small and could miss balanced substrings containing that new letter.
- **Repeated appearances of an existing character:** The distinct count must not increase again. The condition `cnt[s[j]] == 1` is checked after incrementing, so `v` changes exactly once per character for each fixed `i`.
- **Maximum frequency never decreases:** While `j` moves right, counts only increase, so keeping `mx` through `max(mx, cnt[s[j]])` is sufficient. A full recomputation of the maximum is unnecessary. A new outer-loop iteration does reset `mx` because it starts a different family of substrings.
- **Letters absent from the substring:** They must not be treated as having frequency zero in the equality. The variable `v` counts only present letters, so the product uses exactly the frequencies relevant to the definition.
- **Overlapping candidate substrings:** Nothing is consumed or marked when a balanced substring is found. The loops continue extending it and later restart at every other left endpoint, so overlapping and nested answers are all considered.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the length of `s`. For a fixed left endpoint `i`, the inner loop performs `n - i` iterations. Summing over all left endpoints gives
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
