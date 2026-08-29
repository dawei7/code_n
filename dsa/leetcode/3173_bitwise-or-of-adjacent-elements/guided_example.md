# Guided Example: Bitwise OR of Adjacent Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 7, 15]}`
- **Required output:** `[3, 7, 15]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of length `n`, return an array `answer` of length $n - 1$ such that $\text{answer}[i] = \text{nums}[i] | nums[i + 1]$ where `|` is the bitwise `OR` operation.

The objective is to compute `[3, 7, 15]` from `{"nums": [1, 3, 7, 15]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One output corresponds to one adjacent pair

For an input of length $n$, output position $i$ is defined by exactly two values:

$$
\texttt{answer}[i]=\texttt{nums}[i]\mathbin{\mathrm{OR}}\texttt{nums}[i+1].
$$

There are $n-1$ adjacent pairs, so the direct construction is both simplest and sufficient.

`pairwise(nums)` lazily produces `(nums[0],nums[1])`, then `(nums[1],nums[2])`, continuing in left-to-right order. The list comprehension applies `a | b` to each and stores the results in the same order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 7, 15]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of bitwise OR

At each binary bit position, the result bit is 1 if at least one of the two input bits is 1. For 8 (`1000`) and 4 (`0100`), OR is 12 (`1100`).

For 1 and 3, binary `01 | 11 = 11`, so the result is 3.

No carry occurs between bit positions; OR is not addition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why overlapping pairs are intentional

An interior element appears in two outputs: once with its left neighbor and once with its right neighbor. For `[a,b,c]`, results are `a|b` and `b|c`. This is required because both index pairs are adjacent.

`pairwise` retains exactly this overlap. Grouping into disjoint pairs such as $(0,1),(2,3)$ would omit required outputs.


Every pair emitted by `pairwise` contains elements at consecutive indices. Pair number $i$ is exactly `(nums[i], nums[i+1])`, so its computed OR equals required `answer[i]`.

Conversely, every valid output index from 0 through $n-2$ has one emitted pair. The list comprehension therefore creates exactly $n-1$ correct entries in required order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 7, 15]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 7, 15]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 7, 15]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Index loop:** Append `nums[i] | nums[i+1]` for `i` from 0 to $n-2$. It is equivalent and avoids requiring `pairwise`.
- **`zip(nums, nums[1:])`:** Concise, but `nums[1:]` allocates an extra $O(n)$ slice.
- **In-place overwrite:** It risks corrupting the next pair because interior original values are reused.
- **Prefix OR:** Incorrect; it accumulates earlier elements rather than using only adjacent pairs.
- **Two elements:** Exactly one OR value is returned.
- **Equal adjacent values:** `x | x = x`.
- **One value's bits contain the other's:** The OR equals the bitwise superset.
- **Zero neighbor:** `x | 0 = x`.
- **Interior element:** It correctly contributes to two neighboring results.
- **Order preservation:** Pairwise iteration produces outputs by increasing left index.
- **Nonnegative inputs:** Binary OR has the straightforward finite representation intended by the problem.
- **Output length:** Exactly one less than input length.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be input length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
