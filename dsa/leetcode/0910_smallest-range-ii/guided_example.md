# Guided Example: Smallest Range II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1], "k": 0}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `0` from `{"nums": [1], "k": 0}` while avoiding redundant calculations and unnecessary overhead.

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

Every value must receive either $+k$ or $-k$. After sorting, the key structural fact is that an optimal assignment can be represented by one breakpoint:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1], "k": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- a prefix of smaller values receives $+k$;
- the remaining suffix of larger values receives $-k$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Why crossed signs are unnecessary.** Suppose sorted values $a\le b$ receive $-k$ and $+k$, respectively. Their transformed gap becomes

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1], "k": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all sign assignments:** There are $2^n$ possibilities. The sorted breakpoint theorem reduces them to $n+1$ cases.
- **Greedily move every value toward the original midpoint:** Local choices can miss the best final extremes; testing breakpoints is the proven global method.
- **Reuse Smallest Range I formula:** That problem allows any adjustment in `[-k,k]`, while this one requires exactly `+k` or `-k`. The answers can differ.
- **One value:** Original range is zero and the split loop is empty.
- **`k = 0`:** Every transformed value equals the original, so all candidate scores equal the original range.
- **All values equal:** Assigning different signs may widen the range, while the initial uniform case preserves score zero.
- **Duplicate values:** Sorting and breakpoints treat occurrences independently; any optimal sign boundary is still representable.
- **Negative transformed values:** They are allowed; only the final range matters.
- **Uniform sign choice:** Both all-plus and all-minus preserve the original score and are covered by initial `ans`.
- **Breakpoint extremes:** Use `nums[i - 1]` for the raised prefix maximum and `nums[i]` for the lowered suffix minimum; mixing these indices changes the candidate.
- **Input mutation:** Sort a copy if the caller needs the original order.
- **Any operation at every index:** Unlike Smallest Range I, no element may remain unchanged unless $k=0$; the split assigns a sign to all elements.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. Sorting costs $O(n\log n)$ and the breakpoint scan costs $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
