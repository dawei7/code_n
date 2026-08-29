# Guided Example: Count Alternating Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 1, 1]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a binary array `nums`.

The objective is to compute `5` from `{"nums": [0, 1, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Count by right endpoint instead of listing subarrays.** Every subarray has one unique ending index. If the algorithm knows how many alternating subarrays end at each position, adding those counts gives the total without generating any subarray explicitly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact source maintains `s`, the length of the longest alternating suffix ending at the current element. For the first element, `s=1` because a one-element subarray has no adjacent pair that can violate the rule. It also initializes `ans=1` to count that first singleton.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**What makes an alternating suffix extend.** The loop examines adjacent values `a` and `b` through `pairwise(nums)`. If `a != b`, then every alternating subarray ending at `a` can be extended by `b`: the only new adjacency is the pair `(a,b)`, and it differs. The longest alternating suffix therefore grows by one:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run-length formula:** Split the array at equal adjacent pairs. An alternating run of length $L$ contributes $L(L+1)/2$ subarrays. This is also $O(n)$ but postpones contributions until a run ends.
- **Explicit sliding-window start:** Track the earliest index of the current alternating suffix and add `right - left + 1`. It is equivalent to storing `s`.
- **Enumerate every subarray:** Checking all starts and ends is $O(n^2)$ and unnecessary.
- **Single element:** Initialization counts its singleton and no pair loop runs.
- **Equal adjacent values:** They break every alternating subarray crossing that boundary.
- **Different adjacent values:** They extend every currently alternating suffix by exactly one.
- **All values equal:** Every `s` is one, so only the $n$ singleton subarrays are counted.
- **Entire array alternating:** The accumulated sum is $1+2+\cdots+n=n(n+1)/2$.
- **Binary guarantee:** It bounds values but is not needed beyond the adjacent inequality test.
- **Subarray versus subsequence:** Only contiguous suffixes ending at each index are counted; skipped positions are never allowed.
- **Singleton validity:** With no adjacent pair, a one-element subarray is vacuously alternating.
- **Unique right endpoint:** This partitions all valid subarrays and prevents double counting.
- **Large result:** Python is safe; other languages should use a 64-bit integer.
- **Lazy pairwise iterator:** `itertools.pairwise` does not allocate all adjacent pairs.
- **No input mutation:** `nums` is traversed in original order and never changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. `pairwise(nums)` produces each of the $n-1$ adjacent pairs lazily. Every pair triggers constant work: one comparison, one length update, and one addition. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
