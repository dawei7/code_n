# Guided Example: Convert Number Words to Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "onefourthree"}`
- **Required output:** `"143"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters. `s` may contain **valid concatenated** English words representing the digits 0 to 9, without spaces.

The objective is to compute `"143"` from `{"s": "onefourthree"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Follow the parsing rule literally from left to right

At source index `i`, the parser asks whether any complete digit word begins exactly there. If one matches, it emits that digit and skips the entire word. If none matches, it advances by exactly one character.

This is not a general word-segmentation problem that may choose among competing decompositions. The contract specifies a deterministic local scan, and the ten valid words are fixed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "onefourthree"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Try the ten digit words

The list `d` stores words in numeric order, so list index `j` is the digit to emit. For each candidate word `t`, the source first verifies `i+len(t)<=n`, preventing a partial suffix from matching.

It then compares `s[i:i+m]` with `t`. On equality, `str(j)` is appended to `ans`.

No two distinct English digit words are identical, so at most one candidate can match a position. The list order does not change successful parsing, but directly supplies the correct numeric mapping.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the index update

On a match of length `m`, the inner branch adds `m-1` to `i` and breaks. The unconditional `i+=1` after the loop makes the net advance exactly `m`.

On a miss, no inner update occurs, so the same unconditional increment advances exactly one character.

This compact structure implements both contract branches without a separate matched flag.

It helps to view `i` as the first unprocessed source position. The loop never moves it backward. It also never leaves it unchanged: a failed position advances by one, while a successful position advances by the matched word's positive length. Therefore every iteration makes progress and the loop must eventually terminate.

For `"onefourthree"`, index zero matches `"one"` and jumps to three, where `"four"` matches, then `"three"`. The result list becomes `["1","4","3"]`.

For `"ninexsix"`, `"nine"` is consumed, `x` fails all ten comparisons and is skipped alone, and `"six"` then matches.

For `"zeero"`, the failed `z` position advances to the first `e`, then each later position is tested independently. No complete `"zero"` occurs, so the result is empty.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"143"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "onefourthree"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"143"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Trie matching:** A trie can share prefix comparisons, but ten words of bounded length make the simple constant scan sufficient.
- **Regular expression extraction:** It may obscure the mandated one-character fallback and overlapping-start semantics.
- **Skip an entire failed fragment:** This can miss a word starting one position later. Failure advances exactly one.
- **Advance only `m-1` total after a match:** The unconditional increment must be included; the source's net movement is `m`.
- **Partial word at the end:** The bounds check rejects it.
- **No matches:** Joining an empty list returns `""`.
- **Back-to-back words:** Consuming one lands exactly at the next word's first character.
- **Noise between words:** Each noise character is skipped separately until a new match begins.
- **Overlapping letter patterns:** Positions inside a successfully consumed word are intentionally unavailable to later matches.
- **An apparent word that begins inside a consumed word:** It is ignored because parsing resumes after the entire successful token.
- **Large input:** The parser is iterative and does not risk recursion depth.
- **Output digits including zero:** `str(0)` appends the character `'0'` normally when `"zero"` matches.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n=len(s)`. At every visited position, at most ten words of maximum length five are compared. Both are fixed constants, so this is $O(1)$ work per position and $O(n)$ total time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
