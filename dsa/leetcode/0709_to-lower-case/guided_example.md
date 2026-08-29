# Guided Example: To Lower Case

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "Hello"}`
- **Required output:** `"hello"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the string after replacing every uppercase letter with the same lowercase letter*.

The objective is to compute `"hello"` from `{"s": "Hello"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The relevant ASCII relationship

In ASCII, corresponding uppercase and lowercase English letters differ by `32`:

$$
\operatorname{ord}(\texttt{'a'})
=
\operatorname{ord}(\texttt{'A'})+32.
$$

The same relation holds from `A/a` through `Z/z`.

In binary, the uppercase and lowercase codes differ in the bit whose value is `32 = 2^5`. That bit is zero for an uppercase code and one for its lowercase partner.

For example:

- `'A'` is decimal `65`, binary `1000001`;
- `'a'` is decimal `97`, binary `1100001`.

Setting the value-32 bit changes `65` to `97`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "Hello"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why bitwise OR performs the conversion

For an uppercase character `c`, the expression:

`ord(c) | 32`

sets the `32` bit to one while leaving every other bit unchanged. `chr(...)` then converts the resulting integer code back into a character.

Thus:

`chr(ord(c) | 32)`

is the lowercase partner of an ASCII uppercase letter.

This is not a general conversion that should be applied blindly to every printable character. Setting bit 32 can change punctuation into unrelated symbols. The uppercase test is what makes the operation safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Guarding the bit operation

The conditional expression is:

`chr(ord(c) | 32) if c.isupper() else c`.

Because the input contains only printable ASCII, `c.isupper()` is true exactly for `A` through `Z`. Those are the characters for which the bit relationship is intended.

If the character is lowercase, a digit, a space, or punctuation, the `else` branch returns the original character unchanged.

For lowercase ASCII letters, OR with 32 would happen to leave the code unchanged because that bit is already one, but guarding still expresses the contract accurately and protects nonletters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"hello"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "Hello"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"hello"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Built-in `s.lower()`:** It is concise and correct for the input, but using the ASCII relationship demonstrates the requested conversion mechanics.
- **Add 32 arithmetically:** `chr(ord(c) + 32)` works for guarded ASCII uppercase letters. Bitwise OR makes the specific differing bit explicit.
- **Dictionary mapping:** Map every uppercase letter to its lowercase partner. It remains linear but stores a fixed mapping.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
