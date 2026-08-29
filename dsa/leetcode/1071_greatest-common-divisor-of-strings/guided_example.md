# Guided Example: Greatest Common Divisor of Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"str1": "ABCABC", "str2": "ABC"}`
- **Required output:** `"ABC"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

For two strings `s` and `t`, we say "`t` divides `s`" if and only if $s = t + t + t + ... + t + t$ (i.e., `t` is concatenated with itself one or more times).

The objective is to compute `"ABC"` from `{"str1": "ABCABC", "str2": "ABC"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Any common divisor string must be a prefix

A string `t` divides another string only when repeating `t` one or more times produces the entire other string. The first repetition begins at index zero, so `t` must be a prefix of every string it divides.

Therefore, a common divisor of `str1` and `str2` must be a prefix of `str1`. Its length cannot exceed the shorter input length.

The exact solution uses these facts to enumerate every possible prefix length from longest to shortest. The first prefix that repeats to form both inputs is the greatest common divisor string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"str1": "ABCABC", "str2": "ABC"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test whether one candidate repeats to form a string

The nested helper is:



`a` is a nonempty candidate prefix, and `b` is one input string.

The loop appends complete copies of `a` until the constructed string `c` has length at least `len(b)`. There are then two possibilities:

- If `len(b)` is a multiple of `len(a)` and every repeated block matches, `c == b` and `a` divides `b`.
- If the lengths are incompatible, the last append makes `c` longer than `b`, so equality is false.
- If lengths are compatible but any character pattern differs, the equal-length strings compare unequal.

Thus the final equality simultaneously checks length divisibility and content periodicity.

For candidate `"AB"` and input `"ABABAB"`, `c` grows through `"AB"`, `"ABAB"`, and `"ABABAB"`, then returns true.

For candidate `"ABA"` and input `"ABAB"`, appending twice produces `"ABAABA"`, which is too long and unequal, so the helper returns false.

Because outer candidate lengths start at one or more, `a` is never empty. Otherwise, appending it would make no progress and the loop would not terminate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Try candidate lengths in greatest-first order

The outer loop is:



It begins at the entire shorter-string length, the maximum possible divisor length, and ends at one. Every positive candidate length is visited exactly once in descending order.

For each length:



extracts the length-`i` prefix of `str1`. As argued above, every possible common divisor must appear somewhere in this candidate list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"ABC"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"str1": "ABCABC", "str2": "ABC"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"ABC"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Concatenation compatibility plus numeric GCD:** If the two concatenation orders match, the answer length is `gcd(N, M)`. This is the intended linear-time mathematical solution.
- **Virtual concatenation comparison:** Compare characters of `str1 + str2` and `str2 + str1` by index arithmetic to retain `O(1)` auxiliary space rather than allocating both combined strings.
- **Length divisors only:** Enumerate divisors of `gcd(N, M)` from largest to smallest instead of every length. This reduces candidate count but still needs pattern checks.
- **Direct modular periodicity check:** For a candidate length, verify every character against the corresponding prefix position using modulo, avoiding construction of `c`.
- **Identical strings:** The first candidate is the entire string, both checks succeed, and it is returned.
- **One string divides the other:** The shorter string is tested first and returned when it tiles the longer string.
- **Common smaller base:** Inputs such as `"ABABAB"` and `"ABAB"` reject the full shorter string and eventually return `"AB"`.
- **Compatible lengths but incompatible characters:** Numeric length divisibility alone is insufficient; the helper's full equality rejects the candidate.
- **No shared pattern:** Every candidate fails and the empty string is returned.
- **Single-character common base:** The loop reaches length one and returns it only if both strings consist entirely of that character.
- **Uppercase alphabet:** The reasoning depends only on exact character equality, not on alphabet size.
- **Nonempty inputs:** The constraints make every outer candidate nonempty. The helper would loop forever for an empty `a`, but that state cannot occur.
- **Short-circuit evaluation:** `check(t, str2)` runs only if `t` tiles `str1`, saving work without changing correctness.
- **Output allocation:** Returning `str1[:g]` in an optimized Python solution creates the required output string; output space is normally excluded from auxiliary-space claims.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `N = len(str1)`, `M = len(str2)`, and `L = min(N, M)`.
- **Auxiliary Space Complexity:** $O(N + M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
