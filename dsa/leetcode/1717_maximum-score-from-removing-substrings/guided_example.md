# Guided Example: Maximum Score From Removing Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "cdbcbbaaabab", "x": 4, "y": 5}`
- **Required output:** `19`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

The objective is to compute `19` from `{"s": "cdbcbbaaabab", "x": 4, "y": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Always give priority to the more valuable pair

The two removable patterns use the same characters in opposite orders. If one pays more, removing it whenever possible is safe. A local conflict can involve a pattern such as `"aba"` or `"bab"`, where choosing one direction prevents the other. Taking the higher-valued direction yields at least as much as taking the lower one, and all nonconflicting pairs can still be removed.

The source normalizes the problem so the high-value pattern is always called `a+b`. Initially `a="a"` and `b="b"`, with score `x` for `"ab"`. If `x < y`, it swaps both scores and both character labels:

`x, y = y, x` and `a, b = b, a`.

Afterward, `x >= y` and removing the ordered pair `a` followed by `b` earns `x`. If the original `"ba"` was more valuable, the labels make that original pattern the normalized `a+b` without reversing or copying the string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "cdbcbbaaabab", "x": 4, "y": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Other letters divide the string into independent segments

Only adjacent `'a'` and `'b'` can ever form a removable pattern. A different character cannot be deleted, so characters on opposite sides of it can never become adjacent. Each maximal segment containing only the two relevant characters can be optimized independently.

The source processes one segment with two counters and flushes it whenever another character appears.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count unmatched high-pattern first characters

`cnt1` counts currently unmatched occurrences of normalized character `a`. When the scan sees `c == a`, it increments `cnt1`. That character might combine with a future `b` into the high-scoring pair, so it should not be committed to a lower pair yet.

When `c == b` and `cnt1 > 0`, an earlier unmatched `a` exists. Removing that `a+b` pair immediately adds `x` and decrements `cnt1`. The current `b` is consumed rather than stored.

This counter behavior is equivalent to a stack removal of every possible high-value pattern, but it stores only counts.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `19` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "cdbcbbaaabab", "x": 4, "y": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `19` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two stack passes:** Remove the higher pair with a stack, then the lower pair from the remainder. It is $O(n)$ time but uses $O(n)$ space.
- **Reverse when `y>x`:** Reversing converts `"ba"` to `"ab"`, but Python allocates an $O(n)$ copy; swapping character roles avoids it.
- **Repeated string replacement:** Searching and rebuilding after each deletion can become quadratic.
- **Equal scores:** Either pair may be prioritized because every removal is worth the same; the source keeps original `"ab"` priority.
- **No `a` or `b` characters:** Every character is a barrier and the result remains zero.
- **Single-character segment:** No pair forms, and the flush contributes zero.
- **Barrier characters:** They are never removed and correctly prevent cross-segment pairing.
- **All one relevant character:** One counter grows, but `min` is zero.
- **Alternating segment:** High pairs are consumed immediately; remaining opposite-order pairs are counted at the flush.
- **Final segment:** The explicit post-loop flush is necessary when the string ends with relevant characters.
- **Score normalization:** After swapping, `x` always means the high score and `y` the low score, regardless of original pattern names.
- **Constant memory:** Counter magnitudes may grow with $n$, but the number of stored integers does not.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. The loop examines every character once and performs constant work. Barrier flushing and the final flush are constant per occurrence, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
