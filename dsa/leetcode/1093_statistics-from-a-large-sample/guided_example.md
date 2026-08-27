# Guided Example: Statistics from a Large Sample

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"count": [0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}`
- **Required output:** `[1.0, 3.0, 2.375, 2.5, 3.0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a large sample of integers in the range `[0, 255]`. Since the sample is so large, it is represented by an array `count` where $\text{count}[k]$ is the **number of times** that `k` appears in the sample.

The objective is to compute `[1.0, 3.0, 2.375, 2.5, 3.0]` from `{"count": [0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Work with frequencies instead of expanding the sample

The sample may contain up to one billion values, so constructing the sorted sample explicitly is unnecessary and potentially impossible. The array `count` is already a histogram: index `k` is the value, and `count[k]` is how many copies of that value occur.

Because indices run in increasing numeric order, one scan over the 256 buckets provides enough information for the minimum, maximum, weighted sum, sample size, and mode. Median selection can also be answered from cumulative frequencies without materializing any occurrence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"count": [0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collect minimum, maximum, total, size, and mode

`mi` begins at positive infinity and `mx` at `-1`. For every bucket with nonzero frequency `x`, the code updates both with index `k`. Since the loop proceeds from zero upward, the first nonempty bucket becomes the minimum and later nonempty buckets move only the maximum, although using `min` and `max` makes the rule explicit.

The sample’s total numeric sum increases by `k * x` because value `k` occurs `x` times. The sample size `cnt` increases by `x`. Their quotient `s / cnt` is the arithmetic mean. The constraints guarantee at least one occurrence, so division by zero is impossible and both extreme values are replaced by real sample values.

`mode` stores an index. It starts at zero, and a bucket replaces it only when `x > count[mode]`. If bucket zero is empty, the first positive bucket necessarily wins. If bucket zero has occurrences, it is already a legitimate initial candidate. The unique-mode guarantee means no tie-breaking rule is needed for the maximum frequency; the strict comparison eventually leaves the one true mode.

Python integers can represent the weighted sum exactly even when frequencies are large. Conversion to floating point occurs only when forming the returned mean or an even-sample median.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `mi` begins at positive infinity and `mx` at `-1`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find a value by its one-based sorted rank

The helper `find(i)` answers: what value occupies position `i` in the expanded sorted sample, where the first position is one? It accumulates bucket counts from low value to high value. After processing bucket `k`, `t` equals the number of sample elements whose value is at most `k`.

The first index satisfying `t >= i` is precisely the value at rank `i`. Before that bucket, fewer than `i` elements have been accounted for; within that bucket, the cumulative block reaches or passes the requested position.

For an odd sample size, the unique middle rank is `cnt // 2 + 1`. The expression `cnt & 1` tests oddness, so the code calls `find` once for that rank.

For an even sample size, the middle elements occupy one-based ranks `cnt // 2` and `cnt // 2 + 1`. The code finds both values, adds them, and divides by two. They may be equal when both ranks fall inside the same frequency bucket, which naturally produces that same value as the median.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1.0, 3.0, 2.375, 2.5, 3.0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"count": [0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1.0, 3.0, 2.375, 2.5, 3.0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Expand and sort the sample:** Repeating each v:** - **Expand and sort the sample:** Repeating each value according to its count would require time and memory proportional to as many as one billion occurrences. It ignores the central benefit of the histogram representation.
- **Single cumulative scan for both median ranks:** Track the two target ranks during the main traversal and record each when cumulative count reaches it. This avoids the helper’s repeated fixed scans but is slightly more intertwined.
- **Binary search over prefix counts:** Build a 256-entry prefix-sum array and binary-search median ranks. It remains constant under this domain but uses extra storage and is unnecessary for only two queries.
- **Single distinct sample value:** Minimum, maximum, mean, median, and mode all equal that value, regardless of its frequency.
- **Value zero present:** Zero is a valid minimum and can be the mode. Initializing `mode` to zero deliberately supports that case.
- **Leading empty buckets:** They do not affect any statistic. The first nonzero index replaces `mi` and the initial mode when appropriate.
- **Trailing empty buckets:** They leave `mx` at the greatest earlier nonempty index.
- **Odd sample size:** Only rank `cnt // 2 + 1` is used; averaging neighboring ranks would be incorrect.
- **Even sample size:** The two central ranks can belong to different buckets, producing a fractional median such as `2.5`.
- **Large counts:** Multiplication `k * x` and total accumulation remain exact with Python integers before the final floating conversion.
- **Unique mode:** Strictly larger frequency updates are sufficient. Without uniqueness, the problem would need a specified tie-breaking rule.
- **Nonempty sample:** The guarantee `sum(count) >= 1` ensures `find` always reaches requested median ranks and the mean denominator is positive.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The histogram length is fixed at 256 by the contract. The main scan visits 256 buckets, and `find` performs another 256-bucket scan at most twice. This is a fixed amount of work independent of the number of represented sample elements, so the package states $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
