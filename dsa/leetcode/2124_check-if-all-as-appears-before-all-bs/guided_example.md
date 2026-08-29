# Guided Example: Check if All A's Appears Before All B's

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aaabbb"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` consisting of **only** the characters `'a'` and `'b'`, return `true` *if **every** *`'a'` *appears before **every** *`'b'`* in the string*. Otherwise, return `false`.

The objective is to compute `true` from `{"s": "aaabbb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the global ordering rule to one forbidden local pattern

The desired strings have the form

$$
a^p b^q
$$

for some nonnegative counts $p$ and $q$. In plain language, there may be an initial block of `a` characters followed by a block of `b` characters, and either block may be empty.

The ordering fails exactly when an `a` appears somewhere after a `b`. In a binary string, that implies there is an adjacent transition `"ba"` at the point where the string moves from a region containing `b` back to `a`.

The exact solution therefore returns

`"ba" not in s`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aaabbb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an invalid string must contain `ba`

Suppose a `b` occurs before a later `a`. Consider the first `a` that appears after any `b`. The character immediately before this first resumed `a` cannot be `a`, or then that preceding `a` would itself be an earlier resumed `a`. Since the alphabet contains only `a` and `b`, the preceding character must be `b`.

Thus an invalid global ordering always exposes the adjacent substring `ba`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why finding `ba` proves invalidity

If the string contains adjacent characters `b` then `a`, that `a` appears after that `b`. It directly violates the statement that every `a` must occur before every `b`.

The forbidden pattern is therefore both necessary and sufficient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aaabbb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Seen-`b` flag:** Scan left to right and reject an `a` after the flag becomes true. It has the same $O(n)$ time and $O(1)$ space.
- **Sort and compare:** A sorted binary string has all `a` before `b`, but sorting costs more and constructs or mutates data unnecessarily.
- **Find last `a` and first `b`:** The string is valid when one category is absent or the last `a` precedes the first `b`. This is correct but needs more boundary handling.
- **Only `a` characters:** Valid because there are no `b` characters to be preceded.
- **Only `b` characters:** Valid because there are no `a` characters violating the rule.
- **Single character:** Always valid.
- **Exactly `"ab"`:** Valid boundary direction.
- **Exactly `"ba"`:** Minimal invalid case.
- **Several transitions:** Any transition back from `b` to `a` creates the forbidden substring.
- **Binary alphabet:** Essential to the local-pattern equivalence.
- **Vacuous truth:** Missing one character category satisfies the universal statement.
- **Input preservation:** Substring search is read-only.
- **At most one legal block change:** A valid binary string may transition from `a` to `b` once, but never back.
- **Local certificate:** One adjacent `ba` is enough to disprove the universal ordering.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
