# Guided Example: One Edit Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "ab", "t": "acb"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `t`, return `true` if they are both one edit distance apart, otherwise return `false`.

The objective is to compute `true` from `{"s": "ab", "t": "acb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Exactly one edit is different from at most one

The method must reject both strings that need two or more changes and strings
that are already equal. An edit is one insertion, one deletion, or one
replacement with a different character. Performing zero edits does not satisfy
the contract.

String lengths immediately restrict the possibilities. A replacement preserves
length. An insertion or deletion changes length by exactly one. Therefore, if
the lengths differ by more than one, the answer is false without examining any
characters.

The selected solution first ensures that `s` is the longer string, or that both
have equal length. If `len(s) < len(t)`, it calls the same method with the
arguments reversed. This is safe because “one edit apart” is symmetric:
inserting into one direction is deleting in the other, and replacement works
both ways. At most one such swap occurs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "ab", "t": "acb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the first position where the strings disagree

After normalization, let `m = len(s)` and `n = len(t)`, with $m \ge n$ and
$m-n \le 1$. The loop enumerates every character of the shorter string `t` and
compares it with `s` at the same index.

Before the first mismatch at index `i`, the prefixes `s[:i]` and `t[:i]` are
identical. Any single permitted edit must therefore explain the mismatch and
leave everything afterward aligned. There is no benefit to editing an earlier
matching position, because that would introduce a difference rather than fix
one.

Once the first mismatch is found, the length relationship uniquely determines
which operation remains possible.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After normalization, let `m = len(s)` and `n = len(t)`, with... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Equal lengths require one replacement

If $m=n$, insertion and deletion would make the final lengths unequal. The only
possible edit is replacing `s[i]` with `t[i]`. Because the characters differ,
that replacement is a real edit rather than replacing a character by itself.

After spending the one allowed edit at `i`, every later character must already
match in the same position. The source tests
`s[i + 1:] == t[i + 1:]`. If the suffixes are equal, exactly one replacement
converts the strings. If they differ anywhere, at least a second edit would be
needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "ab", "t": "acb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-index scan without slicing:** Advance thro:** - **Two-index scan without slicing:** Advance through the common prefix, skip one position according to the length gap, and compare the remainder. It preserves $O(m+n)$ time and achieves $O(1)$ space.
- **Full edit-distance dynamic programming:** Solves a much more general problem in $O(mn)$ time and space, which is unnecessary when only distance exactly one matters.
- **Count mismatches only:** Works for equal-length replacement, but fails for insertion/deletion because later positions are shifted.
- **Equal strings:** Must return false because the requirement is exactly one edit.
- **Length difference above one:** No single allowed operation can bridge it.
- **Mismatch at index zero:** The same suffix rules work without a special case.
- **Extra character at the end:** No mismatch occurs in the shorter prefix; the length check returns true.
- **Both strings empty:** They are zero edits apart and correctly return false.
- **Argument swap:** It occurs at most once and converts insertion reasoning into deletion reasoning.
- **Python slices:** They are a material space cost even though they make the suffix condition concise.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+n)$. Let $m$ and $n$ be the input lengths. The common-prefix scan and at most one
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
