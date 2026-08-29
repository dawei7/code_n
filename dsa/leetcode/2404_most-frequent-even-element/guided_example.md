# Guided Example: Most Frequent Even Element

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 2, 2, 4, 4, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the most frequent even element*.

The objective is to compute `2` from `{"nums": [0, 1, 2, 2, 4, 4, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter and count only eligible values

Odd values can never be returned, so the Counter is built from a generator that yields only values satisfying `x % 2 == 0`. This includes zero, because zero is divisible by two.

The result `cnt` maps each distinct even value to its frequency in `nums`. Ignoring odds during construction saves unnecessary map entries and makes every later candidate valid by definition.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 2, 2, 4, 4, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track both ranking criteria

The desired ranking has two levels:

1. greater frequency is better;
2. among equal frequencies, smaller numeric value is better.

The source keeps `mx` as the best frequency seen and `ans` as the corresponding value. It updates when:



The first condition handles a new strictly more frequent even value. The second handles a frequency tie and chooses the smaller value.

This explicit comparison is necessary because Counter iteration order reflects first insertion order, not the problem's numeric tie-break.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the initialization encodes the no-even answer

`ans` begins at `-1` and `mx` at zero. Every real Counter frequency is positive, so the first even candidate always satisfies `v > mx` and replaces the sentinel.

If `cnt` is empty, the loop never runs and `ans` remains `-1`, exactly the required result when no even element exists.

The tie clause `ans > x` is not used before a real answer exists because every first candidate wins through frequency. Thus, using negative one as the sentinel does not interfere with smaller-value comparisons among valid nonnegative inputs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 2, 2, 4, 4, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort even values:** Sorting groups equal values but costs $O(n\log n)$ time; hashing counts in expected linear time.
- **Frequency array:** Values are bounded by `10^5`, so a fixed count array is possible. It uses domain-sized space and can scan even indices in ascending order.
- **Counter all values then filter:** Correct but stores irrelevant odd keys.
- **No even values:** The empty loop leaves the answer at `-1`.
- **Only one even value:** It wins regardless of how many odd values appear.
- **Frequency tie:** The explicit numeric comparison selects the smaller even value.
- **Zero:** It is even and can be returned.
- **Separated occurrences:** Counter combines them globally.
- **Arbitrary Counter iteration order:** Correctness does not depend on it because both ranking criteria are checked explicitly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length and $u$ the number of distinct even values. The generator inspects every input once, and expected Counter updates take $O(1)$ each. Building counts costs expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
