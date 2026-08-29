# Guided Example: Reduce Array Size to The Half

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `arr`. You can choose a set of integers and remove all the occurrences of these integers in the array.

The objective is to compute `2` from `{"arr": [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compress the array into frequencies

`Counter(arr)` maps each distinct value to its number of occurrences. If the input is `[3, 3, 3, 5, 5, 2]`, the frequency multiset is three, two, and one. The specific keys still identify which values would be selected, but the required return value is only the number of selected values, so the loop needs only the counts.

`cnt.most_common()` returns `(value, frequency)` pairs ordered from greatest frequency to least frequency. The loop unpacks each pair as `_, v`. The underscore discards the actual value, while `v` is the number of array positions removed by selecting it.

Two accumulators have distinct meanings:

- `m` is the total number of array elements covered by all frequencies selected so far.
- `ans` is the number of distinct values selected, which is the size of the removal set.

For each descending frequency, the code adds `v` to `m` and increments `ans` once. It stops as soon as `m * 2 >= len(arr)`. Multiplying by two avoids floating-point division and states “removed at least half” exactly.

For example, frequencies `[4, 3, 2, 1]` for an array of length ten have a target of five removed elements. Taking four is insufficient. Taking the next frequency three raises the removed total to seven, so two distinct values are enough. The code returns two without needing to build the shortened array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why taking the largest remaining frequency is safe

Suppose the frequencies in descending order are

$$
f_1 \ge f_2 \ge \cdots \ge f_u,
$$

where $u$ is the number of distinct values. Among every possible set of $r$ distinct values, the greatest number of removable elements is $f_1 + f_2 + \cdots + f_r$. Any set that omits one of those top frequencies and includes a smaller frequency instead can remove no more elements; swapping the smaller choice for the omitted larger one never hurts.

Let the loop stop after $r$ frequencies. Their sum reaches at least half of the array. The first $r - 1$ frequencies did not reach half, because otherwise the loop would already have stopped. Since those largest $r - 1$ frequencies are the maximum removal achievable with any $r - 1$ chosen values, no set of size $r - 1$ can meet the target. A set of size $r$ does meet it, so $r$ is the minimum.

This argument also explains why ties do not need a special rule. If several values have the same frequency, choosing any of them removes the same number of elements. `most_common` may order tied keys according to encounter order, but `ans` is unchanged.

The algorithm never mutates `arr` and never simulates deletion. It reasons only about coverage counts, which are enough because removing one value cannot change the number of occurrences belonging to another distinct value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Bucket frequencies:** A frequency cannot exceed $n$, so count how many values occur with each possible frequency and scan buckets downward. This yields $O(n)$ time and $O(n)$ space, avoiding comparison sorting.
- **Sort the original array:** Equal values become adjacent, allowing run lengths to be counted and then sorted. It still takes $O(n\log n)$ time and mutates the input unless a copy is made.
- **Max-heap of frequencies:** Repeatedly pop the largest count until the target is reached. Heap construction can be linear, and each selected value costs $O(\log u)$, which can help when very few values are needed.
- **Choosing values in input order:** This is not optimal because a rare value can consume one set entry while removing very few elements. Frequency order is the property supported by the exchange argument.
- **Exactly half removed:** The condition is inclusive. When `m * 2 == len(arr)`, the requirement has been met and the loop must stop.
- **More than half removed:** Removing all occurrences can overshoot the target, and overshooting is permitted. There is no need to remove only part of the final value’s occurrences.
- **All values equal:** The first frequency is $n$, so one selected integer empties the array and the answer is one.
- **All values distinct:** Every frequency is one. Because the input length is even, exactly $n / 2$ distinct values must be selected.
- **Tied frequencies:** Their internal order cannot affect how many selections are required because equal counts contribute equal coverage.
- **Large integer values:** The counter keys need not form a small numeric range. Complexity depends on the number of elements and distinct keys, not the magnitude of the values.
- **Odd length outside the contract:** The multiplication test would require removal of at least the ceiling of half and still works correctly, even though the stated array length is even.
- **Empty input outside the contract:** The code would return zero because the loop has no entries. The official constraints begin at length two, so the normal proof assumes a positive target.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length and $u$ the number of distinct values.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
