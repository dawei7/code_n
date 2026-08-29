# Guided Example: Maximum Total Sum of K Selected Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [6, 1, 2, 9], "k": 3, "mul": 2}`
- **Required output:** `26`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and two integers `k` and `mul`.

The objective is to compute `26` from `{"nums": [6, 1, 2, 9], "k": 3, "mul": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the selected elements are the `k` largest values

Every processing coefficient is at least one. Suppose a proposed selection contains value `a` but leaves a larger value `b>a` unselected. Replace `a` with `b` in the same processing position with coefficient `c\ge1`. The total changes by

$$
c(b-a)>0.
$$

Therefore any selection omitting a larger value in favor of a smaller one cannot be optimal. Repeating the exchange leaves exactly the `k` largest array elements.

This argument uses the positivity of the values and coefficients. No selected element ever benefits from being replaced by a smaller positive one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [6, 1, 2, 9], "k": 3, "mul": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why larger selected values should be processed earlier

The selected values must also be assigned to the coefficient sequence. Consider two values `a\ge b` and two processing coefficients `p\ge q`. Pairing them in the same order contributes

$$
ap+bq,
$$

whereas crossing the assignments contributes

$$
aq+bp.
$$

Their difference is

$$
(ap+bq)-(aq+bp)
=(a-b)(p-q)\ge0.
$$

So assigning the larger value to the larger coefficient is never worse. Repeatedly removing inverted pairs proves that descending values paired with descending coefficients maximize the total. This is the two-element form of the rearrangement inequality.

The current multiplier decreases after every step regardless of whether multiplication or ordinary addition is chosen. The coefficient sequence is therefore determined solely by the step number; choosing addition does not preserve the multiplier for later.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the source realizes both decisions

The source calls:



which orders the entire input list in nondecreasing order. It then iterates indices from `n-1` downward for exactly `k` elements, thereby taking the selected values from largest to smallest.

For each selected value, it adds:



The factor `max(1,mul)` chooses multiplication when the current multiplier exceeds one and ordinary addition when it is below one. At one, either permitted action gives the same contribution.

After every selected element, the source executes `mul -= 1`, exactly matching the unconditional decrease in the statement.

For `nums=[6,1,2,9]`, `k=3`, and `mul=2`, the chosen descending values are `9,6,2`. The coefficients are `2,1,1`, so the total is

$$
9\cdot2+6\cdot1+2\cdot1=26.
$$

Once the multiplier reaches one, all remaining coefficients stay one even though the raw multiplier continues through zero and negative values. Their relative processing order no longer changes the total, but descending order remains valid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `26` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [6, 1, 2, 9], "k": 3, "mul": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `26` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Size-`k` min-heap:** Scanning all values while retaining only the largest `k` gives `O(n\log k)` time and `O(k)` space. That matches the manifest description but is not the stored source.
- **Selection algorithm plus partial sort:** One can find the top `k` values in linear expected time and then sort only those `k` values, but the implementation is more involved and still differs from the exact code.
- **Try all subsets and orders:** There are exponentially many selections and up to `k!` orders. Exchange arguments determine both choices directly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n` be the length of `nums`. Python's in-place list sort takes `O(n\log n)` worst-case time. The final loop processes exactly `k` values in `O(k)` time. Since `k\le n`, total time is
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
