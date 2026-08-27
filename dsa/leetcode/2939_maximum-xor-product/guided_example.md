# Guided Example: Maximum Xor Product

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": 12, "b": 5, "n": 4}`
- **Required output:** `98`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given three integers `a`, `b`, and `n`, return *the **maximum value** of* $(a XOR x) * (b XOR x)$ *where* $0 \le x < 2^n$.

The objective is to compute `98` from `{"a": 12, "b": 5, "n": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: When the bits of $a$ and $b$ are equal

Suppose bit $i$ of both inputs is zero. Choosing `x_i = 1` makes bit $i$ of both XOR results one.

If both input bits are one, choosing `x_i = 0` also leaves bit $i$ equal to one in both results.

Thus whenever the two source bits match, there is a choice that sets the bit in both $A$ and $B$. This increases both nonnegative factors and can never reduce their product. The source directly applies

`ax |= 1 << i` and `bx |= 1 << i`.

It does not need to record the actual bit of $x$ because the answer asks only for the maximum product.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": 12, "b": 5, "n": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When the source bits differ

If one source bit is zero and the other is one, XOR with the same `x_i` keeps the result bits different: exactly one of $A$ and $B$ receives $2^i$.

The sum contributed by this position is fixed, regardless of which factor receives it. For a fixed total $A+B$, the product

$$
AB
$$

is maximized when the two factors are as close as possible. Therefore the bit should go to the currently smaller partial factor:

- if `ax > bx`, set the bit in `bx`;
- otherwise, set it in `ax`.

The source uses exactly this rule.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If one source bit is zero and the other is one, XOR with the... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why balancing greedily from high bits is correct

After all bits above $i$ have been fixed, their contribution determines the leading comparison between `ax` and `bx`. All still-lower bits together are worth less than $2^i$ in either number, so they cannot undo the significance of assigning the current $2^i$ bit.

At a differing position, the combined sum of the two eventual factors remains fixed whichever side receives the bit. Assigning it to the smaller partial factor minimizes their absolute difference at the highest position where the choice can affect that difference. Lower choices can only refine the balance.

Since

$$
AB=\frac{(A+B)^2-(A-B)^2}{4},
$$

with fixed sum, minimizing $|A-B|$ maximizes the product. The high-to-low greedy choice achieves the smallest possible difference lexicographically by bit significance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `98` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": 12, "b": 5, "n": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `98` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every $x$:** There are $2^n$ possibi:** - **Enumerate every $x$:** There are $2^n$ possibilities, which is infeasible for $n=50$.
- **Dynamic programming over bit states:** Possible but unnecessary because matching bits have a forced best choice and differing bits reduce to balancing.
- **Apply modulo during construction:** Incorrect; modular residues do not preserve magnitude or product ordering.
- **$a=b$ in variable bits:** Every low matching bit can be made one in both results, maximizing both simultaneously.
- **One factor initially larger in high bits:** Differing low bits are preferentially assigned to the smaller factor, though low bits may not fully close the fixed high-bit gap.
- **Tie between partial factors:** The source assigns the differing bit to `ax`. Assigning it to `bx` is symmetric and yields the same attainable optimum.
- **$n=0$:** Only $x=0$ is legal, and the initialization already gives the answer.
- **High bits:** They cannot be changed by legal $x$ and must be copied before low-bit decisions.
- **Actual $x$ not returned:** Each decision corresponds to some legal bit of $x$, but reconstructing it is unnecessary.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop examines exactly $n$ bit positions and performs constant work at each. Time complexity is $O(n)$; with $n\le50$, this is a very small fixed bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
