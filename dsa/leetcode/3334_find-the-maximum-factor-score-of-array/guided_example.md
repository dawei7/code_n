# Guided Example: Find the Maximum Factor Score of Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 4, 8, 16]}`
- **Required output:** `64`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `64` from `{"nums": [2, 4, 8, 16]}` while avoiding redundant calculations and unnecessary overhead.

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

**Evaluate no deletion and every single deletion.** The factor score is $\gcd(\text{array})\cdot\operatorname{lcm}(\text{array})$. Removing an element changes both aggregates, so a locally unusual value can improve the product. Testing each deletion by recomputing over all remaining elements would be quadratic. Prefix and suffix aggregates let the source combine the elements on either side in constant aggregate operations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 4, 8, 16]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Build suffix GCD and LCM arrays.** `suf_gcd[i]` is the GCD of `nums[i:]`, while `suf_lcm[i]` is its LCM. The base identities are zero for an empty GCD and one for an empty LCM:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Build suffix GCD and LCM arrays.** `suf_gcd[i]` is the GCD... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
\gcd(0,x)=x,\qquad\operatorname{lcm}(1,x)=x.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `64` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 4, 8, 16]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `64` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recompute per deletion:** It uses $O(1)$ extra:** - **Recompute per deletion:** It uses $O(1)$ extra space but $O(n^2\log M)$ time.
- **Prefix arrays on both sides:** Store prefix and suffix GCD/LCM arrays. It is equally linear but uses more arrays than the running-prefix source.
- **Exclude no element:** This candidate must be included because deletion can reduce the score, as in arrays already balancing GCD and LCM well.
- **One element:** No deletion yields $x^2$, while deleting it yields the defined empty score zero.
- **Remove first or last:** Empty aggregate identities make endpoint cases require no branches.
- **All values equal:** No-removal score is $x^2$; deletion leaves the same score unless the array had one element.
- **Value one:** It can reduce GCD without increasing LCM, so removing it may improve the score.
- **LCM growth:** Even small elements can create a large LCM; Python handles it but other languages need wide types or overflow analysis.
- **Duplicate values:** Aggregates naturally account for multiplicity; deleting one duplicate may leave GCD and LCM unchanged.
- **Update order:** Prefix aggregates must be updated after evaluating deletion $i$.
- **Import requirement:** The snippet depends on both `gcd` and `lcm` being available.
- **Input preservation:** Suffix construction and prefix scanning never modify `nums`.
- **Why both aggregates are needed:** Optimizing only the GCD or only the LCM is insufficient because deletion can improve one while worsening the other. The score compares their product for each complete candidate.
- **Suffix base construction:** `[0] * (n + 1)` and `[0] * n + [1]` deliberately give different empty identities. Swapping them would corrupt every endpoint deletion.
- **Small bounded values:** Although each input is at most 30, the LCM can combine prime powers from many values. Complexity and integer-width reasoning should use aggregate magnitudes, not only one element's magnitude.
- **Optional deletion proof:** The initial no-removal score is not duplicated by the loop conceptually; even if some deletion produces the same numeric value, both are legal candidates and `max` handles equality harmlessly.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log M)$. There are two linear passes. Each step performs a constant number of GCD/LCM operations. Euclid's algorithm gives logarithmic arithmetic time in operand magnitude, so a conventional bound is $O(n\log M)$ under the small-value constraints, though intermediate LCM operands may exceed individual $M$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
