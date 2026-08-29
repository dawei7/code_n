# Guided Example: Adding Spaces to a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "LeetcodeHelpsMeLearn", "spaces": [8, 13, 15]}`
- **Required output:** `"Leetcode Helps Me Learn"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added. Each space should be inserted **before** the character at the given index.

The objective is to compute `"Leetcode Helps Me Learn"` from `{"s": "LeetcodeHelpsMeLearn", "spaces": [8, 13, 15]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Merge the character stream with the insertion-index stream

The indices in `spaces` are strictly increasing. The string indices are also visited in increasing order by `enumerate(s)`. Two monotonic streams can therefore be merged in one pass.

`j` points to the next unused insertion index. At string index `i`:

- if `j < len(spaces)` and `i == spaces[j]`, append a space and increment `j`;
- append the current character `c`.

Appending the space first implements “insert before the character at that index.”

Strictly increasing insertion indices guarantee at most one space belongs before each character, so one `if` is sufficient rather than a loop.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "LeetcodeHelpsMeLearn", "spaces": [8, 13, 15]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why original indices remain valid

The algorithm compares `spaces` against `i` from the original string, not against positions in the growing output.

Inserted spaces would shift later output positions, but they do not shift the original indices supplied by the problem. Keeping a separate output buffer and enumerating the unchanged input avoids all index-adjustment mistakes.

For `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, `i = 5` still refers to `"Y"` and `i = 9` still refers to `"C"`, regardless of the first space already appended to `ans`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build pieces in a list, then join once

Python strings are immutable. Repeatedly adding to a result string may copy the accumulated prefix many times.

The source appends individual characters and spaces to `ans`, then performs `''.join(ans)` once. The final join allocates the result of length `len(s) + len(spaces)` and copies each collected piece into it.

This makes construction linear in the output size.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Leetcode Helps Me Learn"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "LeetcodeHelpsMeLearn", "spaces": [8, 13, 15]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Leetcode Helps Me Learn"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated string slicing and concatenation:** Inserting one space at a time shifts later positions and can repeatedly copy large strings, leading to quadratic behavior.
- **Build whole string segments:** Appending `s[previous:index]` and a space for each insertion is also linear and may use fewer list elements. The character-wise merge is direct.
- **Use a set of insertion indices:** Membership checks work, but ignore the useful sorted guarantee and require extra $O(m)$ storage.
- **Space before index zero:** The space is appended before the first character correctly.
- **Many consecutive indices:** Each original character receives its own preceding space, producing alternating spaces and characters.
- **Insertion before the last character:** It is encountered normally during the final loop iteration.
- **No insertion after the string:** Such an index is outside the valid domain.
- **Strictly increasing indices:** No duplicate-space handling is needed.
- **Uppercase and lowercase characters:** They are copied unchanged.
- **Original-index semantics:** Inserted output characters never affect `i`.
- **Input preservation:** Neither `s` nor `spaces` is changed.
- **Join once:** Avoids repeated immutable-string copying.
- **Every character retained:** The unconditional `ans.append(c)` ensures insertion never replaces or drops the character at that index.
- **Instruction pointer exhausted:** The bounds test stops reading `spaces[j]` after the final instruction while remaining characters continue normally.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n=\lvert s\rvert$ and $m=\lvert\texttt{spaces}\rvert$.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
