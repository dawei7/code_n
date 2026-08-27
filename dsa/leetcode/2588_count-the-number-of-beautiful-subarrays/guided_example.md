# Guided Example: Count the Number of Beautiful Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 3, 1, 2, 4]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. In one operation, you can:

The objective is to compute `2` from `{"nums": [4, 3, 1, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Analyze each bit independently

An operation chooses a bit position $k$ that is one in two different elements and subtracts $2^k$ from both.

When bit $k$ of a nonnegative integer is one, subtracting $2^k$ clears exactly that bit without borrowing from higher bits or changing lower bits. Therefore, every operation removes two occurrences of one from the same bit position across the subarray.

For all values to become zero, every set-bit occurrence must be paired with another occurrence at the same position. A subarray is beautiful exactly when the number of ones is even at every bit position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 3, 1, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why even bit counts are also sufficient

If every bit position contains an even number of ones, take any bit $k$ and pair its set occurrences arbitrarily. Apply one operation to each pair. This clears bit $k$ from every element.

Operations for one bit do not change other bit positions, so repeat independently for every bit. Eventually every set bit is cleared and all elements become zero.

Thus even parity at every bit is both necessary and sufficient, not merely a useful test.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If every bit position contains an even number of ones, take ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: XOR stores all bit parities at once

At each bit position, XOR is one exactly when an odd number of operands have that bit set. Therefore, the XOR of all elements in a subarray is zero exactly when every bit has even parity.

The operational definition of beautiful subarrays collapses to:

$$
\text{subarray is beautiful}
\quad\Longleftrightarrow\quad
\text{subarray XOR}=0.
$$

This transformation is the main insight. No operation sequence needs to be simulated.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 3, 1, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate operations:** Choosing bit pairs expl:** - **Simulate operations:** Choosing bit pairs explicitly is unnecessary and combinatorial; parity completely characterizes feasibility.
- **Check every subarray:** Computing XOR for all $O(n^2)$ subarrays is too slow for $10^5$ elements.
- **Track parity per bit:** A vector of bit parities works, but XOR packs the same state into one integer.
- **Single zero:** Its XOR is zero, so the one-element subarray is beautiful.
- **Single nonzero:** At least one bit has odd parity, so it is not beautiful.
- **All zeros:** Every subarray counts, producing the maximum $n(n+1)/2$.
- **Repeated prefix XOR:** Each prior occurrence gives a distinct starting boundary and must be counted.
- **Empty prefix seed:** Omitting `cnt[0] = 1` would miss beautiful subarrays starting at index zero.
- **Nonempty requirement:** Updating the answer before the frequency prevents pairing a prefix with itself.
- **Expected hashing:** Linear time assumes standard expected constant-time Counter lookup.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The loop performs one XOR and expected constant-time Counter operations per element, giving expected $O(n)$ time. There can be up to $n+1$ distinct prefix XOR values, so the Counter uses $O(n)$ space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
