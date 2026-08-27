# Guided Example: Number of Distinct Averages

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 1, 4, 0, 3, 5]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of **even** length.

The objective is to compute `2` from `{"nums": [4, 1, 4, 0, 3, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting reveals the forced pairs

Repeatedly removing the current minimum and maximum is equivalent to sorting the array once and pairing symmetric positions:

- smallest with largest;
- second smallest with second largest;
- and so on.

The input length is even, so every value belongs to exactly one pair and there is no unpaired middle element.

The source sorts `nums` in place. For `i` from zero through `n/2-1`, `nums[i]` is the next smallest remaining value and `nums[-i-1]` is the corresponding largest remaining value.

Ties do not cause ambiguity. If several equal minima or maxima exist, choosing any occurrence yields the same numeric pair values, so the multiset of calculated averages is unchanged.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 1, 4, 0, 3, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store sums instead of averages

The average of pair `a,b` is $(a+b)/2$. Two pair averages are equal exactly when their sums are equal because dividing both by the same positive constant two is one-to-one:

$$
\frac{a+b}{2}=\frac{c+d}{2}
\iff
a+b=c+d.
$$

The generator stores `nums[i]+nums[-i-1]` in a set rather than constructing floating-point values. This avoids fractions such as 2.5 and eliminates any concern about floating-point representation.

The number of distinct sums is therefore exactly the number of distinct averages.

Every possible average is either an integer or ends in one half because both inputs are integers. Multiplying an average by two recovers its pair sum exactly. There is no rounding step in the problem, so values such as 2 and 2.5 must remain distinct; their doubled values 4 and 5 remain distinct integers in the set. This scaled representation preserves all information while using exact arithmetic.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The average of pair `a,b` is $(a+b)/2$.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the example

Sorting `[4,1,4,0,3,5]` gives `[0,1,3,4,4,5]`. Symmetric pairs are:

- 0 and 5, sum 5, average 2.5;
- 1 and 4, sum 5, average 2.5;
- 3 and 4, sum 7, average 3.5.

The set of sums is `{5,7}`, whose size is two.

For `[1,100]`, only one symmetric pair exists, so the set has one member regardless of its average.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 1, 4, 0, 3, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeated minimum/maximum scans:** Literally fi:** - **Repeated minimum/maximum scans:** Literally finding extremes and deleting them each round can take $O(n^2)$ time because list deletion shifts elements.
- **Two pointers after sorting:** Explicitly advance left and right pointers while adding sums to a set. It is equivalent to the compact generator.
- **Frequency counting array:** Values are bounded from 0 to 100, so counts can simulate removals in $O(n+U)$ time with fixed domain $U$.
- **Use floating-point averages:** It works for halves of integers here, but sums are simpler and exact.
- **All pair sums equal:** The set has size one even when individual pairs contain different values.
- **Duplicate minima or maxima:** Equal choices yield the same numeric values, so arbitrary tie removal does not alter the answer.
- **Two elements:** Exactly one average is calculated.
- **Even-length guarantee:** It ensures the symmetric loop covers every value with no center leftover.
- **Zeros:** They participate normally as minima and require no special case.
- **Input mutation:** Sorting occurs in place and changes the original order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Sorting $n$ values takes $O(n\log n)$ time. Generating $n/2$ sums and inserting them into a hash set takes expected $O(n)$ additional time. Sorting dominates, giving expected $O(n\log n)$ total time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
