# Guided Example: Split the Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 2, 2, 3, 4]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of **even** length. You have to split the array into two parts `nums1` and `nums2` such that:

The objective is to compute `true` from `{"nums": [1, 1, 2, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

**Translate two distinct halves into a frequency limit.** Each output part must contain distinct elements. Therefore one particular value can appear at most once in `nums1` and at most once in `nums2`. Across both parts, any value may appear at most twice.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 2, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This gives an immediate necessary condition:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | This gives an immediate necessary condition:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
\max_v \operatorname{count}(v)\le2.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 2, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Construct both parts greedily:** It can work b:** - **Construct both parts greedily:** It can work but requires balancing logic that the frequency proof makes unnecessary.
- **Sort and detect triples:** Three equal consecutive values after sorting imply impossibility. That costs $O(N\log N)$ time and may mutate or copy input.
- **Fixed 101-entry frequency array:** It exploits the value bound and has deterministic constant space, equivalent to the counter approach.
- **Every value distinct:** Maximum frequency is one; because length is even, divide the values arbitrarily into equal halves.
- **Every value appears twice:** Put one occurrence of each value in each part; sizes automatically match.
- **Exactly one value appears three times:** The answer is already false regardless of all other values.
- **Length two:** Any two values are splittable into one-element parts, even if equal, because each individual part is distinct.
- **Even-length guarantee:** It is essential for equal-sized halves and for singleton count parity in the sufficiency proof.
- **Bounded values:** This is why the manifest can call the counter storage constant space.
- **Input preservation:** Counting reads elements without reordering or changing them.
- **Why there is no separate half-capacity test:** Once duplicate values contribute one element to each half, every remaining value is a unique singleton and may go to either side. Even singleton count guarantees an exact equal split, so frequency at most two already contains the size argument.
- **Counter maximum versus checking all counts:** `max < 3` is logically equivalent to `all(count <= 2)`. The maximum form is concise because the counter cannot be empty under the input guarantee.
- **Copies remain distinguishable by position:** Two equal occurrences may be placed in different arrays even though their values match. The requirement is distinctness within each part, not across the union.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let $N$ be input length and $U$ the number of distinct values. Building the counter takes $O(N)$ expected time, and finding its maximum takes $O(U)$. Total expected time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
