# Guided Example: Check If N and Its Double Exist

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [10, 2, 5, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that :

The objective is to compute `true` from `{"arr": [10, 2, 5, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the parity guard is necessary

If `x` is odd, it cannot be exactly twice an integer. Using floor division without checking parity would be wrong. For example, `3 // 2` is one, but three is not twice one. The test `x % 2 == 0` ensures the half lookup is performed only when an exact integer half exists.

The double lookup needs no corresponding guard because multiplying any integer by two remains an integer. Negative values also work. If the pair is negative five and negative ten, encountering either value second triggers one of the two checks.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [10, 2, 5, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why one pass covers every input order

Suppose a valid pair has values `a` and `2a`. Whichever occurrence appears later becomes the current `x`:

- If `a` appears later, `x * 2` finds the earlier `2a`.
- If `2a` appears later, `x // 2` finds the earlier `a` because `2a` is even.

Thus no sorting or second pass is needed. The set contains exactly the distinct values at earlier indices, so the two possible arrival orders are both covered.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Distinct indices and the special role of zero

The current value is added with `s.add(x)` only after the pair checks. Therefore, an element can never match itself during its own iteration. Any match found in `s` came from an earlier, distinct index.

This also handles zero correctly. Numerically, zero is twice zero. On the first zero, the set does not yet contain zero, so neither lookup succeeds; the value is then added. On the second zero, `x * 2` is zero and is already in the set, so the method returns true. Exactly one zero does not produce a false match.

If the loop finishes, every element has been checked against all earlier distinct values in both orientations. Any valid pair would have been detected when its later endpoint was processed. Therefore, returning false after the loop proves that no required pair exists.

The input array is not modified. Duplicate nonzero values alone do not automatically form a pair because `x` generally differs from `2x`; zero is the only value equal to its own double.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [10, 2, 5, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency map:** Count all values first, then check whether each double exists. It is also $O(n)$ expected time and naturally handles zero by requiring its frequency to be at least two.
- **Sorting and binary search:** Sort the array and search for each doubled value. It takes $O(n\log n)$ time and needs careful index handling for zero and duplicates.
- **Brute-force pairs:** Check every pair of distinct indices directly. This uses $O(1)$ extra space but $O(n^2)$ time.
- **Only checking the double:** A one-pass method that checks only `2 * x` misses the order where the smaller value appeared earlier and its double appears later. Both orientations are required.
- **Floor division without parity:** This creates false matches for odd values, such as treating one as half of three.
- **Single zero:** It must not satisfy the condition because two distinct indices are required. Insertion after lookup prevents self-matching.
- **Two zeros:** The second zero finds the first and correctly returns true.
- **Negative pair:** Values such as negative four and negative eight satisfy the same doubling relationship and are handled without a special case.
- **Duplicate nonzero values:** Two copies of five do not form a valid pair with each other because five is not twice five.
- **Values at either order:** The double and exact-half checks make the algorithm independent of which member appears first.
- **Input preservation:** The solution builds a separate set and leaves the original array unchanged.
- **Early return:** Once a matching earlier value is found, no later element can invalidate the pair. Returning immediately is safe and can avoid scanning the rest of the array while preserving the $O(n)$ worst-case bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
