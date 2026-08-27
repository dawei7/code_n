# Guided Example: Count Subarrays With Median K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 1, 4, 5], "k": 4}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` of size `n` consisting of **distinct **integers from `1` to `n` and a positive integer `k`.

The objective is to compute `3` from `{"nums": [3, 2, 1, 4, 5], "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn values into a balance around `k`

The array contains distinct integers, so every value other than `k` is unambiguously smaller or greater than `k`. Give a value greater than `k` contribution $+1$ and a value smaller than `k` contribution $-1$.

For a subarray that contains `k`, let $G$ be the count of values greater than `k` and $L$ the count smaller than `k`. Its balance is $G-L$.

If the subarray has odd length, `k` is its middle sorted element exactly when $G=L$, giving balance zero. If it has even length, the problem chooses the left middle element. For `k` to occupy that position, there must be one more greater value than smaller value, so $G=L+1$ and the balance is one.

Therefore, a subarray containing `k` has median `k` exactly when its comparison balance is either zero or one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 1, 4, 5], "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Every valid subarray must cross the unique position of `k`

The code locates `k` at index `i` with `nums.index(k)`. Because values are distinct, this occurrence is unique. A subarray whose median equals `k` must contain that value, so every candidate has a left endpoint at or before `i` and a right endpoint at or after `i`.

This lets the method describe a candidate by two independent extensions from `k`:

- a suffix of the elements left of `i`, scanned outward from `i-1`;
- a prefix of the elements right of `i`, scanned from `i+1` onward.

The center `[k]` alone is always valid, so `ans` starts at one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code locates `k` at index `i` with `nums.index(k)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Collect every right-side balance

The first loop scans positions to the right of `k`. Variable `x` is the balance of the current right prefix. Each greater value adds one and each smaller value subtracts one.

The subarray consisting of `k` plus only that right prefix has total balance `x`. The Boolean expression `0 <= x <= 1` is true exactly when that subarray has median `k`. In Python, adding a Boolean to an integer adds one for `true` and zero for `false`.

The counter `cnt[x]` records how many non-empty right prefixes have each balance. Multiple prefixes can have the same balance, and each corresponds to a different right endpoint, so their multiplicities must be preserved.

Notice that the empty right extension is not put in `cnt`. Right-empty subarrays are counted separately during the left scan, just as left-empty ones are counted directly during the right scan. This organization avoids double counting.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 1, 4, 5], "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prefix-balance map over the whole array:** Cou:** - **Prefix-balance map over the whole array:** Count compatible prefix states while enforcing inclusion of `k`. It is equivalent but often harder to organize without counting subarrays that omit `k`.
- **Brute-force sorting:** Enumerating subarrays and sorting each one is far too slow.
- **Distinct values:** They ensure every non-`k` value contributes exactly $+1$ or $-1$ and that `k` has one center position.
- **Even-length median:** Because the left middle is used, valid balance is one as well as zero.
- **Center only:** `[k]` is counted by the initial answer of one.
- **Empty extension:** It is handled directly rather than inserted into `cnt`.
- **All useful extensions on one side:** The Boolean additions count them without needing a pair from the opposite side.
- **Repeated balances:** Counter frequencies, not mere membership, are required because different endpoints define different subarrays.
- **Negative balance keys:** Python's counter accepts them normally.
- **Boolean arithmetic:** `true` contributes one and `false` contributes zero in the exact implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Finding `k` takes $O(n)$ time. The right and left scans together visit every remaining value once, and expected-time counter operations are $O(1)$. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
