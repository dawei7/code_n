# Guided Example: Next Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `[1, 3, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

The objective is to compute `[1, 3, 2]` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Change the rightmost possible position

Lexicographic order compares arrays from left to right. To obtain the smallest arrangement that is still greater than the current one, the algorithm should preserve the longest possible prefix. It therefore searches from the right for the first index `i` satisfying



This `i` is the pivot. Everything after it is non-increasing: if an ascent had existed farther right, the reverse scan would have found that position first.

A non-increasing suffix is already the greatest lexicographic arrangement of its own multiset. Rearranging only that suffix cannot make the whole array larger. The pivot is consequently the rightmost position that must change.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read the generator-based pivot search carefully

The exact source uses



`range(n - 2, -1, -1)` visits candidate indices from right to left, ending at zero. The generator yields only indices containing an ascent, and `next` takes the first yielded one. If none exists, the supplied default `-1` is returned instead of raising `StopIteration`.

For a one-element array, the range is empty and `i` is also `-1`, which correctly indicates that no larger permutation exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact source uses



`range(n - 2, -1, -1)` visits candi... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the unusual `if ~i` test

The condition is not a logical negation. `~i` is the bitwise complement, equal to `-i - 1` for Python integers. Therefore:

- when `i == -1`, `~i == 0`, which is false; and
- when `i >= 0`, `~i` is a nonzero negative integer, which is true.

So `if ~i:` is a compact but less beginner-friendly spelling of `if i != -1:`. The swap block runs only when a pivot exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 3, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 3, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-pointer suffix reversal:** Swap suffix end:** - **Two-pointer suffix reversal:** Swap suffix endpoints while moving inward. It preserves $O(n)$ time and achieves genuine $O(1)$ auxiliary space.
- **Sort the suffix:** Correct after the pivot swap but costs $O(n\log n)$ rather than exploiting its known reverse order.
- **Generate all permutations:** Factorial time and large storage are unnecessary.
- **Single element:** No pivot exists; reversing the length-one slice leaves it unchanged.
- **Entirely non-increasing input:** Full reversal wraps to the smallest permutation.
- **Entirely increasing input:** The pivot is the penultimate index, so only the final two values swap.
- **Duplicate values:** Strict pivot and successor comparisons avoid treating equal swaps as an increase.
- **Repeated maximum suffix:** The rightmost greater successor remains the smallest legal replacement.
- **No return value:** The function's result is communicated solely through mutation of `nums`.
- **`~i` readability:** It works because only `-1` and nonnegative indices are possible; `i != -1` would express the intent more directly.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
