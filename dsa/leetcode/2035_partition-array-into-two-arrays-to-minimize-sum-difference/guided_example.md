# Guided Example: Partition Array Into Two Arrays to Minimize Sum Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 9, 7, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of $2 * n$ integers. You need to partition `nums` into **two** arrays of length `n` to **minimize the absolute difference** of the **sums** of the arrays. To partition `nums`, put each element of `nums` into **one** of the two arrays.

The objective is to compute `2` from `{"nums": [3, 9, 7, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent a partition as a signed sum

Call the two destination arrays $A$ and $B$. Assign a positive sign to every element placed in $A$ and a negative sign to every element placed in $B$. Then

$$
\sum A-\sum B
$$

is exactly the sum of those signed contributions, and the requested objective is its absolute value.

The extra restriction is cardinality: because the input has $2n$ elements, exactly $n$ signs must be positive and $n$ must be negative.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 9, 7, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Split the input for meet in the middle

Enumerating all assignments directly would inspect $2^{2n}$ possibilities. The source splits `nums` into two halves of length `n` and enumerates only the `2^n` masks for each half.

For one mask, a set bit means the corresponding element is assigned to $A$ and contributes positively. An unset bit means it is assigned to $B$ and contributes negatively.

For the first half, the loop computes signed difference `s` and number of selected positive elements `cnt`, then stores `s` in `f[cnt]`. It performs the analogous calculation for the second half and stores `s1` in `g[cnt1]`.

The same numeric mask is used to generate one entry for each half during an iteration, but the stored collections are independent. Because the loop visits every possible mask, both `f` and `g` receive every subset pattern for their respective half. A later combination may pair values produced by completely different masks.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Enumerating all assignments directly would inspect $2^{2n}$ ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why grouping by selected count is necessary

Suppose a first-half assignment selects `i` elements for $A$. To make $A$ contain exactly `n` elements overall, the second-half assignment must select exactly `n-i` elements.

That is why the combination phase pairs `f[i]` with `g[n-i]`. Every combined pair has $i+(n-i)=n$ positive signs and therefore produces two destination arrays of the required equal length.

Without this grouping, a very small signed difference might correspond to partitions with unequal numbers of elements and would be invalid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 9, 7, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all full assignments:** Costs $O(2^{:** - **Enumerate all full assignments:** Costs $O(2^{2n})$ and misses the meet-in-the-middle advantage.
- **Subset sums using the total sum:** Minimize `abs(total - 2 * selected_sum)` with exactly `n` selected elements; it is algebraically equivalent.
- **Dynamic programming by numerical sum:** Input magnitudes make a sum-indexed table impractically large.
- **Brute-force combinations:** Enumerating all $\binom{2n}{n}$ equal-size selections remains much larger than the half enumeration.
- **Difference zero:** It is globally optimal and corresponds to equal partition sums.
- **One element per destination:** Both possible assignments are represented when `n=1`.
- **All values negative:** Signed sums and absolute value remain valid.
- **Duplicate values or differences:** Sets safely merge equivalent objective states.
- **Choose zero elements from one half:** Group `f[0]` pairs with `g[n]`.
- **Choose all elements from one half:** Group `f[n]` pairs with `g[0]`.
- **Even group size is irrelevant:** Binary search operates on distinct sorted differences, not original subset multiplicities.
- **Exact complement absent:** Checking the lower bound and predecessor finds the nearest available value.
- **Input preservation:** Masks read `nums` without modifying it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n2^n)$. Here $n$ is half the input length. The mask-generation loop has $2^n$ masks and examines $n$ bit positions for each, taking $O(n2^n)$ time.
- **Auxiliary Space Complexity:** $O(2^n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
