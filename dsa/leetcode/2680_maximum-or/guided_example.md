# Guided Example: Maximum OR

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [12, 9], "k": 1}`
- **Required output:** `30`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of length `n` and an integer `k`. In an operation, you can choose an element and multiply it by `2`.

The objective is to compute `30` from `{"nums": [12, 9], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Multiplying by two is a left shift

For a nonnegative integer $x$, multiplying by two moves every set bit one position left. Applying the operation $k$ times to the same element produces:

$$
x\cdot 2^k=\texttt{x << k}.
$$

The question is therefore where to concentrate up to $k$ left shifts before taking the bitwise OR of all elements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [12, 9], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an optimum concentrates all shifts on one element

Consider any allocation of the $k$ operations among several positive elements. Look at an element whose shifted value contains the highest set bit in the resulting array, and suppose that element received $s$ shifts.

If $s<k$, shifting that same element all $k$ times instead moves its highest set bit another $k-s$ positions left. This creates a set bit strictly above the highest bit of the distributed result. Any integer with that higher leading bit is numerically larger than the entire distributed OR, regardless of lower bits that may disappear when other elements are left unshifted.

If $s=k$, all operations were already concentrated on that element.

Thus a distributed allocation cannot beat every concentrated candidate. It is sufficient to try each index as the one element receiving all $k$ shifts. Since inputs are positive, an optimal result can use all available operations.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What remains unchanged for one candidate

When index $i$ is chosen:

- `nums[i]` becomes `nums[i] << k`;
- every index before $i$ stays unchanged;
- every index after $i$ stays unchanged.

The candidate result is:

$$
\operatorname{OR}(\text{before }i)
\mathbin{|}
(\texttt{nums[i] << k})
\mathbin{|}
\operatorname{OR}(\text{after }i).
$$

Computing the unchanged OR from scratch for every index would make the algorithm quadratic. Prefix and suffix summaries supply those two parts in constant time.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `30` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [12, 9], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `30` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every index and recompute all other ORs:** Correct but $O(n^2)$.
- **Prefix and suffix arrays both:** Also $O(n)$ time, but one running prefix is enough.
- **Bit-frequency counts:** Counts can maintain the OR excluding one index with constant bounded-bit work and reduce range storage.
- **Distribute shifts greedily by current value:** Not justified by bitwise interactions; the concentration theorem is the needed argument.
- **Single element:** The result is simply `nums[0] << k`.
- **Chosen first element:** Empty prefix contributes zero.
- **Chosen last element:** Empty suffix contributes zero.
- **Duplicate bits across elements:** Prefix and suffix OR naturally preserve a bit if any unchanged element supplies it.
- **Large values:** Python integers avoid overflow when shifting.
- **Use exactly all operations:** Positive inputs and the leading-bit argument ensure an optimum need not leave shifts unused.
- **Do not mutate `nums`:** Candidates are evaluated algebraically, so each starts from the original array.
- **Update prefix too early:** This would include the chosen number both unshifted and shifted and produce an invalid candidate.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Suffix construction visits $n$ elements once, and the candidate loop visits them once more. Each shift, OR, comparison, and assignment is constant time under the problem's bounded integer widths. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
