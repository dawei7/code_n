# Guided Example: Word Pattern II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"pattern": "abab", "s": "redblueredblue"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `pattern` and a string `s`, return `true`* if *`s`* **matches** the *`pattern`*.*

The objective is to compute `true` from `{"pattern": "abab", "s": "redblueredblue"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The unknown word boundaries require backtracking

Each pattern character must map to a nonempty substring, but the input does not say how long that substring is. For pattern `"abab"` and target `"redblueredblue"`, the successful boundaries are `red | blue | red | blue`, yet the first `a` could initially be tried as `"r"`, `"re"`, `"red"`, or many longer prefixes.

The algorithm must explore possible substring boundaries and abandon a choice when later pattern positions become inconsistent. That is a backtracking search.

The exact helper `dfs(i, j)` means that pattern positions before `i` have already expanded to exactly the target prefix before index `j`. Its task is to decide whether `pattern[i:]` can expand to `s[j:]` under the current mapping.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"pattern": "abab", "s": "redblueredblue"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store both sides of the bijection constraint

Dictionary `d` maps an assigned pattern character to its chosen substring. This enforces the function property: once character `a` maps to `"red"`, every later `a` must use exactly `"red"`.

Set `vis` stores every substring already assigned to some character. A new pattern character may use candidate `t` only when `t not in vis`. This enforces injectivity: two different characters cannot map to the same substring.

Together, the character-to-substring map and used-substring set enforce a bijection between the pattern characters that occur and their assigned target substrings.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Base cases require both suffixes to finish together

If `i == m` and `j == n`, both the pattern and target have been consumed exactly, so the current mapping is a complete match and the helper returns true.

If only one index reaches its end, the branch returns false. A finished pattern cannot explain leftover target characters, and a finished target cannot supply the nonempty substring required by remaining pattern positions.

Testing the joint-success case first matters: when both indices reach their ends, it must return true rather than being caught by the one-end failure condition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"pattern": "abab", "s": "redblueredblue"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct jump for mapped characters:** Retrieve the one mapped word, check `s.startswith(word, j)`, and recurse once. This avoids constructing every longer candidate when the character is already assigned and is the main local optimization missing from the exact source.
- **Stronger remaining-length pruning:** Sum the known mapped lengths for remaining pattern occurrences and one for each unknown occurrence. This can cap candidate endpoints much earlier than the source's simple `n - j < m - i` check.
- **Map without a used set:** Incorrect because two pattern characters could receive the same substring, violating bijectivity.
- **Used set without a map:** It cannot force repeated occurrences of one pattern character to reuse the same substring.
- **One-character mappings:** They are valid; the endpoint loop begins at `k = j`.
- **Empty mappings:** They are forbidden and never generated because every slice ends at least one position after `j`.
- **Repeated pattern character:** It must match its stored substring exactly at every occurrence.
- **All pattern characters distinct:** The search partitions `s` into nonempty pairwise-distinct substrings.
- **Pattern longer than target:** The minimum-length prune returns false at the root.
- **Both inputs exhausted:** This is the only successful base case.
- **Target exhausted first:** Remaining pattern positions cannot receive nonempty strings, so the branch fails.
- **Pattern exhausted first:** Unconsumed target characters make the expansion incomplete, so the branch fails.
- **Failed assignment restoration:** Both `d` and `vis` must be restored. Removing only one would leave the two bijection structures inconsistent.
- **Early success:** Because the return value is Boolean rather than all mappings, the source stops at the first valid assignment.
- **Lowercase alphabet:** At most 26 distinct character keys can occur, though repeated positions still determine recursion depth.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot 2^n)$. Let $n$ be the target length and $p$ the pattern length. A complete expansion partitions `s` at some subset of its $n-1$ internal gaps. There are at most $2^{n-1}$ such boundary patterns. Mapping and bijection constraints prune many of them, but exponential exploration remains possible.
- **Auxiliary Space Complexity:** $O(n + p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
