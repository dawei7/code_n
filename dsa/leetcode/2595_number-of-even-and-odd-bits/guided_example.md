# Guided Example: Number of Even and Odd Bits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `[2, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer `n`.

The objective is to compute `[2, 4]` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Binary indices begin at the least-significant bit

Bit index zero is the rightmost bit of the binary representation. Moving left increases the index by one. Therefore indices alternate:

$$
0\text{ even},\ 1\text{ odd},\ 2\text{ even},\ 3\text{ odd},\ldots
$$

The solution scans bits from right to left, exactly in this indexing order.

`ans[0]` stores the number of set bits at even indices, and `ans[1]` stores the number at odd indices.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read the current lowest bit

The expression `n & 1` isolates the least-significant bit:

- if that bit is one, the result is one;
- if that bit is zero, the result is zero.

Adding this result to the appropriate counter increments it only for a set bit. No conditional branch is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The expression `n & 1` isolates the least-significant bit:

... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Track index parity instead of the full index

Variable `i` is not the absolute bit index. It is only its parity: zero for even and one for odd.

After processing each bit, `i ^= 1` toggles it. XOR with one changes zero to one and one to zero:

$$
0\mathbin{\char94}1=1,\qquad
1\mathbin{\char94}1=0.
$$

Since consecutive bit indices alternate parity, this is all the state required to choose the right counter.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Convert to a binary string:** Reverse `bin(n)`:** - **Convert to a binary string:** Reverse `bin(n)` and inspect characters by index. This is clear but allocates $O(\log n)$ string space.
- **Alternating bit masks:** Mask even and odd positions separately and use a population-count operation, offering another constant-space bit solution.
- **Full integer index:** Incrementing an absolute index and taking modulo two works, but a one-bit parity toggle stores exactly what is needed.
- **Power of two at even index:** The result is `[1,0]`.
- **Power of two at odd index:** The result is `[0,1]`.
- **All significant bits set:** Counts differ by at most one because positions alternate parity.
- **Least-significant bit:** It always belongs to the even counter because its index is zero.
- **Leading zeros:** They are not processed and would contribute nothing anyway.
- **Positive-input guarantee:** At least one significant bit exists.
- **Local right shifts:** They do not mutate any caller-visible structure.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(log n)$. A positive integer $n$ has $\lfloor\log_2 n\rfloor+1$ significant bits. The loop processes one per iteration with constant work, giving $O(\log n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
