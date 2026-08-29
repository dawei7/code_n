# Guided Example: Maximum Enemy Forts That Can Be Captured

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"forts": [1, 0, 0, -1, 0, 0, 0, 0, 1]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `forts` of length `n` representing the positions of several forts. $\text{forts}[i]$ can be `-1`, `0`, or `1` where:

The objective is to compute `4` from `{"forts": [1, 0, 0, -1, 0, 0, 0, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid move is bounded by opposite non-enemy markers

Array values mean:

- `1` is one of your forts;
- `0` is an enemy fort;
- `-1` is an empty position that can be the destination.

To move legally, one endpoint must be `1` and the other `-1`, while every position strictly between them must be zero. The number captured is exactly the length of that consecutive zero run.

The army may move left or right, so endpoint order can be either `1,...,-1` or `-1,...,1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"forts": [1, 0, 0, -1, 0, 0, 0, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Only consecutive nonzero boundaries matter

Ignore zeroes temporarily and look at the nonzero markers in array order. A valid move can occur only between two consecutive such markers.

If another `1` or `-1` lay between the chosen endpoints, then an intermediate position would not be an enemy fort, violating the rule that every crossed position is zero.

Conversely, the interval between consecutive nonzero markers contains only zeroes by definition. It is valid exactly when the marker values are opposite.

The algorithm scans precisely these consecutive boundary pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start at a nonzero boundary and skip its zero run

At index `i`, the condition `if forts[i]` is true for both 1 and $-1$, and false for zero.

When `forts[i]` is nonzero, `j` advances while `forts[j]==0`. At loop end:

- either `j==n` and the zero run reaches the array boundary with no destination marker;
- or `j` is the next nonzero marker after `i`.

The number of zeroes strictly between them is `j-i-1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"forts": [1, 0, 0, -1, 0, 0, 0, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track last nonzero index:** In one simple `for` loop, compare each new nonzero marker with the previous one and measure their gap.
- **Brute-force endpoint pairs:** It repeats zero-run checks and can cost $O(n^2)$.
- **No owned fort:** No move can begin, so return zero.
- **No empty position:** No legal destination exists.
- **Leading or trailing zeroes:** They lack two bounding markers and cannot form a move.
- **Same-type boundaries:** `1...1` and `-1...-1` are invalid.
- **Opposite adjacent boundaries:** They capture zero enemy forts.
- **Movement direction:** Both leftward and rightward moves are accepted by the same sum-zero test.
- **Consecutive nonzero requirement:** Any intervening marker would violate the all-zero interior rule.
- **Nested-loop appearance:** Forward jumps ensure linear total work.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Although there is a nested `while`, indices move only forward. Every position is passed a constant number of times, so total time is $O(n)$ rather than $O(n^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
