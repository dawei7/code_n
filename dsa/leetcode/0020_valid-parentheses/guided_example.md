# Guided Example: Valid Parentheses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "()"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

The objective is to compute `true` from `{"s": "()"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Validity depends on nesting order, not only on counts

For one bracket type, a counter can track how many opening brackets remain unmatched. With three types, separate counters still cannot represent nesting. For example, `([)]` has balanced counts for both round and square brackets, but it is invalid: after reading `([`, the round closer `)` attempts to close `(` while the more recent `[` is still open.

The rule is therefore last opened, first closed. That is precisely the behavior of a stack. Opening brackets are pushed in left-to-right order, and a closing bracket must match the opening bracket currently at the top.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "()"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store the three complete legal pairs

The implementation creates



Each set member is a complete valid adjacent pair: opener first and closer second. Later, the source forms `stk.pop() + c`; membership in `d` tests both bracket type and order in one operation. A set provides expected $O(1)$ membership testing, and its size is fixed at three.

The string `'({['` is used only as an opening-bracket membership collection. Under the contract, every input character is one of the six bracket characters, so any character not in that string is necessarily one of `')'`, `'}'`, or `']'`. A broader text-validation API would need an explicit policy for non-bracket characters, but this problem does not.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The implementation creates



Each set member is a complete ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain exactly the unmatched opening brackets

The essential invariant is:

> After processing a prefix of `s`, `stk` contains exactly the opening brackets in that prefix that have not yet been closed, in their original order. Its final element is the opening bracket that must be closed next.

The stack is initially empty, which correctly describes the empty prefix. When `c` is an opener, `stk.append(c)` adds a newly unmatched opening bracket. It must appear at the top because any brackets opened earlier surround this new bracket and cannot close until the inner one does.

When `c` is a closer, validity requires two facts: an unmatched opener must exist, and the most recent one must have the same type. The branch



checks both.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "()"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Closer-to-opener dictionary:** Map each closer:** - **Closer-to-opener dictionary:** Map each closer to its expected opener, then compare it with the popped top. This avoids constructing a two-character pair and is equally $O(n)$ time and space.
- **Repeated string replacement:** Repeatedly remove `()`, `[]`, and `{}` until nothing changes. It mirrors eliminating innermost pairs but can repeatedly rescan and rebuild the string, leading to $O(n^2)$ time.
- **One or three counters:** Counts can detect surplus brackets but cannot detect crossing order, so `([)]` defeats this approach.
- **Recursive parsing:** A grammar-based parser can validate nesting, but it adds recursion overhead and may use $O(n)$ call-stack depth without improving the bound.
- **Single character:** Any legal one-character input is either an unmatched opener or closer, so the result is `false`.
- **Starts with a closer:** `not stk` short-circuits immediately and safely rejects it.
- **Ends with an opener:** The scan finishes, but `not stk` is false because the opener remains.
- **Adjacent pairs:** Strings such as `"()[]{}"` repeatedly empty the stack and are valid.
- **Deep nesting:** Strings such as `"{[()]}"` exercise last-in-first-out order and are valid when closing types reverse the opening sequence.
- **Correct counts but wrong order:** `"([)]"` is rejected at the first mismatched closer; balanced totals do not override nesting.
- **Non-bracket characters:** The contract excludes them. In this exact source they would enter the closer branch and be rejected, but that behavior is not intended as a general-purpose filtering policy.
- **Non-empty input guarantee:** The stated input is non-empty. If called with `""`, the exact code would return `true`, which is mathematically consistent with an empty balanced sequence but outside the supplied domain.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
