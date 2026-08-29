# Guided Example: Generalized Abbreviation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "a"}`
- **Required output:** `["1", "a"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A word's **generalized abbreviation** can be constructed by taking any number of **non-overlapping** and **non-adjacent** substrings and replacing them with their respective lengths.

The objective is to compute `["1", "a"]` from `{"word": "a"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What a valid abbreviation really chooses.

At every position of `word`, the character is either kept literally or belongs to an abbreviated substring. If several consecutive characters are abbreviated, they must be represented by one number equal to the length of that whole run. Writing two numbers next to each other would represent two adjacent abbreviated substrings, which the definition forbids; those substrings should have been merged into one longer substring instead.

For example, a choice pattern for `abcde` might be:

- keep `a`;
- abbreviate `bc`, producing `2`;
- keep `d`;
- abbreviate `e`, producing `1`.

The result is `a2d1`. The literal `d` separates the two abbreviated runs, so they are non-adjacent. By contrast, abbreviating `ab` and then immediately abbreviating `cde` should not produce `23`; with no kept character between the runs, they form one run of length five and must be written as `5`.

The exact optimal source generates valid results by building this separation rule directly into its recursion. It never creates adjacent number tokens and never needs a later cleanup pass.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "a"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of `dfs(i)`.

Let $n$ be `len(word)`. The helper `dfs(i)` returns every valid abbreviation of the suffix beginning at index `i`, under the condition that index `i` is the next undecided position. Nothing before `i` needs to be reconsidered.

When `i >= n`, the suffix is empty. There is exactly one abbreviation of an empty suffix: the empty string. Returning `['']` is important. It gives callers one neutral suffix to append, allowing a completed prefix to become one full result. Returning an empty list would incorrectly erase every branch that reaches the end because a loop or list comprehension over that list would produce nothing.

For an ordinary index `i`, the helper divides all possibilities into two disjoint groups according to what happens to `word[i]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Group one: keep the current character.

The expression based on `word[i] + s for s in dfs(i + 1)` places `word[i]` literally into every abbreviation of the remaining suffix. Once the current character is kept, index `i + 1` is free to begin either another literal portion or an abbreviated run. This produces every result whose first suffix character remains visible.

For instance, if the current suffix is `cd` and the recursive results for `d` are `d` and `1`, prefixing `c` produces `cd` and `c1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["1", "a"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "a"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["1", "a"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Character-by-character backtracking with a pending count:** At each index, either keep the character or increase a counter for the current abbreviated run. When a character is kept, flush any positive counter before that character. This is a common $O(n2^n)$ method and usually uses only $O(n)$ auxiliary stack space beyond the output. The exact source instead chooses an entire run endpoint at once and forces its separator explicitly.
- **Bitmask enumeration:** Use each integer from `0` through $2^n - 1$ as a keep-or-abbreviate pattern. Scan its bits, count consecutive abbreviated positions, and flush the count before each kept character and at the end. This has the same $O(n2^n)$ time and output space, but constructs each answer independently rather than sharing recursive suffix logic.
- **Memoizing `dfs(i)`:** Caching all suffix result lists avoids recomputing the same index, but the cache itself contains exponentially many strings across suffixes. It can improve constants for this particular recursive structure, yet it cannot improve the asymptotic output bound and may keep more intermediate data alive.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n2^n)$. Let $n$ be the length of `word`. There are exactly $2^n$ abbreviations. Each returned string represents all $n$ source positions and can have $O(n)$ textual length: it may contain many literal characters and number tokens, and constructing it involves string concatenation. The total time complexity is therefore $O(n2^n)$. This bound includes producing the required output, not merely visiting abstract choices.
- **Auxiliary Space Complexity:** $O(n2^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
