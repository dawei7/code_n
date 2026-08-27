# Guided Example: Maximum XOR of Subsequences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` where each element is a non-negative integer.

The objective is to compute `3` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Combining the two subsequences into one selection

For an occurrence with value `v`, there are four possible membership choices:

- it belongs to neither subsequence, so it contributes nothing;
- it belongs only to the first subsequence, so it contributes `v` through `X`;
- it belongs only to the second subsequence, so it contributes `v` through `Y`; or
- it belongs to both subsequences, so its two contributions cancel because `v XOR v = 0`.

Therefore, an occurrence affects `X XOR Y` exactly when it is selected in **one** of the two subsequences, but not both. If $A$ and $B$ denote the sets of selected indices, the relevant indices are their symmetric difference $A \mathbin{\triangle} B$.

Because XOR is associative and commutative,

$$
X \mathbin{\mathrm{XOR}} Y
=
\mathop{\mathrm{XOR}}_{i \in A \mathbin{\triangle} B} \texttt{nums}[i].
$$

Any subset of array indices can be written in increasing order and is therefore a valid subsequence. Conversely, every subset XOR can be realized in the original problem by choosing those indices for the first subsequence and choosing the second subsequence to be empty. The empty subsequence is explicitly allowed and has XOR zero.

Thus, the set of achievable values of `X XOR Y` is exactly the set of XORs of arbitrary subsets of `nums`. The task is to find the largest value in that set.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Viewing integers as binary vectors

XOR behaves like addition over the two-element field: each bit is added modulo two, with no carry between positions. An integer can therefore be viewed as a vector of bits, and the XOR of a subset is a linear combination of the corresponding vectors with coefficients zero or one.

A linear basis stores only independent vectors while preserving every XOR value obtainable from all processed numbers. The source allocates

`basis = [0] * 31`

where `basis[bit]` is either zero or a vector whose highest set bit is `bit`. The input is nonnegative and at most $10^9$, so 31 slots indexed from $0$ through $30$ safely cover every possible set bit. In fact, $10^9 < 2^{30}$, making the top slot harmless extra capacity.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | XOR behaves like addition over the two-element field: each b... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Inserting one number by eliminating leading bits

For each input `value`, `current` begins as that value. Bits are considered from $30$ down to $0$.

If `current` does not have the current bit set, there is nothing to eliminate at that position, so the loop continues downward.

If the bit is set and `basis[bit]` already contains a vector, XORing that basis vector into `current` clears the bit. This works because both values have that bit set, and $1 \mathbin{\mathrm{XOR}} 1 = 0$. The stored vector has no bit above `bit`, so this operation cannot reintroduce any higher bit that was already eliminated.

If the bit is set and the slot is empty, `current` has a leading bit that no existing basis vector has. It is independent of the stored vectors, so the source saves it in `basis[bit]` and stops processing this input.

Sometimes repeated elimination reduces `current` to zero. That means the original value is an XOR combination of existing basis vectors. It adds no new achievable result and does not need to be stored.

As a small example, suppose the basis first receives $5=101_2$ and then $3=011_2$. Five is stored with leading bit $2$, and three is stored with leading bit $1$. If $6=110_2$ arrives later, its leading bit $2$ is cleared with five, producing $011_2$; that is then cleared with three, producing zero. Indeed, $6=5 \mathbin{\mathrm{XOR}} 3$, so the third vector was dependent.

After every insertion, two properties hold:

- every stored basis vector is an XOR of processed input values, so the basis cannot manufacture an unreachable value; and
- every processed input value is either stored independently or was reduced using stored vectors, so it remains expressible as an XOR of the basis.

It follows that the basis and the full processed prefix generate exactly the same set of subset-XOR values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate subsequences:** There are $2^n$ inde:** - **Enumerate subsequences:** There are $2^n$ index subsets, so evaluating every subset XOR is infeasible for $n$ up to $10^5$.
- **Maintain every reachable XOR:** Repeatedly add `old_xor ^ value` to a set of reachable values. The set can grow to $2^B$ distinct values, which is far larger than the 31-vector basis.
- **Use a bitwise trie for array elements:** A trie can maximize the XOR of two stored elements, but the optimum here may require XORing many elements. It does not directly represent the span of all subset XORs.
- **Treat the subsequences as disjoint:** The statement explicitly allows overlap. More importantly, the symmetric-difference reduction already accounts for overlap: occurrences chosen twice cancel, and every remaining subset is achievable.
- **Order of selected indices:** XOR does not depend on order, and every selected index set has a unique increasing order, so the subsequence requirement imposes no extra restriction.
- **Both subsequences empty:** This produces zero. The basis maximization starts from zero, so the empty choice is always available if no positive value can be formed.
- **Zero values:** Zero reduces immediately and never enters the basis. Including or excluding it cannot change any XOR.
- **Duplicate or dependent values:** A value that reduces to zero adds no new combination. Discarding it from the basis does not discard any achievable XOR.
- **All values zero:** Every basis slot remains zero, every maximization step leaves `answer` unchanged, and the method correctly returns zero.
- **Highest bit handling:** The loop includes bit $30$, while values up to $10^9$ need only bits $0$ through $29$. The extra zero slot is safe and keeps the implementation within a conventional 31-bit nonnegative range.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nB)$. Let $n$ be the array length and let $B=31$ be the number of represented bit positions.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
