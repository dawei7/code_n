# Guided Example: Append Characters to String to Make Subsequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "coaching", "t": "coding"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `t` consisting of only lowercase English letters.

The objective is to compute `4` from `{"s": "coaching", "t": "coding"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only a prefix of the target can be matched before appending

Characters may be appended only after the existing string `s`. Suppose some prefix of `t` can already be selected as a subsequence of `s`. Any remaining target characters can then be appended in their original order, producing a complete subsequence equal to `t`.

The key is to make that matched prefix as long as possible. If the longest prefix of `t` that fits inside `s` has length `j`, then exactly the suffix `t[j:]` remains. Its length is `len(t)-j`, which is the returned answer.

It would not help to match a target segment that skips an earlier target character. A subsequence equal to `t` must produce target characters from left to right. Before target position `j` can be matched, every earlier target position must already have been matched.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "coaching", "t": "coding"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Greedily match the next required character

The variable `j` is the index of the next unmatched character in `t`. It begins at zero, meaning no target characters are matched.

The loop reads each character `c` of `s` from left to right. If `j<n` and `c==t[j]`, that source character is used to match the next required target character and `j` advances. Otherwise, `c` is skipped.

The guard `j<n` is important. Once all of `t` has been matched, `j` equals `n`, and indexing `t[j]` would be outside the string. The loop can safely keep scanning `s` because the guard prevents that access and `j` remains `n`.

For `s="coaching"` and `t="coding"`, the scan matches `c` and then `o`. The next required target character is `d`, which does not appear later in `s`, so `j=2` at the end. The unmatched suffix is `"ding"`, whose length is four.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The variable `j` is the index of the next unmatched characte... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why taking the earliest match is optimal

When the current source character equals the next required target character, using it can never make a later match harder. Choosing the earliest possible position for a target character leaves every later source position available for subsequent target characters.

This can be formalized inductively. After scanning any prefix of `s`, `j` equals the greatest number of initial target characters that can be formed from that source prefix. Initially both lengths are zero. When a new source character arrives, any subsequence either ignores it or uses it as the next character after a previously achievable target prefix. If it equals `t[j]`, extending the current longest prefix increases the optimum by one. If it does not, no longer target prefix can use it as its next required character, so the optimum stays unchanged.

Therefore, after the complete scan, no method can match a longer prefix of `t` inside the original `s`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "coaching", "t": "coding"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit two-pointer loop:** Maintain indices :** - **Explicit two-pointer loop:** Maintain indices into both strings with a `while` loop. It has the same greedy invariant and complexity but requires manually advancing the source index.
- **Next-occurrence lookup:** Preprocess positions of letters and binary-search successive matches. That is useful for many target queries against one fixed `s`, but unnecessary for one query.
- **Dynamic programming:** A general subsequence DP uses far more time or space than needed because only the longest matched target prefix matters.
- **`t` already a subsequence:** `j` reaches `n` and the answer is zero.
- **No first-character match:** `j` remains zero, so all of `t` must be appended.
- **Repeated letters:** Each source position can be used once; advancing only one target position per match handles duplicates correctly.
- **Noncontiguous match:** Skipped source characters are allowed because the requirement is subsequence, not substring.
- **Order mismatch:** Having all target letters in `s` is insufficient if they do not occur in target order.
- **Completed target early:** The `j<n` guard prevents an out-of-range target access during the rest of the source scan.
- **Append-only restriction:** New characters cannot be inserted between existing positions, which is why the unmatched portion must be a suffix of `t`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p)$. Let $p=\lvert s\rvert$ and $q=\lvert t\rvert$. The loop visits every character of `s` once and performs constant work. Reading `len(t)` and computing the difference are constant-time operations in Python. The exact runtime is therefore $O(p)$, which is also within the manifest's looser $O(p+q)$ bound because $O(p)\subseteq O(p+q)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
