# Guided Example: Expressive Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "heeellooo", "words": ["hello", "hi", "helo"]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Sometimes people repeat letters to represent extra feeling. For example:

The objective is to compute `1` from `{"s": "heeellooo", "words": ["hello", "hi", "helo"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Think in groups, not individual characters

The target string `s` may contain stretched groups such as `"eee"` or `"oooo"`. A query word is stretchy only when extending some of its existing groups can produce exactly `s`. An extension may add copies of the same character to a group, but it cannot change a character, remove a group, insert a completely new character group, or reorder groups.

For example, both `"hello"` and `"heeellooo"` have the same group sequence:

$$
h,\ e,\ l,\ o.
$$

Their group lengths differ, but their group characters appear in the same order. In contrast, `"helo"` has the sequence $h,e,l,o$ too, yet its one-character `l` group cannot become the two-character `ll` group in the target: an extension is allowed only when the resulting target group has length at least three.

This observation suggests comparing one complete run of equal adjacent characters at a time. Comparing characters one by one without knowing the group boundaries makes it difficult to tell whether a repeated target character is a legal stretch or a required original character.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "heeellooo", "words": ["hello", "hi", "helo"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the helper checks

For each query `t`, the nested `check(s, t)` function decides whether `t` can be extended into `s`. Let `m = len(s)` and `n = len(t)`.

The first test rejects `t` when `n > m`. Extension can only add characters, never delete them, so a word longer than the final target cannot possibly become the target. This check is not required for correctness—the later group comparisons would also reject the word—but it avoids unnecessary scanning.

Two pointers, `i` and `j`, identify the first unprocessed character of `s` and `t`. The key meaning maintained by the loop is:

- everything before `i` in `s` and before `j` in `t` has already been divided into matching, legally compatible groups;
- if both pointers are still inside their strings, they must now begin the next corresponding group.

At the start of an iteration, `s[i]` must equal `t[j]`. If the characters differ, the group sequences differ, and no amount of repetition can repair that mismatch. The helper immediately returns `false`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each query `t`, the nested `check(s, t)` function decide... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Measuring the two corresponding runs

Once the leading characters agree, the code advances a temporary pointer `k` from `i` until it reaches either the end of `s` or a different character. The difference `k - i` is the target group length, stored as `c1`. It then moves `i` to `k`, so `i` begins the following target group.

The implementation reuses `k` for the query. After `i, k = k, j`, the new `k` starts at `j`. A second scan advances over all copies of `t[j]`. The difference `k - j` is the query group length, stored as `c2`, and `j` moves past that query group.

At this point, the group characters match, so only their lengths can make the pair invalid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "heeellooo", "words": ["hello", "hi", "helo"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precompute run-length encodings:** Converting :** - **Precompute run-length encodings:** Converting `s` and every query into arrays of character/count pairs makes the comparison explicit and can avoid rescanning the target encoding for each word. It also allocates storage proportional to the encoded input. The two-pointer implementation obtains the same comparisons directly from the strings with constant auxiliary space.
- **- **Character-by-character matching without group :** - **Character-by-character matching without group lengths:** A simple subsequence test is insufficient. It might accept `"helo"` for `"heeellooo"` even though the target's two-character `l` group cannot legally be produced from one `l`.
- **- **Query longer than the target:** It is rejected:** - **Query longer than the target:** It is rejected immediately because the only permitted operation adds characters. Even without the early test, some group would be too long or remain unmatched.

---

## 7. Complexity Derivation

- **Time Complexity:** $O\left(qm+\sum_{r=1}^{q}w_r\right)$. Let `q` be the number of query words, let `m = |s|`, and let `w_r` be the length of query word `r`. For one query, each target character is advanced over at most once and each query character is advanced over at most once. The check therefore takes `O(m + w_r)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
