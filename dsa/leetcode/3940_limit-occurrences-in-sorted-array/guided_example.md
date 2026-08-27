# Guided Example: Limit Occurrences in Sorted Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}`
- **Required output:** `[1, 1, 2, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **sorted** integer array `nums` and an integer `k`.

The objective is to compute `[1, 1, 2, 2, 3]` from `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The first element is always retained

The constraints guarantee that `nums` is nonempty and `k >= 1`. Therefore the first occurrence of the first value must be kept.

The chained assignment

`cnt = l = 1`

encodes two initial facts:

- `cnt = 1` because `nums[0]` is the first occurrence in its run;
- `l = 1` because index zero is already the compacted output and index one is the next destination for a retained value.

The scan pointer `r` begins at one, so every later input position is considered exactly once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use sorted order to count a run

At position `r`, comparing `nums[r]` with `nums[r - 1]` tells whether the current value continues the same run.

If they differ, sorted order guarantees that a new distinct value has begun and the old value will never appear again. The current value is its first occurrence, so `cnt` resets to one.

If they are equal, this is the next occurrence of the same value, so `cnt` increases by one.

No dictionary is required. In an unsorted array, equal values could reappear after other values and would need global frequency tracking. Here contiguity makes one scalar run count sufficient.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At position `r`, comparing `nums[r]` with `nums[r - 1]` tell... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compact only retained occurrences

When `cnt <= k`, the current occurrence belongs in the result. The source writes it to the next compacted position:

`nums[l] = nums[r]`,

then increments `l`.

When `cnt > k`, it does nothing. The write pointer stays still, so the next retained value will overwrite the earliest output position that has not yet been filled.

For example, with `nums = [1, 1, 1, 2, 2, 3]` and `k = 2`:

- the first two ones occupy output indices zero and one;
- the third one is skipped, leaving `l = 2`;
- the first two twos are written to indices two and three;
- the three is written to index four.

The meaningful prefix becomes `[1, 1, 2, 2, 3]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 2, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1, 2, 2, 3], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 2, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare with the compacted value `k` positions:** - **Compare with the compacted value `k` positions back:** Retain `value` when fewer than `k` outputs exist or `value != nums[l - k]`. This is the manifest's summarized method and also uses $O(1)$ working space, but it is not the source's run counter.
- **Use a frequency dictionary:** It works even for unsorted input but spends $O(D)$ space for $D$ distinct values. Sorted contiguity makes it unnecessary.
- **Build a separate output with append:** This is simple and linear but uses output-sized storage beyond the in-place prefix. The source writes retained values directly into `nums`.
- **Delete excess entries while scanning:** Repeated deletion from the middle of a Python list shifts later values and can produce quadratic time.
- **`k = 1`:** `cnt <= k` keeps only the first element of every run, producing one copy of each distinct value.
- **`k` at least every run frequency:** No element is skipped. Every write is effectively to its own position and the returned slice equals the input values.
- **All values equal:** The first `k` occurrences are retained and every later occurrence is skipped.
- **All values distinct:** `cnt` resets to one at every position, so all values are retained.
- **A run begins after skipped values:** `l` may be behind `r`; the first new value is written into the earliest gap, maintaining order.
- **Nonempty input assumption:** Initializing `cnt` and `l` to one relies on index zero being present. The stated constraints guarantee this.
- **Positive `k` assumption:** The first element is retained unconditionally, which is correct only because `k >= 1`.
- **Returned slice versus original object:** The returned list has the requested length. The supplied `nums` is compacted in its prefix but is not resized by the source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the input length. The loop examines each position from one through $N-1$ once, doing constant work. The time complexity is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
