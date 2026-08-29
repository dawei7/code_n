# Guided Example: Maximum Product of Word Lengths

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]}`
- **Required output:** `16`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string array `words`, return *the maximum value of* $length(\text{word}[i]) * length(\text{word}[j])$ *where the two words do not share common letters*. If no such two words exist, return `0`.

The objective is to compute `16` from `{"words": ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Building one word mask

For character `c`, the expression

`ord(c) - ord("a")`

produces an integer from 0 through 25. Shifting 1 left by that amount creates an integer with exactly the corresponding letter bit set:

$$
1\ll(\operatorname{ord}(c)-\operatorname{ord}(a)).
$$

The source combines this bit into `mask[i]` with bitwise OR.

OR is the correct operation because setting a bit that is already one leaves it one. For example, words `"ab"` and `"aabb"` produce the same mask: both contain letters `a` and `b`, and repeated occurrences do not create new letter types.

After every character of `words[i]` is processed, bit $r$ of `mask[i]` is one exactly when the corresponding letter occurs somewhere in that word.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why bitwise AND detects a common letter

For any bit position, AND produces one only when that bit is one in both operands. Therefore,

`mask[i] & mask[j]`

has a set bit exactly for letters appearing in both words.

If the result is zero, no letter bit is shared and the words are compatible. If it is nonzero, at least one common letter exists and the pair must be rejected.

This turns a potentially character-by-character pair comparison into one constant-size integer operation under the fixed 26-letter alphabet.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why prior masks are ready

The outer loop processes words in increasing index order. It fully constructs `mask[i]` before comparing word `i` with earlier words.

For every earlier index `j < i`, `mask[j]` was completed during a previous outer iteration. Hence, both operands of every compatibility test already represent complete letter sets.

The source obtains earlier words through `words[:i]` and enumerates that slice. The enumeration index `j` matches the original index because the slice begins at zero. Variable `t` is the earlier word itself and supplies `len(t)` for the product.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `16` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `16` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Keep only the maximum length per mask:** Map each distinct mask to the longest word having that letter set, then compare mask pairs. Shorter words with the same mask can never produce a better product. This matches the manifest and can reduce practical comparisons.
- **Avoid prefix slices:** Iterate `for j in range(i)` and read `words[j]`. This preserves behavior while avoiding $O(N^2)$ reference-copy work and $O(N)$ temporary slice space.
- **Use character sets per word:** Disjointness can be tested with set intersection, but integer masks are smaller and use one bitwise operation for the fixed alphabet.
- **Compare raw characters:** Rechecking membership for every pair adds dependence on word lengths to the quadratic pair loop.
- **Sort words by length for pruning:** Compare longer words first and stop when remaining possible products cannot exceed `ans`. This can improve practice but requires careful bounds.
- **Repeated letters inside one word:** They set the same bit repeatedly and do not affect compatibility beyond presence.
- **Different words with the same mask:** Every pair between them is incompatible unless the mask were zero; words are nonempty, so their shared mask has at least one bit.
- **Two identical words:** They share every letter and cannot form a legal pair.
- **One-letter disjoint words:** Their masks have different single bits, producing product one.
- **All pairs overlap:** `ans` never changes from zero.
- **Negative or uppercase characters:** They are outside the contract; lowercase ASCII ordering makes the bit positions valid.
- **Maximum word length:** Length affects only the product, not mask size. A thousand repeated characters still use one relevant bit.
- **Exactly two words:** The one possible pair is tested when outer index 1 is processed.
- **No empty words:** Every mask has at least one bit, consistent with the stated minimum word length.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C+N^2)$. Let $N$ be the number of words and
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
