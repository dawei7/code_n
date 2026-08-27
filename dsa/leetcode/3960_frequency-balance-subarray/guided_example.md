# Guided Example: Frequency Balance Subarray

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 1, 2, 3, 3, 3]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array ​​​​​​​`nums`.

The objective is to compute `5` from `{"nums": [1, 2, 2, 1, 2, 3, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two levels of frequency information

For a fixed left endpoint, the source maintains two counters:

- `cnt[x]` is the number of times value `x` occurs in the current subarray;
- `freq[c]` is the number of distinct values whose current count is exactly `c`.

The second counter is a histogram of the first counter's values. Suppose the current counts are `{4:2, 7:1, 9:2}`. Then `cnt` says values `4` and `9` each occur twice and `7` occurs once, while `freq` is `{1:1, 2:2}`. The number of keys in `freq` immediately tells us how many different positive frequency levels exist.

For every new left endpoint, both structures start empty. When the right endpoint adds a value `x`, only `x` moves from its old count to its new count. The source performs that move in three stages:

1. Read the old count `cnt[x]`. If `freq[cnt[x]]` is positive, decrement that histogram entry because `x` is leaving the old frequency class.
2. If the decremented entry becomes zero, remove its key from `freq`. This cleanup is essential because `len(freq)` must count only frequency levels that are actually present.
3. Increment `cnt[x]` and then increment `freq[cnt[x]]`, placing `x` into its new frequency class.

When `x` has never appeared, its old count is zero. There is intentionally no positive “frequency-zero” class in `freq`, so the conditional decrement does nothing. Afterward `x` enters the positive count-one class.

After this update, `cnt` exactly represents the current subarray `nums[l:r+1]`, and `freq` exactly represents the multiplicities of its positive counts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 1, 2, 3, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognizing the one-value case

The first test is



Because `cnt` receives a key when a value first appears and never removes that value during a fixed-left scan, its number of keys is the number of distinct values in the current subarray. If there is only one, the problem explicitly declares the subarray balanced, regardless of how many times that value occurs.

This separate branch matters. With one value repeated, `freq` has only one key, so it cannot pass the two-frequency test. The explicit rule prevents a valid single-value subarray from being rejected.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first test is



Because `cnt` receives a key when a val... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recognizing the two-level case

For a subarray containing multiple distinct values, balance requires exactly two occupied frequency levels. The source first checks `len(freq) == 2`.

Let `c = cnt[x]` be the new frequency of the value just added. Since `x` is in the current subarray, `c` must be one of the two keys in `freq`. Two positive frequencies have ratio two precisely when either:

- the other frequency is `2c`; or
- `c` is even and the other frequency is `c/2`.

That is what this condition expresses:



Looking relative to `x` is sufficient; there is no need to extract and sort the two histogram keys. The current frequency `c` is guaranteed to be one key, so the other key must be either its double or its half if the required relation holds. `Counter` returns zero for a missing key, allowing these lookups to serve as presence checks.

The requirement that both `f` and `2f` occur is automatically enforced by `len(freq) == 2`. A subarray with several distinct values all at frequency `f` has only one occupied histogram key and is rejected. A subarray with three different frequency levels is also rejected even if two happen to have a factor-of-two relation.

Whenever either balance rule succeeds, the source updates `ans` with the current length `r-l+1`. It initializes `ans=1` because every one-element subarray has one distinct value and is balanced.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 1, 2, 3, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recount every candidate subarray:** Building a:** - **Recount every candidate subarray:** Building a fresh frequency map for each `[l,r]` requires scanning up to `O(n)` elements per candidate, leading to `O(n^3)` time. Incrementally extending the right endpoint removes that redundant scan.
- **- **Scan all counts after every extension:** Maint:** - **Scan all counts after every extension:** Maintaining only `cnt` and then collecting or scanning all its values for each right endpoint can also reach cubic time when the subarray has many distinct values. The histogram `freq` reduces the balance query to constant expected time.
- **- **Sort the frequency values:** Sorting the disti:** - **Sort the frequency values:** Sorting the distinct counts for every subarray is unnecessary. The condition needs only the number of occupied levels and a factor-of-two relationship, both available directly from `freq`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the length of `nums`. There are `n` choices of left endpoint. For a fixed `l`, the right endpoint visits `l,l+1,\ldots,n-1` once. The total number of inner-loop iterations is
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
