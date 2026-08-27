# Guided Example: Equal Score Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "adcb"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters.

The objective is to compute `true` from `{"s": "adcb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Converting a character to its score

For lowercase character `c`, the expression:

`ord(c) - ord("a") + 1`

maps:

- `a` to one;
- `b` to two;
- and `z` to 26.

`ord` returns the character's integer code. Lowercase English letters occupy consecutive code points, so subtracting the code for `a` yields a zero-based alphabet position, and adding one gives the required score.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "adcb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initial left and right totals

The source initializes:

`l = 0`

because no character has yet moved into the prefix.

It computes:

`r = sum(ord(c) - ord("a") + 1 for c in s)`

so `r` initially equals the score of the complete string.

At this conceptual moment, the boundary lies before the string. That is not a legal split because the left substring is empty, so the method does not compare `l` and `r` yet.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source initializes:

`l = 0`

because no character has y... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Moving the boundary

The loop visits:

`s[:-1]`

which contains every character except the final one. For current character score `x`:

`l += x`

`r -= x`.

The same score is added to the prefix and removed from the suffix. Therefore:

- `l` becomes the score through the current split index;
- `r` becomes the score of every character after it.

If the two totals match, the source immediately returns true.

For `s = "adcb"`, total score is:

$$
1+4+3+2=10.
$$

After moving `a`, the totals are one and nine. After moving `d`, they are five and five, so the split `"ad" | "cb"` succeeds.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "adcb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recompute both scores at every boundary:** Sum:** - **Recompute both scores at every boundary:** Summing prefix and suffix substrings repeatedly can take $O(n^2)$ time.
- **Prefix-sum array:** It supports constant-time split checks after $O(n)$ preprocessing but uses $O(n)$ storage. Two running totals are simpler.
- **Index-based scan:** Looping over indices zero through $n-2$ avoids `s[:-1]` and achieves the manifest's intended $O(1)$ auxiliary space.
- **Check `2 * l == total`:** This equivalent condition keeps only a prefix and fixed total, also using constant scalar state.
- **Two-character string:** There is one split, and it succeeds exactly when the two character scores match.
- **Odd total score:** Two integer substring scores cannot both equal half an odd total, so no split can succeed.
- **Repeated letters:** Each occurrence contributes separately according to position; equality depends only on summed scores.
- **Early balanced split:** The method returns immediately because existence is all that is requested.
- **Nonempty suffix:** Excluding the last character from the loop prevents testing an illegal empty right substring.
- **Alphabet mapping:** The added one is essential because the contract assigns `a = 1` rather than zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
