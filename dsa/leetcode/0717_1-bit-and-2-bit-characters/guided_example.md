# Guided Example: 1-bit and 2-bit Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"bits": [1, 0, 0]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We have two special characters:

The objective is to compute `true` from `{"bits": [1, 0, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the encoding rule into a deterministic walk

The input is not an arbitrary stream that may be split into characters in several different ways. Its first unread bit tells us exactly how many bits the next character occupies:

- A leading `0` is a complete one-bit character, so the next unread position is one step later.
- A leading `1` starts a two-bit character. The following bit belongs to that same character, whether it is `0` or `1`, so the next unread position is two steps later.

That observation removes the need for backtracking, dynamic programming, or trying different partitions. Starting at index `0`, there is only one legal move at every character boundary. The exact solution stores the next unread position in `i`. Its update,

`i += bits[i] + 1`,

compactly represents both rules. If `bits[i]` is `0`, the added amount is `1`. If `bits[i]` is `1`, the added amount is `2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"bits": [1, 0, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop stops before the final bit

The question is specifically whether the last bit is a one-bit character. We therefore do not need to decode that bit after reaching it. Instead, the loop processes characters only while `i < n - 1`, where `n - 1` is the final index.

There are two meaningful ways the walk can finish:

- It lands exactly on `n - 1`. Every earlier character has been consumed, and the last bit is now the first unread bit. The input is guaranteed to end in `0`, so that last bit is a valid one-bit character. The answer is `true`.
- It jumps from an earlier `1` to `n`. That jump consumed two bits, and the final bit was the second half of that two-bit character. The answer is `false`.

The return expression `i == n - 1` distinguishes exactly these cases. The pointer cannot stop at some unrelated position beyond `n` under the valid encoding contract: every move is one or two positions, and the final bit is `0`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The question is specifically whether the last bit is a one-b... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The key invariant

At the start of every loop iteration, `i` points to the first bit of the next character, never to the second bit of a two-bit character. This is true initially because index `0` begins the encoded sequence. If the current bit is `0`, advancing once skips precisely that one-bit character. If it is `1`, advancing twice skips precisely the complete two-bit character. Thus the invariant remains true after every update.

This invariant is what makes reading `bits[i]` safe and meaningful. Without it, seeing a `0` would not tell us whether it was a standalone character or the second bit of `10`. Because the walk always arrives at character boundaries, that ambiguity never occurs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"bits": [1, 0, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Count consecutive ones immediately before the :** - **Count consecutive ones immediately before the final zero:** The last zero is standalone exactly when that run of ones has even length. This can also run in `O(n)` time and `O(1)` space, and it may scan backward only through a suffix. The forward parser is usually easier to justify because it follows the encoding definition directly and never depends on deriving a parity rule.
- **- **Dynamic programming over positions:** One coul:** - **Dynamic programming over positions:** One could mark which indices are reachable character boundaries. That is unnecessary because every reachable boundary has only one legal next move; there is no branching to resolve. It would add `O(n)` storage without improving the time bound or clarity.
- **- **Recursive decoding:** Recursively consume one :** - **Recursive decoding:** Recursively consume one or two bits according to the leading bit. This expresses the same deterministic walk but uses up to `O(n)` call-stack space and risks recursion-depth limits on large input.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of bits. Each iteration advances `i` by at least one and never moves it backward. No bit is used as the start of a character more than once, so the loop performs at most `n - 1` iterations. The time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
