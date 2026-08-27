# Guided Example: Once Twice

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 2, 3, 2, 5, 5, 5, 7, 7]}`
- **Required output:** `[3, 7]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. In this array:

The objective is to compute `[3, 7]` from `{"nums": [2, 2, 3, 2, 5, 5, 5, 7, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two-register modulo-three counter

For every bit position, `seen_once` and `seen_twice` encode its occurrence count modulo three:

- `00` means count zero modulo three;
- `01` means count one;
- `10` means count two.

For each `value`:

`seen_once=(seen_once ^ value) & ~seen_twice`

toggles bits into or out of the once state while excluding bits currently assigned to twice.

Then:

`seen_twice=(seen_twice ^ value) & ~seen_once`

updates the twice state while excluding the newly computed once state.

At a single bit, repeated appearances cycle:

`00 -> 01 -> 10 -> 00`.

Because bitwise operations process all positions in parallel, two integers maintain the modulo-three counts for the complete 32-bit patterns.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 2, 3, 2, 5, 5, 5, 7, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What remains after the first pass

Every value appearing three times contributes zero modulo three at every bit.

For a bit:

- if only `A` has it, total count modulo three is one and the bit appears in `seen_once`;
- if only `B` has it, its two occurrences give state two and the bit appears in `seen_twice`;
- if both have it, contribution is `1+2=3` and vanishes;
- if neither has it, it is zero.

Therefore:

`seen_once | seen_twice`

has exactly the bit positions where `A` and `B` differ—the bit pattern of `A XOR B`.

The two exceptional values must be different because one array element value cannot simultaneously have total frequency one and two. Hence at least one differing bit exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every value appearing three times contributes zero modulo th... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choosing a separating bit

`x & -x` isolates the least significant set bit of a nonzero integer. The source applies it to the union above, producing `differing_bit`.

Exactly one of `A` and `B` has this bit. Partitioning all input values by it places the two exceptions into different groups.

Every ordinary triple consists of three identical values, so all three copies go to the same group and still cancel modulo three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 7]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 2, 3, 2, 5, 5, 5, 7, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 7]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency dictionary:** It is simpler but uses:** - **Frequency dictionary:** It is simpler but uses `O(n)` space in the worst case and violates the required constant-space bound.
- **Sort the array:** Frequencies become adjacent, but sorting costs `O(n\log n)` and may mutate input.
- **Per-bit array of 32 counters:** It uses constant space and can find global modulo counts, but still needs separation logic to distinguish once from twice.
- **Use XOR only:** Triples do not cancel under XOR because three copies reduce to one copy, so ordinary values would remain.
- **Shared one bits of A and B:** They vanish in the first pass, which is why direct register output would be incomplete.
- **Least significant differing bit:** Any differing bit would separate the exceptions; choosing the lowest is a convenient constant-time method.
- **Triple values in a partition:** All identical copies choose the same side and continue to cancel.
- **Once value has separator bit:** Global once register identifies this orientation and selects the correct return registers.
- **Twice value has separator bit:** The alternate return branch handles it.
- **Zero as an exception:** Its bits are all zero, but it is separated from a distinct other exception by one of the other value’s set bits.
- **Negative exceptions:** Sign-extension behavior remains consistent under the same partition and modulo formulas.
- **Minimum signed integer:** `x & -x` works with Python’s arbitrary-precision integers, avoiding fixed-width overflow on negation.
- **Output order:** Orientation logic is necessary; simply returning the two group residues could swap once and twice.
- **Input guarantee:** The proof relies on exactly one frequency-one value, one frequency-two value, and every other frequency exactly three.
- **No input mutation:** Both passes read values only.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The algorithm makes two linear passes. Every element causes a constant number of bitwise operations, so time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
