# Guided Example: Find Maximum Balanced XOR Subarray Length

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 1, 3, 2, 0]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return the **length** of the **longest subarray** that has a bitwise XOR of zero and contains an **equal** number of **even** and **odd** numbers. If no such subarray exists, return 0.

The objective is to compute `4` from `{"nums": [3, 1, 3, 2, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Encode both requirements as prefix-state equality

Let `a` be the bitwise XOR of the prefix through the current index. XOR of subarray `l..r` is zero exactly when the prefix XOR before `l` equals the prefix XOR through `r`, because

$$
P_{r}\mathbin{\mathrm{XOR}}P_{l-1}=0
\iff P_r=P_{l-1}.
$$

For parity balance, assign `+1` to every even value and `-1` to every odd value. Let `b` be this prefix sum. A subarray has equal even and odd counts exactly when its balance difference is zero, which again means equal prefix balances at its boundaries.

Therefore a subarray satisfies both conditions exactly when the joint prefix state

`(prefix_xor, parity_balance)`

is the same at its two boundaries.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 1, 3, 2, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Seed the empty prefix

Before reading any element, XOR and balance are both zero at boundary index `-1`. The dictionary starts with `(0,0):-1`.

This seed allows a valid subarray beginning at index zero to be measured. If the current state returns to zero at index `i`, its length is `i-(-1)=i+1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update the state for each element

`a ^= x` incorporates the current value into prefix XOR.

`b += 1 if x%2==0 else -1` updates the even-minus-odd count. Zero is classified as even because `0%2==0`.

If the resulting pair has appeared at earlier index `p`, the subarray `p+1..i` has both zero XOR and zero parity-balance change. Its length is `i-p`.

If the pair is new, the code records the current index.

As a small trace, begin from `(0,0)` at boundary `-1`. Reading odd value three changes the state to `(3,-1)`. Reading odd one changes it to `(2,-2)`. Later XOR and balance updates may return to either state; the interval between equal occurrences then cancels in both algebraic systems simultaneously.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 1, 3, 2, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all subarrays:** Incremental XOR and counts still require $O(n^2)$ endpoint pairs. Prefix-state hashing reduces this to linear expected time.
- **Store latest state indices:** This finds valid ranges but can miss the longest one. Earliest indices maximize length.
- **Track even count and odd count separately:** Only their difference matters for equality, so one signed balance is sufficient.
- **Use element sum parity:** Equal numbers of even and odd elements is not determined by numeric sum parity.
- **Target XOR only:** The tuple must include parity balance as a second independent invariant.
- **Single zero:** XOR is zero but parity counts are one even and zero odd, so the answer remains zero.
- **Whole-array solution:** The empty-prefix seed detects it when the final state is `(0,0)`.
- **No valid subarray:** No useful state repetition occurs and `ans` remains zero.
- **Zero values:** They alter no XOR but do add one to the even count.
- **Negative balance:** More odd than even prefixes are expected; dictionary keys handle negative integers.
- **Duplicate values:** XOR and parity updates operate per position, so every occurrence is accounted for.
- **State repeats many times:** The first occurrence stays stored, while every later repeat tests a potentially longer endpoint.
- **Even and odd counts both zero:** Only the empty interval has this property before scanning; nonempty valid intervals contain at least one of each parity.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. The scan performs expected constant-time dictionary operations per element, giving expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
