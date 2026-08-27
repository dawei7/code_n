# Guided Example: Height Checker

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [1, 1, 4, 2, 1, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where $\text{expected}[i]$ is the expected height of the $$i^{\text{th}}$$ student in line.

The objective is to compute `3` from `{"heights": [1, 1, 4, 2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What the expected arrangement means

The students currently stand in the order recorded by `heights`. The school wants them arranged in non-decreasing height order. Non-decreasing means that every height is at least the height immediately before it. Equal heights are allowed, so a sequence such as `[1, 1, 3, 3, 7]` is correctly ordered.

The task does not ask us to move the students or report the correct arrangement. It asks for the number of indices whose current height differs from the height that belongs at that index in the expected arrangement.

That distinction matters. Suppose the current sequence is `[1, 2, 1]`. Its expected sequence is `[1, 1, 2]`. Index zero already contains the expected value. Indices one and two do not, so the answer is two. We compare the two sequences position by position; we do not merely ask whether the input contains the right collection of heights, because it obviously does.

The expected height sequence is determined uniquely by sorting all values into non-decreasing order. Duplicate heights do not create ambiguity for this problem. Two students of the same height may exchange identities, but the value placed at each index remains the same. Since the answer depends only on heights, not student identities, a sorted list of height values is exactly the reference sequence we need.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [1, 1, 4, 2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the reference sequence without changing the input

The first line is:



Python's `sorted` function reads every value from `heights` and returns a new list whose values are in ascending, and therefore non-decreasing, order. The original `heights` list remains unchanged.

Keeping both lists is essential to this implementation. `heights` represents what we actually observe, while `expected` represents what should be at every position. If the code instead called `heights.sort()` and did not first preserve the original order, it would lose the very information it needs to find mismatches. After an in-place sort, comparing the list with itself would incorrectly produce zero for every input.

For example, with `heights = [1, 1, 4, 2, 1, 3]`, sorting produces `expected = [1, 1, 1, 2, 3, 4]`. This one operation does all of the ordering work. The remaining task is a linear positional comparison.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first line is:



Python's `sorted` function reads every... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Align corresponding indices

The expression `zip(heights, expected)` produces pairs in matching index order. Its first pair contains `heights[0]` and `expected[0]`, its second pair contains the two values at index one, and so on.

Normally, `zip` stops when its shorter input is exhausted. That behavior cannot hide any value here because `expected` was created by sorting `heights`. Sorting neither inserts nor removes elements, so the two lists always have exactly the same length. Consequently, `zip` visits every valid index exactly once.

For the example above, the aligned pairs are:



The first, second, and fourth pairs match. The third, fifth, and sixth pairs differ. Therefore the correct answer is three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [1, 1, 4, 2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency counting for the manifest target:** :** - **Frequency counting for the manifest target:** Allocate counts for all heights from one through `H`, then visit height values in increasing order. Each stored occurrence represents the next expected height. Compare it with the next position of the original list and count a mismatch when they differ. This avoids comparison sorting and achieves `O(N + H)` time with `O(H)` space.
- **Counting without materializing the expected list:** A frequency array does not need to expand into a second list. Keep an index into `heights` and compare it against each height value repeated according to its frequency. This retains the same optimal bounds and saves the separate `O(N)` reference list.
- **In-place sorting after making a copy:** One could copy the original list and sort either copy in place. This is equivalent in purpose to `sorted` but more verbose. Sorting the only copy of the original order is incorrect because it destroys the baseline needed for comparison.
- **Manual mismatch loop:** An explicit counter and loop over indices produce the same answer as `sum(a != b for a, b in zip(heights, expected))`. That form may be useful while learning, but it does not improve the complexity.
- **Bubble sort:** Repeated neighboring swaps can construct the expected sequence, but its `O(N^2)` time is worse than both comparison sorting and frequency counting. The small input limit may allow it to finish, yet it ignores the stronger structure of the height range.
- **Already sorted input:** When `heights` is already non-decreasing, `expected` equals it at every index. Every comparison is false, so the sum correctly returns zero.
- **One student:** A one-element list is necessarily non-decreasing. The single aligned pair matches and the result is zero.
- **All heights equal:** Sorting does not change the sequence. Student identities are irrelevant because every position contains the same height, so the result is zero.
- **Reverse order:** A descending input usually creates many mismatches, but a middle value in an odd-length list may remain at the same index after sorting. The algorithm compares positions rather than assuming every element must be counted.
- **Duplicate heights:** Repeated values are retained with their exact frequencies. The method counts only value mismatches and does not incorrectly distinguish students who have equal heights.
- **Values at the limits:** Heights of one and 100 are ordinary sortable values. A counting implementation must size and index its frequency storage carefully enough to include both endpoints.
- **No required output ordering beyond the count:** The function returns one integer, so no reconstruction or reporting of mismatching indices is necessary.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of students.
- **Auxiliary Space Complexity:** $O(H)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
