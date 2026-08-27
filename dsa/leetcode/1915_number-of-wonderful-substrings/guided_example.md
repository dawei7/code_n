# Guided Example: Number of Wonderful Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "aba"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **wonderful** string is a string where **at most one** letter appears an **odd** number of times.

The objective is to compute `4` from `{"word": "aba"}` while avoiding redundant calculations and unnecessary overhead.

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

**Track parity, not full frequencies.** Whether a substring is wonderful depends only on which character counts are odd. Exact counts are unnecessary. Since input uses only `a` through `j`, a ten-bit integer can store all parities: bit zero for `a`, bit one for `b`, and so on. A set bit means the count in the represented prefix is odd.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "aba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Update a prefix mask with XOR.** `st` starts at zero for the empty prefix. Reading character `c` computes its bit position `ord(c) - ord("a")` and toggles that bit with XOR. Seeing the same character again toggles it back, exactly matching even/odd count changes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Update a prefix mask with XOR.** `st` starts at zero for t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**A substring is the XOR of two prefix masks.** Let one prefix end just before a substring and the other end at the substring's right boundary. XOR cancels characters appearing with the same parity in both prefixes, leaving the parity mask of their difference—the substring. Therefore, prior prefix mask `q` and current mask `st` form a wonderful substring when `st ^ q` has either zero set bits or exactly one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "aba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Array of 1024 frequencies:** Direct mask index:** - **Array of 1024 frequencies:** Direct mask indexing avoids dictionary overhead and makes constant bounded storage explicit.
- **Count full frequency vectors:** Much larger states are unnecessary because only parity matters.
- **Enumerate substrings:** Updating counts for all $O(N^2)$ substrings is too slow; prefix-mask pairs aggregate them by state.
- **Single character:** Current mask differs from the empty prefix by one bit, so the one substring is counted.
- **All same character:** Every substring has either zero or one odd count, so all $N(N+1)/2$ occurrences are wonderful.
- **All-even substring:** Equal prefix masks count it through `cnt[st]`.
- **Exactly one odd letter:** One-bit neighbor masks count it, regardless of that letter's actual odd frequency magnitude.
- **Two odd letters:** Prefix masks differ in two bits and are intentionally absent from both queried categories.
- **Alphabet restriction:** Ten neighbor checks rely on letters `a` through `j`. A larger alphabet changes mask width and constant factors.
- **Update order:** Incrementing `cnt[st]` before queries would count an empty substring at every position; the source correctly increments afterward.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(NA)$. Let $N$ be word length and $A=10$ the alphabet size. Each character performs one mask update, one equal-mask lookup, and ten one-bit-neighbor lookups. Time is $O(NA)$, which is $O(N)$ because $A$ is fixed at ten.
- **Auxiliary Space Complexity:** $O(2^{10})$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
