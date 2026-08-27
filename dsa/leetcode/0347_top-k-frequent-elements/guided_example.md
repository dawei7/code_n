# Guided Example: Top K Frequent Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}`
- **Required output:** `[1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

The objective is to compute `[1, 2]` from `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The exact source delegates ranking to `Counter.most_common`.

The method has two logical stages. First, `Counter(nums)` counts how many times each distinct integer appears. Second, `cnt.most_common(k)` asks the library for the `k` entries with greatest counts. Each returned entry is a pair `(value, frequency)`, and the final list comprehension keeps only `value`.

This is not the frequency-bucket algorithm named in the manifest. No array of buckets is created and no downward frequency scan appears in the checked-in source.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the frequency map.

`Counter` is a dictionary-like collection. Scanning

`[1,1,1,2,2,3]`

produces the conceptual mapping

$$
1\mapsto3,\qquad
2\mapsto2,\qquad
3\mapsto1.
$$

There is one entry per distinct input value, not one entry per occurrence. Negative numbers and zero work like any other hashable integer; their numeric size does not affect the counting logic.

The map's frequency for a value is exact because every input occurrence increments that value's count once. No other key is affected.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `Counter` is a dictionary-like collection.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Ask for the most common entries.

`cnt.most_common(k)` returns up to `k` `(element, count)` pairs ordered from greatest frequency toward smaller frequency. The contract guarantees that `k` is no greater than the number of distinct values, so exactly `k` pairs are returned.

For the example mapping, `most_common(2)` returns pairs equivalent to

`[(1, 3), (2, 2)]`.

The source does not need the counts after ranking. Its list comprehension iterates as `for x, _ in ...`: `x` names the element and `_` conventionally marks the frequency as intentionally unused. The resulting answer is `[1,2]`.

The problem permits any output order. The library's descending-frequency order is acceptable but not required by the contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency buckets:** Create `n + 1` lists wher:** - **Frequency buckets:** Create `n + 1` lists where bucket `f` holds values occurring `f` times. Scan frequencies from `n` down until `k` values are collected. Counting, bucket insertion, and scanning are all $O(n)$, with $O(n)$ space. This meets the follow-up and matches the manifest.
- **- **Min-heap of size `k`:** Count frequencies, the:** - **Min-heap of size `k`:** Count frequencies, then keep only the `k` largest while scanning distinct values. This takes $O(n+u\log k)$ time and $O(u+k)$ space, useful when `k` is small.
- **- **Quickselect:** Partition the distinct values b:** - **Quickselect:** Partition the distinct values by frequency and return the top side. It has $O(n+u)$ expected time but $O(u^2)$ worst-case selection time without a worst-case pivot strategy.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let $n$ be `len(nums)`, let $u$ be the number of distinct values, and retain `k` as the requested output size.
- **Auxiliary Space Complexity:** $O(u+k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
