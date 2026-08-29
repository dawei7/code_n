# Guided Example: Smallest Pair With Different Frequencies

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 2, 2, 3, 4]}`
- **Required output:** `[1, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `[1, 3]` from `{"nums": [1, 1, 2, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count first because validity depends on global frequency

Whether two values form a valid pair depends on how often each value occurs in the entire array. A single left-to-right comparison of neighboring input elements is therefore not enough. The source begins with `Counter(nums)`, producing a mapping `cnt` in which `cnt[v]` is the total frequency of each distinct present value `v`.

Only distinct values matter after counting; individual occurrences do not create different candidate pairs. Let `U` be the number of distinct values. The task is to choose present values `x<y` with `cnt[x] != cnt[y]` and minimize the ordered pair lexicographically: first minimize `x`, then minimize `y`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 2, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The first component must be the smallest present value

The source sets

`x = min(cnt.keys())`.

This deserves justification because it commits to `x` before searching for `y`. Let `m` be the smallest value present in `nums`. If there is any present value whose frequency differs from `cnt[m]`, then pairing the smallest such value with `m` gives a valid pair beginning with `m`. No valid pair can have a smaller first component, so every lexicographically optimal answer must use `x=m`.

What if every other value has the same frequency as `m`? Then every present value has that same frequency. No two values have different frequencies, so no valid pair exists anywhere—not even among two values larger than `m`.

An equivalent contradiction argument makes the point especially clear. Suppose some valid pair `(a,b)` exists, so `cnt[a]\ne cnt[b]`. The frequency `cnt[m]` cannot equal both different numbers `cnt[a]` and `cnt[b]`. Therefore it differs from at least one of them, and `m` can be paired with that value. Thus whenever any solution exists, a solution with the globally smallest present value as its first component also exists.

This property eliminates the need to examine every possible `x`. Lexicographic priority is stronger than a desire to find two nearby numbers or the two rarest numbers: the first numerical value dominates everything else.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the smallest compatible second component

After fixing `x`, the method initializes `min_y` to positive infinity and scans every key `y` in the counter. A value is eligible when its frequency differs from `cnt[x]`. Among eligible keys, the condition `y < min_y` preserves the smallest value seen.

The source does not explicitly write `y > x`, but that condition follows from the other facts. Since `x` is the minimum key, every key satisfies `y\ge x`. The key `y=x` has exactly the same counter entry as itself, so `cnt[x] != cnt[y]` is false. Every key that passes the frequency test must therefore be distinct from `x` and, because no key is smaller, must satisfy `y>x`.

The iteration order of `Counter` does not affect the result. Python counters preserve first-insertion order, not numeric order, but `min_y` is explicitly updated only by a smaller eligible key. After all keys have been visited, it is the minimum eligible `y` regardless of the order in which candidates appeared.

If no key has a frequency different from `cnt[x]`, `min_y` remains `inf` and the method returns `[-1,-1]`. Otherwise it returns `[x,min_y]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 2, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Fixed frequency array of length 101:** Because values are restricted to `[1,100]`, an integer array can replace `Counter`. Scanning the domain first finds the smallest positive-count value and then the first larger value with a different positive count. This gives deterministic `O(N+100)` time and `O(100)`, hence `O(1)`, space.
- **Sort the distinct values:** Sorting counter keys and scanning from the smallest one is easy to reason about, but it adds `O(U\log U)` time. The source obtains the same minima with two linear scans.
- **Enumerate every ordered pair:** Checking all `O(U^2)` value pairs and taking the minimum is correct but ignores the proof that the smallest present value must be the first component of any solution.
- **Choose the two smallest distinct values:** They are valid only if their frequencies differ. If their counts are equal, the second component may need to skip several values, as in the first example.
- **Choose minimum and maximum frequency:** The objective minimizes numeric values, not frequencies. Frequency is only a validity test; it does not determine lexicographic preference among eligible values.
- **Only one distinct value:** No pair of distinct values exists. The scan cannot find a different frequency and returns `[-1,-1]`.
- **All distinct values occur equally often:** No valid pair exists, even when there are many values. Fixing the minimum is still sound because failure to find a different count proves every count is equal.
- **A valid pair appears only among larger values:** This situation cannot exclude the global minimum. If two larger values have different frequencies, at least one of those frequencies differs from the minimum value's frequency, creating a valid pair with the smaller first component.
- **Counter iteration order:** Never assume keys arrive numerically sorted. The explicit `min` calls make this source correct even when first appearances in `nums` are in arbitrary order.
- **Implicit `y>x` test:** The source safely omits it only because `x` is the minimum key and `y=x` fails the different-frequency condition. If `x` were chosen any other way, an explicit ordering test would be necessary.
- **Repeated copies of the returned values:** The output contains values, not indices or occurrences. Counting multiplicity determines eligibility, but the result still contains each chosen value once.
- **Bounded-domain complexity:** Calling the source `O(1)` space relies on the fixed upper bound of one hundred for values. In a generalized version with arbitrary integers, the counter grows with `U` and must be reported as `O(U)`.
- **Sentinel imports:** The exact source requires `Counter` and `inf` to be available. Replacing `inf` with `null` would avoid the second dependency but would require a different comparison condition.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let `N` be the array length and `U` the number of distinct values. Building the counter takes `O(N)` expected time with Python's hash table. Finding the minimum key takes `O(U)` time, and scanning all keys for `min_y` takes another `O(U)`. Since `U\le N`, total time is `O(N+U)=O(N)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
