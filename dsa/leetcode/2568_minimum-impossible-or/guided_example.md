# Guided Example: Minimum Impossible OR

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`.

The objective is to compute `4` from `{"nums": [2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: OR can add bits but can never remove them

The bitwise OR of selected numbers has a one in every bit position that is one in at least one selected number. Once an unwanted bit appears, no later OR operation can turn it back to zero.

This makes powers of two special. The number $2^k$ has exactly one set bit, at position $k$. To express exactly $2^k$, every chosen number must contain no set bit outside position $k$, and at least one chosen number must contain bit $k$. Because all input numbers are positive, the only number satisfying both conditions is $2^k$ itself.

Therefore:

$$
2^k\text{ is expressible if and only if }2^k\text{ appears in }\texttt{nums}.
$$

Combining other numbers cannot manufacture a missing single-bit value. Any number carrying bit $k$ plus some additional bit would make the OR larger and different from $2^k$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the first missing power of two is the answer

Suppose $2^k$ is the first power of two absent from the array. It is impossible to express by the single-bit argument above.

Now consider any positive integer $x<2^k$. Its binary representation uses only bit positions $0$ through $k-1$. Because $2^k$ is the first missing power, all values

$$
1,2,4,\ldots,2^{k-1}
$$

are present in `nums`. Select the power of two corresponding to each set bit of $x$. ORing those selected values reconstructs $x$ exactly.

For example, if $x=13$, its binary representation is `1101`, so

$$
13=8\mathbin{|}4\mathbin{|}1.
$$

If $1$, $4$, and $8$ are present, $13$ is expressible. This construction works for every smaller positive value. Hence the first missing power of two is not merely impossible; every positive integer below it is possible. It is exactly the minimum impossible OR.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose $2^k$ is the first power of two absent from the arra... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the implementation finds that power

The code builds `s = set(nums)`, allowing expected $O(1)$ membership tests. It then generates powers `1 << i` for $i$ from $0$ through $31$ and returns the first one not in the set:

`next(1 << i for i in range(32) if 1 << i not in s)`.

Left-shifting one by $i$ places its only set bit at position $i$, producing $2^i$. The generator tests powers in strictly increasing order, so `next` returns the smallest missing one without generating later candidates.

For `nums = [2,1]`, both $1$ and $2$ are present. Their OR expresses $3$. Power $4$ is absent and cannot be assembled without also introducing some other bit, so the answer is $4$.

For `nums = [5,3,2]`, power $1$ is not an array element. Although both $5$ and $3$ contain their least-significant bit, each also contains another bit. OR cannot remove those extras, so neither can express $1$. The answer is immediately $1$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Bit-presence mask:** Record bit $k$ only when :** - **Bit-presence mask:** Record bit $k$ only when an input equals $2^k$. This preserves the proof and achieves $O(1)$ auxiliary space under the fixed 32-bit domain.
- **Enumerate subsequence OR values:** Maintaining all reachable OR results is much more expensive and unnecessary because the minimum answer is controlled by powers of two.
- **Sort the array:** Sorting does not help; exact membership of a few powers is enough, and a set supplies it directly.
- **Missing one:** If literal value $1$ is absent, the answer is always $1$, even when other numbers have their lowest bit set.
- **All small powers present:** Their subsequences express every number below the first missing higher power by selecting the set-bit components.
- **Duplicates:** Repeated copies do not change OR expressibility and are collapsed by the set.
- **Composite values:** They may express other composites but can never replace a missing single-bit power.
- **Guaranteed generator result:** The value $2^{30}$ exceeds the input maximum and is necessarily absent, so checking 32 positions is sufficient.
- **Expected set behavior:** The $O(n)$ time statement uses normal expected constant-time Python hash membership.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of input values. Building `set(nums)` takes expected $O(n)$ time and $O(n)$ space. The generator checks at most 32 powers, which is $O(1)$ time under the fixed integer bound. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
