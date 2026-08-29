# Guided Example: Determine if String Halves Are Alike

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "book"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` of even length. Split this string into two halves of equal lengths, and let `a` be the first half and `b` be the second half.

The objective is to compute `true` from `{"s": "book"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare counts without creating the two half strings

Two equal-length halves are alike exactly when

$$
\text{vowels in the first half}
=
\text{vowels in the second half}.
$$

The source does not slice `s` into separate strings. It computes `n = len(s) >> 1`. Shifting a nonnegative integer right by one bit is integer division by two, so `n` is the length of each half. The problem guarantees an even string length, making the split exact.

The first half occupies indices zero through `n - 1`, and the second occupies indices `n` through `2n - 1`. During loop iteration `i`, `s[i]` is the character at offset `i` in the first half and `s[i + n]` is the character at the same offset in the second half.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "book"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a fixed vowel lookup set

`vowels = set('aeiouAEIOU')` creates a set containing all five lowercase and all five uppercase vowels. This exactly matches the definition. Consonants are absent, and uppercase characters are not accidentally treated as lowercase without conversion.

Testing `character in vowels` returns a Boolean. Python Booleans behave numerically as integers: `true` contributes one and `false` contributes zero. The solution uses that fact to update one difference counter instead of maintaining two independent counts.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the difference between the halves

The counter begins at zero. For each paired offset, the source performs

`cnt += s[i] in vowels`

and

`cnt -= s[i + n] in vowels`.

After processing offsets zero through `i`, `cnt` equals the number of vowels seen in the first-half prefix minus the number seen in the equally long second-half prefix.

There are four possible contributions from a paired position:

- If both characters are vowels, one is added and one is subtracted, for a net change of zero.
- If neither is a vowel, both membership tests are false and the change is zero.
- If only the first-half character is a vowel, the difference increases by one.
- If only the second-half character is a vowel, the difference decreases by one.

The counter is allowed to become negative. A negative value simply means the processed part of the second half currently has more vowels. Only the final difference matters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "book"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two separate counters:** Count vowels in each half and compare them. It is equally correct and still $O(N)$ time and $O(1)$ space, but uses two accumulators or two loops.
- **Slice each half:** `s[:n]` and `s[n:]` make the split visually explicit, but Python allocates $O(N)$ total substring storage.
- **Lowercase conversion:** Converting `s.lower()` allows a five-letter vowel set but creates another $O(N)$ string; listing both cases avoids it.
- **Vowel string membership:** Testing against `"aeiouAEIOU"` is also correct. Its ten-character scan is constant-sized, while a set expresses lookup intent.
- **Minimum length two:** The loop runs once and directly compares whether the two characters contribute equal vowel counts.
- **No vowels:** Every contribution is zero, so both halves are alike.
- **Every character a vowel:** Each half contains exactly $N/2$ vowels, so additions and subtractions balance.
- **Unequal vowel positions:** Position correspondence is irrelevant; only the final count difference matters.
- **Repeated vowel:** Every occurrence contributes separately, as required.
- **Uppercase vowels:** They are explicitly present in the lookup set.
- **Uppercase consonants:** They are absent and correctly contribute zero.
- **Even-length guarantee:** It ensures `len(s) >> 1` partitions all characters into two equal halves; odd length would leave the definition ambiguous.
- **Negative intermediate counter:** It is expected and safe; it records a temporary surplus in the second half.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the total length of `s`. The loop runs $N/2$ times and performs two membership checks per iteration, so it inspects all $N$ characters in $O(N)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
