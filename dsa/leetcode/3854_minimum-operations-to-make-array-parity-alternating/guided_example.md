# Guided Example: Minimum Operations to Make Array Parity Alternating

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-2, -3, 1, 4]}`
- **Required output:** `[2, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `[2, 6]` from `{"nums": [-2, -3, 1, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: There are only two possible target parity patterns

In a parity-alternating array, every adjacent parity differs. Once the desired parity at index zero is chosen, the parity of every later index is forced. The two possibilities are

$$
\text{even},\text{ odd},\text{ even},\ldots
$$

and

$$
\text{odd},\text{ even},\text{ odd},\ldots.
$$

The source represents these patterns with `k` equal to zero or one. For a value `x` at index `i`, the expression `(x - i) & 1` is constant across a correctly alternating pattern. Subtracting `i` flips the required parity at every step: pattern zero requires `x` and `i` to have the same parity, while pattern one requires opposite parity.

This formulation also works for negative integers in Python. Bitwise `& 1` returns zero for an even integer and one for an odd integer, including negative values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-2, -3, 1, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Minimum operations for one fixed pattern

Adding one or subtracting one always flips an integer's parity. Therefore:

- an element that already has its pattern-required parity needs zero operations;
- a mismatching element needs at least one operation; and
- either `x+1` or `x-1` fixes it in exactly one operation.

Consequently, for a fixed pattern, the minimum operation count is simply the number of mismatching indices. The local variable `cnt` counts them.

The global objective is lexicographic: minimize operations first, then minimize range among results using exactly that many operations. Once a pattern's minimum is fixed, every matching element must remain unchanged and every mismatching element must be changed exactly once. Spending an operation on a matching element would make it wrong, and spending additional canceling operations would exceed the minimum count. Thus a mismatching `x` has exactly two relevant final choices, `x-1` and `x+1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Adding one or subtracting one always flips an integer's pari... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Only the extrema need explicit movement choices

Let `mn` and `mx` be the minimum and maximum of the original array. The helper `f(k)` evaluates the smallest range achievable for pattern `k` without enumerating two choices for every mismatch.

If a mismatching value equals `mn`, moving it to `mn-1` can only push the lower boundary outward. Moving it to `mn+1` is never worse and is the source's choice. Similarly, if a mismatching value equals `mx`, moving it to `mx+1` can only expand the upper boundary, so the source moves it to `mx-1`.

A mismatching value strictly between `mn` and `mx` is treated differently: the source leaves its local proxy `x` unchanged while computing extrema. This does not claim that the final value remains `x`; that would have the wrong parity. It is a compact way to represent the fact that one of `x-1` or `x+1` can be chosen without extending the best boundary determined by the outer values.

For an interior integer,

$$
\texttt{mn}<x<\texttt{mx},
$$

both neighbors lie inside the original closed interval:

$$
\texttt{mn}\le x-1<x+1\le\texttt{mx}.
$$

If the attainable proxy interval has positive width and `x` lies at its lower boundary, choose `x+1`; if it lies at its upper boundary, choose `x-1`; if it lies strictly inside, either safe direction may work. The only exceptional geometry is when all proxy values collapse to one integer. A nontrivial alternating array must contain both parities, so its elements cannot all end at one identical value. The minimum attainable range is then one, which the source enforces with `max(1, b - a)`.

The original extrema also explain why an interior proxy cannot hide a better shrink. A surviving matched minimum is fixed at `mn`; otherwise every occurrence of that minimum can rise by only one, so the lower boundary cannot pass `mn+1`. The analogous upper boundary cannot pass `mx-1`. If an interior proxy becomes an endpoint of the computed interval, it is adjacent to one of those unavoidable inward-shifted boundaries, allowing a parity-correct neighbor choice without producing a range larger than the source reports.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-2, -3, 1, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all changed directions:** For a patt:** - **Enumerate all changed directions:** For a pattern with `m` mismatches, trying `x-1` and `x+1` independently takes `2^m` outcomes. The extrema argument reduces those choices to a linear scan.
- **Dynamic programming over minima and maxima:** A DP could track possible boundaries, but the one-step changes and global original extrema make that state unnecessary. Only outward versus inward movement at the boundaries matters.
- **Greedily minimize each final absolute value:** The objective is the collective range, not the magnitude of individual entries. Moving a negative value toward zero, for example, may be irrelevant or harmful compared with moving it toward the current interval.
- **Evaluate only one starting parity:** The lower-operation pattern depends on the input. Both even-first and odd-first targets must be evaluated, and a tie in operations must be broken by range.
- **Interior values left unchanged in the source:** They are proxies for extrema computation, not literal final assignments. Every mismatching interior value still receives exactly one `+1` or `-1` operation in an actual realizing array.
- **All values equal:** For length greater than one, alternating parity requires changing some positions once. The final range can be one, and `max(1, b-a)` prevents the proxy calculation from incorrectly returning zero.
- **Length one:** It needs no operations and has range zero. The early return is necessary because applying the nontrivial lower bound of one would be wrong.
- **Negative odd numbers:** Python's `& 1` parity check remains correct. Replacing it with language-dependent negative remainder logic should be done carefully in other languages.
- **Duplicate global minima or maxima:** Every mismatching occurrence is moved inward; any matching occurrence remains fixed and continues to anchor that boundary. The per-element scan handles the mixture correctly.
- **Already alternating input:** One of the two patterns has zero mismatches. Because zero operations is globally minimum, the original array cannot be changed merely to improve its range; the source returns that pattern's original range.
- **Exactly optimal operation count:** Additional pairs of operations could preserve parity while changing values farther, but they are forbidden by the secondary objective's domain. Only arrays using exactly the minimum count are considered.
- **Lexicographic list comparison:** Python's `min(f(0), f(1))` is intentional. Comparing only the first entries would lose the required minimum-range tie-break.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `N` be the array length. The source computes `min(nums)` and `max(nums)`, each in `O(N)` time, then scans the array once for each of the two patterns. A constant number of linear passes remains `O(N)` total time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
