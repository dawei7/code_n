# Guided Example: Jump Game VI

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, -1, -2, 4, -7, 3], "k": 2}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` and an integer `k`.

The objective is to compute `7` from `{"nums": [1, -1, -2, 4, -7, 3], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn every destination into a best-score state

Let `f[i]` mean the greatest score obtainable by starting at index zero and ending at index `i`. This state is useful because the final answer is exactly `f[n - 1]`, and every legal way to reach a later index must come from an already solved earlier index.

To land on `i`, the previous position must be one of the indices from `i - k` through `i - 1`, clipped to the beginning of the array. If the path comes from index `j`, its new score is `f[j] + nums[i]`. Therefore the recurrence is

$$
f[i] = \texttt{nums}[i] + \max_{\,\max(0,i-k)\le j<i} f[j].
$$

Checking all of those predecessors separately would take up to `k` work per index. With both the array length and `k` as large as $10^5$, that $O(nk)$ method is too slow. The exact solution instead maintains the maximum of this moving predecessor window with a monotonic deque.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, -1, -2, 4, -7, 3], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the deque stores

The deque `q` stores indices, not scores. Their indices increase from front to back because each current index is appended after all earlier ones. More importantly, their corresponding DP scores decrease strictly from front to back after maintenance. Thus `q[0]` always identifies the largest surviving score and is the best predecessor for the current destination.

An index can be omitted when a later index has an equal or greater score. Suppose `a < b` and `f[a] <= f[b]`. For every future destination at which `a` is still within jump range, `b` is also within range because it is newer. Choosing `b` gives at least as much accumulated score. The older `a` can never become the uniquely best choice, so retaining it provides no benefit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The deque `q` stores indices, not scores.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The first iteration establishes the base case

The implementation initializes `f` with zeros and `q` with index zero, then starts its loop at `i = 0` rather than handling the base case separately. On that iteration, `q[0]` is zero and the still-unwritten `f[0]` is zero, so

`f[0] = nums[0] + f[0]`

sets `f[0]` to `nums[0]`. This works because the zero came from array initialization, not from a real jump from index zero to itself. The following monotonic-maintenance loop removes the existing zero index since its score is equal to the newly computed score, and the final append restores index zero to the deque. After this special first pass, all later iterations use ordinary earlier predecessors.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, -1, -2, 4, -7, 3], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct dynamic programming:** Scan all up to `:** - **Direct dynamic programming:** Scan all up to `k` predecessors for each destination. It follows the same recurrence but costs $O(nk)$ time and is impractical at the maximum constraints.
- **Maximum heap:** Keep score-index pairs in a heap and lazily remove expired maximums. It is easier for some readers but costs $O(n\log n)$ time and can retain stale entries.
- **Segment tree:** Range-maximum queries and point updates also implement the recurrence, but take $O(n\log n)$ time and substantially more machinery.
- **Compressed deque state:** Store pairs of index and score directly in the deque and keep only the latest scalar score. That can reduce space from $O(n)$ to $O(k)$; the exact source intentionally retains the full `f` array.
- **One element:** The first self-initializing iteration sets `f[0] = nums[0]` and that value is immediately returned.
- **`k = 1`:** Every move must go to the next index, so the answer is the sum of every element; the deque still applies without special handling.
- **`k >= n - 1`:** Any earlier position can reach far enough until it becomes dominated; the same window logic remains valid.
- **All negative values:** The algorithm chooses the least harmful legal accumulated score at each step. Initial zeros outside established states never enter later comparisons.
- **Equal DP scores:** Removing the older equal state is safe because the newer index remains usable for at least as long.
- **Single expiration check:** It is correct only because indices are processed consecutively and the deque was valid on the prior iteration; changing the traversal pattern would require re-evaluating that assumption.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Each index is appended to the deque once. It can be removed once from the back when dominated or once from the front when expired, but never repeatedly. Although the source contains a nested `while`, all its iterations across the complete run total $O(n)$. Computing the DP states therefore takes $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
