# Guided Example: Apply Substitutions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"replacements": [["A", "abc"], ["B", "def"]], "text": "%A%_%B%"}`
- **Required output:** `"abc_def"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a `replacements` mapping and a `text` string that may contain **placeholders** formatted as `%var%`, where each `var` corresponds to a key in the `replacements` mapping. Each replacement value may itself contain **one or more** such **placeholders**. Each **placeholder** is replaced by the value associated with its corresponding replacement key.

The objective is to compute `"abc_def"` from `{"replacements": [["A", "abc"], ["B", "def"]], "text": "%A%_%B%"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Interpret replacement values as recursively expandable text.** The source first creates dictionary `d` from each key to its raw replacement value. It then calls nested function `dfs` on the complete `text`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"replacements": [["A", "abc"], ["B", "def"]], "text": "%A%_%B%"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`dfs(s)` searches for the first percent sign. If none exists, `s` contains no placeholder and is returned unchanged. It then searches for the next percent sign. Under the valid-input guarantee, these two delimiters surround one key. If a closing delimiter is unexpectedly absent, the source conservatively returns the text unchanged.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `dfs(s)` searches for the first percent sign.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The key is extracted with `s[i + 1:j]`. Before inserting its value, the code recursively evaluates `dfs(d[key])` because that replacement may contain further placeholders. The source then concatenates:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abc_def"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"replacements": [["A", "abc"], ["B", "def"]], "text": "%A%_%B%"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abc_def"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Memoize expansion by key:** This matches the m:** - **Memoize expansion by key:** This matches the manifest summary and avoids recomputing shared dependencies, but the protected source does not do it.
- **Topologically expand the dependency graph:** A dependency order can resolve each key once without recursion and detect cycles explicitly.
- **Repeated global string replacement:** Repeatedly scanning all keys and all text may do unnecessary work and requires careful termination logic.
- **Cycle detection:** It is unnecessary only because the input guarantees no cyclic dependencies; the source would otherwise recurse indefinitely.
- **Repeated key occurrence:** Every occurrence is expanded correctly but recomputed independently.
- **Several placeholders in one value:** The first-placeholder split plus suffix recursion expands all of them in left-to-right order.
- **Literal underscores:** They contain no percent signs and are preserved by prefix and suffix slicing.
- **Value without placeholders:** The first `find` returns $-1$, so it is returned immediately.
- **Nested dependencies:** `dfs(d[key])` completes the inner value before inserting it into its caller.
- **Unknown key:** Dictionary lookup would fail, but the statement guarantees every placeholder names a mapped key.
- **Unmatched percent sign:** The source returns the current string unchanged; valid inputs never require this fallback.
- **Output growth:** Branching replacements can make the result much larger than the raw input, so output size must appear in realistic complexity analysis.
- **Input preservation:** The mapping is copied into `d` and the immutable input text is never modified.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L + E)$. Let $R$ be the final output length, $C$ the number of placeholder occurrences visited in the full recursive expansion tree including repeated expansions of the same key, and $D$ the maximum dependency depth. At minimum, producing the answer requires $\Omega(R+C)$ work.
- **Auxiliary Space Complexity:** $O(E + k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
