# Guided Example: Isomorphic Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "egg", "t": "add"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `t`, *determine if they are isomorphic*.

The objective is to compute `true` from `{"s": "egg", "t": "add"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “replace consistently” into a two-way mapping

For `s` to become `t`, every occurrence of one source character must always
produce the same target character. That requires a function from source
characters to target characters.

The problem also forbids two different source characters from producing the
same target character. That injectivity requirement is easiest to enforce with
the inverse function as well. Dictionary `d1` maps characters from `s` to `t`,
while `d2` maps characters from `t` back to `s`.

Together, the dictionaries maintain a one-to-one correspondence among all
characters encountered so far.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "egg", "t": "add"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read corresponding positions together

`for a, b in zip(s, t)` pairs the character at each source position with the
character at the same target position. Processing left to right automatically
preserves character order: the algorithm never rearranges positions; it only
checks whether every aligned pair can belong to one consistent mapping.

The Reference guarantees `t.length = s.length`, so `zip` visits every character
of both strings. In a generalized function without that guarantee, `zip` would
silently stop at the shorter string, and an explicit length comparison would be
required before the loop.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reject a source character that changes its target

The first conflict test is:

`a in d1 and d1[a] != b`

If source character `a` has appeared before, `d1[a]` records the only target it
is allowed to produce. A different current `b` would require replacing the same
source character in two different ways, contradicting the “all occurrences”
rule.

For `s = "f11"` and `t = "b23"`, the first `'1'` establishes `'1' -> '2'`.
The next `'1'` is aligned with `'3'`, so this condition detects the mismatch
and returns false.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "egg", "t": "add"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **First-occurrence pattern:** Transform each string into the sequence of first-occurrence indices and compare those sequences; correct but builds proportional output.
- **Last-seen arrays:** Two fixed 128-entry arrays can replace dictionaries for strict ASCII input.
- **One dictionary only:** Insufficient because it allows two source characters to share one target.
- **Set of paired characters:** Comparing counts of source, target, and pair sets can work but is less direct than inverse maps.
- **Equal characters:** Self-mapping is explicitly allowed.
- **Repeated source with new target:** Rejected by `d1`.
- **New source with used target:** Rejected by `d2`.
- **Same-length guarantee:** Makes `zip` complete; otherwise compare lengths first.
- **One-character strings:** Always isomorphic because one correspondence suffices.
- **Empty strings:** Outside the minimum-length constraint, but two empty strings would return true naturally.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common string length and $k$ the number of distinct characters
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
