# Guided Example: Single Number III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 3, 2, 5]}`
- **Required output:** `[3, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in **any order**.

The objective is to compute `[3, 5]` from `{"nums": [1, 2, 1, 3, 2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why `xs` must contain a set bit

The two singletons are distinct; otherwise one value would occur twice rather than two values occurring once. XOR is zero only when its operands are equal, so $p\oplus q\ne0$. At least one bit of `xs` is therefore `1`.

At any such bit, exactly one singleton has a `1` and the other has a `0`. That bit can partition the array so the singletons enter different groups.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 3, 2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Isolate one differing bit

The expression



isolates the least significant set bit of `xs`. In two's-complement arithmetic, negation flips bits above and including the rightmost `1` in a way that leaves only that position common under bitwise AND. The result `lb` is a power of two: it has exactly one set bit.

The algorithm does not depend on choosing the least significant differing bit specifically. Any set bit of `xs` would separate the singletons. The low-bit formula is simply a constant-time way to select one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The expression



isolates the least significant set bit of ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: XOR only one partition

The second pass considers values satisfying `x & lb`, meaning their bit at the selected position is `1`. It XORs those values into `a`.

Every ordinary duplicated value sends both copies to the same partition because identical bit patterns make the same test result. If its selected bit is `1`, both copies enter `a` and cancel; if the bit is `0`, neither enters. The duplicate pairs cannot contaminate the result.

Exactly one of $p$ and $q$ has the selected bit set, so exactly one enters this partition. After all paired values cancel, `a` equals that singleton.

The other singleton is recovered from the total singleton XOR:

$$
b=\text{xs}\oplus a.
$$

If `a = p`, then `(p ^ q) ^ p = q` because the two copies of `p` cancel. The source returns `[a, b]`. Which singleton appears first depends on the selected bit, and the contract permits either order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 3, 2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency hash map:** Count every value and re:** - **Frequency hash map:** Count every value and return the two with count one. It is straightforward and $O(n)$ expected time, but requires $O(n)$ extra space in the worst case.
- **Sort the array:** Paired values become adjacent and singletons can be found by scanning. Sorting takes $O(n\log n)$ time and may mutate the input or require a copy.
- **Build both XOR partitions:** Maintain one accumulator for the selected-bit group and another for the zero-bit group. It directly yields both singletons but is unnecessary because `xs ^ a` recovers the second.
- **Singleton value zero:** Zero participates normally: it changes no XOR accumulator, but after the other singleton is recovered, `xs ^ other` correctly yields zero.
- **Negative values:** Python's bitwise semantics preserve the low-bit and cancellation identities, including the minimum 32-bit value.
- **The two singletons differ only in a high bit:** `xs & -xs` finds their lowest differing bit, whether low or high; at least one difference always exists.
- **Duplicate values with the selected bit set:** Both copies enter `a` and cancel. Copies with the bit clear both stay out, so either case is harmless.
- **Input length two:** There are no duplicate pairs. The differing bit separates the two values immediately.
- **Nonempty-input assumption:** `reduce` is called without an initializer, but the constraints guarantee at least two elements. An empty list outside the contract would raise an error.
- **More or fewer singleton values:** The proof relies on exactly two. With a different occurrence pattern, `xs` would not necessarily encode a separable pair and this method would need redesign.
- **Return order:** The selected bit determines which singleton becomes `a`; the problem explicitly accepts either ordering.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of array elements. `reduce(xor, nums)` reads all $n$ values once. The partition loop reads all $n$ values again. Every visit performs a constant number of fixed-width bit operations under the problem's 32-bit integer model, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
