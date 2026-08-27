# Guided Example: Minimum Operations to Sort a Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 2, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`, where `nums` is a permutation of the integers from 0 to $n - 1$.

The objective is to compute `2` from `{"nums": [0, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two missing names prevent exact execution

The method annotation uses `List[int]`, but `List` is not imported or defined. Under normal Python annotation evaluation, loading `solution.py` itself raises `NameError: name 'List' is not defined` while the class body is being created.

If `List` is supplied externally so the module can load, a call later reaches `ans = inf`, but `inf` is also neither imported nor defined. That produces a second `NameError`.

After supplying only those two missing names in an isolated verification harness, the intended algorithm matched breadth-first shortest paths for every permutation of lengths one through eight. The reasoning below describes that verified intended logic while keeping both source defects explicit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use zero as the anchor

The sorted target is

`[0, 1, 2, ..., n - 1]`.

Because `nums` is a permutation, zero appears exactly once. The source finds its index `zero`. Any cyclic representation of the sorted target must begin at that position, so zero gives a unique anchor for testing both orientations.

The helper `check(step)` walks cyclically from zero. At logical position `i` it compares indices

$$
(\texttt{zero}+(i-1)\cdot step)\bmod n
$$

and

$$
(\texttt{zero}+i\cdot step)\bmod n.
$$

With `step = 1`, it walks forward through array indices. With `step = -1`, it walks backward. Python's modulo maps negative indices into the correct range.

If a previous value is greater than the current one, that orientation is rejected. Since traversal begins at value zero and visits all distinct values from the permutation, a nondecreasing traversal must be exactly $0,1,\ldots,n-1$. Merely checking for descents is enough; no duplicates or missing labels can hide a gap.

If neither direction passes, sorted order is neither a rotation of `nums` nor a rotation of its reversal. No sequence of the allowed global operations can sort it, and the final result is `-1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The sorted target is

`[0, 1, 2, ..., n - 1]`.

Because `num... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Forward cyclic orientation

Suppose `check(1)` succeeds. Reading forward from index `zero` already gives sorted order. Rotating left `zero` times moves that zero to index zero and produces the target. This costs:

$$
\texttt{zero}.
$$

There is another way to realize the same net rotation using reversals. Reversal conjugates a left rotation into a right rotation:

$$
F\,L^q\,F=R^q,
$$

where $F$ is whole-array reversal, $L$ is one left rotation, and $R$ is one right rotation.

Rotating left by `zero` is equivalent to rotating right by `n - zero`. Therefore reverse, rotate left `n - zero` times, and reverse again has cost:

$$
n-\texttt{zero}+2.
$$

The source compares both. Even though the direct route is often cheaper, the second route can win when zero lies near the end because one right rotation would otherwise require many allowed left rotations.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Required annotation import:** `List` must be d:** - **Required annotation import:** `List` must be defined, commonly by importing it from `typing` or by using the built-in `list` annotation. Otherwise the module cannot finish defining `Solution`.
- **Required infinity definition:** `inf` must also be supplied before the method can track a best candidate. The approach does not edit either defect.
- **Breadth-first search over arrays:** BFS proves shortest paths for tiny inputs but can explore permutations and is infeasible for $N=10^5$. The two operations actually generate at most two cyclic orientations, which the source recognizes directly.
- **Check only rotations of the original:** A reversal can make a backward cyclic ordering sortable, so both `step = 1` and `step = -1` are necessary.
- **Always use `zero` left rotations:** That covers only the forward orientation and can miss a cheaper route using two reversals to simulate right rotations.
- **Assume one reversal is enough for backward orientation:** A reversal changes orientation but may leave zero away from the first position. The appropriate rotations must also be counted.
- **Already sorted:** `zero = 0` and the forward check succeeds, giving cost zero.
- **Sorted cyclic shift:** The forward check succeeds and the two formulas compare left rotation with a reversal-assisted right rotation.
- **Reverse cyclic shift:** The backward check succeeds and the two one-reversal placements are compared.
- **Unreachable permutation:** If reading cyclically from zero is not increasing in either direction, global rotations and reversals cannot change its cyclic adjacency structure; the result is `-1`.
- **Length one:** Both checks are vacuously true, but the forward candidate zero wins, correctly requiring no operation.
- **Length two:** Forward and backward cyclic orientations coincide, so considering both merely adds equivalent candidates and the minimum remains correct.
- **Zero near the final index:** A reversal-assisted simulated right rotation can be much cheaper than many direct left rotations.
- **Input preservation:** Modular index calculations inspect the permutation without rearranging it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the permutation length. `nums.index(0)` scans up to $N$ positions. Each orientation check performs $N-1$ comparisons, and there are two checks. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
