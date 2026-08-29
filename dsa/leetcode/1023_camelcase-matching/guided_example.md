# Guided Example: Camelcase Matching

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"queries": ["AbC", "AblueC", "AbcC"], "pattern": "AbC"}`
- **Required output:** `[true, true, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `queries` and a string `pattern`, return a boolean array `answer` where $\text{answer}[i]$ is `true` if $\text{queries}[i]$ matches `pattern`, and `false` otherwise.

The objective is to compute `[true, true, true]` from `{"queries": ["AbC", "AblueC", "AbcC"], "pattern": "AbC"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate insertion into a constrained subsequence test

A query matches the pattern when it can be created by inserting lowercase letters into the pattern. Looking in the opposite direction, the original pattern characters must appear in the query in the same order, and every query character not used for that match must be lowercase.

The first requirement resembles an ordinary subsequence check. The second requirement is the crucial extra rule. An unmatched lowercase letter may be explained as an insertion, but an unmatched uppercase letter cannot. Therefore, the algorithm may skip lowercase query characters while searching for the next pattern character, but it must reject immediately when a different uppercase character blocks the search.

The helper `check(s, t)` treats `s` as one query and `t` as the pattern. The pointer `i` is the next unprocessed position in `s`, while `j` is the next unmatched position in `t`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"queries": ["AbC", "AblueC", "AbcC"], "pattern": "AbC"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the inner loop searches safely

While a pattern character remains, the code runs:

`while i < m and s[i] != t[j] and s[i].islower(): i += 1`.

This skips a query character only when all three facts hold:

- The query still has a character.
- That character does not match the required pattern character.
- The query character is lowercase.

Such a character can legally be one of the lowercase insertions, so discarding it loses no valid match.

The loop stops for one of three reasons. It may find `s[i] == t[j]`, it may reach the end of the query, or it may encounter a mismatching uppercase character. Only the first reason is successful.

The next condition, `if i == m or s[i] != t[j]: return false`, distinguishes those cases. Reaching the end means the required pattern character is absent. A mismatch while still inside the query means the current query character must be uppercase because mismatching lowercase letters would have been skipped. That uppercase letter cannot be inserted, and it does not equal the required pattern character, so no legal alignment can pass it.

When the characters match, `i, j = i + 1, j + 1` consumes both. Pattern characters cannot be reordered or reused, and this simultaneous advance preserves their required left-to-right order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why greedily taking the first match is safe

When `s[i] == t[j]`, the helper immediately pairs them instead of searching for a later copy. This earliest-match choice cannot destroy a solution. A later occurrence would leave the current matching query character unused. If the current character is uppercase, leaving it unused is illegal. If it is lowercase, matching it earlier only leaves a longer suffix in which to match the remaining pattern, never a shorter one.

Thus, among all legal alignments, using the earliest available exact match is always at least as flexible as postponing the match. No backtracking or dynamic programming is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, true, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"queries": ["AbC", "AblueC", "AbcC"], "pattern": "AbC"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, true, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Ordinary subsequence matching:** Checking only whether `pattern` is a subsequence of a query is insufficient because it would skip unmatched uppercase letters. The lowercase-only insertion restriction must be enforced.
- **Delete lowercase letters and compare uppercase skeletons:** Matching the uppercase sequences is necessary but not sufficient when the pattern itself contains lowercase letters. The exact positions and order of every pattern character still matter.
- **Regular expression construction:** One could place a lowercase-letter wildcard around pattern characters, but escaping and anchoring are easy to mishandle, and a two-pointer scan is simpler and strictly linear.
- **Dynamic programming:** A table over query and pattern positions can model skip-or-match choices, but lowercase skips and forced uppercase matches make the greedy earliest-match argument sufficient. DP adds `O(MP)` time or space without benefit.
- **Backtracking over repeated lowercase letters:** Trying every occurrence of a pattern character is unnecessary. Matching the earliest occurrence leaves the largest possible suffix and is always safe.
- **Exact equality:** If query and pattern are identical, every character matches in order, both pointers finish together, and the result is true.
- **All-lowercase additions:** Extra lowercase letters may appear before, between, or after pattern characters. Both loops allow precisely those insertions.
- **Unexpected uppercase before a needed character:** It causes immediate failure even if the needed character appears later, because that uppercase character cannot be explained as an insertion.
- **Unexpected uppercase after the pattern:** The trailing loop stops and returns false, preventing a plain-subsequence false positive.
- **Lowercase pattern characters:** They must be matched exactly and in order. Other lowercase query characters may be skipped around them.
- **Pattern containing uppercase and lowercase:** Character case is part of equality. Lowercase `f` never matches uppercase `F`, and uppercase mismatches cannot be skipped.
- **Repeated characters:** The earliest matching occurrence is consumed. This is safe because pointers only need to preserve order, and earlier consumption leaves at least as much suffix for later pattern characters.
- **One-character pattern:** The method finds that exact character, rejects any blocking uppercase before it, and then requires every remaining query character to be lowercase.
- **Nonempty contract:** Both queries and pattern contain at least one character, so the exact code does not need a special empty-pattern branch. Its trailing logic would still describe the right restriction for an empty pattern: only all-lowercase queries could match.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. For one query of length `M` and a pattern of length `P`, pointer `i` only moves forward and advances at most `M` times. Pointer `j` advances at most `P` times. Neither pointer ever retreats, so the helper takes `O(M + P)` time rather than multiplying the two lengths.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
