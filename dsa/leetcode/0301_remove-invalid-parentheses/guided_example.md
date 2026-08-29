# Guided Example: Remove Invalid Parentheses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "()())()"}`
- **Required output:** `["(())()", "()()()"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

The objective is to compute `["(())()", "()()()"]` from `{"s": "()())()"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Computing the unavoidable removals

The first scan uses `l` as the number of unmatched opening parentheses currently available and `r` as the number of unmatched closing parentheses that have already been proven invalid.

- On `(`, increment `l`. This opening parenthesis may match a later closing parenthesis.
- On `)`, if `l > 0`, decrement `l` and match it with one earlier opening parenthesis.
- On `)` when `l == 0`, increment `r`. No earlier unmatched opening exists, and a later opening cannot move backward to match this closing parenthesis.
- On a letter, change neither count.

At the end, `r` is the number of closing parentheses that could not be matched with anything before them. Every valid result must delete that many closing parentheses. The final `l` is the number of opening parentheses for which no later closing parenthesis exists. Every valid result must also delete that many opening parentheses.

These counts are not merely estimates. They are a lower bound because the unmatched parentheses cannot participate in any valid matching, and they are attainable because the scan greedily matched every possible closing parenthesis to a preceding opening one. Keeping those matched pairs and removing the unmatched occurrences produces a valid parenthesis structure. Thus, `l + r` is exactly the minimum number of deletions.

For `s = "()())()"`, the scan finishes with `l = 0` and `r = 1`. There is one excess closing parenthesis and no excess opening parenthesis, so every minimum solution must delete exactly one `)`.

For `s = ")("`, the first character creates `r = 1`, and the final opening parenthesis leaves `l = 1`. Both parentheses must be removed, producing the empty string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "()())()"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of the backtracking state

The recursive function `dfs(i, l, r, lcnt, rcnt, t)` carries six pieces of information:

- `i` is the next input index to process.
- `l` is the number of opening-parenthesis deletions still required.
- `r` is the number of closing-parenthesis deletions still required.
- `lcnt` is the number of opening parentheses kept in `t`.
- `rcnt` is the number of closing parentheses kept in `t`.
- `t` is the output prefix built from already processed characters.

The initial call begins at index zero with the full deletion budgets, no kept parentheses, and an empty output prefix.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The deletion branches

When `s[i]` is `(` and `l > 0`, the source may delete it. The recursive call advances `i`, reduces `l` by one, and leaves the kept counts and `t` unchanged.

When `s[i]` is `)` and `r > 0`, it may similarly be deleted by reducing `r`. The code uses `elif` because one character cannot be both kinds of parenthesis.

There is no deletion branch for a letter: the task permits removing invalid parentheses, not arbitrary letters. There is also no deletion branch once the relevant budget reaches zero. Any extra deletion would exceed the proven minimum, so it cannot belong to an answer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["(())()", "()()()"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "()())()"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["(())()", "()()()"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Mutable character buffer:** Append a kept character, recurse, and pop it afterward. This avoids retaining a separate copied string at each stack level and realizes $O(n)$ non-output backtracking space.
- **Breadth-first deletion search:** Generate all strings after one deletion, then two deletions, stopping at the first level containing valid strings. The first valid level guarantees minimum removals, but deduplicating many intermediate strings can consume substantial memory.
- **Unrestricted keep/delete backtracking:** Try deleting every parenthesis and track the smallest removal count discovered at leaves. It is correct with careful result replacement, but the precomputed budgets prune all branches that delete too few or too many of either type.
- **Validity check only at the end:** It permits large subtrees beneath prefixes that already have more closing than opening parentheses. Prefix pruning rejects those branches immediately.
- **Greedily delete a particular unmatched occurrence:** A scan can determine the number and type of required removals, but choosing only one occurrence may miss other distinct valid strings. Backtracking is still needed to enumerate all answers.
- **Memoizing only `(i, l, r)`:** Two calls with the same index and budgets can have different kept balances and different output prefixes, so that state is insufficient for enumerating exact strings.
- **Adjacent identical parentheses:** Multiple deletion choices may create the same result. The set removes duplicates even though the DFS does not skip equivalent sibling choices explicitly.
- **Already valid input:** Initial budgets are zero. No deletion branch is allowed, every character is kept, and the set contains only the original string.
- **Only letters:** Parenthesis budgets are zero and letters have only keep branches, so the original string is returned unchanged.
- **Only unmatched closing parentheses:** Each one contributes to `r`; exhausting the budget removes them all, leaving any letters and no invalid prefix.
- **Only unmatched opening parentheses:** The final `l` equals their count; minimum validity requires removing all of them.
- **Empty valid result:** Although the input length is at least one, deleting all parentheses may produce `""`, as in `")("`. The empty parenthesis string is valid.
- **Letters between parentheses:** Letters never affect `lcnt` or `rcnt` and are always copied, but their positions relative to kept parentheses remain unchanged.
- **Minimum-removal guarantee:** A valid string formed by deleting additional matched pairs is deliberately excluded because the DFS has no deletion budget beyond `l_0+r_0`.
- **Output order:** The returned list comes from a set and is not sorted. Any order is explicitly accepted.
- **At most 20 parentheses:** The exponential factor depends on $p$, not on all letters in $n$. This constraint keeps the decision space bounded even though the full string may contain 25 characters.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^p\cdot n)$. Let $n$ be the full string length and $p$ the number of parentheses. Letters do not branch, while each parenthesis has at most a keep and a delete choice. Before pruning, there are at most $2^p$ decision patterns. Building prefixes through `t + s[i]` and hashing a completed string can each involve up to $O(n)$ character work. A conservative worst-case time bound is therefore $O(2^p\cdot n)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
