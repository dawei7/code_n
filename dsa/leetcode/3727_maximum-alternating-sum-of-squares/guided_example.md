# Guided Example: Maximum Alternating Sum of Squares

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `12`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. You may **rearrange the elements** in any order.

The objective is to compute `12` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: After squaring, only the choice of plus or minus positions matters

For an arrangement of length `n`, indices zero, two, four, and so on have positive signs. Indices one, three, five, and so on have negative signs. Therefore there are

$$
\left\lceil\frac{n}{2}\right\rceil
$$

positive slots and

$$
\left\lfloor\frac{n}{2}\right\rfloor
$$

negative slots.

An element contributes its square, so `x` and `-x` have the same magnitude:

$$
(-x)^2=x^2.
$$

The original signs and the order within the positive slots do not affect the score. Likewise, order within the negative slots does not affect it. The entire optimization is to decide which squared magnitudes receive plus signs and which receive minus signs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Largest squares belong in positive slots

Suppose an arrangement assigns square `a` to a positive slot and a larger square `b` to a negative slot, where `a < b`. Their contribution is initially

$$
a-b.
$$

Swap the corresponding elements, so `b` becomes positive and `a` becomes negative. Their new contribution is

$$
b-a.
$$

The score improvement is

$$
(b-a)-(a-b)=2(b-a)>0.
$$

Thus an arrangement with a smaller square added and a larger square subtracted cannot be optimal. Repeatedly removing such inverted assignments leaves all negative-slot squares no larger than all positive-slot squares.

It follows that the `floor(n / 2)` smallest squares must occupy the negative positions, and the remaining `ceil(n / 2)` largest squares must occupy the positive positions. This rule also handles ties: swapping equal squares changes nothing, so any distribution of equal boundary values is optimal.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose an arrangement assigns square `a` to a positive slot... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the exact source creates the two groups

The code sorts `nums` in place with

`nums.sort(key=lambda x: x * x)`.

The key is the square, not the signed numeric value. This distinction matters when negative numbers occur. Ordinary ascending order would place a large negative value early even though its square is large. Sorting by `x * x` produces nondecreasing squared magnitude.

Let `m = n // 2`. The first slice `nums[:m]` contains exactly the `m` smallest squares, which must be subtracted. The remaining slice `nums[m:]` contains `n - m = ceil(n / 2)` elements, which must be added.

The source computes

`s1 = sum(x * x for x in nums[: n // 2])`

and

`s2 = sum(x * x for x in nums[n // 2 :])`,

then returns `s2 - s1`. This is the maximum sum of positive-slot squares minus the minimum group assigned to negative slots.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `12` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `12` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all permutations:** Up to `n!` arran:** - **Enumerate all permutations:** Up to `n!` arrangements exist, even though the score depends only on the two sign groups. The exchange argument reduces the problem to one sort.
- **Sort by the raw integer value:** This is wrong for negatives. For example, `-100` sorts before `2` numerically but has the much larger square and should receive a positive sign.
- **Sort a separate square array:** This produces the same grouping and can make the mathematical reduction explicit. The exact source sorts original values by a square key and squares them while summing, avoiding another stored numeric array.
- **Greedily alternate largest and smallest original values:** A constructed arrangement can work if it assigns square groups correctly, but raw signed size is not the relevant order. Grouping by squares first is safer.
- **Put the smallest squares in positive slots:** That minimizes rather than maximizes the expression because it forces large magnitudes to be subtracted.
- **Odd array length:** There is one more positive slot. `n // 2` selects only the smaller floor half for subtraction and assigns the entire larger ceiling half to addition.
- **Single element:** There are zero negative slots and one positive slot. The first slice is empty, `s1 = 0`, and the answer is the element's square.
- **Zero values:** A zero contributes nothing under either sign. Sorting places it among the smallest squares, usually in a negative slot when one is available, which is never worse.
- **Equal absolute values with opposite signs:** Their squares tie, and either can occupy either group without changing the score.
- **All values negative:** Squaring removes their signs. The same smallest-versus-largest square split remains valid.
- **Already sorted input:** The in-place sort may do less practical work, but the worst-case bound remains $O(n\log n)$.
- **Mutation-sensitive caller:** Sorting a copy would preserve the original list at an additional $O(n)$ allocation. The problem method's contract does not require preservation.
- **Large result:** Summation must use a wide numeric type even though each individual input fits comfortably in 32 bits.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n` be the number of elements. Sorting by squared magnitude takes $O(n\log n)$ time. Computing each key is constant time under the bounded integer model. The two generator-based sums together square and visit every element once, adding $O(n)$ time. The total time complexity is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
