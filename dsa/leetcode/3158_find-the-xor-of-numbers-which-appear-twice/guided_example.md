# Guided Example: Find the XOR of Numbers Which Appear Twice

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 3]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums`, where each number in the array appears **either*** *once* *or* *twice.

The objective is to compute `1` from `{"nums": [1, 2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate frequency detection from XOR aggregation

The result includes a value exactly when its total frequency is two. The exact source first builds

`cnt = Counter(nums)`,

which maps every distinct number to how many times it appears.

The list comprehension

`[x for x, v in cnt.items() if v == 2]`

keeps only keys whose frequency is exactly two. Under the problem guarantee that each number appears once or twice, this is precisely the set of duplicated values.

Finally,

`reduce(xor, duplicated_values, 0)`

folds bitwise XOR across that list, starting from zero. The identity $0\mathbin{\operatorname{XOR}}x=x$ makes the initial value neutral.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why each duplicate is XORed once

We must XOR the numbers that appear twice, not XOR every occurrence in the original array. XORing the original array directly would cancel each duplicate because $x\operatorname{XOR}x=0$ and would instead leave values appearing once—the opposite of the requested set.

The counter's key appears once regardless of its frequency. Filtering the key and reducing it means a duplicated number contributes exactly one copy to the final XOR.

For `[1,2,2,1]`, the filtered list contains 1 and 2. The reduction computes $0\operatorname{XOR}1\operatorname{XOR}2=3$.

For `[1,2,3]`, the filtered list is empty. `reduce` returns its initializer 0, matching the required result when no number appears twice. Without the initializer, reducing an empty list would raise an error.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | We must XOR the numbers that appear twice, not XOR every occ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: XOR order does not matter

Bitwise XOR is associative and commutative:

$$
(a\oplus b)\oplus c=a\oplus(b\oplus c)
$$

and

$$
a\oplus b=b\oplus a.
$$

Therefore, the iteration order of `Counter.items()` does not affect the answer. The code need not sort duplicated values.


For each distinct input value $x$, `Counter` records its exact frequency. The constraint limits that frequency to one or two. The comprehension selects $x$ if and only if it belongs to the problem's duplicate set.

The reduction then computes the XOR of every selected value exactly once and nothing else. This is the requested mathematical result. If the set is empty, the identity initializer produces zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Seen bit mask:** Set bit $x$ on first occurren:** - **Seen bit mask:** Set bit $x$ on first occurrence; on second occurrence, XOR $x$ into the answer. This matches the manifest and uses one fixed-size integer for values up to 50.
- **Seen set:** Add unseen values and XOR a value when it is already present. It uses $O(u)$ space but avoids a second pass and filtered list.
- **Frequency array of length 51:** Count values in fixed slots, then XOR indices with count two. It has constant domain-bounded storage.
- **XOR the whole input:** Incorrect because duplicate pairs cancel and singletons remain.
- **No duplicated value:** The initializer makes the reduction return zero.
- **One duplicated value:** The output is that value because zero is XOR's identity.
- **Several duplicates:** Associativity and commutativity make iteration order irrelevant.
- **Values appearing exactly twice:** Each counter key is selected once, not twice.
- **Frequency greater than two outside the contract:** `v == 2` would exclude it; correctness relies on the once-or-twice guarantee.
- **Duplicate list allocation:** A generator expression could feed `reduce` lazily and avoid this extra list, but the exact code builds it.
- **Fixed small domain:** It enables the constant-space alternatives but does not change the source's data structures.
- **Input preservation:** Counting reads the array and leaves it intact.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the input length and $u$ the number of distinct values.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
