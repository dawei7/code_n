# Guided Example: Concatenation of Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1]}`
- **Required output:** `[1, 2, 1, 1, 2, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where $\text{ans}[i] = \text{nums}[i]$ and $ans[i + n] = \text{nums}[i]$ for $0 \le i < n$ (**0-indexed**).

The objective is to compute `[1, 2, 1, 1, 2, 1]` from `{"nums": [1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the language operation that matches the definition

The required result consists of every element of `nums` in order, followed immediately by every element of `nums` in the same order again. Python's list addition operator already has exactly that meaning. The solution is therefore the single expression `nums + nums`.

For two lists `left` and `right`, `left + right` creates a new list. It copies the element references from `left` first and then the element references from `right`. Here both operands refer to the same input list, so the new list receives two consecutive copies of its sequence.

Let $N$ be the input length. During the first operand, output positions $0$ through $N-1$ receive `nums[0]` through `nums[N - 1]`. During the second operand, output positions $N$ through $2N-1$ receive that same sequence. Thus, for every $0\le i<N$,

$$
\texttt{ans}[i]=\texttt{nums}[i]
$$

and

$$
\texttt{ans}[i+N]=\texttt{nums}[i].
$$

Those are exactly the two required equations.

For `nums = [1, 3, 2, 1]`, list addition places `[1, 3, 2, 1]` from the left operand first and `[1, 3, 2, 1]` from the right operand second. The returned list is `[1, 3, 2, 1, 1, 3, 2, 1]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the input is not changed

List addition differs from `extend` and `+=`. It allocates and returns a distinct list rather than appending into the left operand. The original `nums` retains its original length and contents. This matters if the caller keeps using the input after the method returns.

The output does not recursively clone elements. Python copies references into the new list. In this problem every element is an integer, and integers are immutable, so that shallow-copy detail produces exactly the expected independent array behavior. If the elements were mutable nested objects, both halves and the original list would refer to the same objects; that situation is outside the integer-array contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no explicit index calculation is necessary

An explicit algorithm could allocate length $2N$ and assign two positions for each input index. That makes the formulas visible, but it does not improve the asymptotic cost or correctness. The built-in concatenation operation already implements the same sequential copying in optimized runtime code. Using it removes opportunities for off-by-one mistakes such as writing the second copy at `i + N - 1` or allocating only `2 * N - 1` positions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 1, 1, 2, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 1, 1, 2, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **List repetition:** `nums * 2` produces the same sequence and has the same $O(N)$ time and returned-space costs. Addition mirrors the statement's word “concatenation” particularly directly.
- **Explicit append loop:** Append every item once, then repeat the loop. This is correct but longer and still takes $O(N)$ time and space.
- **Preallocated result:** Create `ans = [0] * (2 * N)` and assign `ans[i]` and `ans[i + N]`. It follows the formula literally but adds indexing code without improving the bounds.
- **In-place `nums += nums`:** This mutates the caller's input and returns no new expression result in the same way. It does not match the side-effect-free behavior of the exact solution.
- **Using `extend`:** `nums.extend(nums)` also changes `nums` in place and returns `null`, so returning its direct result would be wrong.
- **Single element:** An input such as `[7]` becomes `[7, 7]`, satisfying both required positions.
- **Duplicate input values:** They are copied at every original position; uniqueness is neither required nor useful.
- **Order preservation:** Neither half is reversed or sorted. Both are exact left-to-right copies.
- **Input independence at list level:** Appending to the returned list later does not change the length of `nums` because the outer list object is new.
- **Shallow copying:** With the stated integer elements this is harmless. General nested mutable objects would be shared by reference, but the problem does not contain them.
- **Output lower bound:** Since a length-$2N$ list must be materialized, the linear runtime and space cannot be asymptotically improved.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\texttt{len(nums)}$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
