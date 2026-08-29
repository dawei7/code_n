# Guided Example: Additive Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "112358"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An **additive number** is a string whose digits can form an **additive sequence**.

The objective is to compute `true` from `{"num": "112358"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerating the first two numbers

Let the complete digit string have length $n$. The outer boundary `i` ranges from 1 through $n-2$, so `num[:i]` is nonempty and at least two digits remain for the second number and a third number.

For each `i`, boundary `j` ranges from `i + 1` through $n-1$. Thus:

- the first term is `num[:i]`;
- the second term is `num[i:j]`;
- the suffix `num[j:]` is nonempty and must contain at least the third term.

These ranges enforce the requirement of at least three numbers. The helper cannot report success merely after choosing two terms because its initial suffix always contains at least one digit.

Every legal placement of the first two boundaries appears in these loops. There is no need to choose later boundaries independently because their numeric values are determined by addition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "112358"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rejecting leading zeros in the chosen first terms

A multi-digit number cannot begin with zero.

If the first number has length greater than one and `num[0] == '0'`, the source breaks the inner loop. Changing `j` cannot repair the first term because its boundary `i` is fixed. For subsequent larger values of `i`, the first term still begins with zero and remains invalid.

If the second number has length greater than one and `num[i] == '0'`, the source continues to the next `j`. The one-digit second value `"0"` is allowed, but extending it to `"01"`, `"012"`, or any other multi-digit zero-prefixed text is not.

After these checks, converting the two slices with `int` gives valid first values `a` and `b`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Meaning of the recursive helper

`dfs(a, b, remaining)` asks whether all digits in `remaining` can continue a sequence whose previous two numeric values are $a$ and $b$.

If `remaining` is empty, every earlier forced term matched and consumed the complete input, so the helper returns `true`.

Otherwise, the required next value is $a+b$. The helper tries each nonempty prefix `remaining[:i]`, converts it to an integer, and compares it with that required value. On equality, it recurses with:

- old second value $b$ as the new first value;
- matched sum $a+b$ as the new second value;
- the suffix after the matched prefix as the new remaining text.

This shifts the additive window from $(a,b)$ to $(b,a+b)$.

If a recursive match eventually consumes everything, success propagates immediately. If no tried prefix leads to complete consumption, the current state returns `false`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "112358"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct forced-sum matching:** Compute `expected = str(a + b)` and require the remaining suffix to start with exactly that text. Then advance by `len(expected)`. This removes the prefix loop, enforces the zero representation automatically, and realizes the intended polynomial verification.
- **Index-based verification:** Keep one original string plus a current offset instead of passing `num[i:]` slices. It avoids retaining copied suffixes and makes space usage closer to the recursion depth.
- **Manual decimal-string addition:** In a language with fixed-width integer overflow, add the two previous terms digit by digit as strings and compare the resulting text. Python integers already grow as needed, so the exact source needs no overflow workaround.
- **Backtrack every boundary:** Choosing a cut or no cut at every digit gap explores exponentially many partitions even when most later values are already forced. Enumerating only the first two cuts is the central reduction.
- **Stop after three matching numbers:** A valid prefix is not enough; every digit of the original string must be consumed.
- **Allow a multi-digit leading zero:** Terms such as `"01"` are invalid even though integer conversion yields 1. The first two loop checks and positive-sum suffix check prevent these cases.
- **All zeros:** Strings such as `"000"` are valid as `0, 0, 0`. Longer all-zero strings are valid as additional one-digit zero terms.
- **`"101"`:** It is valid as `1, 0, 1`; a one-digit zero is allowed.
- **Too-short input:** With fewer than three digits, the boundary ranges generate no candidate pair, so the method returns `false`.
- **Exactly three terms:** The first recursive match may consume the complete suffix and reach the empty base case immediately.
- **A valid prefix plus extra digits:** The recursion eventually fails unless those extra digits equal further forced sums.
- **Large terms:** A term may contain many digits. Python's `int` conversion and addition remain exact, satisfying the overflow follow-up in this environment.
- **First number begins with zero:** Only the one-digit first term zero may be tried; longer first slices are rejected.
- **Second number begins with zero:** Only the one-digit second term zero is legal; longer choices are skipped.
- **At least three numbers:** Because `j < n`, every initial candidate leaves a nonempty suffix that must match at least one sum.
- **Return on first witness:** The problem asks only whether a partition exists, so the source safely stops when any boundary pair succeeds.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^3)$. Let $n$ be the digit-string length. There are $O(n^2)$ choices for the first two boundaries.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
