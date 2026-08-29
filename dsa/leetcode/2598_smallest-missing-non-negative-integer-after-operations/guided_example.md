# Guided Example: Smallest Missing Non-negative Integer After Operations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, -10, 7, 13, 6, 8], "value": 5}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` and an integer `value`.

The objective is to compute `4` from `{"nums": [1, -10, 7, 13, 6, 8], "value": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Operations preserve the remainder class

Adding or subtracting `value` changes an integer by a multiple of `value`. Therefore its remainder modulo `value` never changes.

Conversely, any two integers with the same remainder differ by a multiple of `value`, so repeated operations can transform one into the other. Each input element is a flexible resource for producing any integer in its own remainder class.

The exact original values and signs are irrelevant after their remainder frequencies are known.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, -10, 7, 13, 6, 8], "value": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Normalize negative values through modulo

Python's `x % value` returns a remainder from zero through `value - 1` even when $x$ is negative. For example, `-10 % 5` is zero and `-1 % 5` is four.

This normalized class is exactly what repeated additions or subtractions preserve. Counter `cnt` records how many array elements are available in each class.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the MEX from zero upward

To make the MEX at least $M$, the transformed array must contain every integer

$$
0,1,2,\ldots,M-1.
$$

Target integer $i$ can be created only from an unused element whose remainder is `i % value`. The loop tries targets in ascending order.

If the required class has an available element, the algorithm spends one by decrementing its count and moves to the next target.

If the class count is zero, no remaining element can become $i$. Since all smaller targets have already been supplied, $i$ is the achieved MEX and is returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, -10, 7, 13, 6, 8], "value": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Transform values explicitly:** Searching actual operation sequences is unnecessary because remainder equivalence completely characterizes reachability.
- **Sort chosen representatives:** Sorting can derive a MEX but does extra $O(n\log n)$ work after classes are already sufficient.
- **Array of remainder counts:** A list of length `value` replaces hashing and gives deterministic $O(n+\texttt{value})$ behavior.
- **Negative inputs:** Python modulo normalizes them into the correct nonnegative class.
- **Value one:** Every element belongs to class zero and can form consecutive targets zero through $n-1$, so MEX is $n$.
- **Missing class zero:** Target zero fails immediately and the answer is zero.
- **Duplicate remainders:** Each occurrence is a separate resource for successive targets in that class.
- **MEX upper bound:** Length $n$ guarantees a return by target $n$.
- **Counter mutation:** Only the local frequency structure is decremented; `nums` remains unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Building the Counter takes expected $O(n)$ time. The loop executes at most $n+1$ iterations with expected constant-time Counter access, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(\texttt{value})$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
