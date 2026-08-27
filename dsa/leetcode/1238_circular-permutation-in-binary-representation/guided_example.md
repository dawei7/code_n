# Guided Example: Circular Permutation in Binary Representation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "start": 3}`
- **Required output:** `[3, 2, 0, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given 2 integers `n` and `start`. Your task is return **any** permutation `p` of $(0,1,2.....,2^n -1)$such that :

The objective is to compute `[3, 2, 0, 1]` from `{"n": 2, "start": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start with the standard reflected Gray-code cycle

A Gray-code ordering lists every \(n\)-bit number exactly once while consecutive numbers differ in one bit. The standard formula for the Gray code of integer \(i\) is

\[
G(i)=i\oplus(i\mathbin{\text{>>}}1),
\]

where \(\oplus\) is bitwise XOR.

The list comprehension

`g = [i ^ (i >> 1) for i in range(1 << n)]`

evaluates this formula for every integer from zero through \(2^n-1\). `1 << n` is \(2^n\), so the list has exactly the required number of entries.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "start": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every value appears exactly once

The Gray transformation is invertible. The most significant binary bit of \(i\) equals the most significant bit of \(G(i)\). Moving downward, each original bit can be reconstructed from the preceding reconstructed bit and the corresponding Gray bit. Therefore, two different integers cannot produce the same Gray code.

There are \(2^n\) inputs and exactly \(2^n\) possible \(n\)-bit outputs. An injective mapping between these equally sized sets is a permutation, so `g` contains every value from zero through \(2^n-1\) once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The Gray transformation is invertible.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why consecutive Gray values differ in one bit

When incrementing \(i\) to \(i+1\), suppose \(i\) ends in \(t\) one-bits. The increment changes those \(t\) trailing ones to zeros and changes the next zero to one. Thus `i ^ (i + 1)` has its lowest \(t+1\) bits set.

In the shifted values, the analogous XOR has its lowest \(t\) bits set. Since

\[
G(i)\oplus G(i+1)
=
\bigl(i\oplus(i+1)\bigr)
\oplus
\bigl((i\mathbin{\text{>>}}1)\oplus((i+1)\mathbin{\text{>>}}1)\bigr),
\]

the two low-bit runs cancel except for bit \(t\). The result has exactly one set bit, proving adjacent Gray values differ in exactly one binary position.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 2, 0, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "start": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 2, 0, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct rotated Gray formula:** XOR every stand:** - **Direct rotated Gray formula:** XOR every standard Gray value with `start`. Because XOR preserves Hamming distance and `G(0)=0`, `[start ^ G(i)]` is also a valid cycle beginning at `start`, avoiding the index search and slices while retaining \(O(2^n)\) output work.
- **Backtracking on the hypercube:** It can find a valid cycle but explores a large search space unnecessarily.
- **Minimum \(n=1\):** The standard cycle `[0,1]` or its rotation has one-bit adjacency in both directions.
- **Start equals zero:** `j` is zero, and the return reproduces the standard Gray list.
- **Start at the final Gray entry:** Rotation moves that entry first and preserves both join edges.
- **Every value unique:** Invertibility of the Gray transform guarantees `g.index(start)` finds exactly one occurrence.
- **Wraparound requirement:** Ordinary adjacent Gray-code proof is not enough by itself; the first and last standard codes differ in the highest bit, establishing circularity.
- **Output size:** At \(n=16\), the list contains 65,536 integers, which is within the stated bound but inherently requires linear output memory.
- **Bit-width:** All generated values are below \(2^n\) because XOR of \(n\)-bit quantities stays within \(n\) bits.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^n)$. Let \(N=2^n\). Building `g` takes \(O(N)\) time. `g.index(start)` scans up to \(N\) entries. The two slices and concatenation copy \(N\) references overall. Total time is \(O(2^n)\).
- **Auxiliary Space Complexity:** $O(2^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
