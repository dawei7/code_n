# Guided Example: Decode String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "3[a]2[bc]"}`
- **Required output:** `"aaabcbc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an encoded string, return its decoded string.

The objective is to compute `"aaabcbc"` from `{"s": "3[a]2[bc]"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Nested encodings require remembering unfinished outer work

While decoding `3[a2[c]]`, the parser begins the outer repeated section, then encounters another repeated section before the outer one is complete. It must remember both the outer repeat count `3` and the already-decoded text that appeared before that section. A stack is appropriate because the innermost bracket closes first: the most recently opened context is the first one completed.

The exact solution uses two parallel stacks:

- `s1` stores repeat counts for open brackets;
- `s2` stores decoded prefixes that appeared before those brackets.

It also keeps two current values:

- `num` is the repeat count currently being read from consecutive digits;
- `res` is the decoded text at the current nesting level.

Entries at the same index in `s1` and `s2` belong to the same open bracket. Their sizes always match.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "3[a]2[bc]"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reading a multi-digit repeat count

When `c.isdigit()` is true, the update is



Multiplying by ten shifts the previously read decimal digits left by one place, and adding the new digit appends it. For example, reading `1`, then `2`, then `3` changes `num` through `1`, `12`, and `123`.

The code must accumulate digits this way because repeat counts can be larger than nine. Treating each digit as a separate count would decode `12[a]` incorrectly.

The input guarantee says digits occur only as positive repeat counts immediately before `[`. Therefore, `num` never needs to represent a literal digit in the decoded output.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Opening a bracket creates a new frame

On `[`, the number just read applies to the enclosed section. The algorithm pushes `num` onto `s1` and the current `res` onto `s2`.

The saved `res` is the decoded prefix that must appear before the repeated bracket result. For `ab3[c]`, it saves `"ab"`; after decoding `c`, the bracket result will become `"ab" + "c" * 3`.

After pushing, it resets `num, res = 0, ''`. The parser is now inside the new brackets:

- a future number should start fresh, not continue the outer count;
- text inside the brackets should be accumulated independently of the outer prefix.

This is analogous to making a recursive call and storing the caller’s local state, but the stacks make that call state explicit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aaabcbc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "3[a]2[bc]"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aaabcbc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive descent:** Parse until `]`, recursively decode nested contents, and return them to the caller. This mirrors the grammar naturally but uses the language call stack and may face recursion-depth limits. Its string-building costs require the same care as the iterative version.
- **Single character stack:** Push raw input characters; on `]`, pop the inner text and preceding number, expand it, and push the result characters back. This is correct but repeatedly moving individual decoded characters can be less efficient and harder to follow than storing whole prefixes and counts separately.
- **Builder or chunk-list frames:** Store lists of string chunks per frame and join strategically. This reduces repeated immutable-string concatenation and better realizes output-sensitive $O(n+m)$ behavior.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m)$. Let $n$ be the encoded input length, $m$ be the fully decoded output length, and $d$ be maximum bracket nesting depth.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
