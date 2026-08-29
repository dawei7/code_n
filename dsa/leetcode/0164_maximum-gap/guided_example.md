# Guided Example: Maximum Gap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 6, 9, 1]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the maximum difference between two successive elements in its sorted form*. If the array contains less than two elements, return `0`.

The objective is to compute `3` from `{"nums": [3, 6, 9, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Avoid comparison sorting by preserving only bucket extremes

If the array were sorted, the answer would be the largest difference between
neighboring values. Comparison sorting costs $O(n\log n)$, so the solution
instead partitions the numeric range into ordered buckets.

Within a bucket, it stores only the smallest and largest assigned values. It
does not need the internal order, because the bucket width is chosen so that a
global maximum adjacent gap can be found between nonempty buckets.

Arrays with fewer than two values return zero immediately, because there is no
pair of successive sorted elements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 6, 9, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Derive a useful bucket width

Let `mi` and `mx` be the minimum and maximum input values, and let $n$ be the
array length. The sorted array has $n-1$ adjacent gaps whose sum is
$mx-mi$. Therefore at least one gap is no smaller than the average:

$$
\frac{mx-mi}{n-1}.
$$

The source chooses
`bucket_size = max(1, (mx - mi) // (n - 1))`. This positive integer width is
at most the average whenever the range is nonzero.

Values mapped to the same bucket differ by less than `bucket_size` under the
integer interval partition. Hence a gap meeting or exceeding the average lower
bound cannot be strictly hidden between two values in the same bucket. A
maximum gap is exposed between the maximum of one occupied bucket and the
minimum of the next occupied bucket.

The `max(1, ...)` guard handles equal values and small ranges without division
by zero in later bucket indexing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Map every value to an ordered bucket

The number of allocated buckets is:

`(mx - mi) // bucket_size + 1`.

Value `v` belongs to index `(v - mi) // bucket_size`. Subtracting `mi` makes
the minimum map to zero. The formula for the count ensures the maximum maps
within the final index, including when the numeric range is an exact multiple
of the width.

Each bucket begins as `[inf, -inf]`, an unmistakable empty state. On insertion,
the first component becomes the smallest value seen there and the second
becomes the largest. Repeated values and arbitrary input order cause no
problem.

Although the floor-width formula can allocate slightly more than $n$ buckets,
the count remains $O(n)$. If the width is one, then the range is below
$2(n-1)$; for larger widths, dividing the range by that width gives the same
constant-factor bound.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 6, 9, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Comparison sorting:** Sort and scan adjacent differences in $O(n\log n)$ time; it is simpler but violates the required linear-time target.
- **Radix sort:** The nonnegative bounded integers can be sorted digit by digit in linear time for a fixed number of digits, using $O(n)$ extra storage.
- **Fewer than two values:** No adjacent sorted pair exists, so return zero.
- **All values equal:** One occupied bucket yields no positive gap.
- **Duplicate values:** They only update the same extrema and do not affect the maximum.
- **Empty buckets:** They are skipped; the gap spans directly between consecutive occupied buckets.
- **Minimum and maximum:** The bucket-count formula includes both endpoints safely.
- **First occupied bucket:** The infinity initialization deliberately suppresses a nonexistent gap before the minimum.
- **Nonnegative contract:** Bucket indexing uses offsets and also works algebraically for negatives, but the stated domain is nonnegative.
- **Missing imports:** `List` and `inf` must be available in a standalone runtime.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let $k$ be the bucket count. Distributing $n$ values takes $O(n)$ time and
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
