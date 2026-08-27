# Guided Example: Check if One String Swap Can Make Strings Equal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s1": "bank", "s2": "kanb"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s1` and `s2` of equal length. A **string swap** is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

The objective is to compute `true` from `{"s1": "bank", "s2": "kanb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A swap can repair only two positions

The strings have equal length, so compare them at matching indices. Positions where `s1[i] == s2[i]` already agree and should remain undisturbed. If one swap is needed, its two chosen indices are the only positions whose characters can move.

This creates exactly three meaningful mismatch counts:

- zero mismatches means the strings are already equal, so using no swap satisfies "at most one";
- exactly two mismatches may be repairable if their characters cross-match;
- one mismatch or more than two mismatches cannot be repaired by one swap.

The protected solution detects these cases in one pass without storing mismatch indices or character-frequency arrays.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s1": "bank", "s2": "kanb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remember the first mismatched pair

The loop visits paired characters `a` from `s1` and `b` from `s2` using `zip(s1, s2)`. Equal pairs require no work. At the first mismatch, the solution increments `cnt` to one and saves `c1 = a` and `c2 = b`.

Suppose the first mismatch is at index $i$, so `c1 = s1[i]` and `c2 = s2[i]`. If a later mismatch occurs at index $j$, swapping indices $i$ and $j$ in `s1` works precisely when

$$
\texttt{s1}[j]=\texttt{s2}[i]
\quad\text{and}\quad
\texttt{s2}[j]=\texttt{s1}[i].
$$

In the loop's local variables, these conditions are `a == c2` and `b == c1`. The solution rejects when their negation, `a != c2 or b != c1`, is true.

This is called a cross-match because the first string's character at one mismatched position must equal the second string's character at the other position, in both directions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop visits paired characters `a` from `s1` and `b` from... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reject impossible mismatch patterns immediately

On every mismatch, `cnt` increases. If it becomes larger than two, one swap cannot repair all affected positions, so the solution returns `false` immediately.

The condition is written with `or`: `cnt > 2 or (...)`. Python evaluates `or` from left to right and stops once the left side is true. Therefore, at a third mismatch the function rejects immediately without needing the saved pair for another comparison.

At the second mismatch, `cnt > 2` is false, so the cross-match test is evaluated. A failed cross-match returns `false`. A successful one means swapping these two positions repairs both mismatches. The assignment `c1, c2 = a, b` still runs after this successful check and replaces the stored pair, but no later mismatch can be accepted: a third mismatch triggers the first rejection condition. Consequently, that reassignment does not alter the final decision.

After the scan, the solution returns `cnt != 1`. This accepts zero mismatches and a successfully cross-matched pair of mismatches, while rejecting the single-mismatch case.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s1": "bank", "s2": "kanb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Store mismatch indices:** Collect at most two :** - **Store mismatch indices:** Collect at most two indices, reject a third, then check crossed characters. This is also $O(n)$ time and $O(1)$ bounded space, but the protected solution stores the first characters directly.
- **Frequency maps plus mismatch count:** Equal 26-letter frequency arrays and exactly two differences are sufficient, yet cross-matching avoids the extra arrays.
- **Sort both strings:** Equal sorted strings prove they are anagrams but do not prove one swap is sufficient; mismatch positions still need checking, and sorting costs $O(n\log n)$.
- **Try every swap:** Testing all index pairs is at least quadratic and unnecessary once the mismatch structure is understood.
- **Zero mismatches:** No operation is allowed by "at most one," so identical strings correctly return `true`.
- **One mismatch:** It cannot be fixed by a swap and is the only mismatch count rejected at the final return.
- **Two cross-matching mismatches:** One exchange repairs both, even when the mismatches are far apart.
- **Two non-cross-matching mismatches:** A swap merely moves the wrong characters and cannot create equality.
- **More than two mismatches:** One swap changes at most two positions, so early rejection is conclusive.
- **Repeated letters:** They cause no ambiguity because only the characters at mismatched indices must cross-match.
- **Length one:** Valid equal one-character strings have zero mismatches; unequal ones have one and are rejected.
- **Swap in either string:** A successful crossed pair can be repaired by swapping those indices in `s1` or symmetrically in `s2`.
- **Same-index swap:** It changes nothing and matters only as an optional interpretation when strings are already equal.
- **Equal-length contract:** Reusing this exact `zip` loop for unequal strings would miss an unmatched suffix and would require an explicit length check.
- **Lowercase alphabet:** The direct comparison logic does not depend on alphabet size; the constraint simply defines valid inputs.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common string length. In the worst case, `zip` supplies all $n$ character pairs and the loop performs constant work for each, so time complexity is $O(n)$. Early rejection can finish sooner but does not change the worst-case bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
