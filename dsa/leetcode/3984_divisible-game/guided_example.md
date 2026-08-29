# Guided Example: Divisible Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4, 6, 8]}`
- **Required output:** `36`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `36` from `{"nums": [1, 4, 6, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why a composite `k` never wins the smallest-value tie-break

Suppose composite `k` divides at least one array value. Let `p` be any prime factor of `k`. Then:

$$
k\mid x\implies p\mid x.
$$

Moving from `k` to `p` has this pointwise effect on the signed sequence:

- every value positive under `k` remains positive under `p`;
- some values negative under `k` may become positive under `p`;
- no positive contribution becomes negative.

Since all `nums[i]` are positive:

$$
a_i(p)\ge a_i(k)
$$

for every index. Therefore every fixed subarray has score at least as large under `p` as under `k`, and so:

$$
\operatorname{bestDifference}(p)
\ge
\operatorname{bestDifference}(k).
$$

If the inequality is strict, composite `k` does not achieve the global maximum. If it is an equality, `p<k` gives the same maximum with a smaller choice, so `k` loses the tie-break.

Consequently, the smallest maximizing `k` can be prime whenever it divides some input value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4, 6, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why candidate `2` covers divisors of no value

An integer `k` that divides none of the input values makes every signed contribution negative. Its best range is the single or multi-element negative subarray with greatest sum, normally the least-magnitude individual value because all magnitudes are positive.

The smallest permitted integer is two. If two also divides no value, it produces exactly this all-negative behavior and is the smallest representative. If two divides some values, changing their signs to positive can only improve the maximum subarray score.

Therefore no absent divisor can beat candidate two, and `2` must be included even when it is not a prime factor of any input value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extracting distinct prime factors

The source starts:



It factors each distinct input value. Processing `set(nums)` avoids factoring duplicate values repeatedly.

For current `value`, trial factor `factor` begins at two. When it divides:

1. add `factor` to the candidate set;
2. divide out every copy of that factor.

Removing all copies ensures that later trial divisors operate on the remaining cofactor and that each prime factor is added only once per number.

The loop continues while `factor * factor <= value`. If a residual `value>1` remains afterward, that residual is prime and is also added.

Although `factor` increments through composite integers too, a composite cannot first divide the reduced value after all its smaller prime factors have been removed. Every added factor is therefore prime.

The outer candidate set automatically removes factors shared by several array values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `36` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4, 6, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `36` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every `k` through `M`:** This can require up to `10^6` Kadane scans. Prime-factor dominance reduces the candidates drastically.
- **Try every divisor, including composites:** Composite candidates cannot beat their prime factors and cannot win an equal-score smallest-`k` tie.
- **Use total signed sum instead of Kadane:** Alice chooses any nonempty subarray, not necessarily the whole array. Negative regions may need to be excluded.

---

## 7. Complexity Derivation

- **Time Complexity:** $O\left(n+U\sqrt M+P\log P+nP\right)$. Let:
- **Auxiliary Space Complexity:** $O(U+P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
