# Guided Example: Find the Maximum Number of Marked Indices

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 5, 2, 4]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`.

The objective is to compute `2` from `{"nums": [3, 5, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn marking into a pairing problem

Every operation consumes two previously unused indices. Within a pair, one value must be at most half the other:

$$
2\cdot\textit{small}\le\textit{large}.
$$

The objective is therefore to form as many disjoint valid small-large pairs as possible. If $p$ pairs are formed, exactly $2p$ indices are marked.

Sorting removes the importance of original positions because the condition depends only on values and any two distinct indices may be paired. It also makes it possible to greedily reserve small values for the left role and large values for the right role.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 5, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why only half the array can supply pairs

No solution can contain more than $\lfloor n/2\rfloor$ pairs because each pair uses two indices. The code divides the sorted array conceptually into:

- a lower candidate region beginning at index $0$;
- an upper candidate region beginning at `(n + 1) // 2`.

The upper region contains exactly $\lfloor n/2\rfloor$ values. For even $n$, the two regions have equal length. For odd $n$, the lower region has one extra middle value, which may remain unmarked.

Any maximum pairing can be rearranged so that the smaller member of each pair comes from the lower region and the larger member comes from the upper region. If a supposedly small member lies in the upper half while some lower-half value is unused or used as a large member, replacing it with the no-larger lower value cannot break `2 * small <= large`. This exchange pushes small roles downward and large roles upward.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | No solution can contain more than $\lfloor n/2\rfloor$ pairs... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The two-pointer greedy scan

Pointer `i` identifies the smallest lower-region value not yet matched. The loop visits upper-region values `x` in ascending order.

If `2 * nums[i] <= x`, the pair is valid. The algorithm commits to it and increments `i`. The current upper value is consumed by the loop automatically, while the pointer moves to the next small candidate.

If the condition fails, `x` is too small even for the smallest unmatched lower value. It is therefore too small for every later lower candidate, because those values are at least `nums[i]`. The current `x` can never participate as the large side of a future pair, so skipping it loses nothing.

Notice that `i` does not advance on failure. A later, larger upper value may still match that same smallest candidate.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 5, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Binary search the number of pairs:** One can t:** - **Binary search the number of pairs:** One can test whether $p$ pairs are possible and binary-search $p$, but the direct two-pointer scan finds the maximum in one pass after sorting.
- **Try every pairing:** Matching combinations grow exponentially and are unnecessary due to sorted monotonicity.
- **Pair adjacent sorted values:** Adjacent values may be too close in magnitude; small candidates need access to the large upper tail.
- **Odd length:** At most $n-1$ indices can be marked, and the lower candidate region intentionally has one extra value.
- **One element:** The upper slice is empty, `i` stays zero, and no index is marked.
- **Duplicate values:** Occurrences are distinct indices, but equal positive values cannot pair with each other because doubling one exceeds the other.
- **Very large values:** The condition may require wider arithmetic in fixed-width languages; Python integers do not overflow.
- **All pairs feasible:** `i` reaches $\lfloor n/2\rfloor$, and the answer is the largest even number not exceeding $n$.
- **Input mutation:** Sort a copy if the original order must be preserved.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. Sorting costs $O(n\log n)$ time. The upper-half slice and loop contain $\lfloor n/2\rfloor$ elements, so scanning is $O(n)$. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
