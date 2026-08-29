# Guided Example: Orderly Queue

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "cba", "k": 1}`
- **Required output:** `"acb"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an integer `k`. You can choose one of the first `k` letters of `s` and append it at the end of the string.

The objective is to compute `"acb"` from `{"s": "cba", "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

The set of reachable strings changes completely depending on whether `k` equals 1 or is at least 2. The solution separates those cases because they have different mathematical behavior.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "cba", "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Case `k == 1`: only rotation is possible.** The only eligible character is the first one. Moving it to the end transforms

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"acb"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "cba", "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"acb"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Booth's minimum-rotation algorithm:** It finds the smallest cyclic rotation in $O(n)$ time, improving the `k == 1` case.
- **Counting sort for lowercase letters:** A 26-entry frequency array can construct the sorted `k > 1` result in $O(n)$ time.
- **Always sort:** Incorrect for `k == 1` because only rotations are reachable.
- **Always test rotations:** Incorrect for `k >= 2` because many non-rotation permutations are reachable.
- **One-character string:** Both branches return the same sole string; no move changes it.
- **`k` equals string length:** Any character can be moved directly, and the general permutation result applies.
- **Duplicate letters:** Several operations may lead to identical strings, but comparing them repeatedly does not alter correctness.
- **Already sorted with `k > 1`:** Sorting returns the input unchanged.
- **Already minimum among rotations:** The initial `ans = s` ensures the original is considered.
- **Exactly $n$ rotations:** The $n$-th returns to the original, so checking the original plus $n-1$ new rotations covers the cycle.
- **Lowercase contract:** Native character sorting matches lexicographic order without locale or case complications.
- **Input immutability:** The local variable `s` is rebound to new rotation strings; the caller's string cannot be mutated.
- **Manifest mismatch:** The exact repeated slicing branch must not be described as $O(n)$ merely because a more advanced minimum-rotation method exists.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n=\lvert s\rvert$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
