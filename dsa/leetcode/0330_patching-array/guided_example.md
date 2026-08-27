# Guided Example: Patching Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3], "n": 6}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range `[1, n]` inclusive can be formed by the sum of some elements in the array.

The objective is to compute `1` from `{"nums": [1, 3], "n": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track a continuous coverage frontier.

Trying to store every subset sum would be far too expensive because each element can be selected or omitted. The greedy solution instead summarizes all relevant subset sums with one number, `x`.

Its invariant is:

> Before each loop iteration, using the input values already consumed plus the patches already chosen, every integer sum from `1` through `x - 1` can be formed. The value `x` is the smallest sum not yet guaranteed to be formable.

It is also useful to include the empty subset's sum zero mentally. The known interval is then every sum from `0` through `x - 1`. Initially, `x = 1`. No positive value is covered yet, so the interval `1` through `0` is empty and the invariant is true.

The loop continues while `x <= n`, because the first uncovered value is still inside the required range. Once `x > n`, every value from `1` through `n` lies below the frontier and is covered.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3], "n": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use the next input value when it can touch the covered interval.

Let the next unused sorted value be $v=\text{nums}[i]$. If $v\le x$, it can extend coverage without leaving a gap.

Before using $v$, old subset sums cover

$$
[0,x-1].
$$

Selecting $v$ together with any old subset produces the shifted interval

$$
[v,v+x-1].
$$

Because $v\le x$, this shifted interval starts no later than one position after the old interval ends. The two intervals therefore touch or overlap, and their union covers

$$
[0,x+v-1].
$$

The new smallest uncovered sum is $x+v$, exactly the source update `x += nums[i]`. The index advances because each array element is an individual item and may be consumed only once.

For example, if all sums through `6` are covered, then `x = 7`. Consuming a next value `5` creates new sums from `5` through `11` by adding `5` to old sums `0` through `6`. Together, the old and new intervals cover everything through `11`, so the frontier becomes `12`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let the next unused sorted value be $v=\text{nums}[i]$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a value larger than `x` cannot help yet.

If the next input value is greater than `x`, it cannot be part of a subset summing to `x`: all values are positive, so including it would already exceed `x`. Excluding it leaves only previously consumed values, which by the invariant do not guarantee `x`. Since `nums` is sorted ascending, every later unused input is at least as large and cannot close the gap either.

At least one patch is therefore unavoidable at this point. This is the key fact that makes a greedy choice possible: the algorithm is not patching merely because it seems helpful; any valid completion must add some value no greater than the current missing sum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3], "n": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit subset-sum set or Boolean table:** Up:** - **Explicit subset-sum set or Boolean table:** Updating all reachable sums can solve smaller bounded targets, but it needs $O(n)$ or more storage and potentially $O(mn)$ time. Here `n` can approach $2^{31}-1$, making that approach impossible.
- **- **Patch with a smaller value than `x`:** It may :** - **Patch with a smaller value than `x`:** It may close the immediate gap, but extends the frontier less than patching `x`. It cannot lead to fewer future patches under the coverage invariant.
- **- **Patch with a value larger than `x`:** Positive:** - **Patch with a value larger than `x`:** Positive numbers already consumed cannot combine with it to make the smaller missing value `x`, so the gap remains. Such a patch is invalid as the next greedy action.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+\log n)$. Let $m$ be `len(nums)`. Each loop iteration does one of two things: it consumes one array element and increments `i`, which can happen at most $m$ times, or it patches and doubles `x`. Starting from one, only $O(\log n)$ doublings can occur before `x > n`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
