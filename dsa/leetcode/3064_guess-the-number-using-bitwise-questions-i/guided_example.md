# Guided Example: Guess the Number Using Bitwise Questions I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 536870912}`
- **Required output:** `536870912`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a number `n` that you have to find.

The objective is to compute `536870912` from `{"n": 536870912}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**A one-bit query isolates one bit of the secret.** Query the API with

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 536870912}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

This number has exactly one set bit, at position $i$. Therefore `n & num` is either zero when secret bit $i$ is zero, or $2^i$ when that bit is one. `commonSetBits(num)` consequently returns either 0 or 1 for a legal single-bit query.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

The source includes `1 << i` in the answer whenever the API result is truthy:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `536870912` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 536870912}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `536870912` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Query all legal bits with `range(30)`:** This is the direct correction and deterministically reconstructs every allowed secret.
- **Group-testing queries:** Asking about several bits at once returns only their count, not identities, so decoding requires a more elaborate scheme and provides no benefit in this first version.
- **Binary search:** The API does not compare magnitudes, so ordinary higher/lower binary search is unavailable.
- **Secret is a power of two:** Exactly one legal single-bit query is truthy, and the sum returns that power.
- **All 30 bits set:** Every legal query succeeds and their sum is $2^{30}-1$.
- **Secret minimum one:** Bit zero or another single bit is detected normally; the contract excludes secret zero.
- **Truthiness:** Legal one-bit queries return 0 or 1, so using the result as a condition is safe.
- **Illegal bits 30 and 31:** The exact source queries them despite the explicit reliability warning, so its result is not guaranteed.
- **Addition versus OR:** Distinct powers make them equivalent; duplicate bit queries would break that simple reasoning but none are duplicated.
- **Manifest mismatch:** “Legal bit positions” describes 30 queries, not the actual 32-query loop.
- **No ambiguity from the returned count:** With a one-hot query there is at most one common bit, so the count reveals that bit exactly. Multi-bit queries would return a total without identifying positions.
- **Highest legal bit:** Position 29 corresponds to $2^{29}$ and is included in `range(30)`. Position 30 corresponds to $2^{30}$ and already exceeds the maximum legal query.
- **Unreliable does not mean guaranteed zero:** The API warning forbids assuming benign behavior outside range. Correctness must hold for every behavior permitted by the contract, which the 32-query source cannot guarantee.
- **Fixed query strategy:** Results from earlier calls do not influence later queries. This makes the reasoning simple and allows each bit to be verified independently.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Under the fixed 30-bit domain, the intended algorithm performs a constant number of API queries and arithmetic operations: $O(1)$ time and $O(1)$ auxiliary space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
