# Guided Example: First Element with Unique Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [20, 10, 30, 30]}`
- **Required output:** `30`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `30` from `{"nums": [20, 10, 30, 30]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Unique frequency is different from frequency one

The task does not ask for the first value that appears once. It asks for a value whose occurrence count is not shared by any other distinct value.

For example, in `[20,20,10,30,30,30]`:

- 10 has frequency 1;
- 20 has frequency 2;
- 30 has frequency 3.

All three frequencies are unique because each count belongs to only one distinct value. The answer is 20 because its first array occurrence comes earliest.

This requires two levels of counting: values first, then the frequencies themselves.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [20, 10, 30, 30]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count each distinct value

`cnt = Counter(nums)` creates:

$$
\texttt{cnt}[x]=F(x),
$$

the number of occurrences of value `x` in the complete array.

The full-array count must be known before deciding any position. A value appearing once in a prefix may appear again later, so a one-pass early decision without future information is unsafe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count how many values share each frequency

`cnt.values()` contains one frequency for every distinct value, not one entry per array position.

The source builds:

`freq = Counter(cnt.values())`.

Its meaning is:

$$
\texttt{freq}[f]
=
\left\lvert\{x:F(x)=f\}\right\rvert.
$$

A value `x` has a unique frequency exactly when:

`freq[cnt[x]] == 1`.

For `[20,10,30,30]`, `cnt` is `{20:1, 10:1, 30:2}`. The second Counter records that frequency 1 belongs to two values while frequency 2 belongs to one. Only 30 qualifies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `30` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [20, 10, 30, 30]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `30` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort the array:** Frequencies can be derived from equal-value runs, but sorting costs $O(N\log N)$ and loses original order unless positions are separately preserved.
- **Fixed value-frequency arrays:** Since values are bounded by $10^5$, arrays can replace Counters for deterministic indexing. They reserve the entire domain even when $D$ is small.
- **Nested comparison of frequencies:** Count values, then compare every pair of distinct frequencies. This costs $O(D^2)$ instead of using the second Counter.
- **Single element:** Its frequency 1 belongs to one distinct value, so that element is returned.
- **All elements distinct:** If there is more than one distinct value, all share frequency 1 and none qualifies.
- **All elements equal:** There is one distinct value, so its frequency is unique and the first element is returned.
- **Several qualifying values:** The scan returns whichever qualifying value appears first, not the one with smallest value or smallest frequency.
- **Repeated qualifying value:** Its first occurrence triggers the return.
- **No qualifying frequency:** The complete scan ends and returns -1.
- **Frequency multiplicity:** It counts distinct values having a frequency, not total array positions belonging to those values.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$ and $D$ be the number of distinct values. Building `cnt` takes expected $O(N)$ time. Building `freq` takes $O(D)$, and the final scan takes at most $O(N)$. Total expected time is $O(N)$.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
