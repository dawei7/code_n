# Guided Example: IP to CIDR

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"ip": "255.0.0.7", "n": 10}`
- **Required output:** `["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An **IP address** is a formatted 32-bit unsigned integer where each group of 8 bits is printed as a decimal number and the dot character `'.'` splits the groups.

The objective is to compute `["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]` from `{"ip": "255.0.0.7", "n": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View IPv4 addresses as consecutive 32-bit integers

CIDR alignment and block size are easiest to reason about numerically. The solution converts the four decimal octets into one unsigned integer by repeatedly shifting the accumulated value eight bits left and combining the next octet.

For octets `a.b.c.d`, the result is

`(a << 24) | (b << 16) | (c << 8) | d`.

Consecutive IP addresses then correspond to consecutive integers. The required interval begins at `current` and contains `remaining` addresses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"ip": "255.0.0.7", "n": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: CIDR blocks have power-of-two sizes and alignment

A prefix length `p` fixes the first `p` bits and leaves `32 - p` bits free. Such a block contains

`2^(32 - p)`

addresses. Its base address must be divisible by that block size, because all free low bits of the base are zero.

At every iteration, the next block must begin exactly at `current`. Beginning later would leave a gap; beginning earlier would cover an address outside the requested interval.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A prefix length `p` fixes the first `p` bits and leaves `32 ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the largest block aligned at the current address

For a positive integer, `current & -current` isolates its lowest set bit. Its value is the largest power of two dividing `current`, which is exactly the largest power-of-two block size aligned at that address.

When `current == 0`, the expression is zero even though address zero is aligned to every IPv4 block size. The special case replaces it with `1 << 32`, the size of the entire IPv4 space.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"ip": "255.0.0.7", "n": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Emit every address as `/32`:** This is exact b:** - **Emit every address as `/32`:** This is exact but uses `n` blocks and is not minimal.
- **- **Choose only by remaining size:** A large block:** - **Choose only by remaining size:** A large block may start at a misaligned address and cover a different CIDR range. Both size and alignment constraints are mandatory.
- **- **Choose only by alignment:** The aligned block :** - **Choose only by alignment:** The aligned block may extend beyond the requested final address. Limit it by the largest power of two no greater than `remaining`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let `B` be the number of returned CIDR blocks. Each loop iteration emits one block and performs constant-width 32-bit arithmetic and formatting, so time is `O(B)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
