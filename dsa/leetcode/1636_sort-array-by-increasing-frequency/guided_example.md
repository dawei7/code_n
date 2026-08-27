# Guided Example: Sort Array by Increasing Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 2, 2, 2, 3]}`
- **Required output:** `[3, 1, 1, 2, 2, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums`, sort the array in **increasing** order based on the frequency of the values. If multiple values have the same frequency, sort them in **decreasing** order.

The objective is to compute `[3, 1, 1, 2, 2, 2]` from `{"nums": [1, 1, 2, 2, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the two sorting rules into one key

Every element is ranked by two criteria:

1. a smaller frequency comes first;
2. when frequencies tie, a larger numeric value comes first.

Python's sorting key can represent both criteria as a tuple. Tuples are compared from left to right, so the source uses

`(cnt[x], -x)`.

The first component is the frequency and is naturally sorted upward. The second is the negated value. If $x_1>x_2$, then $-x_1<-x_2$, so ordinary ascending order on the negatives places the larger original value first.

Combining the rules into one tuple avoids writing a custom pairwise comparator and makes the priority order explicit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 2, 2, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count before sorting

`Counter(nums)` traverses the input and creates `cnt`, a mapping from each distinct value to its number of occurrences. Every later key computation can then retrieve `cnt[x]` in expected constant time.

Counting first is essential. Frequency is a property of the complete input, not of the part of the list already visited by the sorting algorithm. Trying to update counts while sorting would make keys unstable and invalidate comparison consistency.

The source then calls `sorted(nums, key=...)`. `sorted` returns a new list and leaves `nums` unchanged. The key function is evaluated for the input elements, and the resulting keys determine their order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `Counter(nums)` traverses the input and creates `cnt`, a map... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why repeated values remain together

Every occurrence of the same integer `x` receives the identical tuple `(cnt[x], -x)`. Therefore no different key can be ordered between two occurrences of `x` once the full sort is complete. Repeated values form one contiguous block.

Within that block, occurrence order does not matter because the values are identical. Across blocks, the first tuple component orders frequencies, and the second orders values descending among equal frequencies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 1, 1, 2, 2, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 2, 2, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 1, 1, 2, 2, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Count distinct values, sort the keys, then exp:** - **Count distinct values, sort the keys, then expand blocks:** Sort the $k$ unique values by `(frequency, -value)` and append each value its frequency times. This costs $O(n+k\log k)$ and can reduce comparison work when many values repeat.
- **Bucket by frequency:** Frequencies range from 1 through $n$. Values in each bucket can be sorted descending, then expanded. This can be useful with a tightly bounded value domain but requires more bookkeeping.
- **Custom comparator:** Compare counts first and values second. It is equivalent, but a tuple key is shorter and avoids repeatedly looking up comparison operands during sorting.
- **All values distinct:** Every frequency is one, so the entire output is the input values sorted in decreasing numeric order.
- **All values equal:** All occurrences have the same key and the returned list is unchanged in value.
- **Two values share a frequency:** The numerically larger one must come first; negation converts that descending rule into ascending-key order.
- **Negative integers:** Negation still reverses numeric order correctly. “Larger” means, for example, $-1>-6$.
- **Zero:** Its secondary key is also zero and participates normally between positive and negative values.
- **Input preservation:** `sorted` returns a new list. Using `nums.sort` would mutate the caller's array, which the exact source does not do.
- **Stable sorting is not relied upon:** Equal values have identical keys, and their relative occurrence order is unobservable. Different values are fully distinguished by the secondary component when counts tie.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let $n$ be the number of input elements and $k$ the number of distinct values. Building the Counter takes $O(n)$ expected time and $O(k)$ space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
