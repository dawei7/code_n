# Guided Example: Count Good Triplets

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [3, 0, 1, 1, 9, 7], "a": 7, "b": 2, "c": 3}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to find the number of good triplets.

The objective is to compute `4` from `{"arr": [3, 0, 1, 1, 9, 7], "a": 7, "b": 2, "c": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate exactly the objects the problem asks to count

A good triplet is defined by three indices `i < j < k`, not merely by three values. When equal values occur at different positions, their index combinations are distinct triplets and must be counted separately.

The input length is at most one hundred. That small limit makes complete enumeration practical: there are at most $\binom{100}{3}=161700$ increasing index triples. Testing three constant-time inequalities for each one is easily manageable.

The stored solution therefore uses three nested loops. The outer loop chooses `i` from every array index. The middle loop starts at `i + 1`, so it chooses only positions strictly after `i`. The inner loop starts at `j + 1`, so it chooses only positions strictly after `j`.

Those ranges build `i < j < k` directly. No generated combination has repeated or incorrectly ordered indices.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [3, 0, 1, 1, 9, 7], "a": 7, "b": 2, "c": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every increasing triplet appears once

Take any legal index triple with `i < j < k`. The outer loop eventually reaches its `i`. During that outer iteration, the middle loop reaches its `j` because `j` lies in the range beginning at `i + 1`. During that pair of iterations, the inner loop reaches its `k` because `k` lies after `j`.

So every legal triple is visited. Conversely, the loop bounds ensure every visited triple is legal. A particular triple has only one ordered index representation, so it cannot be counted twice.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Test all three pairwise restrictions

For a visited triple, the expression checks:

- `abs(arr[i] - arr[j]) <= a`.
- `abs(arr[j] - arr[k]) <= b`.
- `abs(arr[i] - arr[k]) <= c`.

Absolute difference measures distance regardless of which value is larger. Each threshold is attached to a different pair; they are not interchangeable. Passing the first two conditions does not imply the third, so all three tests are required.

The `and` operators make the combined expression true only when every restriction holds. Python short-circuits this chain: after a false condition, later conditions need not be evaluated. That can reduce constant work for failing triples but does not change the asymptotic bound.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [3, 0, 1, 1, 9, 7], "a": 7, "b": 2, "c": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix-frequency optimization:** Enumerate `j,k` pairs and query how many earlier values fall in the intersection of two allowed intervals. It can reach $O(N^2+NS)$ with value bound $S$, but needs an $O(S)$ structure and is not the stored source.
- **Fenwick tree with coordinate compression:** It can support prefix value counts more generally, but adds substantial machinery for an input of at most one hundred elements.
- **Sort the array:** Sorting alone is invalid because the original index ordering is part of the triplet definition.
- **Exactly three elements:** There is exactly one candidate triple, which is counted if and only if all conditions hold.
- **Zero thresholds:** A corresponding pair must contain equal values; distinct indices may still have equal array values.
- **Repeated values:** Occurrences at different indices create separate triplets and are intentionally counted separately.
- **Very large thresholds:** More triples may qualify, and if all three restrictions always pass, the answer is $\binom{N}{3}$.
- **One failed restriction:** The triple must not be counted even when the other two comparisons pass.
- **Negative differences:** `abs` removes direction, so value order does not matter.
- **Threshold association:** `a` belongs to the `i,j` pair, `b` to `j,k`, and `c` to `i,k`.
- **Boolean arithmetic:** The direct addition is Python-specific; in a language without numeric Booleans, use an explicit conditional increment.
- **Integer safety:** Python integers do not overflow, and the maximum legal triplet count is small in any case.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^3)$. Let $N$ be `len(arr)`. The exact number of inner iterations is $\binom{N}{3}$ because every three-index subset has one increasing order. Each iteration performs at most three differences, absolute values, comparisons, and Boolean operations, all constant time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
